import sys

fin = open("input.txt" , "rt")
sys.stdin = fin

f1 = open("output.txt", "wt")  
sys.stdout = f1 

while True:
    numbers = input("->").strip().split(" ")
    if numbers[0]=="add":
        print(int(numbers[1]) + int(numbers[2]))
    elif numbers[0]=="mul":
        print(int(numbers[1]) * int(numbers[2]))
    elif numbers[0]=="div":
        print(int(numbers[1]) / int(numbers[2]))
    elif numbers[0]=="min":
        print(int(numbers[1]) - int(numbers[2]))