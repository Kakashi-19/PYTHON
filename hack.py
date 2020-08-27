
def count_substring(string, sub_string,):
    a = 0
    c = 0
    for i in range(len(string)):
        while i + a != len(string):
            for a in range(len(sub_string)):
                if string[i + a] == sub_string[a]:
                    c = len(sub_string) - a
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)