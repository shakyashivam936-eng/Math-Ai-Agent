from langchain_core.prompts import ChatPromptTemplate

question_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an expert  Math techer.
        You will be given a question and you will answer it.
        You will provide a detailed explanation of the concept.
        You will provide a formula and practical example in professional way in simple terms of the concept.
        You will provide a important question and answer related to the concept.
        You will Provide Formula based question answer.
        
        """
    ),
    (
        "human",
        """
        Subject: Math
        Class: {class}
        Topic: {topic}
        Difficulty: {difficulty}
        Number of  questions: {num_questions}
        """
    )
])