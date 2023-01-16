import sys
from PIL import Image, ImageOps

def main():
    img_check()
    input_img = sys.argv[1]
    output_img = sys.argv[2]
    shirt = Image.open("shirt.png")
    shirts_overlay(input_img, shirt, output_img)



def img_check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif sys.argv[1].split(".")[1] not in ["jpg", "jpeg", "png"]:
        sys.exit("Not an image format")

    elif sys.argv[2].split(".")[1] not in ["jpg", "jpeg", "png"]:
        sys.exit("Invalid output")

    elif sys.argv[1].split(".")[1] == "jpg" and sys.argv[2].split(".")[1] in ["jpeg", "png"]:
       sys.exit("Input and output have different extensions")

    elif sys.argv[1].split(".")[1] == "jpeg" and sys.argv[2].split(".")[1] in ["jpg", "png"]:
       sys.exit("Input and output have different extensions")

    elif sys.argv[1].split(".")[1] == "png" and sys.argv[2].split(".")[1] in ["jpeg", "jpg"]:
       sys.exit("Input and output have different extensions")

def shirts_overlay(image_input, shirt_image, output_image):
    size_shirt = shirt_image.size
    img_name = image_input.split(".")[0]

    try:
        img = Image.open(image_input)

        if image_input.split(".")[1] == "jpg":
            png_img = Image.open(image_input)
            png_img.save(f"{img_name}.png")
            png_img_cropped = ImageOps.fit(png_img, size = size_shirt)

            png_img_cropped.paste(shirt_image, (0,0), mask = shirt_image)
            png_img_cropped.save("after.png")
            png_img_cropped.save(output_image)

        else:
            img_cropped = ImageOps.fit(img, size = size_shirt)
            img_cropped.paste(shirt_image, (0,0), mask = shirt_image)
            img_cropped.save(output_image)

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
