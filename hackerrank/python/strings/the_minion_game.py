# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    score = dict()
    score['stuart'] = 0
    score['kevin'] = 0
    for i in range(len(string)):
        if string[i] in vowels:
            winner = 'kevin'
        else:
            winner = 'stuart'
        score[winner] += len(string) - i
    if score['stuart'] > score['kevin']:
        print('Stuart', score['stuart'])
    elif score['stuart'] < score['kevin']:
        print('Kevin', score['kevin'])
    else:
        print('Draw')
