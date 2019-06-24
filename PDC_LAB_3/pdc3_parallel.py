#!/usr/bin/python3

from decimal import Decimal
import threading
import time

# input_str = input("Enter input string: ")

input_str = '()((()))(())'
# input_str = '(()()()()()()()()())'

input_length = len(input_str)

arr_b = [None] * input_length
arr_p = [None] * input_length

arr_q = [-1] * input_length
arr_t = [0] * input_length
arr_r = [0] * input_length

# Result
arr_m = [None] * input_length

''' Operations
    'b' - calculates b[i]
    'p' - calculates p[i]
    'qt' - calculates q[i] and t[i]
    'rm' - calculates r[i] and m[i]
'''
operations = ['b', 'p', 'qt', 'rm']

thread_list = []


class MyThread(threading.Thread):
    def __init__(self, threadID, index, to_calc):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.index = index
        self.to_calc = to_calc

    def run(self):
        # print("\nRunning Thread ", self.threadID)
        if(self.to_calc == 'b'):
            '''
                calculates b[i]
            '''
            print("\nCalculating b[" + str(self.index + 1) + "]...")
            arr_b[self.index] = 1 if input_str[self.index] == '(' else -1
            print("\n\t\tb[" + str(self.index + 1) + "] calculated.")

        elif(self.to_calc == 'p'):
            '''
                calculates p[i]
            '''
            print("\nCalculating p[" + str(self.index + 1) + "]...")
            arr_p[self.index] = arr_b[self.index] if self.index == 0 else sum(arr_b[:self.index + 1])
            arr_p[self.index] = arr_p[self.index] + 1 if arr_b[self.index] == -1 else arr_p[self.index]
            arr_p[self.index] = (arr_p[self.index] - (1/(self.index+1)))
            print("\n\t\tp[" + str(self.index + 1) + "] calculated.")

        elif(self.to_calc == 'qt'):
            '''
                calculates q[i] and t[i]
            '''
            print("\nCalculating q[" + str(self.index + 1) + "] and t[" + str(self.index + 1) + "]...")

            # calculates q[i]
            res = []
            val = arr_p[self.index]
            for i in range(input_length):
                if(arr_p[i] < val):
                    res.append(arr_p[i])
            if(res):
                arr_q[self.index] = res and max(res)
            print("\n\t\tq[" + str(self.index + 1) + "] calculated.")

            # calculates t[i]
            res = []
            val = arr_q[self.index]
            for i in range(input_length):
                if(val == arr_p[i]):
                    res.append(i+1)
            if(res):
                arr_t[self.index] = max(res)
            print("\n\t\tt[" + str(self.index + 1) + "] calculated.")

        elif(self.to_calc == 'rm'):
            '''
                calculates r[i] and m[i]
            '''
            print("\nCalculating r[" + str(self.index + 1) + "] and m[" + str(self.index + 1) + "]...")

            # Calculates r[i]
            res = []
            val = self.index + 1
            for i in range(input_length):
                if(val == arr_t[i]):
                    res.append(i+1)
            if(res):
                arr_r[self.index] = min(res)
            print("\n\t\tr[" + str(self.index + 1) + "] calculated.")

            # Calculates m[i]
            arr_m[self.index] = arr_t[self.index] if input_str[self.index] == ')' else arr_r[self.index]
            print("\n\t\tm[" + str(self.index + 1) + "] calculated.")

        else:
            print("Something went wrong !!!")


print("Starting...")

# logs start time
stime = time.time()
for operation in operations:
    id = 1
    thread_list = []
    for i in range(input_length):
        thread_list.append(MyThread(id, i, operation))
        id = id + 1

    for n in range(len(thread_list)):
        thread_list[n].start()

    for n in range(len(thread_list)):
        thread_list[n].join()

# logs end time
etime = time.time()
print("\nDone.")
print("\nTime Taken: " + str(Decimal("%.4f" % (etime - stime))) + " sec")

print("\n\nRESULT\n")

print("input:", input_str)
# print("input:", [char for char in input_str])

print("input length:", input_length, "\n")

print("i:", [i+1 for i in range(input_length)])

print("b:", arr_b)

arr_p_formatted = [float(Decimal("%.2f" % elem)) for elem in arr_p]
print("p:", arr_p_formatted)

arr_q_formatted = [float(Decimal("%.2f" % elem)) for elem in arr_q]
print("q:", arr_q_formatted)

print("t:", arr_t)

print("r:", arr_r)

print("m:", arr_m)
