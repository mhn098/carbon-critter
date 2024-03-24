import os
import site
import sys
import os
import json
import predictionguard as pg
from getpass import getpass
import predictionguard as pg
from sentence_transformers import SentenceTransformer
import faiss
os.environ['PREDICTIONGUARD_TOKEN'] = "q1VuOjnffJ3NO2oFN8Q9m8vghYc84ld13jaqdF7E"
knowledge_base = [
    "Fun Fact 1: It takes more energy to make 1 kg of paper than it takes to make 1 kg of steel.",
    "Fun Fact 2: It takes almost 500,000 litres of water to extract just 1 kg of gold",
    "Sustainability is ability to maintain or support a process over time.",
    "Sustainability is often broken into three core concepts: economic, environmental, and social.",
    "Many businesses and governments have committed to sustainable goals, such as reducing their environmental footprints and conserving resources.",
    "3 Pillars of Sustainability The idea of sustainability is often broken down into three pillars: economic, environmental, and social—also known informally as profits, planet, and people. In that breakdown, the concept of economic sustainability focuses on conserving the natural resources that provide physical inputs for economic production, including both renewable and exhaustible inputs.",
    "Intel Habana Gaudi 2 is a purpose-built AI processor designed for high-performance deep learning training and inference.",
    "Gaudi 2 offers high efficiency, scalability, and ease of use for AI workloads.",
    "By leveraging Gaudi 2 on the Intel Developer Cloud, Prediction Guard can provide powerful and efficient AI capabilities to its users."
]

prompt_template = f"""
### Instruction:
You are a Question answer bot and will give an Answer based on the below input context and respond with a short answer to the given question.
Use only the information in the below input to answer the question.
It is critical to limit your answers to the question and dont print anything else.
It is critical to limit your answers to 20 words or less.
If you cannot answer the question, respond with "Sorry, I don't know."

### Input:
Context: {{}}
Question: {{}}

### Response:
"""

model = SentenceTransformer("all-MiniLM-L6-v2")
kb_embeddings = model.encode(knowledge_base)
index = faiss.IndexFlatL2(kb_embeddings.shape[1]) # 384
index.add(kb_embeddings)

def rag_answer(question):
    try:
        # Generate embedding for the question
        question_embedding = model.encode([question])

        # Find the most similar text from the knowledge base using FAISS
        _, most_relevant_idx = index.search(question_embedding, 1)
        relevant_chunk = knowledge_base[most_relevant_idx[0][0]]
        # Format our prompt with the question and relevant context using f-strings
        prompt=prompt_template.format(relevant_chunk, question)

        # Get a response from the language model
        result = pg.Completion.create(
            model="Neural-Chat-7B", #"Nous-Hermes-Llama2-13B",
            prompt=prompt
        )
        return result['choices'][0]['text']
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "Sorry, something went wrong. Please try again later."
    
print("="*71)
question1 = "Give me a fun Fact"
response1 = rag_answer(question1)
print(f"Question 1: {question1}")
print(f"Response 1: {response1}")
print("="*71)

question2 = "Give me a second fun Fact"
response2 = rag_answer(question2)
print(f"Question 2: {question2}")
print(f"Response 2: {response2}")
print("="*71)

question3 = "What is Intel Liftoff and what is prediction guards relatioship to liftoff?"
response3 = rag_answer(question3)
print(f"Question 3: {question3}")
print(f"Response 3: {response3}")
print("="*71)