#!/usr/bin/python3
'''
    PDC LAB 4
    IMPLEMENT MAXIMAL SUM SUB-SEGMENT IN THE ARRAY
'''

input_array = [31, -41, 59, 26, -53, 58, 97, -93, -23, 24]
input_length = len(input_array)

subset_sum = []

for i in range(0, input_length):
    sum = 0
    for j in range(i, input_length):
        sum = sum + input_array[j]
        subset_sum.append((i, j, sum))

max_tuple = (0, 0, 0)

for tupl in subset_sum:
    if tupl[2] > max_tuple[2]:
        max_tuple = tupl

print("Index starts from 0.\n")
print("Input: " + str(input_array))
print("\nMax sum is " + str(max_tuple[2]) + " when")
print("Start index is " + str(max_tuple[0]) + " and")
print("End index is " + str(max_tuple[1]) + ".")
