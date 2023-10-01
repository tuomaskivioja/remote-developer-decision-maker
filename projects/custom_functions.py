
def custom_len(data):
    count = 0
    for char in data:
        count += 1
    return count


def custom_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def custom_min(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

def custom_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


def custom_sorted(data, reverse=False):
    if type(data) == str:
        data = list(data)
    for i in range(custom_len(data)):
        for j in range(0, custom_len(data)-i-1):
            if (not reverse and data[j] > data[j+1]) or (reverse and data[j] < data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
    if type(data) == str:
        return ''.join(data)
    return data

def custom_reversed(data):
    reversed_data = []
    for i in range(custom_len(data)-1, -1, -1):
        reversed_data.append(data[i])
    if type(data) == str:
        return ''.join(reversed_data)
    return reversed_data
