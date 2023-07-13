# QUIZLER
## Introduction

This is a simple python script that allows to generate rapid, randomized in-class quizzes from a predefined set of questions. Quizlet allows:
* to quickly generate a quiz from a set of questions, without having to manually select the questions. 
* to generate a quiz that is different from the one generated for another group of students.
* to random assign a different group to a student at every iteration.
* to quickly grade the quizzes.
## Usage
### Questions database
The questions are stored in a csv file, with the following format:
```
[Question Group], Question, Answer
```
* Question group - optional - integer value that allows to group questions together. If not specified, the question will be assigned to different groups. The questions in this same group will *NOT* be assigned to the same quiz group.
* Question - the question to be asked.
* Answer - the answer to the question. 

Note: the csv file must be comma-separated and must not contain any empty lines.

### Students database
The students are stored in a csv file, with the following format:
```
Name, Surame, Student ID
```
* Name - the name of the student.
* Surname - the surname of the student.
* Student ID - the student ID as a sequence of numbers and letters (it is used to compute student groups).

### JSON configuration file
The JSON file is used to configure the quiz generation. The following parameters are available:
* name (string, optional): Title of your quiz. It is recommended to include the date.
* question_grouping (boolean, optional): Determines if the questions are grouped in exclusive sets. Default value is false.
* students_list (string, required): File with a list of students.
* questions_list (string, required): File with a list of questions.
* questions_count (integer, required): Number of questions in the quiz.
* group_count (integer, required): Number of groups in the quiz.
* group_computation (array, optional): An array of arrays representing computations for each group. Each sub-array contains a prefix item representing the operation ("add", "subtract", "multiply", "sum", or "take") followed by an integer.
* two_column (boolean, optional): If the number of groups is even, each slide will assign the same question to two different groups. Default value is true.
* repeat_questions (boolean, optional): Allows questions to be repeated on multiple slides. Note that questions will not be repeated within a group. Default value is false.
* slide_template (string, optional): Template of the TeX file used to generate the final presentation. Default value is "quiz_slides_template.tex".

### Generating the quiz
To generate the quiz, run the following command:
```
python quizler.py <config_file.json>
```
### Group computation
The group computation is used to assign students to groups. The core idea is that each student is assigned a unique ID (e.g., student ID) and the group computation is used to compute the group number from the student ID. Let's consider the following example:
1. The student ID is 123456789.
2. The first step is to take three last digits of the student ID: 789.
3. The second step is to add 1 to the number: 790.
4. The third step is to sum the digits of the number: 7+9+0=16.
5. The fourth step is to multiply the number by 2: 16*2=32.
6. The fifth step is to compute modulo 5 of the number: 32%5=2.
7. The final group number is 2.

The group computation is specified in the JSON file as an array of arrays. Each sub-array contains a prefix item representing the operation ("add", "subtract", "multiply", "sum", or "take") followed by an integer. The operations are applied in the order they are specified in the array. 

### Output files
All the resulting files are stored in the folder named as the configuration file.
The script generates the following files:
* questions_in_groups.txt - the list of questions in each group.
* questions_in_groups.tex - the list of questions in each group in TeX format (can be compiled to PDF).
* questions_in_slides_raw.txt - the list of questions in each slide.
* <quiz_name>.tex - the TeX file with the quiz.
* students_groups.vsv - the list of students and their groups.
* students_with_answers.txt - the list of students and the correct answers.

### Two-column slides
In some cases when there is a large number of groups, it is convinient to have two-column slides. In this case, the same question is assigned to two different groups. This is useful when the number of groups is even. To enable two-column slides, set the "two_column" parameter to true in the JSON configuration file.

### Examples 
In the Examples folder you can find an example configuration file and the corresponding input files.

## Contact 
If you have any questions, please contact me at: [tomasz.kucner@aalto.fi](mailto:tomasz.kucner@aalto.fi)

## Bugs and feature requests
If you find any bugs or have any feature requests, please use the [GitHub issue tracker](https://github.com/tkucner/quizler/issues).