def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

# Part A
set1 = {"blue", "green"}
set2 = {"blue", "yellow"}
print("Part A - Symmetric Difference:", symmetric_difference(set1, set2))

# Part B
set1 = {1, 2, 3, 4, 5}
set2 = {1, 5, 6, 7, 8, 9}
print("Part B - Symmetric Difference:", symmetric_difference(set1, set2))