print("hello", "ha", sep="++++", end="\n")
a = 12  # 默认数字是十进制
print(a + 1)

b = 0b11101   # 以0b开头的数字是二进制
print(b + 1)

c = 0o12  # 以 0o 开头的数字是八进制
print(c + 1)

d = 0x1A  # 以 0x 开头的数字是十六进制
print(d + 1)


print(int('0101', 2))


print(bool(''))
print(bool(""))
print(bool(0))
print(bool({}))
print(bool([]))
print(bool(()))
print(bool(None))
