import re

s = input("Nhập chuỗi: ")

numbers = list(map(int, re.findall(r"[+-]?\d+", s)))

tong_duong = sum(n for n in numbers if n > 0)
tong_am = sum(n for n in numbers if n < 0)

print("Giá trị dương:", tong_duong)
print("Giá trị âm:", tong_am)
