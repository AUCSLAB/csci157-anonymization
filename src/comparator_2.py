import sys

class Comparator:
    def run(self, original_filename, deanonymized_filename):
        try:
            original = open(original_filename, 'r')
        except:
            print(f'File {original_filename} is not present in this folder. Exiting.')
            sys.exit(1)

        try:
            deanonymized = open(deanonymized_filename, 'r')
        except:
            print(f'File {deanonymized_filename} is not present in this folder. Exiting.')
            sys.exit(1)

        original_db, deanonymized_db = original.readlines(), deanonymized.readlines()
        original.close()   
        deanonymized.close()
        if len(original_db) == 0 or len(deanonymized_db) == 0:
            print('Empty file(s). Exiting')
            sys.exit(1)


        # key: (first name, last name); value: responses (e.g., '011')
        responses_dictionary = {}


        for line in original_db:
            parsed = line.split(',')
            first_name, last_name = parsed[0], parsed[1]
            responses_dictionary[(first_name, last_name)] = parsed[4] + parsed[5] + parsed[6][:-1]

        match, mismatch = 0, 0
        for line in deanonymized_db:
            parsed = line.split(',')
            first_name, last_name = parsed[0], parsed[1]
            answers = parsed[4] + parsed[5] + parsed[6][:-1]

            if (first_name, last_name) not in responses_dictionary or responses_dictionary[(first_name, last_name)] != answers:
                mismatch += 1
            else:
                match += 1

        return match, mismatch

if __name__ == '__main__':
    c = Comparator()
    match, mismatch = c.run('responses.csv', 'randomized_responses.csv')
    print(f'Percent of the identical answers: {round(match*100/(mismatch+match), 2)}%') 
