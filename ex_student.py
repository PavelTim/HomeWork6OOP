from student import Student, Lecturer, Reviewer
from random import randint, seed
from pprint import pprint

def average_student(students, course):
    ''' Задание 4.
    Функция, подсчитывающая среднюю оценку за курс '''

    if not students:
        return 0
    average_ = 0
    i_ = 0
    for student in students:
        if course in student.courses_in_progress and student.average_course(course):
            average_ += student.average_course(course)
            i_ += 1
    if i_:
        average_ = average_ / i_
    else:
        return 0
    return round(average_, ndigits=2)

def average_lecturer(lecturers, course):
    ''' Задание 4.
    Функция, подсчитывающая среднюю оценку за курс '''

    if not lecturers:
        return 0
    average_ = 0
    i_ = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached and lecturer.average_course(course):
            average_ += lecturer.average_course(course)
            i_ += 1

    if i_:
        average_ = average_ / i_
    else:
        return 0
    return round(average_, ndigits=2)

def init():
    pass
def _print_dict_lecturers(list_dict_):

    print('+++++++++++++++++++ печать списка словарей +++++++++++++++++++++++')
    for dict_ in list_dict_:
        print(dict_['name'], dict_['surname'], dict_['courses'])

def _print_list_mentors(list_, name_):

    print(f'+++++++++++++++++++ печать списка {name_} +++++++++++++++++++++++')
    for mentor_ in list_:
        print(mentor_.name, mentor_.surname, mentor_.courses_attached)
    print(f'-------------------  конец списка {name_} -----------------------')

def _print_list_students(list_, name_):

    print(f'+++++++++++++++++++ печать списка {name_} +++++++++++++++++++++++')
    for student_ in list_:
        print(student_.name, student_.surname, student_.courses_in_progress)
    print(f'-------------------  конец списка {name_} -----------------------')

def ismentorlistname(list_, name, surname):
    for mentor_ in list_:
        if mentor_.name == name and mentor_.surname == surname:
            return True
    return False

def ismentorlistcourse(list_, course):
    for mentor_ in list_:
        if course in mentor_.courses_attached:
            return True
    return False

def get_data():
    student_names = [('Harry', 'Potter', 'male'),
                     ('John', 'Rembo', 'male'),
                     ('Lucius', 'Malfoy', 'male'),
                     ('Miles', 'Vorkosigan', 'male'),
                     ('Germione', 'Granger', 'female'),
                     ('Emma', 'Watson', 'female'),
                     ('Ronald', 'Weasley', 'male'),
                     ('Wazzdakka', 'Gutsmek', 'lichen')]
    lecturer_names = [('Albert', 'Einstein', 'physics'),
                     ('Emmy', 'Noether', 'physics', 'abstract algebra', 'mathematical physics'),
                     ('David', 'Hilber', 'abstract algebra'),
                     ('Guido', 'van Rossum', 'Python', 'Java'),
                     ('James', 'Gosling', 'Java', 'Python'),
                     ('Bjarne', 'Stroustrup', 'Python', 'Java'),
                     ('Severus', 'Snape', 'defense against the dark arts', 'Potions'),
                     ('Salazar', 'Slytherin', 'defense against the dark arts', 'Potions', 'dark arts'),
                     ('Donatien', 'de Sade', 'artistic spanking'),
                     ('Bellatrix', 'Lestrange', 'artistic spanking', 'dark arts')]
    courses = ['physics', 'abstract algebra', 'mathematical physics', 'Python', 'Java',
               'defense against the dark arts', 'Potions', 'dark arts', 'artistic spanking']

    lecturer_list = []
    for lecturer_ in lecturer_names:
        lecturer_dict = {}
        lecturer_dict['name'] = lecturer_[0]
        lecturer_dict['surname'] = lecturer_[1]
        lecturer_dict['courses'] = lecturer_[2:]
        lecturer_list.append(lecturer_dict)
    # pprint(lecturer_list, sort_dicts=False)

    return [student_names[:], courses[:], lecturer_list[:]]

def get_students_list(student_names, courses):

    students = []
    set_activ_courses = set()
    # print('++++++++++++++ курсы', courses)
    # print('++++++++++++++ имена студентов', student_names)
    for student_name_ in student_names:
        student_ = Student(student_name_[0], student_name_[1], student_name_[2])
        for i in range(randint(1, 4)):
            course_ = courses[randint(0, len(courses) - 1)]
            set_activ_courses.add(course_)
            student_.add_courses(course_)
        students.append(student_)
    # print('\n ###set:', set_activ_courses)
    # any(print(student_.name, student_.surname, student_.courses_in_progress) for student_ in students)
    return set_activ_courses, students

def create_lecturers_lists(set_activ_courses, lecturer_list):

    lecturers, reviewers = [], []
    for course_ in set_activ_courses:
        if not ismentorlistcourse(lecturers, course_):
            filt_ = tuple(filter(lambda x: course_ in x['courses'], lecturer_list))
            if filt_:
                lect_ = filt_[randint(0, len(filt_) - 1)]
                lecturer_list.remove(lect_)
                lecturer = Lecturer(lect_['name'], lect_['surname'])
                lecturer.add_courses(*lect_['courses'])
            else:
                lecturer = Lecturer('Universum', f'Random{randint(100,1000)}')
                lecturer.add_courses(course_)
            lecturers.append(lecturer)
        if not ismentorlistcourse(reviewers, course_):
            filt_ = tuple(filter(lambda x: course_ in x['courses'], lecturer_list))
            if filt_:
                rev_ = filt_[randint(0, len(filt_) - 1)]
                lecturer_list.remove(rev_)
                reviewer = Reviewer(rev_['name'], rev_['surname'])
                reviewer.add_courses(*rev_['courses'])
            else:
                reviewer = Reviewer('Universum', f'Random{randint(100, 1000)}')
                reviewer.add_courses(course_)
            reviewers.append(reviewer)

    return lecturers, reviewers

def test_create():

    student_names, courses, lecturer_list = get_data()
    set_activ_courses, students = get_students_list(student_names, courses)
    lecturers, reviewers = create_lecturers_lists(set_activ_courses, lecturer_list)
    _print_list_mentors(lecturers, 'lecturers')
    _print_list_mentors(reviewers, 'reviewers')
    print(set_activ_courses)
    _print_list_students(students, 'students')

def get_lists():
    student_names, courses, lecturer_list = get_data()
    set_activ_courses, students = get_students_list(student_names, courses)
    lecturers, reviewers = create_lecturers_lists(set_activ_courses, lecturer_list)
    return students, lecturers, reviewers, set_activ_courses

def get_mentor(list_, course):
    ''' Находит ментора по курсу в списке и возвращает на него ссылку '''
    for mentor_ in list_:
        if course in mentor_.courses_attached:
            return mentor_

def test():

    seed('plop plop')
    students, lecturers, reviewers, set_activ_courses = get_lists()

    for i_ in range(5):
        for student_ in students:
            for course_ in student_.courses_in_progress:
                lecturer_ = get_mentor(lecturers, course_)
                reviewer_ = get_mentor(reviewers, course_)
                student_.rate_lecturers(lecturer_, course_, randint(1, 10))
                reviewer_.rate_hw(student_, course_, randint(3, 10))

    for course_ in set_activ_courses:
        print(f'Средняя оценка студентов за курс {course_}: '
              f'{average_student(students, course_)}')
        print(f'Средняя оценка лекторов за курс {course_}: '
              f'{average_lecturer(lecturers, course_)}')
        print()

    for student in students:
        print(student)
    print()
    for lecturer in lecturers:
        print(lecturer)
    print(help(round))

def test_1():
    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student_2 = Student('Emmy', 'Noether', 'female')
    best_student.courses_in_progress += ['Python']
    best_student_2.courses_in_progress += ['Python']
    not_best_student = Student('John James', 'Rambo', 'male')
    not_best_student.courses_in_progress += ['Python']

    # cool_mentor = Mentor('Some', 'Buddy')
    cool_lecturer = Lecturer('SomeLecturer', '1')
    not_cool_lecturer = Lecturer('SomeDude', 'Big')
    cool_reviewer = Reviewer('SomeReviewer', '2')
    # cool_mentor.courses_attached += ['Python']
    cool_lecturer.courses_attached += ['Python']
    cool_reviewer.courses_attached += ['Python']
    not_cool_lecturer.courses_attached += ['Python']

    for _ in range(3):
        cool_reviewer.rate_hw(best_student, 'Python', 10)
        cool_reviewer.rate_hw(best_student_2, 'Python', 10)
    any(cool_reviewer.rate_hw(not_best_student, 'Python', 8) for _ in ['одын', 'дфа', 'тры', 'цытыры'])

    any(best_student.rate_lecturers(cool_lecturer, 'Python', 10) for _ in [1, 2, 3, 4])
    any(not_best_student.rate_lecturers(not_cool_lecturer, 'Python', 4) for _ in [1, 2, 3, 4])

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    print('################# сравнение студентов #########################')
    print(best_student._average_grade(), not_best_student._average_grade())
    print('best_student > not_best_student:', best_student > not_best_student)
    print('best_student < not_best_student:', best_student < not_best_student)
    print('not_best_student > best_student:', not_best_student > best_student)
    print('not_best_student < best_studentt:', not_best_student < best_student)
    print(best_student == not_best_student)
    print(best_student == best_student_2)
    print(best_student != not_best_student)
    print(best_student != best_student_2)
    print('best_student >= not_best_student:', best_student >= not_best_student)
    print('best_student <= not_best_student:', best_student <= not_best_student)

    print('\n################ сравнение лекторов #########################')
    print(cool_lecturer._average_grade(), not_cool_lecturer._average_grade())
    print('cool_lecturer > not_cool_lecturer:', cool_lecturer > not_cool_lecturer)
    print('cool_lecturer < not_cool_lecturer:', cool_lecturer < not_cool_lecturer)

    print('cool_lecturer == not_cool_lecturer:', cool_lecturer == not_cool_lecturer)
    print('cool_lecturer != not_cool_lecturer:', cool_lecturer != not_cool_lecturer)

    print('cool_lecturer >= not_cool_lecturer:', cool_lecturer >= not_cool_lecturer)
    print('cool_lecturer <= not_cool_lecturer:', cool_lecturer <= not_cool_lecturer)

def main():
    # test_1()
    test()
    # test_create()
if __name__ == '__main__':
    main()