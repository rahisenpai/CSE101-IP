menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
print(menu,'\n')

l=[]
while(1):
    x = [int(a) for a in input('enter item number and quantity: ').split()]
    if not x:
        break
    l.append(x)
print()

to,bill = 0,[]
for j in l:
    print(menu[j[0]-1][0],',', j[1],', Rs', menu[j[0]-1][1]*j[1])
    to+=j[1]
    bill.append(menu[j[0]-1][1]*j[1])
print('\nTOTAL,',to,'items, Rs',sum(bill))