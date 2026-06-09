# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

Student reviews of UCLA professors across Computer Science 
and related departments, sourced from Rate My Professors. 
This knowledge is valuable because official university 
channels don't share student opinions on teaching style, 
exam difficulty, or grading — the stuff students actually 
need when choosing classes.

---

## Document Sources


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


**Chunk size:**
300 characters
**Overlap:**
50 characters
**Why these choices fit your documents:**
Rate My Professors 
reviews are short and opinion-based. 300 characters captures 
roughly one complete review. 50 character overlap prevents 
key opinions from being cut off at chunk boundaries.
**Final chunk count:**
61
---

## Embedding Model

**Model used:**
all-MiniLM-L6-v2 via sentence-transformers. 
**Production tradeoff reflection:**
For a production system I 
would consider OpenAI's text-embedding-3-small for higher 
accuracy, but it costs money per token. I would also consider 
multilingual support if students write reviews in other 
languages, and a model with longer context length if documents 
were longer than short reviews.
---

## Grounded Generation

System prompt grounding instruction: "Answer the question 
using ONLY the information in the provided reviews below. 
If the reviews don't contain enough information to answer, 
say 'I don't have enough information on that.' Always mention 
which professor(s) the information comes from."

How source attribution is surfaced: Retrieved source 
filenames are passed into the prompt as context headers 
(e.g. "Source: david_smallberg.txt") and the model is 
instructed to reference them in its response. Source files 
are also displayed separately in the interface.

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | What do students say about Professor Smallberg's lectures? |Reviews mention whether lectures are long, detailed, interesting, etc. | According to the reviews, it is mentioned that "Professor Smallberg makes you watch two-hour-long lectures online three times per week." However, no further information on what students think of his lectures is provided.

From david_smallberg.txt | Relevant | Partially Accurate |
| 2 | Is Professor Smallberg a good professor for beginners?  |Reviews mention whether the professor is approachable and explains concepts clearly | Based on one of the reviews from 'david_smallberg.txt', I can provide an answer.

The review states that "Prof Smallberg makes you watch two-hour-long lectures online three times per week". This may suggest that Professor Smallberg's teaching style is more demanding and not ideal for beginners. However, it also mentions that "he is certainly great at explaining C++".

While there isn't enough information to provide a definitive answer on whether Professor Smallberg is the best professor for beginners, some other perspectives can be drawn from other sources.

Based on 'tc_wittman.txt', a CS student reported that assignments were good and lectures were interesting. This indicates that Professor Wittman might have more suitable teaching styles but was not mentioned in relation to beginners specifically.

Also based on 'jordan_mendler.txt'. The review highlights Prof Smallberg as having an effective ability for students, but it does not indicate his effectiveness regarding beginners.

I don't have enough information to answer definitively if Professor Smallberg is the best professor for beginners. | Partial | Partially Accurate |
| 3 |How is Professor Rebecca Emigh's grading?  |Reviews mention grading style, fairness, and curve policy  | Based on the reviews from Source: rebecca_emigh.txt, it seems that Professor Rebecca Emigh has high expectations for academic rigor and strict grading. Students have reported feeling stressed due to the difficulty level of the class.

On one hand, some students (Q1 in the grade section) think her teaching style is terrible because she "does homework are terrible" with very harsh grades. If someone forgets a text citation, they will receive an automatic 0.

However, other students have given positive feedback about Professor Emigh's curve-grading practice (q3), suggesting that if the grading may appear tough initially but ultimately results in passing for everyone.

Therefore, it can be concluded that with Rebecca Emigh professors in SOC102, professor has a highly demanding academic approach but curatively grades, and the impact depends on individual adaptability to her style. | Relevant | Accurate
| 4 | Does Professor Mendler give oppurtunities for improvement? |Reviews mention whether feedback is detailed or unhelpful | According to the reviews, it appears that Professor Mendler does provide opportunities for improvement.

In jordan_mendler.txt (August 29th, 2022), someone mentions "Its the little things like this that differentiate him from average professors" implying that he anticipates and provides opportunities for improvement.

This person also mentions in a different review of Jordan Mendler on January 17th, 2019: 'Super chill professor. If you show up and want to learn he will teach you so'. It implies that if students put in the effort (show up), Professor Mendler will facilitate their learning and provide necessary support and opportunities for growth.

I don't have enough information on whether students were given specific feedback or guidance by Professor Mendler to improve their performance. | Relevant | Partially Accurate |
| 5 | Which professor has the best teaching style?|Reviews from multiple professors compared, specific teaching traits mentioned  | Based on the reviews, it appears that Professor Wittman (Source: tc_wittman.txt) has an engaging and humorous teaching style. He makes the subject interesting and keeps lectures entertaining.

Additionally, Professor Mendler (Source: jordan_mendler.txt) is described as "super chill" with a teacher who will guide students to learn if they show up and are willing to put in effort. | Relevant | Accurate |


**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

**Question that failed:**
Is Professor Smallberg a good 
professor for beginners?
**What the system returned:**
The system pulled chunks from 
three different professor files (david_smallberg.txt, 
tc_wittman.txt, jordan_mendler.txt) instead of focusing 
on Smallberg's reviews only. The answer was unfocused and 
inconclusive.
**Root cause (tied to a specific pipeline stage):**
The chunk size of 300 characters is too small 
to carry enough semantic meaning on its own. When the 
embedding model searched for "good professor for beginners" 
it matched loosely related chunks from multiple files 
instead of confidently identifying the most relevant source. 
This is a retrieval stage problem — the chunks don't carry 
enough context for the similarity search to distinguish 
between professors.
**What you would change to fix it:**
Increase chunk size to 500 characters 
so each chunk carries more semantic meaning, making it 
easier for the embedding model to match the right professor 
to the right query. Metadata filtering by professor name 
would also help constrain retrieval to the correct source 
file.
---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**
Writing the chunking strategy in planning.md before coding forced 
me to think about document structure first. Because I knew 
my documents were short reviews, I chose 300 characters 
instead of a generic 500 — and that decision was already 
made before I wrote a single line of code.

One way the spec helped me during implementation: Writing 
the chunking strategy in planning.md before coding forced 
me to think about document structure first. Because I knew 
my documents were short reviews, I chose 300 characters 
instead of a generic 500 — and that decision was already 
made before I wrote a single line of code.

**One way your implementation diverged from the spec, and why:**
I planned to use Groq as my LLM but my account was restricted during 
development. I switched to Ollama running llama3.2 locally 
as a free alternative. The rest of the pipeline stayed the 
same — only the generation step changed.
---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->


**Instance 1**

- *What I gave the AI:* My chunking strategy section from 
  planning.md and my pipeline diagram
- *What it produced:* A complete ingest.py script with 
  load_documents() and chunk_text() functions
- *What I changed or overrode:* I changed the chunk size 
  from 500 to 300 characters after seeing that 500 produced 
  only 35 chunks, which was too few for good retrieval

**Instance 2**

- *What I gave the AI:* My retrieval approach section and 
  grounding requirements
- *What it produced:* query.py with ChromaDB retrieval and 
  a Groq API connection
- *What I changed or overrode:* I replaced the Groq client 
  with Ollama after my Groq account was restricted, and 
  adjusted the model name from llama-3.3-70b-versatile 
  to llama3.2
