'''
Copyright 2022 Garegin Grigoryan (grigoryan@alfred.edu)

This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import sys

class SimpleAnonymizer:
    def run(self, responses_filename, output_filename):
        '''
        Method that removes the names of respondents of the survey.
        Input: name of the file with the responses, name of the file for the anonymized responses.
        '''

        '''
        Steps to implement:
              1. Open the original file and store the data into a list of lines "data".
              2. Create a new file object to store the anonymized responses (you may use open(..) function with the writing mode).
              3. Create a counter i (initialize it to one).
              4. For each item of the list "data":
                 - Use .split(',') method to extract fields of the original line (first name, last name, birthday, zipcode and 3 yes/no answers)
                 - Replace the first and the last names with Person<i> and write it into the new file object.
                 - Write the original responses for the 3 questions into the new file object.
                 - Increase the counter i.
              5. Close the new file object to write the contents of the file object into the file.
        '''
        #Step 1
        try:
            responses = open(responses_filename, 'r')
        except:
            print(f'File {responses_filename} is not present in this folder. Exiting.')
            sys.exit(1)

        data = responses.readlines()
        responses.close()

        #Step 2
        noname_responses = open(output_filename, 'w')

        # Steps 3 and 4: write your code

            
        #Step 5
        noname_responses.close()

if __name__ == '__main__':
    anonymizer = SimpleAnonymizer()
    anonymizer.run('responses.csv', 'anonymous_responses.csv')
