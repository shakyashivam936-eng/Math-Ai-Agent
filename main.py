from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from prompts import question_prompt


def main():
    # Initialize the local LLM
    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    # Connect the prompt with the model.
    chain = question_prompt | llm | StrOutputParser()

    print("======= AI Question Generator =======")

    # Get user input for the prompt.
    Class = input("Enter the class: ")
    concept = input("Enter the concept: ")
    difficulty = input("Enter the difficulty level: ")
    num_questions = int(input("Enter the number of questions: "))

    # Provide dynamic input to the prompt.
    response = chain.invoke({
        "class": Class,
        "topic": concept,
        "difficulty": difficulty,
        "num_questions": num_questions
    })

    # Display the response.
    print(response)

if __name__ == "__main__":
    main()