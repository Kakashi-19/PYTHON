# Enter your code here. Read input from STDIN. Print output to STDOUT
size = input().split()
N = int(size[0])
M = int(size[1])

#top part
for i in range((N - 1) // 2):
    print(('').rjust(((M - 3) // 2) - (3*i), '-') + '.|.'*((2*i) + 1) + ('').ljust(((M - 3) // 2) - (3*i), '-'))
#middle line
print('WELCOME'.center(M, '-'))
#lower part
for i in range((N - 1) // 2):
    print(('').rjust(3*(i +1), '-') + '.|.'*(((M // 3) - 2) - 2*i)   + ('').ljust(3*(i + 1), '-'))
