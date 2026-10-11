test_dictionary = {
    "Codingal": 3,
    "is": 2,
    "best": 2,
    "for": 2,
    "Coding": 1
}

print("Test dictionary:", test_dictionary)

value_to_check = input("Enter a word to check its frequency: ")
frequency = test_dictionary.get(value_to_check, 0)

print(f"Frequency of '{value_to_check}': {frequency}")