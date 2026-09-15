import re
from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
from tools import searcha
import ollama
from document_reader import query
import prompt
import time
import json
import word as w

load_dotenv()
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")



model=init_chat_model("groq:qwen/qwen3-32b", temperature=0.3,
    timeout=30,
    max_tokens=5000,
    max_retries=6,)

#model_2=ollama.chat(model='llama3',




agent=create_deep_agent(
    model=model,
    tools=[searcha],
    system_prompt="You are a strict exam paper setter. Follow rules strictly.",
    memory=None, 

)






question_bank_A = """
1. What is Machine Learning?
2. Explain types of Machine Learning.
3. What is supervised learning?
4. What is unsupervised learning?
5. Define overfitting.
6. What is OpenCV?
7. Explain database normalization.
8. What is SQL?
9. What is primary key?
10. Explain data preprocessing.
"""






chain = prompt.prompt | model

response = chain.invoke({
    "subject": "ML",
    "topic": "Machine learning",
    "question_bank_A": {question_bank_A},
})

def extract_final_output(text: str) -> str:
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    return text

a=extract_final_output(response.content)
print(a)
a = a.strip()
out=json.loads(a)

print(out)
def gen(sub,s_no):
    sub=sub
    s_no=s_no
    for k in out:
        
        a=out[k]
        if k=='SET A':
            q1=a['PART A'][0].lstrip('1.')
            q2=a['PART A'][1].lstrip('2.')

            q3=a['PART B']['Section a–e'][0]
            q4=a['PART B']['Section a–e'][1]
            q5=a['PART B']['Section a–e'][2]
            q6=a['PART B']['Section a–e'][3]
            q7=a['PART B']['Section a–e'][4]
            q8=a['PART B']['Long Questions'][0].lstrip('7.')
            q9=a['PART B']['Long Questions'][1].lstrip('8.')
            w.DOX_GEN("A",sub,s_no,q1,q2,q3,q4,q5,q6,q7,q8,q9)


        elif k=='SET B':
            q1=a['PART A'][0].lstrip('1.')
            q2=a['PART A'][1].lstrip('2.')

            q3=a['PART B']['Section a–e'][0]
            q4=a['PART B']['Section a–e'][1]
            q5=a['PART B']['Section a–e'][2]
            q6=a['PART B']['Section a–e'][3]
            q7=a['PART B']['Section a–e'][4]
            q8=a['PART B']['Long Questions'][0].lstrip('7.')
            q9=a['PART B']['Long Questions'][1].lstrip('8.')
            w.DOX_GEN("B",sub,s_no,q1,q2,q3,q4,q5,q6,q7,q8,q9)

            
        elif k=='SET C':
            q1=a['PART A'][0].lstrip('1.')
            q2=a['PART A'][1].lstrip('2.')

            q3=a['PART B']['Section a–e'][0]
            q4=a['PART B']['Section a–e'][1]
            q5=a['PART B']['Section a–e'][2]
            q6=a['PART B']['Section a–e'][3]
            q7=a['PART B']['Section a–e'][4]
            q8=a['PART B']['Long Questions'][0].lstrip('7.')
            q9=a['PART B']['Long Questions'][1].lstrip('8.')
            w.DOX_GEN("C",sub,s_no,q1,q2,q3,q4,q5,q6,q7,q8,q9)

            
        
        elif k=='SET D':
            q1=a['PART A'][0].lstrip('1.')
            q2=a['PART A'][1].lstrip('2.')

            q3=a['PART B']['Section a–e'][0]
            q4=a['PART B']['Section a–e'][1]
            q5=a['PART B']['Section a–e'][2]
            q6=a['PART B']['Section a–e'][3]
            q7=a['PART B']['Section a–e'][4]
            q8=a['PART B']['Long Questions'][0].lstrip('7.')
            q9=a['PART B']['Long Questions'][1].lstrip('8.')
            w.DOX_GEN("D",sub,s_no,q1,q2,q3,q4,q5,q6,q7,q8,q9)

            
        elif k=='SET E':
            q1=a['PART A'][0].lstrip('1.')
            q2=a['PART A'][1].lstrip('2.')

            q3=a['PART B']['Section a–e'][0]
            q4=a['PART B']['Section a–e'][1]
            q5=a['PART B']['Section a–e'][2]
            q6=a['PART B']['Section a–e'][3]
            q7=a['PART B']['Section a–e'][4]
            q8=a['PART B']['Long Questions'][0].lstrip('7.')
            q9=a['PART B']['Long Questions'][1].lstrip('8.')
            w.DOX_GEN("E",sub,s_no,q1,q2,q3,q4,q5,q6,q7,q8,q9)

            
        

a=input("enter subject:-")
b=input("subjecct_number")

print(gen(a,b))


    
