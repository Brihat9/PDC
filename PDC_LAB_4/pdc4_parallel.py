#!/usr/bin/python3
'''
    PDC LAB 4 (Parallel)
    IMPLEMENT MAXIMAL SUM SUB-SEGMENT IN THE ARRAY
'''

from decimal import Decimal
import threading
import time

input_array = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]

input_length = len(input_array)

arr_s = [None] * input_length
arr_M = [None] * input_length
arr_e = [None] * input_length
arr_m = [None] * input_length
arr_t = [None] * input_length

# RESULT
maximal_sum = 0
start_index = 0
end_index = 0

''' Operations
    's' - calculates s[i]
    'Mem' - calculates M[i] and e[i] and m[i]
'''
operations = ['s', 'Mem']

thread_list = []


class MyThread(threading.Thread):
    def __init__(self, threadID, index, to_calc):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.index = index
        self.to_calc = to_calc

    def run(self):
        # print("\nRunning Thread ", self.threadID)
        if(self.to_calc == 's'):
            '''
                calculates s[i]
            '''
            print("\nCalculating s[" + str(self.index + 1) + "]...")
            arr_s[self.index] = sum(input_array[:self.index + 1])
            print("\n\t\ts[" + str(self.index + 1) + "] calculated.")

        elif(self.to_calc == 'Mem'):
            '''
                calculates M[i] and e[i] and m[i]
            '''
            print("\nCalculating M["
                  + str(self.index + 1) + "] and e["
                  + str(self.index + 1) + "] and m["
                  + str(self.index + 1) + "]...")

            arr_M[self.index] = max(arr_s[self.index:])
            print("\n\t\tM[" + str(self.index + 1) + "] calculated.")

            res = []
            val = arr_M[self.index]
            for i in range(input_length):
                if(val == arr_s[i]):
                    res.append(i)
            if(res):
                arr_e[self.index] = max(res)
            print("\n\t\te[" + str(self.index + 1) + "] calculated.")

            index = self.index
            arr_m[index] = arr_M[index] - arr_s[index] + input_array[index]
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

maximal_sum = max(arr_m)
start_index = arr_m.index(maximal_sum)
end_index = arr_e[start_index]

# logs end time
etime = time.time()
print("\nDone.")
print("\nTime Taken: " + str(Decimal("%.4f" % (etime - stime))) + " sec")

print("\n\nRESULT\n")

print("input:", input_array)
print("input length:", input_length, "\n")

print("i:", [i+1 for i in range(input_length)])
print("s:", arr_s)
print("M:", arr_M)
print("e:", arr_e)
print("m:", arr_m)

print("\nMaximal Sum:", maximal_sum)
# adding 1 to start and end index as index in result starts from 1
print("Start Index:", start_index + 1)
print("End Index:", end_index + 1)

print("Max sum sub-array:", input_array[start_index:end_index+1])
