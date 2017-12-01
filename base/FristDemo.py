print('hello')
a =1
b =2
# if判断
if (a==b):
    print('a=b')
else:
    print('a!=b')

# 循环语句
numbers =[1,2,3,4]
even =[]
odd = []
while len(numbers)>0:
    number = numbers.pop()
    if(number%2):
        even.append(number)
    else:
        odd.append(number)
print(even)
print(odd)

# for循环遍历

for letter in 'python':
    print("当前字母",letter)
print('for 循环结束')

fruits = ['banana', 'apple',  'mango']

for index in range(len(fruits)):
   if(fruits[index]=='apple'):
       break
   print ('当前水果 :', fruits[index])

#pass是空语句，是为了保持程序结构的完整性。
print('pass -----------begin')
for letter in 'python':
    if letter =='h':
        pass
        print('这是 pass 块')
    print('当前字母',letter)
print('pass -----------end')

#字符串是 Python 中最常用的数据类型。我们可以使用引号('或")来创建字符串。
print('')
print('String -----------end')
a = "Hello"
b = "Python"

print ("a + b 输出结果：", a + b)
print ("a * 2 输出结果：", a * 2 )
print ("a[1] 输出结果：", a[1])
print ("a[1:4] 输出结果：", a[1:4])

if( "H" in a) :
    print ("H 在变量 a 中" )
else :
	print ("H 不在变量 a 中")

if( "M" not in a) :
    print( "M 不在变量 a 中" )
else :
	print ("M 在变量 a 中")

print (r'\n')
print (R'\n')
print('String -----------end')