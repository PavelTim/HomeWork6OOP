# student.py

class Student:
    ''' class Student '''
    def __init__(self, name, surname, gender):
        ''' Student method. '''
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def add_courses(self, *course_names):
        ''' Student method.'''
        for course_name in course_names:
            if course_name not in self.courses_in_progress:
                self.courses_in_progress.append(course_name)

    def finish_courses(self, course_name):
        ''' Student method.'''
        self.courses_in_progress.remove(course_name)
        self.finished_course.append(course_name)

    def rate(self, reviewer, course, grade):
        ''' Student method. '''
        if isinstance(reviewer, Reviewer) and course in self.courses_in_progress and course in reviewer.courses_attached:
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'

    def rate_lecturers(self, lecturer, course, grade):
        ''' Student method.
        Задание 2. Выставление оценки лекторам
        .rate_lecturers(lecturer: Lecturer, course: str, grade: int) '''
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_course(self, course):
        ''' Student method.
         Задание 4. Средняя оценка студента за курс. '''
        if self.grades.get(course):
            average_ = sum(self.grades[course])/len(self.grades[course])
        else:
            return 0
        return round(average_, ndigits=2)

    def _average_grade(self):
        ''' Student method.
         Задание 3. Средняя оценка студента. '''
        average_ = 0
        i_ = 0
        for _ in self.grades.values():
            if _:
                average_ += sum(_)/len(_)
                i_ += 1
        if i_:
            average_ = average_ / i_
        return round(average_, ndigits=2)

    def __str__(self):
        ''' Student method.
         Задание 3. Переопределение __str__'''

        return (f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за домашние задания: {self._average_grade()}\n'
        f'Курсы в процессе изучения: {" ".join(self.courses_in_progress if self.courses_in_progress else "нет курсов")}\n'
        f'Завершенные курсы: {" ".join(self.finished_courses) if self.finished_courses else "нет курсов" }')

    def __str__(self):
        ''' Student method.
        Переопределено для лучшей печати '''
        str_ = ''
        for key_, value_ in self.grades.items():
            str_ += f'{key_}(Среднее: {self.average_course(key_)}): {value_}\n'
        return (f'{self.name} {self.surname}\n'
                f'Средняя оценка за курсы: {self._average_grade()}\n'
                f'{str_}')

    def __lt__(self, other):
        ''' Student method.
        Задание 3. Переопределение операторов сравнения
        - x < y вызывает x.__lt__(y).'''
        return self._average_grade() < other._average_grade()

    def __le__(self, other):
        ''' Student method.
        Задание 3. Переопределение операторов сравнения
        - x ≤ y вызывает x.__le__(y).'''
        return self._average_grade() <= other._average_grade()

    def __eq__(self, other):
        ''' Student method.
        Задание 3. Переопределение операторов сравнения
        - x == y вызывает x.__eq__(y).'''
        return self._average_grade() == other._average_grade()
'''
    __ne__(self, other) - x != y
    вызывает
    x.__ne__(y)

    __gt__(self, other) - x > y
    вызывает
    x.__gt__(y).

    __ge__(self, other) - x ≥ y
    вызывает
    x.__ge__(y).'''


class Mentor:
    ''' class Mentor. '''
    def __init__(self, name, surname):
        ''' Mentor method. '''
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        ''' Mentor method. '''
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    ''' Задание 1. Класс Лекторы.
        Задание 2. Оценки за лекции. '''
    def __init__(self, name, surname):
        ''' Lecturer method.
        self.name = name
        self.surname = surname
        self.courses_attached = [] '''
        super().__init__(name, surname)
        self.grades = {}

    def add_courses(self, *course_names):
        ''' Lecturer method.'''
        for course_name in course_names:
            if course_name not in self.courses_attached:
                self.courses_attached.append(course_name)

    def rate_hw(self, student, course, grade):
        ''' Lecturer method.
         Задание 1. '''
        message = f'Ошибка, Лекторы не могут выставлять оценки'
        print(message)
        return message

    def average_course(self, course):
        ''' Lecturer method.
         Задание 4. Средняя оценка лектора за курс. '''
        if self.grades.get(course):
            average_ = sum(self.grades[course])/len(self.grades[course])
        else:
            return 0
        return round(average_, ndigits=2)

    def _average_grade(self):
        ''' Lecturer method.
        Задание 3. Средняя оценка лектора. '''
        average_ = 0
        i_ = 0
        for _ in self.grades.values():
            if _:
                average_ += sum(_)/len(_)
                i_ += 1
        if i_:
            average_ = average_ / i_
        return round(average_, ndigits=2)

    # переопределение магических методов Lecturer -----------------------------
    def __str__(self):
        ''' Lecturer method.
        Задание 3. Переопределение __str__
        print(some_lecturer)
        Имя: Some
        Фамилия: Buddy
        Средняя оценка за лекции: 9.9 '''

        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self._average_grade()}')

    def __str__(self):
        ''' Lecturer method.
        Переопределено для лучшей печати '''
        str_ = ''
        for key_, value_ in self.grades.items():
            str_ += f'{key_}(Среднее: {self.average_course(key_)}): {value_}\n'
        return (f'{self.name} {self.surname}\n'
                f'Средняя оценка за лекции: {self._average_grade()}\n'
                f'{str_}')

    def __lt__(self, other):
        ''' Lecturer method.
        Задание 3. Переопределение операторов сравнения
        - x < y вызывает x.__lt__(y).'''
        return self._average_grade() < other._average_grade()

    def __le__(self, other):
        ''' Lecturer method.
        Задание 3. Переопределение операторов сравнения
        - x ≤ y вызывает x.__le__(y).'''
        return self._average_grade() <= other._average_grade()

    def __eq__(self, other):
        ''' Lecturer method.
        Задание 3. Переопределение операторов сравнения
        - x == y вызывает x.__eq__(y).'''
        return self._average_grade() == other._average_grade()

class Reviewer(Mentor):
    '''  Reviewer method.
        Задание 1. Класс Эксперты, проверяющие домашние задания
        Задание 2. Метод rate_hw наследуется и нормально работает. '''
    def __init__(self, name, surname):
        '''  Reviewer method. '''
        super().__init__(name, surname)

    def add_courses(self, *course_names):
        ''' Reviewer method.'''
        for course_name in course_names:
            if course_name not in self.courses_attached:
                self.courses_attached.append(course_name)

    def __str__(self):
        ''' Reviewer method.
        Задание 3. Переопределение __str__
        print(some_reviewer)
        Имя: Some
        Фамилия: Buddy '''

        return (f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}')




if __name__ == '__main__':

    best_student = Student('Ruoy', 'Eman', 'your_gender')
    best_student.courses_in_progress += ['Python']
    not_best_student = Student('John James', 'Rambo', 'male')
    not_best_student.courses_in_progress += ['Python']

    cool_mentor = Mentor('Some', 'Buddy')
    cool_lecturer = Lecturer('SomeLecturer', '1')
    cool_reviewer = Reviewer('SomeReviewer', '2')
    cool_mentor.courses_attached += ['Python']
    cool_lecturer.courses_attached += ['Python']
    cool_reviewer.courses_attached += ['Python']

    print('Ментор Лектор и Проверяющий ставят оценки')
    cool_mentor.rate_hw(best_student, 'Python', 10)
    cool_lecturer.rate_hw(best_student, 'Python', 10)
    cool_reviewer.rate_hw(best_student, 'Python', 10)
    any(cool_reviewer.rate_hw(not_best_student, 'Python', 8) for _ in ['одын', 'дфа', 'тры', 'цытыры'])

    print('Оченки студента:', best_student.grades)
    print(cool_mentor.courses_attached)
    print()
    print('Студент, курсы:', best_student.courses_in_progress)
    print('Лектор, курсы:', cool_lecturer.courses_attached)

    print('#'*50+'\n', 'Оценки cool_lecturer', cool_lecturer.grades)
    print('Средняя оценка cool_lecturer', cool_lecturer._average_grade())
    any(best_student.rate_lecturers(cool_lecturer, 'Python', 10) for _ in [1, 2, 3, 4])
    print('Оченки лектора:', cool_lecturer.grades)
    print('Lecturer.__dict__:', Lecturer.__dict__)

    print('################# __str__ #########################')
    print('-'*25, 'Лучший студент:\n', best_student)
    print('-'*25, 'Клевый лектор:\n', cool_lecturer)
    print('-'*25, 'Клевый проверяющий:\n', cool_reviewer)

    print('################# сравнение студентов #########################')
    print(best_student._average_grade(), not_best_student._average_grade())
    print(best_student > not_best_student)
    print(best_student < not_best_student)
    print(best_student == not_best_student)
    print(best_student != not_best_student)
    print(best_student >= not_best_student)
    print(best_student <= not_best_student)
