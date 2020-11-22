from Questions import Question
questions_prompts = [
    "Who is the creator of Java Programming Language?\n(a) Dennis Ritchie\n(b) BJarne\n(c) James Gosling\n\n",
    "Who is the creator of C Programming Language?\n(a) Dennis Ritchie\n(b) BJarne\n(c) James Gosling\n\n",
    "Who is the creator of C++ Programming Language?\n(a) Dennis Ritchie\n(b) BJarne\n(c) James Gosling\n\n",
    "Who is the creator of Python Programming Language?\n(a) Dennis Ritchie\n(b) Guido van Rossum\n(c) James Gosling\n\n",
    "Who is the creator of Perl Programming Language?\n(a) Larry Wall\n(b) BJarne\n(c) James Gosling\n\n",
    ]

questions = [
    Question(questions_prompts[0], "c"),
    Question(questions_prompts[1], "a"),
    Question(questions_prompts[2], "b"),
    Question(questions_prompts[3], "b"),
    Question(questions_prompts[4], "a"),
]


def check_ans(questions):
    score = 0;
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct.")

check_ans(questions)