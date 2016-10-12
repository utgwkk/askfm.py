from . import parser


class Answers:
    def __init__(self, answers):
        self._count = 0
        self._answers = parser.parse(answers)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def __len__(self):
        return len(self._answers)

    def next(self):
        if self._count >= len(self._answers):
            raise StopIteration
        retval = self._answers[self._count]
        self._count += 1
        return retval
