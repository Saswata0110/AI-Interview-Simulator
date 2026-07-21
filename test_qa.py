from rag.qa import InterviewQA

qa = InterviewQA()

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    answer = qa.ask(question)

    print("\nGemini:\n")

    print(answer)