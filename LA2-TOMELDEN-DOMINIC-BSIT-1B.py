import random

def generate_password(length, use_upper, use_lower, use_numbers):
    characters = ""

    if use_upper == "yes":
        characters = characters + "POGIAKO123"

    if use_lower == "yes":
        characters = characters + "pogiako123"

    if use_numbers == "yes":
        characters = characters + "0123456789"

    password = ""

    for i in range(length):
        password = password + random.choice(characters)

    return password


def main():
    length = int(input("Enter password length: "))
    upper = input("Include uppercase? ").lower()
    lower = input("Include lowercase? ").lower()
    numbers = input("Include numbers? ").lower()

    password = generate_password(length, upper, lower, numbers)

    print("\nGenerated Password:", password)
    print("\nPassword generated with", length, "length")


if __name__ == "__main__":
    main()