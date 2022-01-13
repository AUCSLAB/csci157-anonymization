# CSCI-157 Anonymization
Reviewing Python while learning about data privacy and anonymization.

### Objectives

In this assignment, you will:
* Review basic Python syntax and data structures, such as loops, functions, list, dictionaries and classes.
* Use Python to work with files.
* Learn about privacy issues resulting from data release.
* Use Python dictionaries to perform a join of two datasets.
* Learn about the limitations of simple data anonymization techniques.
* Apply a simple differential privacy technique.
* Use Python dictionaries to compute statistics over a dataset.

### Useful Resources

Review the lecture notes and provided example code for a review of Python 
syntax.  You will also want to read the Python references provided below:

* [Python Documentation](https://docs.python.org/3/index.html)
  * [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
  * [Python Input Output and Files](https://docs.python.org/3/tutorial/inputoutput.html)
  * [Python Classes](https://docs.python.org/3/tutorial/classes.html)
* [Help Sheets](https://github.com/AUCSLAB/csci157-anonymization/tree/main/help)
  * [Basics, strings, functions, loops](https://github.com/AUCSLAB/csci157-anonymization/blob/main/help/Python%20help%20sheet%201.pdf)
  * [Lists, tuples, files, dictionaries, sets](https://github.com/AUCSLAB/csci157-anonymization/blob/main/help/Python%20help%20sheet%202.pdf)

## Background: Anonymization

Suppose you are working for Company X and your team is tasked with producing a 
health record data set to be released to the participants in an upcoming 
hackathon. Your colleague removed the columns for names and says that the data 
is ready to go but you aren't convinced. After reviewing the data set, you are 
concerned that if someone were to combine your "anonymous" data with other 
publicly available sources there could be trouble. Unfortunately  your colleague
doesn't share in your concerns and requires proof.

Is this so far fetched? In 2007, Netflix held a competition to improve their 
recommendation algorithms. This required releasing a large amount of anonymous 
data from their customers' movie ratings and viewing histories. By combining the
Netflix data set with the Internet movie database (IMDb) site data, [researchers 
found a way to link the identity of a Netflix user to a user's IMDb profile 
based on the select reviews that they published](https://ieeexplore.ieee.org/document/4531148).

With more data being generated and released (and redacted) every day, this is 
not limited to an old and irrelevant data set. Consider the APIs that expose 
locations of bikeshare/scooter information (e.g., [NABSA](https://github.com/NABSA/gbfs)).
Making these locations publicly available through an API allows for this data to
be incorporated into ecosystems that extend beyond the provider's control. As a 
result you can get useful features like Google maps providing walking directions
to the closest scooter/bike within a city, regardless of the service provider. 
But what is the cost of this? After all, these locations are public knowledge 
since we can physically see these bikes and scooters on the street. So the exact
location of a scooter at a given time may not expose much. What about the pairs 
of start and end locations along with the date and time of usage? Now we can 
track usage habits at a particular location and possibly an address. Combining 
this data and auxiliary information we may be able to identify a set of 
candidates that are using the scooters. Further analysis may expose things such 
as daily habits -- particularly when someone normally leaves their house and 
returns, exposing further sensitive information. Fortunately there are 
[techniques to thwart this](https://gretel.ai/blog/using-generative-differentially-private-models-to-build-privacy-enhancing-synthetic-datasets-from-real-data).

To address this we have two main problems to tackle: (i) maintain the 
statistical relevance of the sensitive data and (ii) protect the people 
represented by the data. Fortunately, there is a well-studied body of tools and 
techniques under the umbrella of differential privacy for exactly this purpose. 
By training a model to understand an originally sensitive, but anonymized, data 
set we can generate synthetic data that looks statistically similar but further 
protects the individuals contained within. To see more about this, you can read 
[the blog post by Alexander Watson] (https://gretel.ai/blog/using-generative-differentially-private-models-to-build-privacy-enhancing-synthetic-datasets-from-real-data) and follow along with the example notebook they provide to understand further. 

## Assignments

You were assigned to process data of a survey among three age groups from three ZIP codes. The purpose of this survey was to find the answer to the following questions:

* What is the most popular food in each ZIP code among pizza, pasta, and burgers?
* What is the most popular food for each age group among pizza, pasta, and burgers?

Your task is to protect the anonymity of the responses while sharing the respondents' date of birth and ZIP codes. You will investigate two anonymization techniques:

* Eliminating respondents' first and last names from the database (Homework 1).
* Response randomization, a toy differential privacy technique (Homework 2).

### Setup

All files for both homework are present in the `/src` directory. The directory includes two artificial databases in the form of .csv files (names and DOB are generated via [Mockaroo](https://mockaroo.com)).
* `voters.csv`: 
  * Structure: First Name, Last Name, Birthday, Zipcode
  * Description: artificial "voters" database for zipcodes 91762, 91763, 91764 from three age groups: people born in 1960s, 1970s and 1980s.
* `responses.csv`:
  * Structure: First Name, Last Name, Birthday, Zipcode, Question 1, Question 2, Question 3
  * Description: artificial "voters" "responses" to the following sensitive questions (0: No, 1: Yes):
    * Do you like pizza?
    * Do you like pasta?
    * Do you like burgers?
   
  The answers were generated using `/src/tools/data_generator.py` script. You do not need to run this script to complete any of assignments.

### Homework 1

In this homework, you will investigate a simple method for ensuring survey anonymity, such as eliminating respondents' first and last names from the database.

#### Problem 1

This step is our first attempt to anonymize the data from `src/responses.csv` by replacing the first and last names of respondents with "Person #1", "Person #2", "Person #3", etc. 

Complete the method ```.run(..)``` in `src/simple_anonymizer_template.py` to store the nameless responses into the file `anonymous_responses.csv`. Follow the instructions given in the template.

Rename `simple_anonymizer_template.py` to `simple_anonymizer.py` and submit it.  

#### Problem 2

In this step you will show the vulnerability of our simple anonymizer. Using the "publicly available" artificial voters' database `voters.csv`, you need to de-anonymize  `anonymous_responses.csv` by matching Date of Birth (DOB) and ZIP code fields of these databases.

In `src\simple_deanonimyzer_template.py`, the constructor of the class ```SimpleDeanonymizer``` initializes ```self.voters_dictionary``` from the `voters.csv` by storing the tuple ```(dob, zipcode)``` as keys and the tuple ```(first_name, last_name)``` as values.

Your task is to complete the method  ```.run(..)``` to match the DOB and ZIP codes from `anonymous_responses.csv` with ```self.voters_dictionary```, obtain the first and last names of each respondents and store the de-anonymized responses into the file `deanonymized_responses.csv`. Note that using a dictionary data structure for matching two datasets guarantees O(n) linear running time for the de-anonymization algorithm.

One you are done with this task, you may compare the approximate correctness of your de-anonymization using `src\comparator_1.py' that compares the answers in the original file `src/responses.csv` with the answers in the de-anonymized file `deanonymized_responses.csv`.

Rename `simple_deanonimyzer_template.py` to `simple_deanonimyzer.py` and submit it.  

### Homework 2

In this homework, you will investigate a simple alternative to the anonymization you did from Homework 1. Specifically, you will use (response randomization)[https://en.wikipedia.org/wiki/Differential_privacy#Randomized_response] - a toy differential privacy technique. 

#### Problem 1

In this step you will use a simple differential privacy algorithm for anonymization. Instead of replacing names of the respondents (as in Homework 1), for each of 3 questions, your program will:

* Toss a coin (use an external/built-in library to randomly generate 0 or 1).
* If it heads (1), store the truthful response.
* If it tails (0), then toss the coin again and write its outcome (0 or 1).

Complete the function ```randomized_response(truthfull_response)``` in `src\simple_randomizer_template.py` to generate the randomized responses.

Similar to the previous homework, once your code is working, you may compare the original responses with the randomized responses using `src\comparator_2.py`.

Rename `simple_randomizer_template.py` to `simple_randomizer.py` and submit it.  

#### Problem 2

Now is the time to produce the answer to the survey questions based on the responses. Specifically, you will compare the original file `src\responses.csv` and `randomized_responses.csv` and see if they produce similar results.

In `src\statistics_template.py`, the method ```.read(responses_filename)``` of the class ```Statistics``` stores the survey responses into two dictionaries:

* self.zipcodes with keys 91762, 91763, 91764
* self.age_groups with keys 1960, 1970, 1980.

Per each key, these dictionaries contain values of the dictionary format ```{'pizza': <int>, 'pasta': <int>, 'burgers': <int>}``` where the integer values are the counters of the "Yes" responses.

Example: 
```
>>> s = Statistics()
>>> s.read('responses.csv')
>>> print(s.zipcodes)
{91762: {'pizza': 10, 'pasta': 4, 'burgers': 25}, 91763: {'pizza': 33, 'pasta': 44, 'burgers': 15}, 91764: {'pizza': 4, 'pasta': 1, 'burgers': 2}
```
Your task is to complete methods ```.favorite_by_zipcode(self)``` and ```.favorite_by_agegroup(self)``` that find and print the most favorite food per each ZIP code and age group. Compare the results from the original survey and randomized survey and see if they match. 

Rename `statistics_template.py` to `statistics.py` and submit it.

### Collaboration policy

You may work in groups for this homework. Make sure to specify group members in the comments of the code files you submit.

## Revision History
* Summer 2021 - Initial project draft developed as part of the [Mozilla Responsible Computer Science Challenge](https://foundation.mozilla.org/en/what-we-fund/awards/responsible-computer-science-challenge/) by:
    * Joshua Caskie (jmcaskie@buffalo.edu)
    * Alexander Fernandez (adfernan@buffalo.edu)
    * Garegin Grigoryan (grigoryan@alfred.edu)
    * Andrew Hughes (ahughes6@buffalo.edu)
    * Macy McDonald (macymcdo@buffalo.edu)
* Spring 2022 - Adapted for CSCI-157 by Garegin Grigoryan (grigoryan@alfred.edu)
