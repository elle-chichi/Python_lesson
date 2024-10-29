# list datastructure, mutable(changeable)

cars=["Toyota", "Nissan", "Mercedes"]
cars[1]="Subaru"

# num[6,8,1,9,78,0,5,7,1]


print(cars)
print(f"I love {cars[1]}")

# tuple, ordered, immutable
fruits=("mangoes", "bananas", "watermelon", "pineapple")



print(fruits)
print(f"I love eating {fruits[2]}")

# set, unordered - order changes. Doesnot have index

computers={"hp","Dell", "Lenovo", "IBM", "Apple"}
print(computers)

# dictionaries
employee={"name": "Daniel", "age": 56, "salary":3000}

print(employee)
print(f"The name of the employee is {employee['name']}")
print("The age of the employee is {}".format(employee["age"]))