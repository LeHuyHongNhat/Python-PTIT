import re


def find_smallest_number_in_string(s):
    # find all number in string by regular expression
    numbers = re.findall(r'\d+', s)
    if not numbers:
        return None
    # convert string to integer
    number = [int(num) for num in numbers]
    return max(number)


for _ in range(int(input().strip())):
    s = input()
    result = find_smallest_number_in_string(s)
    if result is not None:
        print(result)
