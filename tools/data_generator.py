import random
import numpy as np

'''
3 questions (yes/no): Love pizza? Love pasta? Love burgers?

91762 1960s    25%   80%  10%
91762 1970s    30%   65%   20%
91762 1980s    45%   60%   40%
91763 1960s    10%   30%  65%
91763 1970s    15%  20%  75%
91763 1980s    25%  10%   95%
91764 1960s    55%   25%  15%
91764 1970s    70%   15%   25%
91764 1980s    85%   5%   35%

'''
def get_distributions():
    d =  {(91762, 1960): [0.25, 0.80, 0.10], (91762, 1970): [0.30, 0.65, 0.20], (91762, 1980): [0.45, 0.60, 0.40],
             (91763, 1960): [0.10, 0.30, 0.65], (91763, 1970): [0.15, 0.20, 0.75], (91763, 1980): [0.25, 0.10, 0.95],
             (91764, 1960): [0.55, 0.25, 0.15], (91764, 1970): [0.70, 0.15, 0.25], (91764, 1980): [0.85, 0.05, 0.35]}

    return d

def gen_answer(yob, zipcode):
    d = get_distributions()

    distr = d[(zipcode, (yob // 10)*10)]
    
    pizza = np.random.choice(np.arange(0, 2), p=[1-distr[0], distr[0]])
    pasta = np.random.choice(np.arange(0, 2), p=[1-distr[1], distr[1]])
    burgers = np.random.choice(np.arange(0, 2), p=[1-distr[2], distr[2]])

    return pizza, pasta, burgers

            
if __name__ == '__main__':
    voters = open('voters.csv', 'r')
    data = voters.readlines()
    random.shuffle(data)
    health_data = open('responses.csv', 'w')
    for line in data:
        n = random.randint(1, 5)
        if n == 5:
            continue
        parsed = line.split(',')
        yob = int(parsed[2].split('/')[2])
        zipcode = int(parsed[3])
        pizza, pasta, burgers = gen_answer(yob, zipcode)
        health_data.write(f'{parsed[0]},{parsed[1]},{parsed[2]},{zipcode},{pizza},{pasta},{burgers}\n')
    health_data.close()
