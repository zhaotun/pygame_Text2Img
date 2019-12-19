import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
from PIL import Image
import glob

# path of images
src_img_dir = "test-lineBoxDigit-500"
src_xml_dir = src_img_dir
src_txt_dir = src_img_dir

classes = ["1","2","3","4","5","6","7","8","9","10"]

def convert(size, box):
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
	
	
img_Lists = glob.glob(src_img_dir + '/*.jpg')
 
img_basenames = [] # e.g. 100.jpg
for item in img_Lists:
    img_basenames.append(os.path.basename(item))
	
img_names = [] # e.g. 100
for item in img_basenames:
    temp1, temp2 = os.path.splitext(item)
    img_names.append(temp1)
	
	
def convert_annotation(image_id):
	
    in_file = open( src_xml_dir + '/' +'%s.xml'%(image_id),'r',encoding='UTF-8')
    out_file = open( src_txt_dir + '/' +'%s.txt'%(image_id), 'w')
	
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

for img in img_names:	
	convert_annotation(img)
	

