import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def meaning(word):
    return data.get(word)


def display_meaning(l):
    for line in l:
        print(line)


def main():
    word = input("Enter a word: ").lower()
    result = meaning(word)

    if not result:
        close_matches = get_close_matches(word, data.keys())
        if close_matches:
            choice = input(f"Did you mean {close_matches[0]}. Y if yes. N if no.: ").lower()
            if choice == "y":
                result = meaning(close_matches[0])
                display_meaning(result)
            elif choice == "n":
                print("Word doesn't exist. Check what you entered.")
                main()
        else:
            print("Word doesn't exist. Check what you entered.")
            main()

    else:
        display_meaning(result)


if __name__ == '__main__':
    main()
