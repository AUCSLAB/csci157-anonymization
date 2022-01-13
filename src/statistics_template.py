'''
Copyright 2022 Garegin Grigoryan (grigoryan@alfred.edu)

This work is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit
http://creativecommons.org/licenses/by-nc-sa/4.0/.
'''

import sys

def add_data(dct, key, pizza, pasta, burgers):
    dct[key]['pizza'] += pizza
    dct[key]['pasta'] += pasta
    dct[key]['burgers'] += burgers

class Statistics:
    def __init__(self, zipcodes, age_groups):
        ''' Constructor: inintializes dictionaries self.zipcodes and self.age_groups
            with counters per each food (initially 0)'''
        self.zipcodes = {}
        for zipcode in zipcodes:
            self.zipcodes[zipcode] = {'pizza': 0, 'pasta': 0, 'burgers': 0}
            
        self.age_groups = {}
        for age_group in age_groups:
            self.age_groups[age_group] =  {'pizza': 0, 'pasta': 0, 'burgers': 0}

    def read(self, responses_filename):
        try:
            responses = open(responses_filename, 'r')
        except:
            print(f'File {responses_filename} does not exist')
            sys.exit(1)

        data = responses.readlines()

        for line in data:
            parsed = line.split(',')
            dob = parsed[2]
            year = int(dob.split('/')[2])
            age_group = (year // 10) * 10
            zipcode, pizza, pasta, burgers = parsed[3], int(parsed[4]), int(parsed[5]), int(parsed[6])

            add_data(self.zipcodes, zipcode, pizza, pasta, burgers)
            add_data(self.age_groups, age_group, pizza, pasta, burgers)

    def favorite_by_zipcode(self):
        ''' Prints the favorite food for each ZIP code in self.zipcodes '''

        ''' Implementation:
                - Step 1. Iterate through the dictionary self.zipcodes
                    - Step 2. Initialize variable favFood to store the favorite food 
                    - Step 3: Initialize variable favCounter to store total number of "Yes" answers for the favorite food
                    - Step 4: For each food item (for food in self.zipcodes[zipcode]):
                        - Compare its counter (self.zipcodes[zipcode][food]) with favCounter
                        - If favCounter is smaller, then set favFood to food and favCounter to self.zipcodes[zipcode][food] 
                    - Step 5: Print the ZIP code and the favorite food item on the screen
        '''
        print('-----Favorite food per each zipcode')
       # Step 1
        for zipcode in self.zipcodes:
           # Step 2
           favFood = None
           # Step 3
           favCounter = 0
           # Steps 4: Write a loop here

           # Step 5
           print(f'{zipcode}: {favFood}')
       
       
    def favorite_by_agegroup(self):
        ''' Prints the favorite food for each age group in self.age_groups '''
        
        ''' Implementation:
                - Step 1. Iterate through the dictionary self.age_groups
                    - Step 2. Initialize variable favFood to store the favorite food 
                    - Step 3: Initialize variable favCounter to store total number of "Yes" answers for the favorite food
                    - Step 4: For each food item (for food in self.age_groups[age_group]):
                        - Compare its counter (self.age_groups[age_group][food]) with favCounter
                        - If favCounter is smaller, then set favFood to food and favCounter to self.age_groups[age_group][food] 
                    - Step 5: Print the age group and the favorite food item on the screen
        '''
        
        print('-----Favorite food per each age group')
        for age_group in self.age_groups:
           # Step 2
           favFood = None
           # Step 3
           favCounter = 0
           # Steps 4: Write a loop here

           # Step 5
           print(f'{age_group}: {favFood}')
            

                        
if __name__ == '__main__':
    s = Statistics(zipcodes= ('91762', '91763', '91764'), age_groups=(1960, 1970, 1980))
    
    print('Original responses')
    s.read('responses.csv')
    s.favorite_by_zipcode()
    s.favorite_by_agegroup()

    #reset the counters
    s = Statistics(zipcodes= ('91762', '91763', '91764'), age_groups=(1960, 1970, 1980))
    
    print('---------------------')
    print('Randomized responses')
    s.read('randomized_responses.csv')
    s.favorite_by_zipcode()
    s.favorite_by_agegroup()


                        
                    
        

            
