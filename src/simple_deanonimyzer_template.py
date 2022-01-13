'''
Copyright 2022 Garegin Grigoryan (grigoryan@alfred.edu)

This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import sys

class SimpleDeanonymizer:
    def __init__(self, voters_filename):
        '''
        Initializes voters dictionary given voters database filename.
        self.voters
                - keys: (dob, zipcode)
                - values: (first name, last name)
        '''
        try:
            voters = open(voters_filename, 'r')
        except:
            print(f'File {voters_filename} is not present in this folder. Exiting.')
            sys.exit(1)

        # read voters database into a list of lines    
        voters_db = voters.readlines()
        # initialize the voters dictionary
        self.voters_dictionary = {}    

        for line in voters_db:
            # extract the fields from the voters dictionary: first name, last name, date of birth and zipcode
            parsed = line.split(',')
            try:
                fname, lname, dob, zipcode = parsed[0], parsed[1], parsed[2], parsed[3].rstrip()
            except:
                print(f'Incorrect file format in {voters_filename}')
                sys.exit(1)

            # add a record into the dictionary 
            self.voters_dictionary[(dob, zipcode)] = (fname, lname)

        voters.close()

    def run(self, anonymized_responses_filename, deanonymized_responses_filename):
        '''
        Method that perform the de-anonymization.
        Input: name of the file with the anonymous responses, name of the file for the de-anonymized responses.
        '''
        
        '''
        Steps to implement:
            1. Open the file with anonymous responses.
            2. Store its data into the list of lines "anonymous_data" (using .readlines()) and close that file object.
            3. Create a new file object to store the de-anonymized responses (use the mode 'w' - write).
            4. For each line of the list "anonymous_data":
                 - Use .split(',') method to extract DOB and ZIP code from that line.
                 - If (dob, zipcode) in self.voters_dictionary:
                         a. Extract the corresponding fist and last name from the dictionary.
                         b. Write the first name, last name, dob, zipcode and the answers to the question into "de-anonymized" file object. 
            5. Close the "de-anonymized" file object to write the contents of the file object into the file.               
        '''
        # Step 1
        try:
            anonymized = open(anonymized_responses_filename, 'r')
        except:
            print(f'File {anonymized_responses_filename} is not present in this folder. Exiting.')
            sys.exit(1)

        # Step 2-5: Write your code here


            

if __name__ == '__main__':
    deanonymizer = SimpleDeanonymizer('voters.csv')
    deanonymizer.run('anonymous_responses.csv', 'deanonymized_responses.csv')
    
