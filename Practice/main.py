score = 0


def ask(question, answer):
    global score
    response = input(question)
    if response == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong")
    print(f"Your score is: {score}")


ask("What is my favorite color?", "blue")
ask("How many times have I eaten pie?", "7")
ask("How many kung fu panda movies are there?", "3")
ask("Do you like tacos?", "yes")
print(f"""

Your final score is {score}/4!""")
