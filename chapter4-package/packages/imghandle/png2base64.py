import base64
from PIL import Image
import io

# 打开PNG图片
with Image.open('IMG_202412162504_64x64.png') as img:
    # 检查图片模式，保留透明度
    if img.mode != 'RGBA':
        img = img.convert('RGBA')  # 转换为RGBA模式以保留透明度

    # 创建一个缓冲区
    buffered = io.BytesIO()
    # 将图片保存到缓冲区，确保格式为PNG以支持透明度
    img.save(buffered, format="PNG")
    # 获取Base64编码
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

# 打印Base64编码字符串
print(img_str)
