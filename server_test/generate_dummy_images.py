from PIL import Image, ImageDraw
import os

os.makedirs('images', exist_ok=True)

colors = ['red', 'orange', 'yellow', 'green', 'blue']

for i, color in enumerate(colors, 1):
    img = Image.new('RGBA', (500, 200), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 体
    draw.ellipse([80, 20, 470, 180], fill=color)
    
    # 尻尾
    draw.polygon([(80, 100), (10, 20), (10, 180)], fill=color)
    
    # 目
    draw.ellipse([400, 55, 445, 100], fill='white')
    draw.ellipse([415, 65, 435, 85], fill='black')
    
    img.save(f'images/fish{i}.png')
    print(f'Created fish{i}.png')
