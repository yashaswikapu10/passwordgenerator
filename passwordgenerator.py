import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 to ensure it contains all character types.")
    
    # Characters to include in the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure the password has at least one character of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with random choices from all characters
    all_chars = lowercase + uppercase + digits + special_chars
    password += random.choices(all_chars, k=length-4)

    # Shuffle the resulting password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 4): "))
            count = int(input("Enter the number of passwords to generate: "))
            if length < 4:
                raise ValueError("Password length should be at least 4.")
            break
        except ValueError as e:
            print(e)
            print("Please enter valid integers.")

    print("\nGenerated Passwords:")
    for _ in range(count):
        print(generate_password(length))

if _name_ == "_main_":
    main()