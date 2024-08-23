# Đọc 10 số nguyên dương
numbers = []
while len(numbers) < 10:
    numbers.extend(map(int, input().split()))

# Tính phép chia dư cho 42 và lưu vào set
remainders = set(num % 42 for num in numbers)

print(len(remainders))