#create a random list and a target and there are 2 numbers that'll add up to the target
def TwoSum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return i, j
    return "NoPair"
print(TwoSum([1, 4, 5, 1], 2))