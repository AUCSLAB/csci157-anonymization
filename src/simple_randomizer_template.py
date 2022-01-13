'''
Copyright 2022 Garegin Grigoryan (grigoryan@alfred.edu)

This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import sys
import numpy as np

def randomized_response(truthfull_response):
    '''
    Takes a truthfull response (integer) and  returns a randomized response (integer) according to the algorithm:
           Step 1. Toss a coin.
           Step 2.1. If heads (1), return the truthfull response.
           Step 2.2. If tails (0), then toss the coin again and return the corresponding response.
    '''
    # Write your code for 1 and 2.1

    # Step 2.2    
    return np.random.randint(0,2)

class SimpleRandomizer:
    def run(self, responses_filename, output_filename):
        '''
        Method that randomizes the responses of the survey.
        Input: name of the file with the responses, name of the file for the randomized responses.
        Implementation: for each question, call the function randomized_response for a randomazitaion.
        '''     

        try:
            responses = open(responses_filename, 'r')
        except:
            print(f'File {responses_filename} is not present in this folder. Exiting.')
            sys.exit(1)

        data = responses.readlines()
        responses.close()

        dp_responses = open(output_filename, 'w')
   
        for line in data:
            parsed = line.split(',')
            dp_responses.write(f'{parsed[0]},{parsed[1]},{parsed[2]},{parsed[3]}')
            for j in range(4, len(parsed)):
                truthfull_response = int(parsed[j])
                # writing the randomized response by calling the function randomized_response
                dp_responses.write(f',{randomized_response(truthfull_response)}')
            dp_responses.write('\n')
            
        dp_responses.close()

if __name__ == '__main__':
    randomizer = SimpleRandomizer()
    randomizer.run('responses.csv', 'randomized_responses.csv')
