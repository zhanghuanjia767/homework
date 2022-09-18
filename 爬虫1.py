from urllib import request,parse
import random
import daili
name=input('输入贴吧名：')
begin=int(input('输入起始页：'))
stop=int(input('输入终止页：'))
url ='http://tieba.baidu.com/f?{}'

beginn = begin
stopp = stop +1
while beginn < stopp :
    pn = (beginn-1)*50
    params={
                'kw':name,
                'pn':str(pn)
            }
    params=parse.urlencode(params)
    urll = url.format(params)
    req = request.Request(url=urll,headers={'User-Agent':random.choice(daili.ua_list)})
    res = request.urlopen(req)
    html=res.read().decode("gbk","ignore")
    #使用gbk解码，ignore忽略不可处理字节
    filename='{}-{}页.html'.format(name,beginn)
    with open(filename,'w') as f:
            f.write(html)
    print('第%d页抓取成功'%beginn)
    beginn = beginn + 1

print("结束了！")
