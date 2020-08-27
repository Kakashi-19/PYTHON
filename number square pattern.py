#print a pattern of squares in decreasing numerical order
#numerical input from user

import sys

try:
    n = int(input())
    print(str(n)*(n*2-1))
    for i in range(n*2-3):
        print(n, end='')
        b =[str(n-j-1) for j in range(i+1) if n-j-1 != 1]
        print(''.join(b), end='')

        print(str(n-i-1)*(n*2-3-2*len(b)), end='')

        b.reverse()
        print(''.join(b), end='')
        print(n)
        if n-i-1 == 1:
            for i in range((n*2-3)//2, -2, -1):
                if n - i - 1 != 1:
                    print(n, end='')
                    b =[str(n-j-1) for j in range(i+1) if n-j-1 != 1]
                    print(''.join(b), end='')

                    print(str(n-i-1)*(n*2-3-2*len(b)), end='')

                    b.reverse()
                    print(''.join(b), end='')
                    print(n)
                    if int(''.join(b)) % n == 0:
                        break

except ValueError:
    sys.exit()





