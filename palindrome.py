#!/usr/bin/python3

def palindromeChecker(stringIn):
    check = stringIn[::-1]
    if check.lower() == stringIn.lower():
        print(f"{stringIn} is a palindrome")
    else:
        print(f"{stringIn} is not a palindrome")

string = input("Please enter a word: ")
try:
    palindromeChecker(string)
except:
    print("Input is not a string")
