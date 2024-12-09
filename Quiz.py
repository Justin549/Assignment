quiz = [
    {
        "question": "Who's the teacher for Analytics Micro Courses?",
        "choices": ["A) Hannan", "B) Rob", "C) Steve"],
        "answer": "B"
    },
    {
        "question": "How many datacamp courses are required for this assignment?",
        "choices": ["A) 3", "B) 5", "C) 25"],
        "answer": "A"
    },
    {
        "question": "What is the colour of course textbook given?",
        "choices": ["A) Red", "B) Yellow", "C) Purple"],
        "answer": "C"
    },
    {
        "question": "Which technique is not taught in Analytics Micro Course?",
        "choices": ["A) Python", "B) Tableau", "C) Java"],
        "answer": "C"
    }
]#use list to record three question, and dictionary to storage question's information


score = 0#initiate the score

print("Welcome to the quiz game! Answer the following questions:")

for i, question in enumerate(quiz, 1):#use enumerate method to automatically generate index 'i' and extract each question content from list first
    print(f"\nQuestion {i}: {question['question']}")#print what the question is
    for choice in question["choices"]:#print every option from the list
        print(choice)
    
    while True:
        user_answer = input("Your answer (A, B, C): ").strip().upper()#exclude any other input but upper character answer
        if user_answer in ['A', 'B', 'C']:
            break
        print("❌Invalid input! Please enter A, B, or C.")#in case user randomly give a wrong answer
    
    if user_answer == question["answer"]:#check the answer
        print("✅Correct!")
        score += 25
    else:
        print(f"❌Wrong! The correct answer was {question['answer']}.")#show the correct answer

print("\nQuiz completed!")
print(f"Total score is 100, Your final score is: {score}")#show final score