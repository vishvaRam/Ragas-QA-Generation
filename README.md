# 🧪 Synthetic Dataset Generation with Ragas & Knowledge Graphs

This repository showcases how to use the **Ragas framework** to generate **high-quality synthetic Q&A datasets** from documents using **Knowledge Graphs**, **LLMs**, and **custom personas**.

The example focuses on **Chemistry educational content** and demonstrates persona-driven, exam-level question generation (e.g., JEE Advanced).

---

## ✨ What This Example Demonstrates

- 📄 Loading documents from local directories  
- 🧠 Building and reusing a **Knowledge Graph** with Ragas  
- 🔄 Applying LLM-based transforms to extract relationships  
- 🎭 Using **personas** to control question difficulty and style  
- 🧪 Generating synthetic test datasets  
- 💾 Exporting results as JSON  

The Knowledge Graph is saved and reused to avoid recomputation.

---

## 🚀 Setup

### Install Dependencies
```bash
pip install ragas langchain-community langchain-huggingface langchain-openai python-dotenv
````

### Configure API Key

Create a `.env` file:

```env
GOOGLE_API_KEY=your-api-key-here
```

---

## 📂 Data Format

* Supported formats: `.md`, `.txt`
* Documents should be organized in directories

```
Data/
└── Books-MD/
    └── Chemistry/
        └── Chemistry-kech2-MD/
```

---

## 🧪 Running the Example

```bash
python main.py
```

The script will:

1. Load or create a Knowledge Graph
2. Apply Ragas transforms
3. Generate synthetic Q&A pairs
4. Save outputs to JSON

---

## 📦 Outputs

* **Synthetic Dataset**
  `Ragas/Chemistry-kech2-MD.json`

* **Knowledge Graph**
  `Ragas/Chemistry-kech2-MD-knowledge_graph.json`

Each dataset entry contains:

```json
{
  "question": "...",
  "answer": "...",
  "contexts": [...]
}
```

---

## 🎯 Use Cases

* RAG evaluation datasets
* LLM testing & benchmarking
* Educational content generation
* Domain-specific QA synthesis

---

## 📚 Reference

See `docs/howtos/testset-generation.md` for more details on Ragas testset generation.

If you want an **even more minimal README (10–15 lines)** or a **research-paper style README**, I can compress it further 👌
