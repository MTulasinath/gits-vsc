import random
from wordls import word_list,hangmanart,hanglist
chosen_word = random.choice(word_list)
leng_chosenword = len(chosen_word)
endofgame = False
lives = 0
display_blank = ['-' for _ in range(leng_chosenword)]
print(hangmanart)
print(f'your random word is {chosen_word}')
while not endofgame:
    guess = input('guess a letter').lower()
    for position in range(leng_chosenword):
        letter = chosen_word[position]
        if letter==guess:
            display_blank[position]=guess
    print(display_blank)
    if guess not in chosen_word:
        print('you have one life')
        print(hanglist[lives])
        lives+=1
        if lives==7:
            print('You lost')
            endofgame=True
    elif '-' not in display_blank:
        print("You win")
