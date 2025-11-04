from operator import itemgetter


class Student:
    def __init__(self, id, last_name, score, class_id):
        self.id = id
        self.last_name = last_name
        self.score = score
        self.class_id = class_id


class SchoolClass:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class StudentClass:
    def __init__(self, class_id, student_id):
        self.class_id = class_id
        self.student_id = student_id


classes = [
    SchoolClass(1, 'математический класс'),
    SchoolClass(2, 'физический класс'),
    SchoolClass(3, 'химический класс'),
    SchoolClass(11, 'математический кружок'),
    SchoolClass(22, 'физический кружок'),
    SchoolClass(33, 'химический кружок'),
]

students = [
    Student(1, 'Иванов', 85, 1),
    Student(2, 'Петров', 92, 2),
    Student(3, 'Сидоров', 78, 3),
    Student(4, 'Козлов', 95, 1),
    Student(5, 'Смирнов', 88, 2),
]

students_classes = [
    StudentClass(1, 1),
    StudentClass(2, 2),
    StudentClass(3, 3),
    StudentClass(1, 4),
    StudentClass(2, 5),
    StudentClass(11, 1),
    StudentClass(22, 2),
    StudentClass(33, 3),
    StudentClass(11, 4),
    StudentClass(22, 5),]


def main():

    one_to_many = [(s.last_name, s.score, c.name)
                   for c in classes
                   for s in students
                   if s.class_id == c.id]

    many_to_many_temp = [(c.name, sc.class_id, sc.student_id)
                         for c in classes
                         for sc in students_classes
                         if c.id == sc.class_id]

    many_to_many = [(s.last_name, s.score, class_name)
                    for class_name, class_id, student_id in many_to_many_temp
                    for s in students if s.id == student_id]

    print('Задание A1')
    print('Список всех связанных школьников и классов, отсортированный по классам:')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    for item in res_11:
        print(f'Школьник: {item[0]}, Баллы: {item[1]}, Класс: {item[2]}')

    print('\n' + '=' * 50 + '\n')

    print('Задание A2')
    print('Список классов с суммарными баллами школьников, отсортированный по суммарным баллам:')
    res_12_unsorted = []

    class_groups = {}
    for s_name, s_score, c_name in one_to_many:
        if c_name not in class_groups:
            class_groups[c_name] = []
        class_groups[c_name].append(s_score)

    for c_name, scores in class_groups.items():
        total_score = sum(scores)
        res_12_unsorted.append((c_name, total_score))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    for item in res_12:
        print(f'Класс: {item[0]}, Суммарные баллы: {item[1]}')

    print('\n' + '=' * 50 + '\n')

    print('Задание A3')
    print('Список всех классов, у которых в названии присутствует слово "класс", и список школьников в них:')
    res_13 = {}


    for c in classes:
        if 'класс' in c.name.lower():
            c_students = [s_name for s_name, s_score, class_name in many_to_many
                          if class_name == c.name]
            res_13[c.name] = c_students

    for class_name, students_list in res_13.items():
        print(f'Класс: {class_name}')
        print(f'  Школьники: {", ".join(students_list)}')


if __name__ == '__main__':

    main()
