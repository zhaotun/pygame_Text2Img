# 本代码用于将字符生成图片，可用于在字符检测时制作训练样本
# 需要先安装 pygame 包：pip install pygame
# https://www.pygame.org/news
# 支持数字、大小写字母、特殊字符、中文
# 支持随机加粗、随机倾斜、随机大小、随机颜色等
# 支持第三方字体


# 载入必要的模块
import pygame
import random

# pygame初始化
pygame.init()

# 指定生成结果图片的保存目录，如果图片中出现空白框，说明该字体不支持显示中文
res_path = "test2imgs_res"
# 指定字符串长度
string_length = 5
# 指定生成图片的数量
img_count = 50

# 生成图片的字符列表
# 支持数字、大小写字母、特殊字符、中文
# 仅部分字体支持中文显示
char_list = ['1','2','A','a','#','&','↑','年','中']

# pygame支持的字体列表
font_styles = ['microsoftyaheimicrosoftyaheiui','arial', 'arialblack', 'calibri', 
			'cambria',  'comicsansms', 'consolas', 
			 'ebrima', 'franklingothicmedium',  'gadugi', 
			 'impact', 'leelawadeeui', 
			'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 'malgungothic', 
			'malgungothicsemilight', 'microsofthimalaya', 
			'microsoftnewtailue', 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 
			 'microsoftyaheimicrosoftyaheiuibold', 
			 'microsoftyibaiti', 
			 'msgothicmsuigothicmspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 
			 'palatinolinotype', 
			  'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 
			'segoeuisemibold',  'segoeuisymbol', 'simsunnsimsun', 'simsunextb', 
			'sylfaen',  'tahoma', 'timesnewroman', 'trebuchetms', 'verdana',
			 'fangsong', 'kaiti', 'simhei', 
			 ]

# 自己下载的字体列表，需先自行下载ttf格式的字体文件，并放在myfonts目录下
my_fonts = ["儷特圓.ttf","晴圆等宽.ttf","锐字云细圆体.ttf",
			"腾祥嘉丽中圆.ttf","腾祥沁圆简体.ttf","字体管家细圆体.ttf"]
			
# 创建字符串的子函数
def create_text():
	text = ''
	for i in range(1,string_length+1):# 定义字符串的长度
		text = text + random.choice(char_list) # 每个字符从 char_list 中随机选取
	return text

for j in range(1,img_count+1):#生成字符串图片的数目
    # 先创建一个字符串
    text=create_text()
    print("第 %d 串数字为："%j)
    print(text)
    
    # 字体样式设置
    # 字体颜色：随机设置字体的颜色，也可以直接指定
    font_color = (random.randint(230,255),random.randint(230,255),random.randint(230,255))

    # 背景颜色：随机设置背景的颜色，也可以直接指定
    background_color = (random.randint(0,100),random.randint(0,100),random.randint(190,255))

    # 字体格式：从字体列表 font_styles 中随机选取字体格式，也可以直接指定
    font_style = random.choice(font_styles)

    # 字体大小：随机设置字体的大小，也可直接指定
    font_size = random.randint(60,250)

    # 是否加粗：随机加粗，也可直接指定
    font_blod = random.choice([True,False])

    # 是否倾斜：随机倾斜，也可直接指定
    font_italic = random.choice([True,False])

    # 根据设置的字体样式生成图片
    #font = pygame.font.Font("myfonts/"+my_fonts[random.randint(0,5)],random.randint(65,75))#加载自己下载的字体
    font = pygame.font.SysFont(font_style, font_size, font_blod, font_italic)#加载系统字体
    ftext = font.render(text,True,font_color,background_color)
    #ftext = font.render(text,True,font_color )#透明背景
 
    # 将生成的图片保存到本地
    image_name = res_path + "/" + font_style + "_" + text + ".jpg"
    pygame.image.save(ftext, image_name)
    
	#w=ftext.get_width()
	#h=ftext.get_height()

	#将文字显示在背景中
	#background=pygame.Surface((w+50,h+30))
	#background.fill(color=(40,78,185))
	#center=(background.get_width()/2,background.get_height()/2)
	#textpos=ftext.get_rect(center=center)
	#background.blit(ftext,textpos)

#保存图片
#pygame.image.save(ftext, "arial.jpg")#图片保存地址
#pygame.image.save(background, "background.jpg")#图片保存地址