# 175. groupby - agrupando valores (itertools)
'''
os dados precisam estar ordenados para funcionar corretamente!
O ideal é usar sorted para organizar os grupos

'''

from itertools import groupby

students = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Carlos', 'nota': 'B'},
    {'nome': 'Lucas', 'nota': 'A'},
    {'nome': 'Maicon', 'nota': 'C'},
    {'nome': 'Leticia', 'nota': 'D'},
    {'nome': 'Susane', 'nota': 'A'},
    {'nome': 'Marta', 'nota': 'C'},
]


def sort_students(student):
    return student['nota']

#ordenou alunos por nota:
copy_students = sorted(students, key=sort_students)

# grupo:
groups = groupby(copy_students, key=sort_students)

for key, group in groups:
    print(key)
    for student in group:
        print(student)
