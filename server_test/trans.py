"""
images/ フォルダ内の画像の緑背景を透過 PNG に変換
"""
from PIL import Image
import os

INPUT_DIR = 'images'
OUTPUT_DIR = 'images_transparent'

# 透過処理の設定
TARGET_COLOR = (0, 200, 0)  # 抜く色 (R, G, B) - 緑
THRESHOLD = 100              # 色の許容範囲

os.makedirs(OUTPUT_DIR, exist_ok=True)


def get_dominant_corner_color(img):
    """4 隅の色の平均を取得（背景色の推定用）"""
    pixels = img.load()
    width, height = img.size
    
    corners = [
        pixels[0, 0],
        pixels[width - 1, 0],
        pixels[0, height - 1],
        pixels[width - 1, height - 1]
    ]
    
    avg_r = sum(p[0] for p in corners) // 4
    avg_g = sum(p[1] for p in corners) // 4
    avg_b = sum(p[2] for p in corners) // 4
    
    return (avg_r, avg_g, avg_b)


def make_transparent(img, target_color, threshold):
    """指定した色 (RGB) を透明にする"""
    img = img.convert('RGBA')
    pixels = img.load()
    width, height = img.size
    
    target_r, target_g, target_b = target_color
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            distance = ((r - target_r) ** 2 + (g - target_g) ** 2 + (b - target_b) ** 2) ** 0.5
            if distance < threshold:
                pixels[x, y] = (0, 0, 0, 0)
    
    return img


def process_image(filename):
    """1 つの画像を処理"""
    input_path = os.path.join(INPUT_DIR, filename)
    output_path = os.path.join(OUTPUT_DIR, filename)
    
    img = Image.open(input_path).convert('RGBA')
    
    # 背景色を自動検出（隅の色を参考に）
    detected_bg = get_dominant_corner_color(img)
    print(f'{filename}: detected background = {detected_bg}')
    
    # 検出した色を target_color として使用
    img = make_transparent(img, detected_bg, THRESHOLD)
    
    # 保存
    img.save(output_path, 'PNG')
    print(f'  → Saved to {output_path}')


def main():
    if not os.path.exists(INPUT_DIR):
        print(f'Error: {INPUT_DIR} directory not found')
        return
    
    files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not files:
        print(f'No images found in {INPUT_DIR}')
        return
    
    print(f'Processing {len(files)} images...\n')
    
    for filename in files:
        try:
            process_image(filename)
        except Exception as e:
            print(f'Error processing {filename}: {e}')
    
    print(f'\nDone. Transparent images saved to {OUTPUT_DIR}/')


if __name__ == '__main__':
    main()