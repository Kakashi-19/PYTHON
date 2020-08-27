# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    try:
        string = input().split()
        print(int(string[0]) // int(string[1]))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)


