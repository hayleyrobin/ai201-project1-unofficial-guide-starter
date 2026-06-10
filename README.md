# The Unofficial Guide — Project 1

---

## Domain

Student reviews of UCLA professors across Computer Science and related departments, sourced from Rate My Professors. This knowledge is valuable because official university channels don't share student opinions on teaching style, exam difficulty, or grading — the stuff students actually need when choosing classes.

---

## Document Sources

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | Rate My Professors | Reviews for David Smallberg (CS) | ratemyprofessors.com |
| 2 | Rate My Professors | Reviews for Deb Pires (CS) | ratemyprofessors.com |
| 3 | Rate My Professors | Reviews for Jordan Mendler (CS) | ratemyprofessors.com |
| 4 | Rate My Professors | Reviews for Navid Amini (CS) | ratemyprofessors.com |
| 5 | Rate My Professors | Reviews for Paul Eggert (CS) | ratemyprofessors.com |
| 6 | Rate My Professors | Reviews for Rebecca Emigh (Sociology) | ratemyprofessors.com |
| 7 | Rate My Professors | Reviews for Richard Korf (CS) | ratemyprofessors.com |
| 8 | Rate My Professors | Reviews for T.C. Wittman (CS) | ratemyprofessors.com |
| 9 | Rate My Professors | Reviews for Taimie Bryant (Law) | ratemyprofessors.com |
| 10 | Rate My Professors | Reviews for Terri Anderson (Sociology) | ratemyprofessors.com |

---

## Chunking Strategy

**Chunk size:** 300 characters

**Overlap:** 50 characters

**Why these choices fit my documents:** Rate My Professors reviews are short and opinion-based. 300 characters captures roughly one complete review. 50 character overlap prevents key opinions from being cut off at chunk boundaries.

**Final chunk count:** 61

---

## Embedding Model

**Model used:** all-MiniLM-L6-v2 via sentence-transformers. Runs locally with no API key or cost.

**Production tradeoff reflection:** For a production system I would consider OpenAI's text-embedding-3-small for higher accuracy, but it costs money per token. I would also consider multilingual support if students write reviews in other languages, and a model with longer context length if documents were longer than short reviews.

---

## Grounded Generation

**System prompt grounding instruction:** "Answer the question using ONLY the information in the provided reviews below. If the reviews don't contain enough information to answer, say 'I don't have enough information on that.' Always mention which professor(s) the information comes from."

**How source attribution is surfaced in the response:** Retrieved source filenames are passed into the prompt as context headers (e.g. "Source: david_smallberg.txt") and the model is instructed to reference them in its response. Source files are also displayed separately in the interface.

---

## Evaluation Report

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What do students say about Professor Smallberg's lectures? | Reviews mention whether lectures are long, detailed, interesting, etc. | System found that Smallberg makes students watch two-hour-long lectures online three times per week, but provided limited additional detail. Source: david_smallberg.txt | Relevant | Partially Accurate |
| 2 | Is Professor Smallberg a good professor for beginners? | Reviews mention whether the professor is approachable and explains concepts clearly | System pulled chunks from three files (david_smallberg.txt, tc_wittman.txt, jordan_mendler.txt) and gave an unfocused answer. Noted he is great at explaining C++ but also demanding. | Partial | Partially Accurate |
| 3 | How is Professor Rebecca Emigh's grading? | Reviews mention grading style, fairness, and curve policy | System correctly identified that Emigh has strict grading, gives automatic zeros for missing citations, but also curves. Source: rebecca_emigh.txt | Relevant | Accurate |
| 4 | Does Professor Mendler give opportunities for improvement? | Reviews mention whether feedback is detailed or unhelpful | System found that Mendler is described as "super chill" and willing to help students who show up, but could not confirm specific feedback practices. Source: jordan_mendler.txt | Relevant | Partially Accurate |
| 5 | Which professor has the best teaching style? | Reviews from multiple professors compared, specific teaching traits mentioned | System identified Wittman as engaging and humorous, and Mendler as laid back and supportive. Sources: tc_wittman.txt, jordan_mendler.txt | Relevant | Accurate |

---

## Failure Case Analysis

**Question that failed:** Is Professor Smallberg a good professor for beginners?

**What the system returned:** The system pulled chunks from three different professor files (david_smallberg.txt, tc_wittman.txt, jordan_mendler.txt) instead of focusing on Smallberg's reviews only. The answer was unfocused and inconclusive.

**Root cause (tied to a specific pipeline stage):** The chunk size of 300 characters is too small to carry enough semantic meaning on its own. When the embedding model searched for "good professor for beginners" it matched loosely related chunks from multiple files instead of confidently identifying the most relevant source. This is a retrieval stage problem — the chunks don't carry enough context for the similarity search to distinguish between professors.

**What I would change to fix it:** Increase chunk size to 500 characters so each chunk carries more semantic meaning, making it easier for the embedding model to match the right professor to the right query. Metadata filtering by professor name would also help constrain retrieval to the correct source file.

---

## Spec Reflection

**One way the spec helped me during implementation:** Writing the chunking strategy in planning.md before coding forced me to think about document structure first. Because I knew my documents were short reviews, I chose 300 characters instead of a generic 500 — and that decision was already made before I wrote a single line of code.

**One way my implementation diverged from the spec, and why:** I planned to use Groq as my LLM but my account was restricted during development. I switched to Ollama running llama3.2 locally as a free alternative. The rest of the pipeline stayed the same — only the generation step changed.

---

## AI Usage

**Instance 1**

- *What I gave the AI:* My chunking strategy section from planning.md and my pipeline diagram
- *What it produced:* A complete ingest.py script with load_documents() and chunk_text() functions
- *What I changed or overrode:* I changed the chunk size from 500 to 300 characters after seeing that 500 produced only 35 chunks, which was too few for good retrieval

**Instance 2**

- *What I gave the AI:* My retrieval approach section and grounding requirements
- *What it produced:* query.py with ChromaDB retrieval and a Groq API connection
- *What I changed or overrode:* I replaced the Groq client with Ollama after my Groq account was restricted, and adjusted the model name from llama-3.3-70b-versatile to llama3.2