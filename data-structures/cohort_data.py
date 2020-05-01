"""Functions to parse a file containing student data."""

def generate_cohort_info_list(file):
  """Accept a text file of cohort info and return a list with student info.

  Each item in list is structured as [first_name, last_name, house, /
  adviser, cohort_name]
  """

  cohort_data = open(file)
  cohort_list = []
  for line in cohort_data:
    line = line.rstrip()
    words = line.split("|")
    first_name, last_name, house, adviser, cohort_name = words
    cohort_list.append([first_name, last_name, house, adviser, cohort_name])
  return cohort_list

def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    houses = set()
    person_info = generate_cohort_info_list(filename)
    for person in person_info:
      if person[2] != "":
        houses.add(person[2])

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []

    person_info = generate_cohort_info_list(filename)

    for person in person_info:
      full_name = person[0] + " " + person[1]
      if cohort == 'All':
        if len(person[4]) > 1:
          students.append(full_name)
      elif person[4] == cohort:
        students.append(full_name)

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    all_houses = ["Dumbledore's Army", "Gryffindor", "Hufflepuff", "Ravenclaw", 
                  "Slytherin", "G", "I"]

    names_by_house = [[], [], [], [], [], [], []]

    person_info = generate_cohort_info_list(filename)
    index = -1 

    for house in all_houses:
      index += 1
      for person in person_info: 
        full_name = person[0] + " " + person[1]
        if person[2] == house:
          names_by_house[index].append(full_name)
        elif person[4] == "G":
          names_by_house[5].append(full_name)
        elif person[4] == "I":
          names_by_house[6].append(full_name)

    names_by_house[5] = list(set(names_by_house[5]))
    names_by_house[6] =list(set(names_by_house[6]))

    for name in names_by_house:
      name.sort()      

    return names_by_house


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """
    
    all_data = []

    person_info = generate_cohort_info_list(filename)

    for person in person_info:
      full_name = person[0] + " " + person[1]
      all_data.append((full_name, person[2], person[3], person[4]))

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """
    person_info = generate_cohort_info_list(filename)

    for person in person_info:
      full_name = person[0] + " " + person[1]
      if full_name == name:
        return person[4]

    return None


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    last_names = []
    repeated_last_names = []

    person_info = generate_cohort_info_list(filename)

    for person in person_info:
      last_names.append(person[1])

    for name in last_names:
      count = last_names.count(name)
      if count > 1:
        repeated_last_names.append(name)

    return list(set(repeated_last_names))


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    # TODO: replace this with your code

    person_info = generate_cohort_info_list(filename)

    housemates = []

    for person in person_info:
      full_name = person[0] + " " + person[1]
      if full_name == name:
        house = person[2]
        cohort = person[4]
        break 

    for person in person_info:
      full_name = person[0] + " " + person[1]
      if person[2] == house and person[4] == cohort:
        housemates.append(full_name)
    
    housemates.remove(name)

    return set(housemates)




##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
