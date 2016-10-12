class Pair:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __dict__(self):
        return {'question': question, 'answer': answer}

    def __tuple__(self):
        return (question, answer)
