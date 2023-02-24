def getEvenNumbers(arr):
    newArr = []
    for i in arr:
        if not i % 2:
            newArr.append(i)

    return newArr


numbers = [33, 56, 22, 6, 23, 12, 1298]

print(getEvenNumbers(numbers))
