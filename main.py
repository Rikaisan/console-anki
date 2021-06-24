from random import shuffle

with open("data/available_data.txt", encoding="UTF-8") as file:
    print("Available data lists:")
    for data_name in file.read().splitlines():
        print(f"- {data_name}")
    data_name = input("Which data do you want to load?\n").strip().lower()

with open(f"data/{data_name}_data.txt", encoding="UTF-8") as file:
    data = [[component.strip() for component in item.split(";")] for item in file.read().splitlines()]
    shuffle(data)

with open(f"data/{data_name}_messages.txt", encoding="UTF-8") as file:
    messages = eval(file.read())


print(f"Loaded {len(data)} {messages.get('item_name')}!")
show_correct_answer = True if input("Show the correct answer if the answer is wrong? [Y/N]\n").strip().lower()[0] == 'y' else False

right_answers = 0
mistakes = 0

while right_answers != len(data):
    item = data[right_answers][0]
    user_input = input(f"[{right_answers + 1}/{len(data)}] {messages.get('question').format(item)}\n").strip().lower()
    if user_input == data[right_answers][1].lower():
        print("Correct!")
        right_answers += 1
    else:
        if show_correct_answer:
            print(f"Incorrect, it was {data[right_answers][1]}!")
        else:
            print("Incorrect!")
        mistakes += 1
        shuffle(data)

print(f"Thanks for playing, you had {mistakes} mistakes!")
