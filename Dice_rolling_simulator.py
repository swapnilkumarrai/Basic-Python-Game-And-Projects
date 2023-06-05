import random
i=1
while(i==1):
    i=int(input('press 1 to roll a dice or press 0 to quit the game: '))
    r=random.randint(1,6)
    if(r==1):
        print('[     ]')
        print('[  0  ]')
        print('[     ]')
    elif(r==2):
        print('[0    ]')
        print('[     ]')
        print('[    0]')
    elif(r==3):
       print('[0    ]')
       print('[  0  ]')
       print('[    0]')
    elif(r==4):
        print('[0   0]')
        print('[     ]')
        print('[0   0]')
    elif(r==5):
        print('[0   0]')
        print('[  0  ]')
        print('[0   0]')
    else:
        print('[0 0 0]')
        print('[0 0 0]')
        print('[0 0 0]')
    