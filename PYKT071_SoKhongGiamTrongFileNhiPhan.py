import pickle


def read_binary_file(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)


def is_non_decreasing(num):
    s = str(num)
    return all(s[i] <= s[i + 1] for i in range(len(s) - 1))


def count_occurrences(numbers):
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict


data1 = read_binary_file('DATA1.in')
data2 = read_binary_file('DATA2.in')

non_decreasing_numbers1 = [num for num in data1 if is_non_decreasing(num)]
non_decreasing_numbers2 = [num for num in data2 if is_non_decreasing(num)]

count_dict1 = count_occurrences(non_decreasing_numbers1)
count_dict2 = count_occurrences(non_decreasing_numbers2)

common_numbers = set(count_dict1.keys()) & set(count_dict2.keys())

result = sorted(common_numbers)

for num in result:
    print(f"{num} {count_dict1[num]} {count_dict2[num]}")
