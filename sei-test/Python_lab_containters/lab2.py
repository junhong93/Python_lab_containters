''' Exercise 1 '''

students = ["Jun Hong", "Sachin", "Herman", "Kareem"]

print(students[1])
print(students[-1])

''' Exercise 2 '''

foods = ('pizza', 'BBQ', 'beef', 'chicken')
for food in foods:
    print(f"{food} is a good food")

''' Exercise 3 '''  

for food in foods[-2:]:
    print(food)


''' Exercise 4 '''

home_town = {
    "city" : "seoul",
    "state" : "seoul",
    "population" : 15000000,
}

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

''' Exercise 5 '''

for key, value in home_town.items():
  print(f'{key} = {value}')


''' Exercise 6 '''

cohort = []

for food in range(len(students)):
    dictionary = {
        'student' : students[food],
        'fav_food' : foods[food]
    }
    cohort.append(dictionary)

for food in cohort:
    print(food)


''' Exercise 7 '''
awesome_students=[]
for food in students:
  awesome_students.append(food +' is awesome!')

for food in awesome_students:
  print(food)


''' Exercise  8 '''

for food in foods:
  if 'a' in food:
    print(food)