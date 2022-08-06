from asyncio import SendfileNotAvailableError
from ctypes import resize
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random as r
import qrcode as qr
from .models import resources


def generateUID():
    return 'DRCN'+str(r.randint(100000000000,999999999999))

def generateQR(uid):
    return qr.make(uid)

def generateCard(uid,info):
    uid_temp=' '.join(uid[i:i+4]for i in range(0,len(uid),4))
    qrimg=generateQR(uid)
    img= Image.open(resources.objects.get(pk=1).img)
    photo= Image.open(resources.objects.get(pk=2).img)
    resize_photo=photo.resize((round(photo.size[0]*0.30),round(photo.size[0]*0.30)))
    I1=ImageDraw.Draw(img)
    uid_font=ImageFont.truetype('arial.ttf',65)
    info_font=ImageFont.truetype('arial.ttf',45)
    I1.text((270,660),uid_temp,font=uid_font,fill=(0,0,0))
    I1.text((380,400),info,font=info_font,fill=(0,0,0))
    img.paste(qrimg,(910,380))
    img.paste(resize_photo,(90,400))
    return img



    