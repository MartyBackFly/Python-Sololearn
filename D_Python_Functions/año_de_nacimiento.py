class Person:
    def __init__(self, name, year):
        self.name = name
        self.year_of_birth = year
        self.age = self.calculate_age()

    def calculate_age(self):
        return 2023 - self.year_of_birth

# Request user to input year of birth
input_year = int(input("Enter Year of Birth: "))

p = Person("Fede", input_year)

# Check if user is an adult
if p.age < 18:
    print("Explicit Content! Access Denied")
    print("You are under age..go back")
else:
    print("Access Allowed")
    print("View our exciting adult content")
