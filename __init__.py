from os import system as cmd, getcwd as folder
from tkinter import filedialog as explorer
cmd("cls")
code = []
line = 1
opened = False
while True:
    codeline = input(f" \033[1m\033[34m\033[3m{line}\033[0m\033[39m    ")
    
    if codeline.lower() == "$run":
        program = """"""
        for lineofcode in code:
            program = program+lineofcode+"\n"
        cmd("cls")
        try:
            exec(program)
        except Exception as E:
            print(E)
        break
    elif codeline.lower() == "$close":
        exit()
    elif codeline.lower() == "$clear":
        code = []
        lineno = 1
        continue
    else:
        code.append(codeline)
    cmd("cls")
    for l in range(1, line+1):
        print(" "*((len(str(line))-(len(str(l))))), f"\033[32m\033[1m{l}\033[0m", "  ", code[l-1])
    line += 1