import random

def hang(j):
    if(j==3):
                       print( """
        ------
        |    |
        |
        |
        |
        |
        |
    ------------
    """)
    elif(j==6):
                        print("""
        ------
        |    |
        |    O
        |    |
        |    |
        |
        |
    ------------
    """)
    elif(j==9):
                        print("""
        ------
        |    |
        |    O
        |    |
        |    |
        |   /
        |
    ------------
    """)
    elif(j==12):
                        print("""
        ------
        |    |
        |    O
        |  --|
        |    |
        |   / \\
        |
    ------------
    """)
    elif(j==15):
                        print("""
        ------
        |    |
        |    O
        |  --|--
        |    |
        |   / \\
        |
    ------------
    """)
                        print(f"{'-'*10}You are dead{'-'*10}")
    else:
                        print(end='')
def game():
    read_word=''
    word=['apple', 'banana', 'papaya', 'mango', 'kiwi', 'orange', 'pineapple', 'grapes', 'cherry', 'watermelon']
    alphabets="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
    alphabets=alphabets.split(',')
    guess=0
    i=0
    j=1
    rand_word=random.choice(word)
    rand_split=list(rand_word)
    rand_list=list(rand_word)
    rand_list.sort()
    read_list=[]
    read_word=''
    
    guess_word="-"*len(rand_word)
    print(f'Hint: Length of the given word is {len(rand_word)}\n{guess_word}')
    while(guess<15 and read_list!=rand_list):
        read=input(f'Guess {guess+1}: enter any alphabet:')
        if(len(read)==1):
            if(read in alphabets):
                if(read in rand_split):
                    print('Your guess is correct!!')
                    rand_split.remove(read)
                    read_word+=read
                    read_list=list(read_word)
                    read_list.sort()
                    
                    if(i<len(guess_word)):
                        guess_word=list(guess_word)
                        guess_word[i]=read
                        guess_word=''.join(guess_word)
                        
                        if(i==len(guess_word)-1):
                            print(f'All blanks are filled: {guess_word}')
                        else:
                            print(f'Remainig words to guess: {guess_word}')
                        i+=1
                else:
                    print('You guessed wrong')
                    hang(j)
                    j+=1
            else:
                print('Invalid input')
                hang(j)
                j+=1
        else:
            print('Error...\nYou have to enter 1 alphabet at a time')
            hang(j)
            j+=1
        guess+=1
    if(guess==15):
        hang(15)
        print(f'You are out of given guesses.\n The correct word was {rand_word}.')
    else:
        print('Congratulations!!!..You guessed the correct word')
    inp=input('Want to play again.\n Press 0 if yes else press 1:')
    if(inp=='0'):
        game()
    else:
        print('You are succesfully out of the game')

inp=input(f"{'*'*10}Welcome to Hangman Game{'*'*10}.\nWant to play.\n If yes then press 0 else 1:")
if(inp=='0'):
    game()
else:
    print('You are out of the game')
