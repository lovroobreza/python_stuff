import pandas

data_set = pandas.read_csv("./files/nato_phonetic_alphabet.csv")
alpha_dictionary={row.letter:row.code for (index, row) in data_set.iterrows()}

def sayName(word):
   for letter in word:
      print(f"{letter} : {alpha_dictionary[letter.upper()]}\n")

user_word = input("Say your name")

sayName(user_word)