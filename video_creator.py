import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

def generate_reel(script_text, output_path="output/reel.mp4"):
    os.makedirs("output", exist_ok=True)

    width, height = 1080, 1920
    duration = 3  # seconds per slide
    fps = 24
    font_path = "arial.ttf"  # Make sure this font file exists or replace it with a path to TTF

    lines = [line.strip() for line in script_text.split("\n") if line.strip()]
    frames = []

    for line in lines:
        # Create a white canvas using PIL
        img = Image.new("RGB", (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype(font_path, 70)
        except:
            font = ImageFont.load_default()

        text_width, text_height = draw.textsize(line, font=font)
        x = (width - text_width) // 2
        y = (height - text_height) // 2

        draw.text((x, y), line, fill="white", font=font)
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Repeat the frame for desired duration
        for _ in range(fps * duration):
            frames.append(frame)

    # Create video
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    for frame in frames:
        out.write(frame)
    out.release()

    return output_path
