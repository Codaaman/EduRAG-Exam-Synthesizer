from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a professional college exam paper setter.

Your task is to generate 5 unique question paper sets in STRICT JSON format.

NON-NEGOTIABLE RULES:
1. Output must be VALID JSON only.
2. Do not output markdown.
3. Do not output triple backticks.
4. Do not output any explanation.
5. Do not output any reasoning.
6. Do not output any text before or after the JSON.
7. Do not use <think> tags.
8. Do not change the JSON keys.
9. Do not change the JSON hierarchy.
10. Do not rename any section.
11. Do not add extra fields.
12. Do not remove any fields.
13. Every value must be a string or list of strings exactly as required.
14. Output must start with "{{" and end with "}}".
15. If you cannot comply, still return the same JSON structure with best possible content.

The output JSON structure must be EXACTLY this:

{{
  "SET A": {{
    "PART A": [
      "",
      ""
    ],
    "PART B": {{
      "Section a–e": [
        "",
        "",
        "",
        "",
        ""
      ],
      "Long Questions": [
        "",
        ""
      ]
    }}
  }},
  "SET B": {{
    "PART A": [
      "",
      ""
    ],
    "PART B": {{
      "Section a–e": [
        "",
        "",
        "",
        "",
        ""
      ],
      "Long Questions": [
        "",
        ""
      ]
    }}
  }},
  "SET C": {{
    "PART A": [
      "",
      ""
    ],
    "PART B": {{
      "Section a–e": [
        "",
        "",
        "",
        "",
        ""
      ],
      "Long Questions": [
        "",
        ""
      ]
    }}
  }},
  "SET D": {{
    "PART A": [
      "",
      ""
    ],
    "PART B": {{
      "Section a–e": [
        "",
        "",
        "",
        "",
        ""
      ],
      "Long Questions": [
        "",
        ""
      ]
    }}
  }},
  "SET E": {{
    "PART A": [
      "",
      ""
    ],
    "PART B": {{
      "Section a–e": [
        "",
        "",
        "",
        "",
        ""
      ],
      "Long Questions": [
        "",
        ""
      ]
    }}
  }}
}}
"""
    ),
    (
        "user",
        """
Generate 5 unique question paper sets:
SET A, SET B, SET C, SET D, SET E

Subject: {subject}
Topic: {topic}

Time: 2 Hours
Maximum Marks: 30

PART – A RULES:
- Select exactly 2 questions for each set
- Each question carries 5 marks
- Questions MUST be selected ONLY from the given Question Bank
- DO NOT modify the wording of Part A questions
- DO NOT repeat any Part A question across all 5 sets
- Each Part A question must appear only once across all 5 sets

PART – B RULES:
Section a–e:
- Generate exactly 5 one-word or very short answer questions
- Each question carries 1 mark

Long Questions:
- Generate exactly 2 questions
- First long question is for 7 marks
- Second long question is for 8 marks
- These long questions MUST be based on the topic: {topic}

GENERAL RULES:
- Maintain the same difficulty level across all sets
- Avoid repetition across sets
- Use formal academic language
- Questions should be clear and exam-oriented
- Cover different concepts of the topic
- Return STRICT JSON only
- Use EXACTLY the same keys and structure as defined in the system instruction

Question Bank (Part A):
{question_bank_A}

FINAL REMINDER:
Return ONLY valid JSON.
Do not write anything except JSON.
"""
    )
])