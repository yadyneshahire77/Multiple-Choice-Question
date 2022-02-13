#mini project/Multiple choice quiz

question_prompts=["What colors are Apples?\n(a)Red\n(b)Purple\n(c)orange\n\n",
                  "what colors are Bananas?\n(a)Teal\n(b)Magenta\n(c)Yellow\n\n",
                  "what colors are strawberries?\n(a)Yellow\n(b)Red\n(c)Blue\n\n"
                  ]

class Question():
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer
#a=Question(question_prompts[0],"a")

questions=[
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b")

]
def run_test(questions):
    score=0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)




