#!/usr/bin/python3

import threading
import numpy as np

input_array = np.random.randint(1,999,4)
input_length = len(input_array)
input_index = list(range(input_length))

print("PDC LAB 2\n")
print("input array: ")
print(input_array)
# print(input_index)

num_threads = int((input_length * (input_length - 1)) / 2)

print("\nRequired number of threads: " + str(num_threads))

thread_list = []
output_index = []

class MyThread(threading.Thread):
    def __init__(self, threadID, index1, index2):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.index1 = index1
        self.index2 = index2
        self.num1 = input_array[index1]
        self.num2 = input_array[index2]

    def run(self):
        print("\nRunning thread " + str(self.threadID))
        if(self.num1 > self.num2):
            print("\nindexes [" + str(self.index1) + ", " + str(self.index2) + \
                  "] = (" + str(self.num1) + ", " + str(self.num2) + \
                  ") -> -ve outcome index " + str(self.index1))
            output_index.append(self.index1)
        else:
            print("\nindexes [" + str(self.index1) + ", " + str(self.index2) + \
                  "] = (" + str(self.num1) + ", " + str(self.num2) + \
                  ") -> -ve outcome index " + str(self.index2))
            output_index.append(self.index2)

id = 1
print("\nPossible combinations:")
for i in input_index:
    for j in range(i+1, input_length):
        print(str(id) + ". " + str(input_array[i]) + ", " + str(input_array[j]))
        thread_list.append(MyThread(id, i, j))
        id = id + 1

print("\nStarting...\n")
for n in range(len(thread_list)):
    thread_list[n].start()
for n in range(len(thread_list)):
    thread_list[n].join()


ip_index_set = set(input_index)
op_index_set = set(output_index)

print("\noutput index: ")
print(list(op_index_set))

diff_set = ip_index_set - op_index_set

print("\nindex not in output index: ")
print(list(diff_set))

smallest_element = input_array[list(diff_set)[0]]
print("\nSo, smallest element in array is " + str(smallest_element))
print("Complete.")
