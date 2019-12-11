# -*- utf-8 -*-

import fitz
import glob


pdffile = glob.glob(r"*.pdf")[0]
doc = fitz.open(pdffile)
start = 0
totaling = doc.pageCount


for pg in range(start,totaling):
    page = doc[pg]
    #   变焦，像素大小
    zoom = int(10)
    #   旋转角度
    rotate = int(0)
    trans = fitz.Matrix(zoom/4.0, zoom/4.0).preRotate(rotate)
    pm = page.getPixmap(matrix=trans, alpha=False)
    pm.writePNG(r"page%03d.png"%(pg+1))
    print('page%03d.png  ok...' %(pg+1))

