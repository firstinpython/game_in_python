def statFun(a, b):
    difference = a - b
    percent_diff = (difference / a) * 100
    return difference, percent_diff


difference, percent_diff = statFun(1,2)
print(difference)
print(percent_diff)
