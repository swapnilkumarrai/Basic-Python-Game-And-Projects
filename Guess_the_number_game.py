import random
print("Welcome to Guess The Number Game")
print("You will get 5 guesses")
r=random.randint(1,100)
with open('high_score.txt','w') as f:
    f.write('19')
with open('high_score.txt') as f:
            c=int(f.read())
a=1
b=1
while(b==1):
    if(a==6):
        print(f"Your 5 guesses are over____. You lost___\n The correct number was {r}")
        b=int(input('Want to try again. Press 1 if Yes else 0: '))
        r=random.randint(1,100)
        if(b!=1):
            break
        a=1
    i=int(input(f"Guess no. {a}: "))
    if(i==r):
        print('You guessed right!!!!')
        b=int(input("Want to try again. Press 1 if Yes else 0: "))
        r=random.randint(1,100)
        if(a<c):
            with open('high_score.txt','w') as f:
                f.write(f'New high score is {a}')
            c=a
        a=0
    elif(i>r and i<r+10):
        print("more but very close")
    elif(i<r and i>r-10):
        print("less but very close")
    elif(i<r-10):
        print("very less")
    else:
        print("very high")
    a+=1
        
    