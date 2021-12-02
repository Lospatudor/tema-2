def add_numbers(*args, **kwargs):
    sum = 0
    list = []
    for elem in args:
        if isinstance(elem, int):
            list.append(elem)
            sum += elem
        else:
            return sum
    return sum


print(add_numbers(2, 4, "abc", param_1=2))
#your_function()
#your_function(2, 4, "abc", param_1=2)
#your_function(1, 5, -3, "abc", [12, 56, "cad"])