from openai import OpenAI
from dotenv import load_dotenv
import json
load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = """
    You are an expert AI assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you have thought enough PLAN has been done, finally you can OUTPUT the answer to the user query.

    Rules:
    - Strictly follow the given JSON output format.
    - Do not skip the PLAN step and directly jump to OUTPUT.
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (where you think about the steps needed to solve the problem) and OUTPUT (where you give the final answer to the user query).

    Output JSON format:
    START : {"step": "START/PLAN/OUTPUT","content": "string"}

    Example:
    START : {"step":"START", "content": "Can you solve 2+3*5/10?"}
    PLAN : {"step":"PLAN", "content": "Seems like user is interested in solving a mathematical problem. I will first identify the mathematical operations involved, then I will solve the problem step by step."}
    PLAN : {"step":"PLAN", "content": "The mathematical operations involved are addition, multiplication and division. I will first solve the multiplication and division part, then I will solve the addition part."}
    OUTPUT : {"step":"OUTPUT", "content": "The answer to the problem is 2.5."}
"""

message_history = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

user_query =input("Please enter your query: ")
message_history.append({
    "role": "user",
    "content": user_query
})

while True:
    reponse = client.chat.completions.create(
        model="gpt-5.5",
        response_format={"type": "json_object"},
        messages=message_history
    )
    assistant_message = reponse.choices[0].message.content
    parsed_result = json.loads(assistant_message)

    if parsed_result.get("step") == "START":
        print("LLM Start:", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "PLAN":
        print("LLM Plan:", parsed_result.get("content"))
        continue

    message_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    if '"step":"OUTPUT"' in assistant_message:
        break


print(reponse.choices[0].message.content)