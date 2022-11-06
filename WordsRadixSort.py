def __get_num_digits(A):
    m = 0
    for item in A:
        m = max(m, len(item))
    return m

from functools import reduce
def __flatten(A):
    return reduce(lambda x, y: x + y, A)

def radix(A):
    num_digits = __get_num_digits(A)
    for digit in range(0, num_digits):
        B = [[] for i in range(26)]
        for item in A:
            # num is the bucket number that the item will be put into
            num = ord(item[num_digits-digit-1])-65
            B[num].append(item)    
        A = __flatten(B)
    return A

def main():
    A = ["COW", "DOG", "SEA", "RUG", "ROW", "MOB", "BOX", "TAB", "BAR", "EAR", "TAR", "DIG", "BIG", "TEA", "NOW", "FOX"]
    A = radix(A)
    print(A)
    

main()            