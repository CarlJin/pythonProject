import os

'''str = input("请输入：")
print(str)'''

#
fo = open('fileTest.py', 'r+')
print("文件名", fo.name)
print("访问模式", fo.mode)
print("是否已经关闭", fo.close)

for line in fo:
    print(line)

print(os.getcwd())

fo.close()

try:
    1 / 0
except ZeroDivisionError:
    print("发生异常")
else:
    print("没有异常")

class NetWorkerror(RuntimeError):
    def __init__(self,args):
        self.args=args

try:
    raise NetWorkerror("bad hostName")
except NetWorkerror:
    print("")
