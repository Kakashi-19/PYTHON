def is_leap(y):

    if y % 100 == 0:
        if y % 400 == 0:
            return True
        else:
            return False
    else:
        if y % 4 == 0:
            return True
        else:
            return False
year = int(input())
print(is_leap(year))