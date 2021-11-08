from CREDENTIALS import *

from os import system, name
from time import sleep

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def main():
    while True:
        print(USERNAME)
        print(PASSWORD)
        temp = input()
        clear()

if __name__ == "__main__":
    main()