# 本代码利用pygame模块在背景图片随机放置字符，可用于制作字符的目标检测数据集
# 需要先安装 pygame 包：pip install pygame
# https://www.pygame.org/news

#载入必要的模块
import pygame
import random
import glob
import os,sys

#pygame初始化
pygame.init()

# 指定背景图片路径
src_img_path = "background_img"
# 指定添加字符后的结果图片路径
dst_img_path = "textdetect_res_img"

# 背景图片尺寸
img_width  = 960
img_height = 540

text=''

# 正样本字符列表，即要检测的目标字符列表
digit_list = ['0','1','2','3','4','5','6','7','8','9']
# 正样本字符字体，尽量保证与实际样本的字体一致
digit_font_styles = ['simhei', 'simsunnsimsun', 'simsunextb','fangsong']

# 负样本字符列表
negchar_list = [ 'A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z',
                 'a','b','c','d','e','f','g','h','i','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z',
                 '/','->','->.','->',')','`','=','+','-!','@','#','$','%','^','&','*','_']
# 负样本字体
negchar_font_styles = ['arial',  'bahnschrift', 'calibri', 'cambriacambriamath', 'consolas',  'corbel'] 

TF = [True,False]

#转换为yolo需要的标注格式
def convert_to_yolo_format(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

# 随机生成长度为5的负样本字符串
def create_negchars():
	text = ''
	for i in range(1,6):
		text = text + random.choice(negchar_list)
	return text

# 随机生成长度为5的正样本字符串
def create_5digits():
	text = ''
	for i in range(1,6):
		text = text + random.choice(digit_list)
	return text

#生成字体文件
def create_text():
	
	#渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
	#字体颜色随机
	font_color = (random.randint(222,255),random.randint(222,255),random.randint(222,255))
	#背景颜色随机
	background_color = (random.randint(34,42),random.randint(97,102),random.randint(200,210))
	#随机字体
	font_style = random.choice(digit_font_styles)
	#随机大小
	font_size = random.randint(35,70)
	#随机加粗
	font_blod = random.choice(TF)
	#font_blod = False
	#随机倾斜
	#font_italic = random.choice(TF)
	font_italic =  False 
	
	#生成数字串图片
	global text
	text=create_5digits()  # 随机生成长度为5的正样本字符串
	#text=create_negchars()# 随机生成长度为5的负样本字符串
	print(text)

	font = pygame.font.SysFont(font_style, font_size, font_blod, font_italic)
	#ftext = font.render(text,True,font_color,background_color) # 生成指定颜色背景的图片
	ftext = font.render(text,True,font_color )# 生成透明背景的图片
	
	return ftext

def create_noise():
	
	#渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
	#字体颜色随机
	font_color = (0,0,0)
	#背景颜色随机
	background_color = (random.randint(34,42),random.randint(97,102),random.randint(200,210))
	#随机字体
	font_style = random.choice(noise_font_styles)
	#随机大小
	font_size = random.randint(35,50)
	#随机加粗
	#font_blod = random.choice(TF)
	font_blod = False
	#随机倾斜
	#font_italic = random.choice(TF)
	font_italic =  False 
	
	#生成数字串图片
	#global textn
	textn=create_chars()
	#print(text)

	font = pygame.font.SysFont(font_style, font_size, font_blod, font_italic)
	#ftext = font.render(text,True,font_color,background_color)
	ftext = font.render(textn,True,font_color )#透明背景
	
	return ftext


dirs = os.listdir(src_img_path)#遍历背景图片路径
for file in dirs:
	print(file)
	#加载背景图片
	background = pygame.image.load(src_img_path +"/"+file)
	#提取无.jpg后缀的图片名称
	img_name,name2 = os.path.splitext(file)
	#标注文件名称
	txt_name = dst_img_path + "/" + img_name + ".txt"	
	txt_file = open(txt_name, 'w')			
	
	pos_list = []
	rect = ()

	#每张图片产生4组数字
	for j in range(1,5):
		stext = create_text()  #生成长度为5的正样本字符串
		#ntext = create_noise() #生成长度为5的负样本字符串 
		
		# 获取字符串图片大小
		width  = stext.get_width()
		height = stext.get_height()
		
		# 设置放置的最大宽高，即在背景图片放置字符串时，不能超出图片边界
		max_X = img_width  - 10 - width
		max_y = img_height - 70 - height

		# 判断即将放置的字符串与已放置的字符串是否位置重叠，若重叠，则重新指定放置位置
		t = 1
		while(t>0):
			# 设定放置字符串的位置
			tmp_x = random.randint(30,max_X)
			tmp_y = random.randint(30,max_y)
			tmp_rect = pygame.Rect(tmp_x,tmp_y,width,height)

			k = 0
			for i in range(0,len(pos_list)):
				#print("i=%d"%i)
				#print(pos_list[i])
				if tmp_rect.colliderect(pos_list[i]):#如有相交,直接退出，重新赋值
					#print("break")
					break
				else:#如无相交，则继续比较list中下一个rect
					k=k+1
					continue
					
			#print("k = %d"%k)		
			if k >= len(pos_list):
				t = 0 #如果全部不相交，则退出比较，保存该rect
					
		# 放置的起点坐标
		pos_X = tmp_x
		pos_Y = tmp_y	
		# 保存字符串位置
		pos_list.append((pos_X,pos_Y,width,height))
		#print(pos_list)
		
		# 添加噪音，向字符串添加随机大小随机颜色的方块
		for j in range(1,10): 
			fillColor = ( random.randint(0, 255),random.randint(0, 255),random.randint(0, 255) )
			fillX = random.randint( int(0.1*width), int(0.8*width) ) 
			fillY = random.randint( int(0.1*height), int(0.8*height) ) 
			fillw = random.randint(0, 25) 
			fillh = random.randint(0, 4) 
			fillRect = (fillX,fillY, fillw, fillh)
			stext.fill(fillColor,fillRect)
		
		# 将加过噪音后的字符串添加到背景图片的指定位置
		textpos=( pos_X , pos_Y )
		background.blit(stext,textpos)
		
		# 获取字符串中每个字符的位置，作为标注值，用于模型训练
		size=(img_width,img_height)
		b0 = (0.0*width+pos_X, pos_X+0.2*width,  pos_Y,  pos_Y + height)
		b1 = (0.2*width+pos_X, pos_X+0.4*width,  pos_Y,  pos_Y + height)
		b2 = (0.4*width+pos_X, pos_X+0.6*width,  pos_Y,  pos_Y + height)
		b3 = (0.6*width+pos_X, pos_X+0.8*width,  pos_Y,  pos_Y + height)
		b4 = (0.8*width+pos_X, pos_X+1.0*width,  pos_Y,  pos_Y + height)	
		
		# 将每个字符的位置转换为适于yolo训练的标注格式
		bb0 = convert_to_yolo_format(size, b0)
		bb1 = convert_to_yolo_format(size, b1)
		bb2 = convert_to_yolo_format(size, b2)
		bb3 = convert_to_yolo_format(size, b3)
		bb4 = convert_to_yolo_format(size, b4)
		
		# 保存标号，需要减1，如字符为1，则标记为0，如字符为0，则标记为9
		list = []
		for i in range(0,5):
			a = int(text[i])-1 #减1
			if(  int(text[i])-1 < 0 ) :#如字符为0，则标记为9
				list.append('9')
			else:
				list.append( str(a) )
				
		# 标注信息 写入标注文件		
		txt_file.write(str(list[0]) + " " + " ".join([str(a) for a in bb0]) + '\n')
		txt_file.write(str(list[1]) + " " + " ".join([str(a) for a in bb1]) + '\n')
		txt_file.write(str(list[2]) + " " + " ".join([str(a) for a in bb2]) + '\n')
		txt_file.write(str(list[3]) + " " + " ".join([str(a) for a in bb3]) + '\n')
		txt_file.write(str(list[4]) + " " + " ".join([str(a) for a in bb4]) + '\n')
	
	#保存最终图片
	print(len(pos_list))
	pos_list.clear
	print("clear list")
	pygame.image.save(background,  dst_img_path + "/" + file )#图片保存地址