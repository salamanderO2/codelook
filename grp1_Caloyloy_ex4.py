# Part 1: If statement that returns True or False
def about_me(age):
    if age >= 18:
        return True  # Returns True if the age is 18 or older (legal adult)
    else:
        return False  # Returns False if under 18

# Example usage of the if statement condition
my_age = 22
is_adult = about_me(my_age)
print(f"Am I an adult? {is_adult}")  # This should print True since age is 21

# Part 2: List, Tuples, Sets, and Dictionaries with String, int, and boolean data types

# List
about_me_list = ["Rodrigo", 21, True]  # Name, Age, is_Student
print("List:", about_me_list)

# Tuple
about_me_tuple = ("Caloyloy", 3, False)  # Last name, Year level, is_Graduate
print("Tuple:", about_me_tuple)

# Set
about_me_set = {"BSCS", 3, True}  # Course, Year, is_Enrolled
print("Set:", about_me_set)

# Dictionary
about_me_dict = {
    "name": "Rodrigo",
    "age": 21,
    "is_student": True,
    "course": "BSCS"
}
print("Dictionary:", about_me_dict)

# Accessing elements from each collection
print("First element in list (name):", about_me_list[0])  # Accessing list element
print("Second element in tuple (year):", about_me_tuple[1])  # Accessing tuple element
print("Checking if 'BSCS' is in set:", "BSCS" in about_me_set)  # Checking set membership
print("Age in dictionary:", about_me_dict["age"])  # Accessing dictionary value
