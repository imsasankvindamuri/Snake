import os
while True:
    print("0"+"."*9,end="\n")
    for i in range(9):
        print("."*10,end="\n")
    inp=input("")
    if inp!="":
        break
    else:
        pass
    os.system('cls')