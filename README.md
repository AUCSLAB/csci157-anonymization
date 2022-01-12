# CSCI157 Anonymization
Reviewing basic Python while learning about data privacy and anonymization

## Objectives

In this assignment, you will:
* Review basic Python syntax and data structures, such as loops, functions, list, dictionaries and classes.
* Use Python to work with files.
* Learn about privacy issues resulting from data release.
* Use Python dictionaries to perform a join of two datasets.
* Learn about the limitations of simple data anonymization techniques.
* Apply a simple differential privacy technique.
* Use Python dictionaries to compute statistics over a dataset.

## Useful Resources

Review the lecture notes and provided example code for a review of Python 
syntax.  You will also want to read the Python references provided below:

* [Python Documentation](https://docs.python.org/3/index.html)
  * [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
  * [Python Input Output and Files](https://docs.python.org/3/tutorial/inputoutput.html)
  * [Python Classes](https://docs.python.org/3/tutorial/classes.html)
  * [Mutable HashMap](https://www.scala-lang.org/api/current/scala/collection/mutable/HashMap.html)
* [Help Sheets](https://github.com/AUCSLAB/csci157-anonymization/tree/main/help)
  * [Basics, strings, functions, loops] (https://github.com/AUCSLAB/csci157-anonymization/blob/main/help/Python%20help%20sheet%201.pdf)
  * [Lists, tuples, files, dictionaries, sets] (https://github.com/AUCSLAB/csci157-anonymization/blob/main/help/Python%20help%20sheet%202.pdf)

---

## Anonymization: bakcground

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
[the blog post by Alexander Watson](https://gretel.ai/blog/using-generative-differentially-private-models-to-build-privacy-enhancing-synthetic-datasets-from-real-data) and follow along with the example notebook they provide to understand further.
---

## Assignment desicription

#### Homework 1

##### Problem 1
