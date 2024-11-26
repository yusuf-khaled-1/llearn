import random

word = ["hello" , "world" , "yusuf"]
rondom_word = random.choice(word)
word_list = list(rondom_word)
random.shuffle(word_list)
scrumbed_word = ''.join(word_list)
attemps = 5

print(f"""Welcome to the Word Scramble Game!
Try to guess the original word from the scrambled word: {scrumbed_word}
""")

ind = 0
print(f" you have {attemps} attemps")
while attemps > 0:
    attemps -= 1
    gess = input("Enter your gess :")
    if gess == rondom_word:
        print("Congratulations! You guessed the correct word!")
        break
    elif gess != rondom_word and attemps > 0:
        print(f"Incorrect! Try again. You have {attemps} attempts left.")
if attemps == ind:
    print(f"You’re out of attempts! The correct word was:{rondom_word}")