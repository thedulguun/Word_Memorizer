import re
import random

MULTIPLE_CHOICE_LENGTH = 4

word_list = []

def assigner(text):

    # Regex pattern to extract Korean and Mongolian words
    pattern = r"^\d+\. ([^–-]+)[–-] (.+)$"

    match = re.match(pattern, text)
    if match:
        korean_word = match.group(1).strip()
        mongolian_word = match.group(2).strip()
        word_list.append({"korean": korean_word, "mongolian": mongolian_word})

def ask_word_multi_choice():
    rand_num = random.randint(0, len(word_list))
    print(word_list[rand_num]["korean"])
    
    rand_choices = [entry["mongolian"] for entry in random.sample(word_list, MULTIPLE_CHOICE_LENGTH-1)]
    rand_choices.append(word_list[rand_num]["mongolian"])
    random.shuffle(rand_choices)
    
    for i in range(0, MULTIPLE_CHOICE_LENGTH):
        print(f"{i+1}. {rand_choices[i]}", end="  ")
    
    answer = rand_choices[int(input())-1]
    if answer == word_list[rand_num]["mongolian"]:
        print("Correct")
    elif answer == "exit":
        exit()
    else:
        print("Wrong")
    print("__________________\n")
    

with open("words.txt", "r", encoding="utf-8") as file:
    for line in file:
        assigner(line.strip())  # Removes extra spaces and newline characters


while True:
    ask_word_multi_choice()
