from xml.dom.minidom import parse
from xml.dom import minidom
import urllib
from urllib.request import urlopen


# 使用minidom解析器打开 XML 文档
doc = minidom.parse("fcg_list_album.xml")
collection = doc.documentElement
#if collection.hasAttribute("shelf"):
#   print ("Root element : %s" % collection.getAttribute("shelf"))

#  获取所有pic
pics = collection.getElementsByTagName("pic")

i = 0
#  打印每张照片的详细信息
for pic in pics:
   print ("\n*****Pic*****\n")
#   if movie.hasAttribute("title"):
#      print ("Title: %s" % movie.getAttribute("title"))

   shoottime = pic.getElementsByTagName('shoottime')[0]
   print ("Shoottime: %s" % shoottime.childNodes[0].data)

   # cameratype = pic.getElementsByTagName('cameratype')[0]
   # print ("Cameratype: %s" % cameratype.childNodes[0].data)

   # rawshoottime = pic.getElementsByTagName('rawshoottime')[0]
   # print ("Rawshoottime: %s" % rawshoottime.childNodes[0].data)

   origin_url = pic.getElementsByTagName('origin_url')[0]
   imgurl = origin_url.childNodes[0].data
   print ("origin_url: %s" % imgurl)
   data = urllib.request.urlopen(imgurl).read()   #打开URL
   path = str(i)+"-"+shoottime.childNodes[0].data+"me.jpg"     #用序号累加的方式为每张照片命名
   f = open('img/'+path,"wb")
   i = i+1                    
   f.write(data) 
   

