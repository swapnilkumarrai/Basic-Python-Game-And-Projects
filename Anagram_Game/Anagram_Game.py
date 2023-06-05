import json
import random

data=json.load(open('words.json')) 
data1=list(data.keys())
def rand_word(data1):
    word=random.choice(data1)
    return word

def shuffle(word):
    shuffle1=list(word)
    random.shuffle(shuffle1)
    shuffle2=''.join(shuffle1)
    return shuffle2

while(True):
    word=rand_word(data1)
    question=shuffle(word)
    print('Question: ',question)
    print('Hint(Meaning): ', data[word])
    word=word.lower()
    for i in range(0,5):
        word1=input(f'Guess no. {i+1}:')
        if(word1==word):
            print('Congratulations!!! You guessed right.\nWant to play again, If yes then press 0 else press 1')
            a=input()
            break
        else:
            print('Wrong. Try again')
            if(i<4):
                print('If you want to quit, press 1 else 0')
                a=input()
            else:
                print(f'You have reached your guessing limit.\nThe right word is {word}\nWant to try again, If yes then press 0 else press 1')
                a=input()
            if(a=='1'):
                break
    if(a=='1'):
        print('*******You are succesfully out of the game *******')
        break
        