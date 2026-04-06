import random

def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age <= 0:
                print("Invalid input. Please enter a positive number.")
            else:
                return age
        except:
            print("Invalid input. Please enter a positive number.")

def generate_category(num):
    if num <= 3:
        return "Patience"
    elif num <= 6:
        return "Adventure"
    else:
        return "Prosperity"

def save_to_file(name, category, fortune):
    with open("fortune_output.txt", "w") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Category: {category}\n")
        f.write(f"Fortune: {fortune}\n")

def main():
    print("*" * 42)
    print("*      FORTUNE TELLER v2.0       *")
    print("*   Discover what the stars hold *")
    print("*" * 42)

    name = input("Enter your full name: ")
    age = get_valid_age()
    color = input("Enter your favorite color: ")

    lucky_number = random.randint(1, 10)
    category = generate_category(lucky_number)

    fortunes = [
        "Good things are coming your way.",
        "You will succeed in your goals.",
        "A new opportunity is near.",
        "Stay positive and focused.",
        "Hard work will pay off soon.",
        "You will meet someone important.",
        "Expect good news soon.",
        "Your efforts will be rewards."
    ]

    fortune = random.choice(fortunes)

    name_clean = name.strip()
    percentage = (lucky_number / age) * 100

    print("\n" + "=" * 40)
    print("YOUR FORTUNE READING")
    print("=" * 40)

    print(f"Name: {name_clean.upper()}")
    print(f"Name length: {len(name_clean)} characters")
    print(f"Age: {age}")
    print(f"Favorite color: {color.lower()}")
    print(f"Lucky number: {lucky_number}")
    print(f"Fortune category: {category}")
    print(f"Lucky percentage: {percentage:.3f}%")

    print("\nYour fortune:")
    print(f"\"{fortune}\"")

    save_to_file(name_clean, category, fortune)

    first_name = name_clean.split()[0]
    print("\n" + "=" * 40)
    print(f"Goodbye, {first_name}!")
    print("=" * 40)

main()