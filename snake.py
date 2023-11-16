import os

def print_to_screen():
    str=''
    for i in range(10):
        str.append("."*10,end="\n")
    print(str)




while True:
    print_to_screen()
    inp=input("")
    if inp!="":
        break
    else:
        pass
    os.system('cls')