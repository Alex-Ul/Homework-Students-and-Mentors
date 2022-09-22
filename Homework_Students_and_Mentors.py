class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
                course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')

    def __av_grade(self):
        if len(self.grades) == 0:
            print('Нет оценок')
            return
        else:
            sum_av = 0
            for course in self.grades:
                course_av = sum(self.grades.get(course)) / len(self.grades.get(course))
                sum_av += course_av
            res = round((sum_av / len(self.grades)), 1)
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Нет в списке студентов')
            return
        sum_av_self = 0
        for course in self.grades:
            course_av_self = sum(self.grades.get(course)) / len(self.grades.get(course))
            sum_av_self += course_av_self
        res_self = round((sum_av_self / len(self.grades)), 1)
        sum_av_other = 0
        for course in other.grades:
            course_av_other = sum(other.grades.get(course)) / len(other.grades.get(course))
            sum_av_other += course_av_other
        res_other = round((sum_av_other / len(other.grades)), 1)
        return res_self > res_other

    def __str__(self):
        res = f"""Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__av_grade()}
Курсы в процессе изучения: {self.courses_in_progress}\nЗавершённые курсы: {self.finished_courses}"""
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __av_grade(self):
        if len(self.grades) == 0:
            print('Нет оценок')
            return
        else:
            sum_av = 0
            for course in self.grades:
                course_av = sum(self.grades.get(course)) / len(self.grades.get(course))
                sum_av += course_av
            res = round((sum_av / len(self.grades)), 1)
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Нет в списке лекторов')
            return
        sum_av_self = 0
        for course in self.grades:
            course_av_self = sum(self.grades.get(course)) / len(self.grades.get(course))
            sum_av_self += course_av_self
        res_self = round((sum_av_self / len(self.grades)), 1)
        sum_av_other = 0
        for course in other.grades:
            course_av_other = sum(other.grades.get(course)) / len(other.grades.get(course))
            sum_av_other += course_av_other
        res_other = round((sum_av_other / len(other.grades)), 1)
        return res_self > res_other

    def __str__(self):
        res = f"""Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__av_grade()}"""
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        res = f"""Имя: {self.name}\nФамилия: {self.surname}"""
        return res


def av_rate(persons, course):
    total_score = []
    for person in persons:
        if course in list(person.grades.keys()):
            score = person.grades[course]
            total_score += score
        else:
            continue
    av_total_score = round(int(sum(total_score)) / len(total_score), 1)
    print(f"средняя оценка по курсу {course} - {av_total_score}")


petr_vasiliev = Student('Пётр', 'Васильев', 'муж')
petr_vasiliev.add_courses('Stage_1')
petr_vasiliev.grades = {'Stage_1': [8, 9, 10]}
petr_vasiliev.courses_in_progress = ['Stage_1', 'Stage_2', 'Stage_3']

olga_smirnova = Student('Ольга', 'Смирнова', 'жен')
olga_smirnova.add_courses('Stage_1')
olga_smirnova.add_courses('Stage_2')
olga_smirnova.grades = {'Stage_1': [10, 9, 10], 'Stage_2': [9, 10]}
olga_smirnova.courses_in_progress = ['Stage_3', 'Stage_4']

sergey_semenov = Lecturer('Сергей', 'Семёнов')
sergey_semenov.courses_attached = ['Stage_1', 'Stage_3']

svetlana_stepanova = Lecturer('Светлана', 'Степанова')
svetlana_stepanova.courses_attached = ['Stage_2', 'Stage_4']

natalia_orlova = Reviewer('Наталья', 'Орлова')
natalia_orlova.courses_attached = ['Stage_1', 'Stage_2']

vladimir_volkov = Reviewer('Владимир', 'Волков')
vladimir_volkov.courses_attached = ['Stage_1', 'Stage_2', 'Stage_3', 'Stage_4']

petr_vasiliev.rate_lec(sergey_semenov, 'Stage_3', 8)
petr_vasiliev.rate_lec(sergey_semenov, 'Stage_3', 9)
petr_vasiliev.rate_lec(sergey_semenov, 'Stage_1', 8)
olga_smirnova.rate_lec(sergey_semenov, 'Stage_3', 9)
olga_smirnova.rate_lec(sergey_semenov, 'Stage_3', 10)


petr_vasiliev.rate_lec(svetlana_stepanova, 'Stage_2', 10)
petr_vasiliev.rate_lec(svetlana_stepanova, 'Stage_2', 8)
olga_smirnova.rate_lec(svetlana_stepanova, 'Stage_4', 10)
olga_smirnova.rate_lec(svetlana_stepanova, 'Stage_4', 10)

natalia_orlova.rate_hw(petr_vasiliev, 'Stage_2', 8)
natalia_orlova.rate_hw(petr_vasiliev, 'Stage_2', 9)
natalia_orlova.rate_hw(petr_vasiliev, 'Stage_2', 9)

vladimir_volkov.rate_hw(olga_smirnova, 'Stage_3', 10)
vladimir_volkov.rate_hw(olga_smirnova, 'Stage_3', 9)
vladimir_volkov.rate_hw(olga_smirnova, 'Stage_3', 9)
vladimir_volkov.rate_hw(olga_smirnova, 'Stage_4', 8)
vladimir_volkov.rate_hw(olga_smirnova, 'Stage_4', 10)

# print(petr_vasiliev)
# print(petr_vasiliev.grades)
# print()
# print(olga_smirnova)
# print(olga_smirnova.grades)
# print()
# print(sergey_semenov)
# print(sergey_semenov.grades)
# print()
# print(svetlana_stepanova)
# print(svetlana_stepanova.grades)
# print()
# print(vladimir_volkov)
# print()
# print(natalia_orlova)
# print()
# print(petr_vasiliev < olga_smirnova)
# print(sergey_semenov > svetlana_stepanova)

students_list = [petr_vasiliev, olga_smirnova]
lecturers_list = [sergey_semenov, svetlana_stepanova]
course = str(input('Введите название курса: '))
print('Для студентов')
av_rate(students_list, course)
print('Для преподавателей')
av_rate(lecturers_list, course)
