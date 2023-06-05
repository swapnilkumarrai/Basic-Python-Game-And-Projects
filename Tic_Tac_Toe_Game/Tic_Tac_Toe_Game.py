import random
import sys


def demo():
    print("Demo")
    print('     |     |     ')
    print('  1  |  2  |  3  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  4  |  5  |  6  ')
    print('     |     |     ')
    print('-----------------')
    print('     |     |     ')
    print('  7  |  8  |  9  ')
    print('     |     |     ')


def input_data():
    
    j=int(input('enter the position where you want to enter the desired symbol'))
    if(j==1):
        a=input('enter your symbol')
        b=c=d=e=f=g=h=i=''
        show_data(a,b,c,d,e,f,g,h,i)
        flag=comparison(a,b,c,d,e,f,g,h,i)
    if(j==2):
        b=input('enter your symbol')
        a=c=d=e=f=g=h=i=''
        show_data(a,b,c,d,e,f,g,h,i)
        flag=comparison(a,b,c,d,e,f,g,h,i)
    if(j==3):
        c=input('enter your symbol')
        a=b=d=e=f=g=h=i=''
        show_data(a,b,c,d,e,f,g,h,i)
        flag=comparison(a,b,c,d,e,f,g,h,i)
    if(j==4):
        d=input('enter your symbol')
        a=b=c=e=f=g=h=i=''
        show_data(a,b,c,d,e,f,g,h,i)
        flag=comparison(a,b,c,d,e,f,g,h,i)
    if(j==5):
        e=input('enter your symbol')
        a=b=c=d=f=g=h=i=''
        show_data(a,b,c,d,e,f,g,h,i)
        flag=comparison(a,b,c,d,e,f,g,h,i)
    if(j==6):
        f=input('enter your symbol')
        a=b=c=e=d=g=h=i=''
        show_data(a,b,c,d,e,f,g,h,i)
        flag=comparison(a,b,c,d,e,f,g,h,i)
    if(j==7):
        g=input('enter your symbol')
        a=b=c=e=f=d=h=i=''
        show_data(a,b,c,d,e,f,g,h,i)
        flag=comparison(a,b,c,d,e,f,g,h,i)
    if(j==8):
        h=input('enter your symbol')
        a=b=c=e=f=g=d=i=''
        show_data(a,b,c,d,e,f,g,h,i)
        flag=comparison(a,b,c,d,e,f,g,h,i)
    if(j==9):
        i=input('enter your symbol')  
        a=b=c=e=f=g=h=d=''
        show_data(a,b,c,d,e,f,g,h,i)
        flag=comparison(a,b,c,d,e,f,g,h,i)
    
    
    if(flag==1):
        sys.exit('player * won the match')
    elif(flag==2):
        sys.exit('player 0 won the match')
    elif(flag==3):
        sys.exit('Draw match')
    else:
        print(end='')
    


def show_data(a,b,c,d,e,f,g,h,i):
    
    print(f'     |     |     ')
    print(f'  {a}   |  {b}   |  {c}   ')
    print(f'     |     |     ')
    print(f'-----------------')
    print(f'     |     |     ')
    print(f'  {d}   |  {e}   |  {f}   ')
    print(f'     |     |     ')
    print(f'-----------------')
    print(f'     |     |     ')
    print(f'  {g}   |  {h}   |  {i}   ')
    print(f'     |     |     ')

def comparison(a,b,c,d,e,f,g,h,i):
    
    
    if((a==b==c=='*') or (d==e==f=='*') or (g==h==i=='*') or (a==d==g=='*') or (b==e==h=='*') or (c==f==i=='*') or (a==e==i=='*') or (c==e==g=='*')):
        return 1
    elif((a==b==c=='0') or (d==e==f=='0') or (g==h==i=='0') or (a==d==g=='0') or (b==e==h=='0') or (c==f==i=='0') or (a==e==i=='0') or (c==e==g=='0')):
        return 2
    elif((a!='') and (b!='') and (c!='') and (d!='') and (e!='') and (f!='') and (g!='') and (h!='') and (i!='')):
        return 3
    else:
        return ''




def game():
    global a1,a2,a3,flag
    ch=input('Want to play with user or computer. for user press u else press c')
    if(ch=='u'):
        demo()
        while(True):

            print('User * chance:')
            input_data()
            
           

            print('User 0 chance: ')
            input_data()
            
            

   
                


game()

        



