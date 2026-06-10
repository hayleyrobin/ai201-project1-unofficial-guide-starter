# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain
UCLA professor reviews across Computer Science and related 
departments, sourced from Rate My Professors. This knowledge 
is valuable because official university channels don't share 
student opinions on teaching style, exam difficulty, or 
grading — the stuff students actually need to pick classes.
---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|ratemyprofessors.com|
| 1 |Rate My Professors |Reviews for David Smallberg (CS) |ratemyprofessors.com |
| 2 |Rate My Professors |Reviews for Deb Pires (CS) |ratemyprofessors.com |
| 3 |Rate My Professors |Reviews for Jordan Mendler (CS) |ratemyprofessors.com |
| 4 |Rate My Professors |Reviews for Navid Amini (CS) |ratemyprofessors.com |
| 5 |Rate My Professors |Reviews for Paul Eggert (CS) |ratemyprofessors.com |
| 6 |Rate My Professors |Reviews for Rebecca Emigh(CS) |ratemyprofessors.com |
| 7 |Rate My Professors |Reviews for Richard Korf (CS) |ratemyprofessors.com |
| 8 |Rate My Professors |Reviews for T.C Wittman (CS) |ratemyprofessors.com |
| 9 |Rate My Professors |Reviews for Taimie Bryant(CS) |ratemyprofessors.com |
| 10 |Rate My Professors |Reviews for Terri Anderson (CS) |ratemyprofessors.com |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**
300 characters per chunk
**Overlap:**
50 characters of overlap
**Reasoning:**
Since Rate My Professors reviews are 
short and self-contained (usually 2-4 sentences each), 500 
characters captures roughly one full review per chunk. The 
50-character overlap prevents important context from being 
lost at chunk boundaries.
---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**
all-MiniLM-L6-v2 via sentence-transformers.
This runs locally with no API key or cost.
**Top-k:**
4 chunks per query. This gives the LLM enough context 
to form a good answer without diluting it with loosely related 
results.
**Production tradeoff reflection:**
For a production system, tradeoffs to consider would include:
- Cost: API-based models like OpenAI embeddings cost per token
- Context length: some models handle longer text better
- Accuracy: larger models are more accurate but slower
- Local vs API: local models are free but require more setup
---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 |What do students say about Professor Smallberg's lectures? |Reviews mention whether lectures are long, detailed, interesting, etc. |
| 2 | Is Professor Smallberg a good professor for beginners?  |Reviews mention whether the professor is approachable and explains concepts clearly |
| 3 |How is Professor Rebecca Emigh's grading?  |Reviews mention grading style, fairness, and curve policy  |
| 4 |Does Professor Mendler give oppurtunities for improvement? |Reviews mention whether feedback is detailed or unhelpful |
| 5 | Which professor has the best teaching style?|Reviews from multiple professors compared, specific teaching traits mentioned  |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. Chunk boundary splits: a single review might get cut across 
two chunks, meaning neither chunk has the complete opinion. 
This could cause retrieval to return incomplete context.

2. Cross-document queries: questions that compare multiple 
professors require retrieving relevant chunks from different 
files simultaneously, which may return inconsistent or 
incomplete results.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

```
Documents (.txt files)
        |
        v
[Document Ingestion] -- pdfplumber / plain text loader
        |
        v
[Chunking] -- 500 char chunks, 50 char overlap
        |
        v
[Embedding] -- sentence-transformers (all-MiniLM-L6-v2)
        |
        v
[Vector Store] -- ChromaDB
        |
        v
[Retrieval] -- top-4 semantic search
        |
        v
[Generation] -- Groq (llama-3.3-70b-versatile)
        |
        v
[Response + Source Citation]
```
---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->
   
1. Chunking and ingestion code: I will share my chunking 
strategy section with Claude and ask it to implement the 
chunk_text() function that splits documents by 300 characters 
with 50 character overlap.

2. Retrieval code: I will share my retrieval approach section 
and pipeline diagram with Claude and ask it to implement the 
embedding and ChromaDB storage functions.

3. Generation code: I will share my grounding requirements 
with Claude and ask it to write the prompt template and Groq 
API connection.

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
