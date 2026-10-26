import random
import string
def generate_password(length=12):
    if length < 3:
        raise ValueError("Password length must be at least 3 to include all character types.")
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    password_pool = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]
    all_characters = lower + upper + digits
    password_pool += [random.choice(all_characters) for _ in range(length - 3)]
    random.shuffle(password_pool)
    return "".join(password_pool)
new_password = generate_password(14)
print(f"Generated Password: {new_password}")