# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem

def person_lister(f):
    def inner(people):
        # complete the function
        return [f(person) for person in sorted(people, key=lambda x: int(x[2]))]
    return inner
