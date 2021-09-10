class QuizBrain:
    def __init__(self, qList):
        self.questionNumber = 0
        self.questionList = qList
        self.score = 0
    
    def nextQuestion(self):
        currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber += 1
        input(f"Q.{self.questionNumber}: {currentQuestion.text} (True/False): ")

    def stillHasQuestions(self):
        return self.questionNumber < len(self.questionList)

    def checkAnswer(self, userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"The correct answer was: {correctAnswer}")
        print(f"Your current score is: {self.score}/{self.questionNumber}")
        print("\n")