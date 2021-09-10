from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []
for question in question_data:
    questionText = question["text"]
    questionAnswer = question["answer"]
    newQuestion = Question(questionText, questionAnswer)
    questionBank.append(newQuestion)

quiz = QuizBrain(questionBank)

while quiz.stillHasQuestions():
    quiz.nextQuestion()
