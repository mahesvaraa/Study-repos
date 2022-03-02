from random import shuffle, choice

arr = [choice([2, 3, 4, 5]) for i in range(12)]
for i in range(10):
    shuffle(arr)
    print(arr[:12], '->', arr[2:7][::-1])
