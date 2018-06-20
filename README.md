## 利用python下载QQ相册照片

标签（空格分隔）： python3 QQ相册

---

一直觉得Python很有趣，但却没机会学，如今终于把毕业的事情做完了，可以静下心一段时间来做自己想做的事情了。
为了提高对Python的兴趣，在正式学习Python的语法之前，我特意在网上查找各种Python比较好玩的代码，然后一点一点的实现，不管怎样，先获取一点成就感再说。找了一遍发觉还是Python的图像处理库PIL比较适合新手来提高兴趣，但本次的项目使用的却不是PIL，下面将介绍这个可以一键下载好友相册的全部照片的脚本使用方法和原理（Python小白班门弄斧，大神请略过）  

**注意！，此方法下载的照片是神不知过不觉的，不会产生访问记录，适合像本屌一样的不敢跟女神表白的人使用**

<div align=center><img width="200" src="https://github.com/Songyang2017/download_qq_album/blob/master/images/v2-2c30710aa2c17134e658a9b18605ed2d_r.jpg?raw=true"/></div> 

废话不多说，开撸！

#### 1. 获取好友相册的XML文件
打开链接获取好友相册列表  [http://photo.qq.com/fcgi-bin/fcg_list_album?uin=QQ号码](http://photo.qq.com/fcgi-bin/fcg_list_album?uin=QQ号码)  
打开链接获取好友相册照片  [http://photo.qq.com/fcgi-bin/fcg_list_photo?uin=QQ号码&albumid=相册ID](http://photo.qq.com/fcgi-bin/fcg_list_photo?uin=QQ号码&albumid=相册ID)
