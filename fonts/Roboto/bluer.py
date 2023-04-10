from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter

# https://unsplash.com/s/photos/parrot
if __name__ == '__main__':
    
    try:
        # https://medium.com/analytics-vidhya/some-interesting-tricks-in-python-pillow-8fe5acce6084
        radius, diameter = 20, 40

        image = Image.open('images/parrot.jpeg')
        width, height = image.size

        background_size = (
            width + diameter,
            height + diameter
        )
        background = Image.new('RGB', background_size, (255, 255, 255))
        background.paste(image, (radius, radius))

        # White
        mask_size = (width + diameter, height + diameter)
        mask = Image.new('L', mask_size, 255)
        
        # Black
        black_size = (width  - diameter, height - diameter)
        black = Image.new('L', black_size, 0)

        mask.paste(black, (diameter, diameter) ) 

        blur = background.filter(ImageFilter.GaussianBlur(radius / 2))
        background.paste(blur, mask=mask)

        background.save("test_image_blurred.jpg", quality=100)
        background.show()

    except FileNotFoundError as e:
        print('No es posible obtener la imagen.')