#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding:utf-8
# 使用Python Image Library对某个目录下的JPG文件进行批量修改大小，修改大小需要判断缩放后的尺寸以决定是以高或宽来进行缩放。
# 目标图像大小为tag_width和tag_height指定的尺寸。
# 转化图像时，转换了颜色空间，最终输出的为RGB颜色，以兼容IE6这种不支持透明度的浏览器。
# 尚未考虑小于宽度1000和高度670像素的情况，（因为用户提供的图片大都是广告公司设计的，一般大于这个像素）
import os,os.path
import Image
import sys

def resize(ifilename):
	try:
		img=Image.open(ifilename)
		mode=img.mode
		if mode not in ('L','RGB'):
			if mode=='RGBA':
				alpha=img.split()[3]
				bgmask=alpha.point(lambda x: 255-x)
				img=img.convert('RGB')
				img.paste((255,255,255),None,bgmask)
			else:
				img=img.convert('RGB')

		tag_width=1000
		tag_height=670
		w,h=img.size

# 尝试计算以宽度1000像素进行缩放时得到的高度，如果高度超过670，则以高度来进行缩放
		r1=float(tag_width)/float(w)
		try_height=int(r1*h)
		if try_height> tag_height :
			r2=float(tag_height)/float(h)
			wi=int(r2*w)
			hi=tag_height
		else:
			wi=tag_width
			hi=try_height

		small_img=img.resize((wi,hi),Image.ANTIALIAS)
		filebasename=os.path.splitext(ifilename)[0]
		fileextname=os.path.splitext(ifilename)[1]
		small_img.save(filebasename+"_OUT"+fileextname,"JPEG",quality=100);
	except IOError:
		print 'source picture open fail ;-)'

def main():
	cur_dir=os.path.abspath(os.curdir)
	files=os.listdir(cur_dir)
	for name in files:
		if os.path.splitext(name)[1].upper()==".jpg".upper():
			resize(name)
			print "reconvert image size %s." % (name)



if __name__ == '__main__':
   try:
       main()
   except KeyboardInterrupt:
       pass
