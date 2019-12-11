# ---coding:UTF-8 ---- #
import os
from PIL import Image
import pytesseract
from multiprocessing import Pool
from re import findall
import glob



def ocr(image_name): 
    num=findall('\d+',image_name)
    if num==[]:
        page=''.join(num)
    else:
        page=image_name.split('.')[0]
    #   打开图片并识别
    image = Image.open(image_name)
    result = pytesseract.image_to_string(image,lang='deu')
    print('%s ok...' % image_name)
    return '-'*30 + '    %s    '%page + '-'*30 +'\n'+result +'\n'*10


if __name__ == "__main__":
    #   检索当前文件夹的png文件
    images = glob.glob(r"*.png")
    result=[]
    text=''
    #   选择多进程数量
    pool=Pool(4)
    for image_name in images:
        #   异步多进程开始
        result.append(pool.apply_async(ocr,[image_name]))
    pool.close()
    pool.join()
    print(result)
    #   读取所有子进程的resul内容
    for i in result:
        text += i.get()
    #   获取pdf名称
    pdf_name = glob.glob(r'*.pdf')
    if  pdf_name==[]:
        pdf_name='unnamed'
    else:
        pdf_name=pdf_name[0].split('.')[0]
    #   写入文件
    f=open("%s.txt"%pdf_name,'w',encoding='utf-8')
    f.write(text)
    f.close()
