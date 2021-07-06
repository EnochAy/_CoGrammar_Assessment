Note down all the findings and conclusions you’re making in a report at the end of the projects
HR Analytics: Job Changes of Data Scientists
HR Analytics: Job Change of Data Scientists. To predict who will move to a new job.
A company which is active in Big Data and Data Science wants to hire data scientists among people who successfully pass some courses which are conducted by the company. Many people sign up for their training. Company wants to know which of these candidates really wants to work for the company after training or looking for a new employment because it helps to reduce the cost and time as well as the quality of training or planning the courses and categorization of candidates. Information related to demographics, education, experience are in hands from candidates signup and enrollment. This dataset is designed to understand the factors that lead a person to leave their current job for HR research too. By model(s) that uses the current credentials,demographics,experience data you will predict the probability of a candidate to look for a new job or will work for the company, as well as interpreting affected factors on employee decision. The whole data is divided to train and test . Target isn't included in the test as this is the variable we are trying to predict.
Problem Definition (Using a What Question): What are the possible factors (features) that could influence a worker's decision to change jobs and work for a company?
Hypothesis: There is no significant relationship between the frequency of change of job by data scientists and Development index of their cities, years of experience, educational level, company size, last new job, and training hours.
 






Note:
The dataset is imbalanced.
Most features are categorical (Nominal, Ordinal, Binary), some with high cardinality.
Missing imputation can be a part of your pipeline as well.
Features
enrollee_id : Unique ID for candidate
city: City code
city_ development _index : Development index of the city (scaled)
gender: Gender of candidate
relevent_experience: Relevant experience of candidate
enrolled_university: Type of University course enrolled if any
education_level: Education level of candidate
major_discipline :Education major discipline of candidate
experience: Candidate total experience in years
company_size: No of employees in current employer's company
company_type : Type of current employer
lastnewjob: Difference in years between previous job and current job
training_hours: training hours completed
target: 0 – Not looking for job change, 1 – Looking for a job change
Inspiration
Predict the probability of a candidate will work for the company
Interpret model(s) such a way that illustrate which features affect candidate decision
















Further Research Questions
Why will an experienced data scientist decide to change jobs?
Answer: An experienced data scientist desires a new job when the current job isn't paying him/her well enough or the working conditions/environments aren't nice enough.

Why do STEM data scientists easily change jobs?
Why do data scientists that get a new job recently still desire to change jobs?
Why do the training hours of data scientists influence their decision to change jobs or not?
Why does the size of the company affect the decision to change jobs or not for a data scientist?



The following outputs show the sum of missing values in the train dataset;
enrollee_id                  0
city                         0
city_development_index       0
gender                    4508
relevent_experience          0
enrolled_university        386
education_level            460
major_discipline          2813
experience                  65
company_size              5938
company_type              6140
last_new_job               423
training_hours               0
target                       0
dtype: int64


The following outputs show the sum of missing values in the test dataset;
enrollee_id                 0
city                        0
city_development_index      0
gender                    508
relevent_experience         0
enrolled_university        31
education_level            52
major_discipline          312
experience                  5
company_size              622
company_type              634
last_new_job               40
training_hours              0
dtype: int64

There are 19158 observations, and 14 variables in the train dataset, while the test dataset consists of 2129 observations and 13 variables, with the exclusion of target, the response variable.


DATA ANALYSIS AND VISUALIZATION
The "target" is 0 implies “Not looking for a job change”, OR, 1 means “Looking for a job change”.

From the visuals, there is no special correlation between the variables with the target function to distinguish the value of the target. Furthermore, categorical variables cannot determine the correlation factor between these variables and the target function.

Also, from the next visual, we can clearly observe that the target has a high dependence on the city_development_index which means candidates from cities with a higher amount of development index tend to move towards the field of data science.



## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

  
## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

  
## Appendix

Any additional information goes here

  
## Authors

- [@EnochAy](https://github.com/EnochAy)
  