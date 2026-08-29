'''
Exercise 2: Fibonacci Sequence Generator
Write a Python script to print the first $N$ terms of the Fibonacci sequence, where $N$ is provided by the user

Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21
Sample Input N = 6
Sample Output 0, 1, 1, 2, 3, 5
'''

def main():
    fib_seq = int(input("Enter a number: "))

    prev, curr = 0, 1
    count = 2

    while(count <= fib_seq): # if entered 7; the loop will break when encountered 8 after incrementation
        '''
        curr = curr + prev: 0+1=2
        '''
        sum = curr + prev
        prev = curr
        curr = sum
        count += 1
        
        print(f"{sum},", end='')
main()