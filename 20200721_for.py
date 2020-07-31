# 1.遍历字符串
n = "hello world"
for i in n:
    print(i)

# 2.遍历list
l=['he','12','hello',12,'22']
for i in l:
    print(i)

# 3.range()，左闭右开
# python3的range前面加list转换，如:list(range(10))取的是0-9
s=0
for i in list(range(10)):
    s+=i
    print(s)
print(s)

# 1-100的加法
s=0
for i in list(range(1,101)):
    # print(i)
    s+=i
    # print(s)
print(s)