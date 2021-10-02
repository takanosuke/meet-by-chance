from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import uuid
import numpy as np
import random
import os

FRAME_PATH = Path(settings.MEDIA_ROOT) / "frames"
RESULT_PATH = Path(settings.MEDIA_ROOT) / "results"


class Imgae:
    @classmethod
    def create(cls, params):
        density = int(params["density"])
        shift = int(params["shift"])
        blurry = int(params["blurry"])
        frame_name = params["frame"]
        base_w, base_h = frame_max_size()
        img = Image.new("RGBA", (base_w, base_h))
        for i in range(1, random.randint(density, density * 3)):
            figure = Image.new("RGBA", (base_w, base_h))
            draw = ImageDraw.Draw(figure)
            x1, y1, x2, y2 = random_position(base_w, base_h)
            r, g, b, a = random_color(int(params["color"]), int(params["visibility"]))
            for i in range(0, shift):
                ax = random.randint(-(x2 - x1), (x2 - x1))
                ay = random.randint(-(y2 - y1), (y2 - y1))
                x1 += ax
                x2 += ax
                y1 += ay
                y2 += ay
                draw.ellipse((x1, y1, x2, y2), fill=(r, g, b, a))
            # figure = figure.filter(ImageFilter.GaussianBlur(random.randint(0, 5)))
            img = Image.alpha_composite(img, figure)
            img = img.filter(
                ImageFilter.GaussianBlur(random.randint(0, int(blurry / 12)))
            )
        img_id = uuid.uuid4()
        img.save(RESULT_PATH / f"{img_id}.png")
        return merge_and_save(img, img_id, frame_name)

    @classmethod
    def changeframe(cls, params):
        img_id = params["img_name"].split("_")[0]
        img = Image.open(RESULT_PATH / f"{img_id}.png").convert("RGBA")
        return merge_and_save(img, img_id, params["frame"])

    @classmethod
    def delete(cls, img_name):
        img_id = img_name.split("_")[0]
        for img_path in RESULT_PATH.glob(f"{img_id}*"):
            try:
                img_path.unlink()
            except FileNotFoundError as fnfe:
                print("Not exsit file!!!")


def merge_and_save(img, img_id, frame_name):
    img_name = f"{img_id}_{frame_name}"
    if not Path(img_name).exists():
        frame = Image.open(FRAME_PATH / frame_name).convert("RGBA")
        upper_left = (
            int((img.size[0] - frame.size[0]) / 2),
            int((img.size[1] - frame.size[1]) / 2),
        )
        lower_right = (frame.size[0] + upper_left[0], frame.size[1] + upper_left[1])
        img.paste(frame, box=upper_left, mask=frame)
        img.crop(upper_left + lower_right).save(RESULT_PATH / img_name)
    return img_name


def random_color(color, visibility):
    visibility = int(visibility / 100 * 255)
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


def random_position(base_w, base_h):
    x1 = random.randint(0, base_w)
    y1 = random.randint(0, base_h)
    x2 = random.randint(x1, base_w)
    y2 = random.randint(y1, base_h)
    return (x1, y1, x2, y2)


def make_frame(img_path):
    img = Image.open(img_path)
    gray = img.convert("L")
    gray = gray.point(lambda x: 0 if x < 220 else 255)
    gray.save(RESULT_PATH / "result_frame.png")


def frame_max_size():
    max_size = (0, 0)
    for img_path in FRAME_PATH.glob(f"*.png"):
        size = Image.open(img_path).size
        max_size = (max(max_size[0], size[0]), max(max_size[1], size[1]))
    return max_size
