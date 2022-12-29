from PIL import Image

density1 = 'Ñ@#W$9876543210?!abc;:+=-,._ '

density = " _.,-=+:;cba!?0123456789$W#@Ñ"


def main():

    try:
        image = Image.open("./cat100.jpg").convert("P")
    except:
        print("Cannot get the image")

    image = resize(image)
    grayscale_img: Image = to_grayscale(image)
    ascii_str = pixel_to_ascii(image)
    ascii_img = split_ascii_str(
        ascii_str=ascii_str, grayscale_img=grayscale_img)

    with open("./ascii_image.txt", "w") as f:
        f.write(ascii_img)


def resize(image: Image, new_width=48):
    """Adjusts the new_height with respect to the new_width and preserve aspect ratio so image is not distorted


    Args:
        image (Image): Pillow image_
        new_width (int, optional): Define the new width of the image. Defaults to 100.

    Returns:
        Calculated image height and width
    """

    old_width, old_height = image.size
    new_height = int(new_width * old_height / old_width)

    return image.resize((new_width, new_height))


def to_grayscale(image):
    """Converts the image to grayscale image

    Args:
        image (Image): Pelletized color image 

    Returns:
        Image:  Grayscale color image
    """
    return image.convert("L")


def pixel_to_ascii(image: Image) -> str:
    """Converts every pixel to ASCII character according to an intensity range

    Args:
        image (Image): Palettized Pillow image 

    Returns:
        str: String containing the ASCII version of the image
    """

    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += density[pixel//25]

    return ascii_str


def split_ascii_str(ascii_str, grayscale_img) -> str:
    """Splits the generated ASCII string with respect to the width of the image

    Args:
        ascii_str (str): Generated ASCII string from the image
        grayscale_img (Image): Converted grayscale image

    Returns:
        str: Split ASCII string with proper width
    """
    # Splits the generated ascii_str according to the new width of the image

    img_width = grayscale_img.width
    ascii_str_len = len(ascii_str)

    ascii_img = ""
    for index in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[index:index+img_width] + "\n"
    return "".join(ascii_img)


main()
