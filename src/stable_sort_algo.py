def show(people):
    for person in people:
        print(f"{person['position']:<2} {person['name']:<9} {person['age']}")

def bubble_sort(people, key):
    for i in range(len(people)):
        for j in range(0, len(people) - i - 1):
            if people[j][key] > people[j+1][key]:
                people[j], people[j+1] = people[j+1], people[j]


people = [
    { 'name': 'William', 'age': 21, 'position': 1 },
    { 'name': 'Smith', 'age': 23, 'position': 2 },
    { 'name': 'Alex', 'age': 27, 'position': 3 },
    { 'name': 'Paul', 'age': 21, 'position': 4 },
    { 'name': 'Max', 'age': 18, 'position': 5 },
    { 'name': 'John', 'age': 23, 'position': 6 },
    { 'name': 'Bob', 'age': 25, 'position': 7 },
    { 'name': 'Patrick', 'age': 21, 'position': 8 },
    { 'name': 'Jane', 'age': 23, 'position': 9 }
]

print('***** Original *****')
show(people)

bubble_sort(people, 'age')

print('\n***** After sorting *****')
show(people)
