# How to redirect standard input and output to file in python

#### in this code we make a calculator as an example to get you fimiliar with input and output to file in python

#### our first step is to import the needed libraries. in this code we need the `sys` library.

```python
import sys
```

#### then we need to open the input file and and enter the content of it into out terminal so we use `sys.stdin` 

```python
fin = open("input.txt" , "rt")
sys.stdin = fin
```
#### the we open the output file and enter the output of our program to it using `sys.stdout`

```python
fout = open("output.txt", "wt")  
sys.stdout = fout 
```

#### now that everything's setup we add out main code

```python
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
```