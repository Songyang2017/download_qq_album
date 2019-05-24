from xml.dom.minidom import parse
from urllib import request
import os

k = 0
fileName = input('文件名：')
Dom = parse(fileName).documentElement
folderName = Dom.getElementsByTagName('name')[0].childNodes[0].data
pics = Dom.getElementsByTagName('pic')
os.mkdir(folderName)

for i in pics:
    url = i.getElementsByTagName('origin_url')[0].childNodes[0].data
    shoottime = i.getElementsByTagName('shoottime')[0].childNodes[0].data
    print('--------Pic--------')
    print(shoottime)
    data = request.urlopen(url).read()
    k = k + 1
    file = str(k) + '.jpg'
    f = open(folderName + '/' + file, 'wb+')
    f.write(data)
