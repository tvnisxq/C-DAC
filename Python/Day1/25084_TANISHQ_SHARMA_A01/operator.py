def main():
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("enter the 2nd number: "))
    op = input("Enter the operator: ")
    if op=="+":
        add = n1 + n2
        print(f"sum of {n1} and {n2} is {add}")


    if op=="-":
        sub = n1 - n2
        print(f"difference of {n1} and {n2} is {sub}")

    if op=="*":
            multi = n1 * n2
            print(f"product of {n1} and {n2} is {multi}")
            
    if op=="/":
            div = n1 / n2
            print(f"div of {n1} and {n2} is {div}")

    
main()