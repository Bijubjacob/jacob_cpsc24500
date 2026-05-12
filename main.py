from word_collection import WordCollection
from story_template import TEMPLATES


def print_summary(words):

    counts = {
        "adj": 0,
        "adv": 0,
        "n": 0,
        "prep": 0,
        "v": 0
    }

    for word in words:
        counts[word.part_of_speech] += 1

    print(f"\nLoaded {len(words)} words:")

    for pos in counts:
        print(f"{pos}: {counts[pos]}")


def main():

    print("=" * 40)
    print("Welcome to StoryTeller")
    print("=" * 40)

    filepath = input("Enter path to word file: ")

    words = WordCollection.from_file(filepath)

    print_summary(words)

    while True:

        print("\nAvailable story styles:")

        for i, template in enumerate(TEMPLATES, start=1):
            print(f"{i}. {template.name}")

        choice = int(input("Choose a style: "))

        template = TEMPLATES[choice - 1]

        count = int(input("How many sentences? "))

        print(f"\n--- {template.name} Story ---\n")

        for _ in range(count):
            print(template.generate(words))

        again = input("\nGenerate another story? (yes/no): ").lower()

        if again != "yes":
            break

    print("\nThank you for using StoryTeller!")


if __name__ == "__main__":
    main()