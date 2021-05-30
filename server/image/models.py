from django.db import models
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import uuid
import numpy as np
import random
from django.conf import settings
import os
FRAME_PATH = Path(settings.MEDIA_ROOT) / 'frames'
RESULT_PATH = Path(settings.MEDIA_ROOT) / 'results'
class ImageManager(models.Model):
    image = models.ImageField(upload_to='./results', null=True)

    @classmethod
    def create(cls, params):
        density = int(params['density'])
        shift = int(params['shift'])
        blurry = int(params['blurry'])
        frame_name = params['frame']
        base = Image.open(FRAME_PATH / 'rectangle.png').convert('RGBA')
        frame = Image.open(FRAME_PATH / frame_name).convert('RGBA')
        width = base.size[0]
        height = base.size[1]
        img = Image.new('RGBA', (width, height))
        for i in range(1, random.randint(density, density*3)):
            figure = Image.new('RGBA', (width, height))
            draw = ImageDraw.Draw(figure)
            x1, y1, x2, y2 = random_position(width, height)
            r, g, b, a = random_color(int(params['color']), int(params['visibility']))
            for i in range(0, shift):
                ax = random.randint(-(x2-x1),(x2-x1))
                ay = random.randint(-(y2-y1),(y2-y1))
                x1 += ax
                x2 += ax
                y1 += ay
                y2 += ay
                draw.ellipse((x1, y1, x2, y2), fill=(r, g, b, a))
            # figure = figure.filter(ImageFilter.GaussianBlur(random.randint(0, 5)))
            img = Image.alpha_composite(img, figure)
            img = img.filter(ImageFilter.GaussianBlur(random.randint(0, int(blurry/12)))) 
        img_id = uuid.uuid4()
        img_name = f'{img_id}_{frame_name}'
        img.save(RESULT_PATH / f'{img_id}.png')
        img.paste(frame, box=(max(int((base.size[0]-frame.size[0])/2),0),max(int((base.size[1]-frame.size[1])/2),0)), mask=frame)
        img.save(RESULT_PATH / img_name)
        return img_name

    @classmethod
    def changeframe(cls, params):
        img_id = params['img_name'].split('_')[0]
        frame_name = params['frame']
        img_name = f'{img_id}_{frame_name}'
        if not Path(img_name).exists():
            img = Image.open(RESULT_PATH / f'{img_id}.png').convert('RGBA')
            frame = Image.open(FRAME_PATH / frame_name).convert('RGBA')
            img.paste(frame, box=(max(int((img.size[0]-frame.size[0])/2),0),max(int((img.size[1]-frame.size[1])/2),0)), mask=frame)
            img.save(RESULT_PATH / img_name)
        return img_name
        
    @classmethod
    def delete(cls, img_name):
        img_path = RESULT_PATH / img_name
        try:
            img_path.unlink()
        except FileNotFoundError as fnfe:
            pass

def random_color(color, visibility):
    visibility = int(visibility/100*255)
    ar = ab = 0
    if color > 50:
        ar = int((color - 50) * 4)
    elif color < 50:
        ab = int((50 - color) * 4)
    r = random.randint(ar, 255)
    g = random.randint(0, 255)
    b = random.randint(ab, 255)
    a = random.randint(-128 + visibility, 128 + visibility)
    a = max(1, min(a, 255))
    return (r, g, b, a)

def random_position(width, height):
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(x1, width)
    y2 = random.randint(y1, height)
    return (x1, y1, x2, y2)

def make_frame(img_path):
    img = Image.open(img_path)
    gray = img.convert('L')
    gray = gray.point(lambda x: 0 if x < 220 else 255)
    gray.save(RESULT_PATH / 'result_frame.png')
