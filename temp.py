from PIL import Image, ImageDraw, ImageFont
import textwrap
txt=''
for i in range(300):
    txt=txt+str(i)
img = Image.new('RGB', (300,300), color = 'white')
font_size=1
font = ImageFont.truetype("arial.ttf",font_size)
width, height = font.getsize('0'*40)
while(width<300):
    font_size=font_size+1
    font = ImageFont.truetype("arial.ttf",font_size)
    width, height = font.getsize('0'*40)

font_size=font_size-1
font = ImageFont.truetype("arial.ttf",font_size)
d = ImageDraw.Draw(img)
lines = textwrap.wrap(txt, width=40)
y_text = 0
for line in lines:
    width, height = font.getsize(line)
    d.text((0, y_text), line, font = font, fill=(0,0,0))
    y_text += height
img.show()


