import random
player=int(input("Choose Odd(0)/Even(1): "))

pmove=int(input("Choose number between 1 and 6: "))
cmove=random.randint(1,6)
if player==0:
    if (pmove+cmove)%2==0:
        win='c'
    else:
        win='p'
else:
    if(pmove+cmove)%2==0:
        win='p'
    else:
        win='c'
print("Computer choice was", cmove, " and your choice was ",pmove)
if win=='p':
    p=int(input("Choose bat (0) or ball (1)"))
else:
    c=random.choice([0,1])

pscore=0
cscore=0

if((win=='p' and p==0) or (win=='c' and c==1)):
    print("\n\nYour Batting")
    while(1):
        ptemp=int(input("Throw [1,6]"))
        ctemp=random.randint(1,6)
        print("You throw: ", ptemp, "Computer throw: ", ctemp)
        if(ptemp!=ctemp):
            pscore+=ptemp
        else:
            break
    print("\n\nComputer batting")
    while(1):
        ptemp=int(input("Throw [1,6]"))
        ctemp=random.randint(1,6)
        print("You throw: ", ptemp, "Computer throw: ", ctemp)
        if(ptemp!=ctemp):
            cscore+=ptemp
        else:
            break
else:
    print("\n\nComputer batting")
    while(1):
        ptemp=int(input("Throw [1,6]"))
        ctemp=random.randint(1,6)
        print("You throw: ", ptemp, "Computer throw: ", ctemp)
        if(ptemp!=ctemp):
            cscore+=ptemp
        else:
            break
    print("\n\nYour Batting")
    while(1):
        ptemp=int(input("Throw [1,6]"))
        ctemp=random.randint(1,6)
        print("You throw: ", ptemp, "Computer throw: ", ctemp)
        if(ptemp!=ctemp):
            pscore+=ptemp
        else:
            break
print("Game Over")
print("Your score is: ", pscore, "\nand computer score is: ",cscore)

if(pscore>cscore):
    print("You won")
elif(pscore<cscore):
    print("Computer won")
else:
    print("Draw")