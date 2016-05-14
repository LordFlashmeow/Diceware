from random import randint
import csv

with open('word_list.csv') as f:
    dice = dict(csv.reader(f, delimiter=','))  # Import word_list


def select(repeat_times, dice_list):
    final_word = ""
    for x in range(1, repeat_times + 1):
        number = number_pick()
        word = dice_list[number] + " "
        final_word += word
    return final_word


def number_pick():
    ten_thousand = (randint(1, 6)) * 10000
    thousand = (randint(1, 6)) * 1000
    hundred = (randint(1, 6)) * 100
    ten = (randint(1, 6)) * 10
    one = (randint(1, 6))

    return str(ten_thousand + thousand + hundred + ten + one)


print(select((int(input("How many words do you want? \n"))), dice))
