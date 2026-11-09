class reverse:
    def __init__(self, s=""):
        self.s = s
    def get_reversed(self):
        return self.s[::-1]
user_input = input("Enter a word: ")
reverser = reverse(user_input)
print("Reversed string:", reverser.get_reversed())
