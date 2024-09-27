people = {
"Thameem": 22,
"Mausooq": 30,
"Raz": 25
}
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")
for name, age in people.items():
    greet_person(name, age)
