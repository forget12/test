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
a = 123

print(bin(a))
print(oct(a))
print(hex(a))

print(9.0 // 3.0)

print(5.5 ** 2)


# print('123' == 123)
# print('ac' < 'ab')

4 > 3 or print('哈哈哈')
# 4 < 3 or print('嘿嘿嘿')

print(not (5 > 2))

4 > 3 and print('hello world')
4 < 3 and print('你好世界')
