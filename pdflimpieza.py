# -*- coding: utf-8 -*-
"""PDFLimpieza.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FVsrSIvvo8TW_FzM7MqQq9TFPbK-HppE
"""

!pip install PdfReader
!pip install PyPDF2
from urllib import request
import re
import pandas as pd
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader, PdfWriter

pdf_path = 'Art_BERT_Pre-training of Deep Bidirectional Transformers for Language Understanding.pdf'
pdf = PdfReader(pdf_path)
pdf_resultado = PdfWriter()
pattern =  r'[A-Za-z0-9\-\ \.\:\;\,@,\n\(\)\[\]\%]+'
pattern3 =  r'[A-Za-z0-9\-\ \.\:\;\,]+'
pattern2 =  r'[?=^\(]\n*?[A-Za-z0-9\-\ \.\:\;\%\,\n*]+[\)]\n*?'

resultados=[]
resultadosNoDeseados=[]
txt=""
for num_pagina, pagina in enumerate(pdf.pages, start=0):
    texto = pagina.extract_text()
    coincidencias = re.findall(pattern, texto)
    resultados.append(coincidencias)
    print(coincidencias)

for num_pagina, pagina in enumerate(pdf.pages, start=0):
    texto = pagina.extract_text()
    coincidencias2 = re.findall(pattern2, texto)
    resultadosNoDeseados.append(coincidencias2)
resultadosNoDeseados

for n in resultados:
  txt=txt+str(n)
txt
result =txt
result = result.replace("\\n", " ")
result = result.replace("- ", "")
result = result.replace("', '", "")
result = result.replace("['", "")
result = result.replace("']", "")
print(result)

with open("text.txt","w") as file:
    file.write(result)