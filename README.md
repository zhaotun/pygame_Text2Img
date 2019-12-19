# pygame_Text2Img
Generate image from text with pygame.

本项目通过pygame将字符转为图片，可以用来制作字符分类或字符识别的数据集，可以对字符的字体、大小、颜色、是否加粗等进行一系列的设置。

## 需要安装：
python 和 pygame (pip install pygame)

## text2image.py

这是一个字符转图片的简单demo，运行的结果保存在test2imgs_res目录。

## GenerateTextImagesForClassification.py

这个文件可以生成字符分类的数据集，运行结果保存在 text_image_classification 目录

## GenerateTextDetectDatasets.py

这个文件可以生成字符检测的数据集，将字符添加到 background_img 目录中的背景图片上，生成结果保存在 textdetect_res_img 目录，同时会在该目录生成yolo格式的标注文件

## txt2xml.py xml2txt.py

用于yolo格式的标注文件与xml格式进行相互转换
