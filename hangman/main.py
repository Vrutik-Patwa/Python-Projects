import random
import time
import hangman_art
import words
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)

end_of_game =False
lives =6

print(chosen_word)

print(f"Welcome to {'. ' * 10}\n")

print(" __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.")
time.sleep(0.15)
print("|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |")
time.sleep(0.15)
print("|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |") 
time.sleep(0.15)
print("|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |") 
time.sleep(0.15)
print("|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |") 
time.sleep(0.15)
print("|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|\n")
time.sleep(0.15)
display = []
for _ in range(word_length):
    display+="_"
print(display)



while not end_of_game:
    guess = input("Guess a letter :").lower()

    if guess in display:
        print("You have already guessed The word")
    
    for position in range(word_length):
        if guess == chosen_word[position]:
            display[position] = guess
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You have gueesed word {guess} which is not in the chosen word you lose a life")
        lives-=1
        if(lives==0):
            end_of_game=True
            print("You lose")

    print("lives remaining",lives)

    if '_' not in display:
        end_of_game = True
        print("You won")

    print(hangman_art.stages[lives])



