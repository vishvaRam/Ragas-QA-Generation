import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from ragas.testset import TestsetGenerator
from ragas.llms import llm_factory
import google.genai as genai
from ragas.embeddings import HuggingFaceEmbeddings
from ragas.testset.synthesizers import default_query_distribution
from dotenv import load_dotenv

load_dotenv()

# --- Configuration ---
DIRECTORIES = ["Data/Books-MD/Chemistry"]
OUTPUT_FILE = "ragas_testset.json"

# --- 1. Load Documents ---
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

processed_docs = []
for doc in documents:
    doc.metadata['source'] = doc.metadata.get('source', 'unknown')
    processed_docs.append(doc)
    
print(f"Total chunks created: {len(processed_docs)}")

# --- 3. Initialize Ragas Generator ---
client = genai.Client()
generator_llm = llm_factory("gemini-2.0-flash-lite", provider="google", client=client)
embeddings = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

generator = TestsetGenerator(llm=generator_llm, embedding_model=embeddings)
query_distribution = default_query_distribution(generator_llm)

# --- 4. Generate Testset ---
print("Generating testset... this may take a while.")
testset = generator.generate_with_langchain_docs(
    processed_docs,
    testset_size=100,
    transforms_llm=generator_llm,
    query_distribution=query_distribution
)

# --- 5. Save to JSON ---
df = testset.to_pandas()
df.to_json(OUTPUT_FILE, orient="records", indent=4)

print(f"Successfully saved {len(df)} Q&A pairs to {OUTPUT_FILE}")
