array = input().split()
target = int(input())

# search for the sum of two numbers in array equal to target
# and return their indices
def twoSum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if int(arr[i]) + int(arr[j]) == target:
                return [i, j]

# print indices of the two numbers
print(twoSum(array, target))
