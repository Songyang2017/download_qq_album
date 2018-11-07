利用python下载QQ相册照片
------

`python3` `QQ相册`  

**最新更新！**  
**新增自动创建存放照片的文件夹功能，并且自动以相册名命名**  

一直觉得Python很有趣，但却没机会学，如今终于把毕业的事情做完了，可以静下心一段时间来做自己想做的事情了。
为了提高对Python的兴趣，在正式学习Python的语法之前，我特意在网上查找各种Python比较好玩的代码，然后一点一点的实现，不管怎样，先获取一点成就感再说。找了一遍发觉还是Python的图像处理库PIL比较适合新手来提高兴趣，但本次的项目使用的却不是PIL，下面将介绍这个可以一键下载好友相册的全部照片的脚本使用方法和原理（Python小白班门弄斧，大神请略过）  

**注意！，此方法下载的照片是神不知过不觉的，不会产生访问记录，适合像本屌一样的不敢跟女神表白的人使用**

<div align=left><img width="200" src="https://github.com/Songyang2017/download_qq_album/blob/master/images/v2-2c30710aa2c17134e658a9b18605ed2d_r.jpg?raw=true"/></div> 

废话不多说，开撸！

#### 1. 获取好友相册的XML文件
获取好友相册列表  [http://photo.qq.com/fcgi-bin/fcg_list_album?uin=QQ号码](http://photo.qq.com/fcgi-bin/fcg_list_album?uin=QQ号码)  
获取好友相册照片  [http://photo.qq.com/fcgi-bin/fcg_list_photo?uin=QQ号码&albumid=相册ID](http://photo.qq.com/fcgi-bin/fcg_list_photo?uin=QQ号码&albumid=相册ID)

链接需要携带登录信息，因此需要在浏览器登录QQ空间，若无数据则多刷新几遍即可。

将获取到的相册列表的XML文件下载下来，用编辑器打来并将其编码格式改为`UTF-8`格式（我使用的是Sublime Text），同时把XML文件的头部的`encoding`属性改为`utf-8`，不然后面解析时会报错

#### 2. 实现原理
该脚本使用Python的`xml.dom.minidom`模块来解析XML文件，将文件中的`origin_url`字段提取出来，然后再使用`urllib`模块将图片保存下来

#### 3. 运行并下载
打开`index.py`文件，在```doc = minidom.parse("")```中填入所要解析的XML文件，注意路径要正确，然后在```f = open('img/'+path,"wb")```中~~将`'img/'`改为你要存放文件的文件夹（注意路径），脚本不会创建文件夹，因此需要手动来建~~ **已新增自动创建存放照片的文件夹功能，并且自动以相册名命名。**

完成这一切之后运行`index.py`即可！
