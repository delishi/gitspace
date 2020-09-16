import sys
list = [1,2,3,4]
it = iter(list)
for x in it:
    print(x,end=" ")
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        break
def change(a):
    print(id(a))
    a = 10
    print(id(a))

a = 1
print(id(a))
change(a)

sum = lambda arg1,arg2 : arg1+arg2

print("after adding:",sum(10,20))
print("after adding:",sum(20,20))

f = open("./foo.txt","w")
f.write("python is a very good programming language!")

f.close()

f = open("./foo.txt","r")
str = f.read()

print(str)

f.close()
