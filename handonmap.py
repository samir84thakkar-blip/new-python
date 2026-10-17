numbers1 = [5, 10, 15, 20, 25]
numbers2 = [30, 35, 40, 45, 50]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("Addition of 2 Lists")
print(list(result))
nums = [5, 10, 15, 20, 25, 30, 35, 40, 45]
def sq(n):
    return n*n
square = list(map(sq, nums))
print("Square of numbers in list:")
print(square)