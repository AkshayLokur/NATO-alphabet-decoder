import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

user_word = input("Enter a word which you want to convert to phonetic code words: ")
user_word = user_word.upper()

result = [nato_dict[letter] for letter in user_word]
print(result)


