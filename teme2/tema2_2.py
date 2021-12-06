#Sum numbers from 0 to n
def sum_num(n):
    if n == 0:
        return 0
    return n + sum_num(n-1)


print(sum_num(5))

#Sum even numbers from 0 to n
def sum_even(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + sum_even(n - 1)
    else:
        return sum_even(n - 1)


print(sum_even(5))


#Sum odd numbers from 0 to n
def sum_even(n):
    if n == 0:
        return 0
    if n % 2 == 1:
        return n + sum_even(n - 1)
    else:
        return sum_even(n - 1)


print(sum_even(7))
