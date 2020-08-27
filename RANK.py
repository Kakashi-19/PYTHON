#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    ways = 0
    ar.sort()
    for i in range(n):
        for a in range(i + 1, n):
            if (ar[i] + ar[a]) % k == 0:
                if i == n - 2:
                    if (ar[i] + ar[n - 1]) % k == 0:
                        ways += 1
                        break
                ways += 1


    return ways




nk = input().split()

n = int(nk[0])

k = int(nk[1])

ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs(n, k, ar)

print(str(result) + '\n')


