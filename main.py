import random


# Checks if a list is sorted from greatest to least
def check_sort(n, greatest_to_least):
    output = True
    if greatest_to_least:
        for i in range(0, len(n) - 1):
            if n[i] >= n[i + 1]:
                continue
            else:
                output = False
                break
    else:
        for i in range(0, len(n) - 1):
            if n[i] <= n[i + 1]:
                continue
            else:
                output = False
                break

    return output


# sorting a list of integers from greatest to least
def sort_from_greatest_to_least(n):
    output_list = []
    for i in range(0, len(n)):
        output_list.append(n[i])
        output_list[i] = int(output_list[i])

    for i in range(0, len(n)):
        if i < len(n) - 1 and output_list[i] < output_list[i + 1]:
            output_list[i + 1], output_list[i] = output_list[i], output_list[i + 1]
    if check_sort(output_list, True):  # error with recursion
        return output_list
    else:
        return sort_from_greatest_to_least(output_list)


# sorting a list of integers from lest to greatest
def sort_from_least_to_greatest(n):
    output_list = []
    for i in range(0, len(n)):
        output_list.append(n[i])
        output_list[i] = int(output_list[i])

    for i in range(0, len(n)):
        if i < len(n) - 1 and output_list[i] > output_list[i + 1]:
            output_list[i + 1], output_list[i] = output_list[i], output_list[i + 1]
    if check_sort(output_list, False):  # error with recursion
        return output_list
    else:
        return sort_from_least_to_greatest(output_list)


# generating a list of random numbers
def random_int(n):
    output = []
    for i in range(0, n):
        rand = random.randint(0, n)
        output.append(rand)
    return output


numbers = random_int(10)
print(sort_from_greatest_to_least(numbers))
print(sort_from_least_to_greatest(numbers))
