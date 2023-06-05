import json
from difflib import get_close_matches
data=json.load(open('C:\swapnil\Interactive_Dictionary\words.json'))
input1=input('enter the word whose meaning you want to find: ')
flag=1
for item in data.keys():
    if(input1.lower()==item):
        print(f'Meaning of {input1} is: {data[item]}')
        flag=0
        break

if(flag==1):
    if(len(get_close_matches(input1, data.keys()))>0):
        print('You have entered the wrong word. Do you mean any of these words')
        print(get_close_matches(input1, data.keys()))
        input2=input('If yes, then please again enter the word here from above list else press 0: ')

        if(input2=='0'):
            print('There is no such word in a dictionary that you entered') 
        else:
            print(f'Meaning of {input2} is: {data[input2.lower()]}')

    

        
        

