from api.problems import problem1, problem2, problem3


class Problems:

    def __init__(self, input, problem):
        self.input = input
        self.problem = problem

    def solve(self):
        return eval("%s.resolve(self.input)" % self.problem)
