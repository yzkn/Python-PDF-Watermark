#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 YA-androidapp(https://github.com/YA-androidapp) All rights reserved.

# Required: py -m pip install PyPDF2 reportlab


from PyPDF2 import PdfWriter, PdfReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


LABEL_MESSAGE = '社外秘'


def main(in_filepath, out_filepath):
    font_name = 'SourceHanSans'
    pdfmetrics.registerFont(TTFont(font_name, 'fonts/SourceHanSans-VF.ttf'))
    with BytesIO() as buf:
        pdf = canvas.Canvas(buf, pagesize=A4)

        # 直線
        pdf.setLineWidth(1)
        pdf.setStrokeColorRGB(0, 1, 0)
        pdf.line(75*mm, 94*mm, 135*mm, 94*mm)

        # 矩形
        pdf.setFillAlpha(0.3)
        pdf.setFillColorRGB(1, 0.8, 0.8)
        pdf.setStrokeColorRGB(1, 0.6, 0.6)
        pdf.rect(75*mm, 95*mm, 60*mm, 25*mm, stroke=1, fill=1)

        # 文字
        pdf.setFont(font_name, 48)
        pdf.setFillAlpha(0.5)
        pdf.setFillColorRGB(1, 0, 0)
        # pdf.setFillColor(HexColor('#FF0000'))
        pdf.drawString(80*mm, 100*mm, LABEL_MESSAGE)
        # pdf.drawCentredString(80*mm, 100*mm, LABEL_MESSAGE)

        # 画像
        # pdf.daraInlineImage(‘foo.png’, 100*mm, 100*mm, 40*mm, 40*mm)

        pdf.showPage()
        pdf.save()
        buf.seek(0)
        pdf_txt = PdfReader(buf)
        pdf_in = PdfReader(open(in_filepath, 'rb'), strict=False)
        out = PdfWriter()
        for page_num in range(0, len(pdf_in.pages)):
            page = pdf_in.pages[page_num]
            page.merge_page(pdf_txt.pages[0])
            out.add_page(page)
        with open(out_filepath, 'wb') as pdf_out:
            out.write(pdf_out)


if __name__ == '__main__':
    main('./pdfs/ghy.pdf', './pdfs/out.pdf')
