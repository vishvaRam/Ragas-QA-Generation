import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from ragas.testset.graph import KnowledgeGraph, Node, NodeType
from langchain_huggingface import HuggingFaceEmbeddings
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.testset.transforms import default_transforms, apply_transforms
from langchain_openai import ChatOpenAI
from ragas.testset.persona import Persona
from ragas.llms import LangchainLLMWrapper
from ragas.testset import TestsetGenerator
from ragas.testset.synthesizers import SingleHopSpecificQuerySynthesizer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- Configuration ---
DIRECTORIES = ["Data/Books-MD/Chemistry/Chemistry-kech1-MD"]
OUTPUT_FILE = "Ragas/Chemistry-kech1-MD.json"
KG_OUTPUT_FILE = "Ragas/Chemistry-kech1-MD-knowledge_graph.json"

# --- Setup LLM and Embeddings ---
print("\nSetting up Gemini LLM and HuggingFace embeddings...")

openai_compatible_llm = ChatOpenAI(
    model="gemini-2.5-flash-lite",
    openai_api_key=os.environ.get("GOOGLE_API_KEY"),
    openai_api_base="https://generativelanguage.googleapis.com/v1beta/openai/"
)
generator_llm = LangchainLLMWrapper(openai_compatible_llm)

hf_embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
embeddings = LangchainEmbeddingsWrapper(hf_embeddings)

# --- Knowledge Graph Logic ---
if os.path.exists(KG_OUTPUT_FILE):
    print(f"\n✅ Found existing Knowledge Graph at {KG_OUTPUT_FILE}. Loading...")
    kg = KnowledgeGraph.load(KG_OUTPUT_FILE)
    print(f"Loaded {len(kg.nodes)} nodes from file.")
else:
    print("\n⚠️ No existing graph found. Creating new Knowledge Graph...")
    
    # 1. Load Documents
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

    processed_docs = []
    for doc in documents:
        doc.metadata['source'] = doc.metadata.get('source', 'unknown')
        processed_docs.append(doc)

    # 2. Create KG Nodes
    kg = KnowledgeGraph()
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
    
    # 3. Apply Transforms
    print("Applying transforms...")
    default_transforms = default_transforms(
        documents=processed_docs, 
        llm=generator_llm, 
        embedding_model=embeddings
    )
    apply_transforms(kg, transforms=default_transforms)
    
    # 4. Save KG
    print(f"Saving Knowledge Graph to {KG_OUTPUT_FILE}...")
    kg.save(KG_OUTPUT_FILE)
    print("Knowledge graph saved successfully!")

# --- Setup Persona and Generator ---
jee_persona = Persona(
    name="JEE_Chemistry_Professor",
    role_description=(
        "You are a distinguished Chemistry Professor and Chief Examiner for the JEE Advanced "
        "Entrance Exam in India. Your task is to create a challenging test dataset for top-tier "
        "engineering aspirants.\n\n"
        "GUIDELINES:\n"
        "1. **Complexity:** Generate multi-step questions that require deep conceptual understanding "
        "of Physical, Organic, and Inorganic Chemistry.\n"
        "2. **Formatting:** Use LaTeX formatting (e.g., $\\text{H}_2\\text{SO}_4$) for formulas "
        "only when necessary. For purely theoretical questions, clear text is preferred.\n"
        "3. **Topics:** Focus on reaction mechanisms, stoichiometry, and periodic trends.\n"
        "4. **Tone:** Academic, rigorous, and precise."
    )
)

print("\nGenerating testset...")
query_distribution = [
    (SingleHopSpecificQuerySynthesizer(llm=generator_llm), 1.0),
]

generator = TestsetGenerator(
    llm=generator_llm, 
    embedding_model=embeddings,
    knowledge_graph=kg,
    persona_list=[jee_persona]
)

testset = generator.generate(
    testset_size=50,
    query_distribution=query_distribution
)


# --- Save Results ---
print(f"\nSaving testset to {OUTPUT_FILE}...")
df = testset.to_pandas()

df = df.rename(columns={
    "user_input": "question",
    "reference": "answer",  # or "answer"
    "reference_contexts": "contexts"
})

df = df[["question", "answer", "contexts"]]
df.to_json(OUTPUT_FILE, orient="records", indent=4)

print(f"\n✅ Successfully generated {len(df)} Q&A pairs!")
