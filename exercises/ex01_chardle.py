"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730485225"

response: str = input("Enter a 5-character word: ")
if len(response) != 5:
    print("Error: Word must contain 5 characters")
else:
    searching: str = input("Enter a single character: ")
    if len(searching)>1:
        print("Error: Character must be a single character.")
    else:
        print("Searching for "+ searching + " in " + response)
    in_case: int = 0
    if response[0] == searching:
        print(searching + " found at index 0")
        in_case = in_case + 1
    if response[1] == searching:
        print(searching + " found at index 1")
        in_case = in_case + 1
    if response[2] == searching:
        print(searching + " found at index 2")
        in_case = in_case + 1
    if response[3] == searching:
        print(searching + " found at index 3")
        in_case = in_case + 1
    if response[4] == searching:
        print(searching + " found at index 4")
        in_case = in_case + 1
    if in_case == 0:
        print("No instances of "+ searching + " found in " + response)
    else:
        print(str(in_case) + " instances of " + searching + " found in " + response)
