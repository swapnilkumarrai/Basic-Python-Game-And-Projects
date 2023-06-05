print('welcome to currency convertor')
with open('C:\swapnil\convert_currency.txt','r') as f:
    lines=f.readlines()
#print(lines)
dict={}
for line in lines:
    list=line.split('\t')
    dict[list[0]]=list[1]
amount=int(input('enter amount you want to convert: '))
print(f'please give the currency you want to convert into. Available currencies are {dict.keys()}')
currency=input()
print(f'Your {amount} inr after getting converted into {currency} will be {amount*float(dict[currency])} {currency}')

   