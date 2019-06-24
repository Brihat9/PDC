#!/usr/bin/python3

from decimal import Decimal
import time

# input_str = input("Enter input string: ")

input_str = '()((()))(())'

input_length = len(input_str)

b = [None] * input_length
p = [None] * input_length

q = [-1] * input_length
t = [0] * input_length
r = [0] * input_length

# Result
m = [None] * input_length

print("Starting...")

stime = time.time()

''' calculates b '''
for i in range(input_length):
    print("\nCalculating b[" + str(i + 1) + "]...")
    b[i] = 1 if input_str[i] == '(' else -1
    print("\n\t\tb[" + str(i + 1) + "] calculated.")

''' calculates p '''
for i in range(input_length):
    print("\nCalculating p[" + str(i + 1) + "]...")
    p[i] = b[i] if i == 0 else sum(b[:i + 1])
    p[i] = p[i] + 1 if b[i] == -1 else p[i]
    p[i] = (p[i] - (1/(i+1)))
    print("\n\t\tp[" + str(i + 1) + "] calculated.")


def q_arr(val):
    ''' calculates q '''
    res = []
    max_val = -1
    for i in range(input_length):
        if(p[i] < val):
            res.append(p[i])

    if(res):
        max_val = max(res)

    return max_val


print("\nCalculating q...")
q = [q_arr(p[i]) for i in range(input_length)]
print("\n\t\tq calculated.")


def t_arr(val):
    ''' calculates t '''
    res = []
    max_val = 0
    for i in range(input_length):
        if(val == p[i]):
            res.append(i+1)

    if(res):
        max_val = max(res)

    return max_val


print("\nCalculating t...")
t = [t_arr(q[i]) for i in range(input_length)]
print("\n\t\tt calculated.")


def r_arr(val):
    ''' calculates r '''
    res = []
    max_val = 0
    for i in range(input_length):
        if(val == t[i]):
            res.append(i+1)

    if(res):
        max_val = min(res)

    return max_val


print("\nCalculating r...")
r = [r_arr(i+1) for i in range(input_length)]
print("\n\t\tr calculated.")

''' calculates m '''
for i in range(input_length):
    print("\nCalculating m[" + str(i + 1) + "]...")
    m[i] = t[i] if input_str[i] == ')' else r[i]
    print("\n\t\tm[" + str(i + 1) + "] calculated.")

etime = time.time()
print("Done.")
print("\nTime Taken: " + str(Decimal("%.4f" % (etime - stime))) + " sec")

print("\n\nRESULT\n")

print("input:", input_str)
# print("input:", [char for char in input_str])

print("input length:", input_length, "\n")

print("i:", [i+1 for i in range(input_length)])

print("b:", b)

p_formatted = [float(Decimal("%.2f" % elem)) for elem in p]
print("p:", p_formatted)

q_formatted = [float(Decimal("%.2f" % elem)) for elem in q]
print("q:", q_formatted)

print("t:", t)

print("r:", r)

print("m:", m)
