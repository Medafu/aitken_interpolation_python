import time

def calc_x(x):
    return round(17 / (8 * x**2 + 42)**2, 5)

def deter(x1, x2, x3, x4):
    return round((x1 * x4) - (x2 * x3), 5)

def calc_p(x1 ,x2):
    if x2 - x1 == 1:
        return round((1 / (x2 - x1)) * deter(dict[x1], x1 - x, dict[x2], x2 - x), 5)

    p1 = calc_p(x1, x2 - 1)
    p2 = calc_p(x1 + 1, x2)
    return round((1 / (x2 - x1)) * deter(p1, x1 - x, p2, x2 - x), 5)

def aitken_inter(x, begin, end):
    for i in range(begin, end + 1):
        x1 = calc_x(i)
        dict.update({i: x1})

    for i in range(begin + 1, end):
        if i == 2:
            first = calc_p(begin, i)
        
        second = calc_p(begin, i + 1)

        print("P " + str(begin - 1) + "," + str(i - 1) + ": " + str(first))
        print("P " + str(begin - 1) + "," + str(i) + ": " + str(second) + "\n")

        if first == second:
            print("Значення функції в точці " + str(x) + " дорівнює: " + str(first))
            break
        
        first = second

x = 2.6
begin = 1
end = 8
dict = {}
t_start = time.perf_counter()
aitken_inter(x, begin, end)
t_end = time.perf_counter()
print("time of execution: " + str(t_end - t_start))