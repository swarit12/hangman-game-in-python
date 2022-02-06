import random
from words import word_list

print("This is a hangman game")
print("guess the word by guessing any letter of that word")
randomword = random.choice(word_list).upper()

def play():
    global randomword
    lives= 6
    # print(randomword)
    print(f"lives left {lives}")
    print(displayhangman(lives))
    global guessed
    guessed= False
    guessedletters=[]
    guessedwords=[]
    wordlen= (len(randomword))
    word_completion= "_ "*wordlen
    print(word_completion)

    while not guessed and lives>0:
        guess = input().upper()
        if guess not in randomword:
            print(f"{guess} is not in the word")
            guessedletters.append(guess)
            lives= lives-1
            print(f"Lives left: {lives}")
            print(displayhangman(lives))
            print(word_completion)


        elif 1<len(guess)<wordlen:
            print("INVALID GUESS!!")
            print(f"Lives left: {lives}")
            print(displayhangman(lives))
            print(word_completion)


        elif len(guess)==wordlen:
            if guess==randomword:
                print(f"YOU WON!! THE WORD WAS {randomword}")
                break

            elif guess!= randomword:
                    print(f"THE WORD IS NOT {guess}")
                    guessedwords.append(guess)
                    print(f"Lives left: {lives}")
                    print(displayhangman(lives))
                    print(word_completion)


        elif len(guess)>wordlen:
            print("INVALID GUESS!!")
            print(f"Lives left: {lives}")
            print(displayhangman(lives))
            print(word_completion)


        elif guess in guessedletters or guessedwords:
            print(f"you already guessed {guess}")
            print(f"Lives left: {lives}")
            print(displayhangman(lives))
            print(wordlen)
            print(word_completion)

        elif guess in randomword:
           print(f"Good job {guess} is in the word!")
           guessedletters.append(guess)
           word_as_list = list(word_completion)
           indices = [i for i, letter in enumerate(randomword) if letter == guess]
           for index in indices:
              word_as_list[2*index] = guess
           word_completion = "".join(word_as_list)
           if "_" not in word_completion:
              guessed = True
           print(f"Lives left: {lives}")
           print(displayhangman(lives))
           print(word_completion)

        elif lives==0:
            print(f"No luck!! Try again next time. The word was {randomword}")
            break

def displayhangman(lives):
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # head, torso, and both armst

        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -sa
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,

        # head
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[lives]

play()
while True:
    displayhangman(lives=0)
    print(f"THE WORD WAS {randomword}")
    ui= input("do you want to play again? (y/n) ")
    if ui.lower()=='y':
        randomword = random.choice(word_list).upper()
        play()
    else:
        quit("thanks for playing")