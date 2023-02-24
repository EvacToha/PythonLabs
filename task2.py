def doAction(a, b, *, op):
    if op == "sum":
        return a + b
    if op == "sub":
        return a - b
    if op == "mult":
        return a * b
    if op == "div" and b != 0:
        return a / b
    return "NaN"


print(doAction(3, 4, op="sum"))
print(doAction(6, 9, op="sub"))
print(doAction(7, 5, op="mult"))
print(doAction(2, 2, op="div"))
print(doAction(1, 0, op="div"))
