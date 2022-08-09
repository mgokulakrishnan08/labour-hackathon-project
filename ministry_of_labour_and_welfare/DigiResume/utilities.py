from asyncio import SendfileNotAvailableError
from ctypes import resize
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random as r
import qrcode as qr
from .models import resources,Person


def generateUID():
    return 'DRCN'+str(r.randint(100000000000,999999999999))

def generateQR(uid):
    return qr.make(uid)

def generateCard():
    p_obj = Person.objects.get(uid = uid)
    uid=p_obj.uid
    name= p_obj.name
    dob= p_obj.dob
    gender= p_obj.gender
    photo = p_obj.photo
    info=f'Name:{name}\n\nDOB:{dob}\n\nGender:{gender}'
    uid_temp=' '.join(uid[i:i+4]for i in range(0,len(uid),4))
    qrimg=generateQR(uid)
    img= Image.open(resources.objects.get(pk=1).img)
    photo= Image.open(photo)
    resize_photo=photo.resize((300,300))
    I1=ImageDraw.Draw(img)
    uid_font=ImageFont.truetype('arial.ttf',85)
    info_font=ImageFont.truetype('arial.ttf',100)
    I1.text((1400,1900),uid_temp,font=uid_font,fill=(0,0,0))
    I1.text((1000,1200),info,font=info_font,fill=(0,0,0))
    img.paste(qrimg.resize((600,600)),(2700,1200))
    img.paste(resize_photo, (200,1200))
    return img



    