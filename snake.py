import os

def print_to_screen():
    str=''
    for i in range(10):
        str+="."*10+"\n"
    print(str)




while True:
    print_to_screen()
    inp=input("")
    if inp!="":
        break
    else:
        pass
    os.system('cls')