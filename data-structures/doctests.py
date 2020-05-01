"""
Tests for cohort_data.py
========================

>>> from cohort_data import *

all_houses
----------

Take in the path to a data file and return a set of all house names in the
file.

>>> sorted(all_houses('cohort_data.txt'))
["Dumbledore's Army", 'Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

students_by_cohort
------------------

Return a list of student names, in alphabetical order, by cohort.

>>> students_by_cohort('cohort_data.txt')
['Adrian Pucey', 'Alicia Spinnet', 'Andrew Kirke', 'Angelina Johnson', 'Anthony Goldstein', 'Blaise Zabini', 'Cedric Diggory', 'Cho Chang', 'Colin Creevey', 'Cormac McLaggen', 'Dean Thomas', 'Demelza Robins', 'Dennis Creevey', 'Draco Malfoy', 'Eddie Carmichael', 'Eleanor Branstone', 'Eloise Midgeon', 'Ernie Macmillan', 'Euan Abercrombie', 'Fred Weasley', 'George Weasley', 'Ginny Weasley', 'Graham Pritchard', 'Gregory Goyle', 'Hannah Abbott', 'Harry Potter', 'Hermione Granger', 'Jack Sloper', 'Jimmy Peakes', 'Justin Finch-Fletchley', 'Katie Bell', 'Kevin Whitby', 'Laura Madley', 'Lavender Brown', 'Lee Jordan', 'Lisa Turpin', 'Luna Lovegood', 'Malcolm Baddock', 'Mandy Brocklehurst', 'Marcus Belby', 'Marcus Flint', 'Marietta Edgecombe', 'Mary Macdonald', 'Michael Corner', 'Miles Bletchley', 'Millicent Bullstrode', 'Natalie McDonald', 'Neville Longbottom', 'Oliver Wood', 'Orla Quirke', 'Owen Cauldwell', 'Padma Patil', 'Pansy Parkinson', 'Parvati Patil', 'Penelope Clearwater', 'Percy Weasley', 'Ritchie Coote', 'Roger Davies', 'Romilda Vane', 'Ron Weasley', 'Rose Zeller', 'Seamus Finnigan', 'Stewart Ackerley', 'Susan Bones', 'Terence Higgs', 'Terry Boot', 'Theodore Nott', 'Vincent Crabbe', 'Zacharias Smith']

>>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
['Angelina Johnson', 'Cho Chang', 'Colin Creevey', 'Dennis Creevey', 'Draco Malfoy', 'Eddie Carmichael', 'Harry Potter', 'Hermione Granger', 'Mandy Brocklehurst', 'Michael Corner', 'Oliver Wood', 'Penelope Clearwater', 'Ron Weasley', 'Seamus Finnigan', 'Terence Higgs', 'Theodore Nott']

>>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
['Adrian Pucey', 'Andrew Kirke', 'Anthony Goldstein', 'Blaise Zabini', 'Cedric Diggory', 'Eleanor Branstone', 'Ginny Weasley', 'Graham Pritchard', 'Hannah Abbott', 'Lee Jordan', 'Luna Lovegood', 'Marietta Edgecombe', 'Mary Macdonald', 'Natalie McDonald', 'Neville Longbottom', 'Owen Cauldwell', 'Padma Patil', 'Pansy Parkinson', 'Roger Davies', 'Susan Bones']

>>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
['Cormac McLaggen', 'Demelza Robins', 'Eloise Midgeon', 'Ernie Macmillan', 'Jimmy Peakes', 'Justin Finch-Fletchley', 'Laura Madley', 'Lisa Turpin', 'Malcolm Baddock', 'Miles Bletchley', 'Millicent Bullstrode', 'Orla Quirke', 'Parvati Patil', 'Percy Weasley', 'Zacharias Smith']

>>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
['Alicia Spinnet', 'Dean Thomas', 'Euan Abercrombie', 'Fred Weasley', 'George Weasley', 'Gregory Goyle', 'Jack Sloper', 'Katie Bell', 'Kevin Whitby', 'Lavender Brown', 'Marcus Belby', 'Marcus Flint', 'Ritchie Coote', 'Romilda Vane', 'Rose Zeller', 'Stewart Ackerley', 'Terry Boot', 'Vincent Crabbe']

all_names_by_house
------------------

Return a list that contains rosters for all houses, ghosts, and instructors.

Rosters appear in this order:
- Dumbledore's Army
- Gryffindor
- Hufflepuff
- Ravenclaw
- Slytherin
- Ghosts
- Instructors

Each roster is a list of names sorted in alphabetical order.

>>> all_names_by_house('cohort_data.txt')
[['Alicia Spinnet', 'Cho Chang', 'Colin Creevey', 'Dennis Creevey', 'Hannah Abbott', 'Marietta Edgecombe', 'Theodore Nott'], ['Andrew Kirke', 'Angelina Johnson', 'Cormac McLaggen', 'Dean Thomas', 'Demelza Robins', 'Euan Abercrombie', 'Fred Weasley', 'George Weasley', 'Ginny Weasley', 'Harry Potter', 'Hermione Granger', 'Jack Sloper', 'Jimmy Peakes', 'Katie Bell', 'Lavender Brown', 'Lee Jordan', 'Mary Macdonald', 'Natalie McDonald', 'Neville Longbottom', 'Oliver Wood', 'Parvati Patil', 'Percy Weasley', 'Ritchie Coote', 'Romilda Vane', 'Ron Weasley', 'Seamus Finnigan'], ['Cedric Diggory', 'Eleanor Branstone', 'Eloise Midgeon', 'Ernie Macmillan', 'Justin Finch-Fletchley', 'Kevin Whitby', 'Laura Madley', 'Owen Cauldwell', 'Rose Zeller', 'Susan Bones', 'Zacharias Smith'], ['Anthony Goldstein', 'Eddie Carmichael', 'Lisa Turpin', 'Luna Lovegood', 'Mandy Brocklehurst', 'Marcus Belby', 'Michael Corner', 'Orla Quirke', 'Padma Patil', 'Penelope Clearwater', 'Roger Davies', 'Stewart Ackerley', 'Terry Boot'], ['Adrian Pucey', 'Blaise Zabini', 'Draco Malfoy', 'Graham Pritchard', 'Gregory Goyle', 'Malcolm Baddock', 'Marcus Flint', 'Miles Bletchley', 'Millicent Bullstrode', 'Pansy Parkinson', 'Terence Higgs', 'Vincent Crabbe'], ['Bloody Baron', 'Friendly Friar', 'Grey Lady', 'Nearly Headless Nick'], ['Filius Flitwick', 'Minerva McGonagall', 'Pomona Sprout', 'Severus Snape']]

all_data
--------

Return a list of student data.

Each student is a tuple of (full_name, house, advisor, cohort)

>>> all_data('cohort_data.txt')
[('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Minerva McGonagall', '', '', 'I'), ('Laura Madley', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Orla Quirke', 'Ravenclaw', '', 'Spring 2016'), ('Marcus Belby', 'Ravenclaw', 'Flitwick', 'Summer 2016'), ('Euan Abercrombie', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Neville Longbottom', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Vincent Crabbe', 'Slytherin', 'Snape', 'Summer 2016'), ('Parvati Patil', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Mandy Brocklehurst', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Ritchie Coote', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Friendly Friar', '', '', 'G'), ('Eloise Midgeon', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Zacharias Smith', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Filius Flitwick', '', '', 'I'), ('Katie Bell', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Cedric Diggory', 'Hufflepuff', 'Sprout', 'Winter 2016'), ('Ron Weasley', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Cormac McLaggen', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Lisa Turpin', 'Ravenclaw', 'Flitwick', 'Spring 2016'), ('Oliver Wood', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Pansy Parkinson', 'Slytherin', 'Snape', 'Winter 2016'), ('Demelza Robins', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Terry Boot', 'Ravenclaw', 'Flitwick', 'Summer 2016'), ('Lavender Brown', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Anthony Goldstein', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Ernie Macmillan', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Colin Creevey', "Dumbledore's Army", 'McGonagall', 'Fall 2015'), ('Padma Patil', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Cho Chang', "Dumbledore's Army", 'Flitwick', 'Fall 2015'), ('Gregory Goyle', 'Slytherin', 'Snape', 'Summer 2016'), ('Michael Corner', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Luna Lovegood', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Eleanor Branstone', 'Hufflepuff', 'Sprout', 'Winter 2016'), ('Draco Malfoy', 'Slytherin', 'Snape', 'Fall 2015'), ('Marcus Flint', 'Slytherin', 'Snape', 'Summer 2016'), ('Lee Jordan', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Marietta Edgecombe', "Dumbledore's Army", 'Flitwick', 'Winter 2016'), ('Andrew Kirke', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Ginny Weasley', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Mary Macdonald', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Blaise Zabini', 'Slytherin', 'Snape', 'Winter 2016'), ('Millicent Bullstrode', 'Slytherin', 'Snape', 'Spring 2016'), ('Seamus Finnigan', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Eddie Carmichael', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Dean Thomas', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Grey Lady', '', '', 'G'), ('Percy Weasley', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Jack Sloper', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Theodore Nott', "Dumbledore's Army", 'Snape', 'Fall 2015'), ('Terence Higgs', 'Slytherin', 'Snape', 'Fall 2015'), ('Jimmy Peakes', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Natalie McDonald', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Justin Finch-Fletchley', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Pomona Sprout', '', '', 'I'), ('Rose Zeller', 'Hufflepuff', 'Sprout', 'Summer 2016'), ('Miles Bletchley', 'Slytherin', 'Snape', 'Spring 2016'), ('Stewart Ackerley', 'Ravenclaw', 'Flitwick', 'Summer 2016'), ('Adrian Pucey', 'Slytherin', 'Snape', 'Winter 2016'), ('Fred Weasley', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Severus Snape', '', '', 'I'), ('Hannah Abbott', "Dumbledore's Army", 'Sprout', 'Winter 2016'), ('Nearly Headless Nick', '', '', 'G'), ('Graham Pritchard', 'Slytherin', 'Snape', 'Winter 2016'), ('George Weasley', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Hermione Granger', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Penelope Clearwater', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Malcolm Baddock', 'Slytherin', 'Snape', 'Spring 2016'), ('Angelina Johnson', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Susan Bones', 'Hufflepuff', 'Sprout', 'Winter 2016'), ('Dennis Creevey', "Dumbledore's Army", 'McGonagall', 'Fall 2015'), ('Roger Davies', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Romilda Vane', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Alicia Spinnet', "Dumbledore's Army", 'McGonagall', 'Summer 2016'), ('Bloody Baron', '', '', 'G'), ('Kevin Whitby', 'Hufflepuff', 'Sprout', 'Summer 2016'), ('Owen Cauldwell', 'Hufflepuff', 'Sprout', 'Winter 2016')]

get_cohort_for
--------------

Given someone's name, return the cohort they belong to.

>>> get_cohort_for('cohort_data.txt', 'Harry Potter')
'Fall 2015'

>>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
'Winter 2016'

>>> get_cohort_for('cohort_data.txt', 'Balloonicorn')

find_duped_last_names
---------------------

Return a set of duplicated last names that exist in the data.

>>> sorted(find_duped_last_names('cohort_data.txt'))
['Creevey', 'Patil', 'Weasley']

get_housemates_for
------------------

Return a set of housemates for the given student.

Given a student's name, return a list of their housemates. Housemates are
students who belong to the same house and were in the same cohort as the
given student.

>>> housemates = get_housemates_for('cohort_data.txt', 'Hermione Granger')
>>> type(housemates) is set
True
>>> if housemates:
...     print(sorted(housemates))
...
['Angelina Johnson', 'Harry Potter', 'Oliver Wood', 'Ron Weasley', 'Seamus Finnigan']

"""
