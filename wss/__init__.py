import requests

tup1 = ('12', '34')
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100;

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)
print(tup2 * 2)
print(tuple(tup2))
for x in tup2:
    print(x)

count = 9
i = 0
while i < count:
    i += 1
    if i % 2 > 0:
        continue
    print(i)

for letter in 'python':
    print(letter)

print(range(5))

print("My name is %s and weight is %d kg!", 'Zara', 21)
hi = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
print(hi)
hi.capitalize()

'''
get post 发送请求
'''
def get(url):
    date = {"userId": "108"}
    r = requests.get(url, params=date)
    r.encoding = 'utf-8'
    print(r.status_code)
    print(r.content)


def post(url):
    date = {'noticeNo': "69519e6b43ca47ffbcd68da7ae65570c", 'merchantNo': '0101000001259388',
            'outUserNo': '00120171116120023000000000033944'}
    r = requests.post(url, data=date)
    # r.encoding='utf-8'

    print(r.status_code)
    print(r.text)

get('http://192.168.4.111:8080/acc-app/accManager/queryBalance')
post('http://192.168.3.67:8080/acc-fae-app/query/queryBankCardInfo')
