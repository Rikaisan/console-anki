from random import shuffle
import os

DATA_DIR = 'data'

print("Available data lists:")
for data_name in [file.split('.')[0] for file in os.listdir(DATA_DIR)]:
    print(f"- {data_name}")
data_name = input("Which data set do you want to load?\n").strip().lower()

with open(f"{DATA_DIR}/{data_name}.txt", encoding="UTF-8") as file:
    data = eval(file.read())
    items = [[component.strip() for component in item.split(";")] for item in data.get('data').splitlines() if item]
    number_of_items = len(items)
    shuffle(items)

print(f"Loaded {number_of_items} {data.get('item_name')}!")
show_correct_answer = True if input("Show the correct answer if the answer is wrong? [Y/N]\n").strip().lower()[0] == 'y' else False

right_answers = 0
mistakes = 0

while right_answers != number_of_items:
    item = items[0][0]
    user_input = input(f"[{right_answers + 1}/{number_of_items}] {data.get('question').format(item)}\n").strip().lower()
    if user_input == items[0][1].lower():
        print("Correct!")
        del items[0]
        right_answers += 1
    else:
        if show_correct_answer:
            print(f"Incorrect, it was {items[0][1]}!")
        else:
            print("Incorrect!")
        mistakes += 1
        shuffle(items)

print(f"Thanks for playing, you had {mistakes} mistakes!")
