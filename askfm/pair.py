class Pair:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __iter__(self):
        return iter({'question': self.question, 'answer': self.answer}.items())
