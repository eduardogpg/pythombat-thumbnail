import glob

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def get_image(image_path):
    try:
        return Image.open(image_path)
    
    except FileNotFoundError as e:
        print('No fue posible obtener la imagen.')

def show_images():
    for image in glob.glob('tmp/images/*.png'):
        print(image)
    
if __name__ == '__main__':

    width, heigth = 780, 150

    try:
        hexadecimal = input('Ingresa un color hexadecimal: ')
        hexadecimal = hexadecimal.replace('#', '')
    except:
        print('No fue posible obtener el color de fondo!')

    title = input('Ingresa el titulo de la imagen: ')

    background_color = tuple( int( hexadecimal[i:i+2], 16) for i in (0, 2, 4)) 
    image = Image.new('RGBA', (width, heigth), background_color)

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('fonts/Roboto/Roboto-Bold.ttf', 65)
    text_width, text_height = draw.textsize(title, font)

    draw.text( ( (width // 2) - (text_width // 2), heigth // 2 - text_height // 2 ), title , (255, 255, 255), font=font)

    title = title.replace(' ', '_').lower()
    final_path = f'{title}.png'

    image.save(final_path)
    image.show()