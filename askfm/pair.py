class Pair:
    def __init__(self, _id, question, answer):
        self.id = _id
        self.question = question
        self.answer = answer

    def __iter__(self):
        return iter({'id': self.id, 'question': self.question, 'answer': self.answer}.items())
