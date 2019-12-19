# 本代码利用pygame模块生成字符图片，可用于字符图片分类数据集的制作
# 需要先安装 pygame 包：pip install pygame
# https://www.pygame.org/news

# 支持数字、大小写字母、特殊字符、中文
# 支持随机加粗、随机倾斜、随机大小、随机颜色等
# 支持第三方字体


#载入必要的模块
import pygame
import random
import glob
import os,sys
import cv2 as cv
import numpy as np

#pygame初始化
pygame.init()

#指定结果图片保存路径
img_path = "text_image_classification"

#指定要生成的字符列表，可支持数字、大小写字母、特殊字符、汉字
char_list = ['0','1','A','B','d','e','%','&','@','中','国','航']

#字体列表
font_styles=['arial','calibri','simhei','verdana',  'ebrima','mvboli',  'segoeuiemoji',  'kaiti','mongolianbaiti', 'malgungothic', 'microsoftyibaiti','microsoftphagspa','nirmalaui', 'ebrima', 'gadugi']

#自己下载的字体列表
my_fonts = ["儷特圓.ttf","晴圆等宽.ttf","锐字云细圆体.ttf","腾祥嘉丽中圆.ttf","腾祥沁圆简体.ttf","字体管家细圆体.ttf"]

TF = [True,False]
	
#依次从字符列表中取相应字符
for j in range(0,11):
	for i in range(1,5):# 每个字符生成的图片数量
		font_color = (255,255,255)
		background_color = (0,0,0)
		font_style = random.choice(font_styles)
		font_size  = random.randint(35,45)
		font_blod  = random.choice(TF) #随机加粗
		font_italic = random.choice(TF)#随机倾斜
		
		#依次从字符列表中取出1个字符
		global text
		text = char_list[j]   

        #加载自己下载的字体
		#font  = pygame.font.Font("myfonts/"+my_fonts[random.randint(0,5)],random.randint(65,75))
		#font  = pygame.font.Font("myfonts/"+ "儷特圓.ttf",random.randint(50,54))
		
		#加载系统字体
		font = pygame.font.SysFont(font_style, font_size, font_blod, font_italic)
		
		#生成字符图片
		ftext = font.render(text,True,font_color,background_color)	
		
		#随机角度旋转	
		angle = random.randint(-20,20) 
		stext = pygame.transform.rotate(ftext,angle) 
		
		#图片大小
		stext = pygame.transform.scale(stext,(227,227))
		
		#随机翻转		
		#xbool = random.choice(TF)
		#ybool = random.choice(TF)
		#stext = pygame.transform.flip(stext,xbool,ybool)

		#将生成的图片保存到指定路径
		path = img_path + "/" + text + "/"
		isExists = os.path.exists(path)
		if not isExists:
			os.makedirs(path)
		dst_image_name = path + text +"_" + str(i) + ".jpg"
		pygame.image.save(stext,  dst_image_name )
		
	print("char %c done!" % text)
	
print("all done!")