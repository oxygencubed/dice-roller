import random

while True: 
    diceinput = input("enter dice you want to roll (i.e. 1d20, etc): ")
    diceamount = int(diceinput[0:diceinput.index('d')])
    dicetype = int(diceinput[diceinput.index('d')+1:len(diceinput)])
    dicearray = []
    dicetotal = 0

    print("amount of dice rolling: ", diceamount)
    print("number of sides of dice: ", dicetype)

    for x in range(diceamount):
        result = random.randint(1, dicetype)
        dicearray.append(result)
        dicetotal += result
    
    print("results for ", diceinput, ": ", dicearray)
    print("total: ", dicetotal)
    print()
