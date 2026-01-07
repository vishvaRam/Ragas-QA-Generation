import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from ragas.testset.graph import KnowledgeGraph, Node, NodeType
from ragas.llms import llm_factory
from ragas.embeddings import HuggingFaceEmbeddings
from ragas.testset.transforms import (
    # HeadlinesExtractor,
    # HeadlineSplitter,
    # KeyphrasesExtractor,
    default_transforms,
    apply_transforms
)
from ragas.testset import TestsetGenerator
from ragas.testset.synthesizers import (
    SingleHopSpecificQuerySynthesizer,
    # MultiHopAbstractQuerySynthesizer,
    # MultiHopSpecificQuerySynthesizer
)
import google.genai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- Configuration ---
DIRECTORIES = ["Data/Books-MD/Chemistry/Chemistry-Test"]  # Change to your directory
OUTPUT_FILE = "ragas_testset.json"
KG_OUTPUT_FILE = "knowledge_graph.json"

# --- 1. Load Documents ---
print("Loading documents...")
documents = []
for directory in DIRECTORIES:
    if os.path.exists(directory):
        print(f"Loading from {directory}...")
        loader = DirectoryLoader(
            directory, 
            glob="**/*.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"}
        )
        documents.extend(loader.load())
    else:
        print(f"Warning: Directory {directory} not found.")


print(f"Total documents loaded: {len(documents)}")


# Process documents with metadata
processed_docs = []
for doc in documents:
    doc.metadata['source'] = doc.metadata.get('source', 'unknown')
    processed_docs.append(doc)
    
print(f"Total documents processed: {len(processed_docs)}")


# --- 2. Setup LLM and Embeddings ---
print("\nSetting up Gemini LLM and HuggingFace embeddings...")


# Configure Gemini
client = genai.Client()
generator_llm = llm_factory(
    "gemini-2.5-flash", 
    provider="google", 
    client=client
)


# Configure HuggingFace embeddings
embeddings = HuggingFaceEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)


# --- 3. Create Knowledge Graph ---
print("\nCreating knowledge graph...")
kg = KnowledgeGraph()


# Add documents as nodes
for doc in processed_docs:
    kg.nodes.append(
        Node(
            type=NodeType.DOCUMENT,
            properties={
                "page_content": doc.page_content,
                "document_metadata": doc.metadata,
            },
        )
    )


print(f"Initial nodes in KG: {len(kg.nodes)}")


# --- 4. Apply Transforms ---
print("\nApplying transforms to knowledge graph...")

default_transforms = default_transforms(documents=processed_docs, llm=generator_llm, embedding_model=embeddings)

apply_transforms(kg, transforms=default_transforms)
print(f"Nodes after transforms: {len(kg.nodes)}")


# --- 5. Save Knowledge Graph as JSON ---
print(f"\nSaving knowledge graph to {KG_OUTPUT_FILE}...")
kg.save(KG_OUTPUT_FILE)
print("Knowledge graph saved successfully!")

# --- 7. Setup Query Distribution ---
print("\nSetting up query synthesizers...")
query_distribution = [
    (SingleHopSpecificQuerySynthesizer(llm=generator_llm), 1.0),
    # (MultiHopAbstractQuerySynthesizer(llm=generator_llm), 0.25),
    # (MultiHopSpecificQuerySynthesizer(llm=generator_llm), 0.25),
]


# --- 8. Generate Testset ---
print("\nGenerating testset... this may take a while.")
generator = TestsetGenerator(
    llm=generator_llm, 
    embedding_model=embeddings,
    knowledge_graph=kg,
)


testset = generator.generate(
    testset_size=10,  # Adjust size as needed
    query_distribution=query_distribution
)


# --- 9. Save Testset to JSON ---
print(f"\nSaving testset to {OUTPUT_FILE}...")
df = testset.to_pandas()
df.to_json(OUTPUT_FILE, orient="records", indent=4)


print(f"\n✅ Successfully generated {len(df)} Q&A pairs!")
print(f"✅ Testset saved to: {OUTPUT_FILE}")
print(f"✅ Knowledge graph saved to: {KG_OUTPUT_FILE}")

