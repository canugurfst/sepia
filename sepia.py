from PIL import Image

def apply_sepia_filter(image):
    width, height = image.size
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))

            # Apply sepia filter formula
            sepia_r = int(0.393 * r + 0.769 * g + 0.189 * b)
            sepia_g = int(0.349 * r + 0.686 * g + 0.168 * b)
            sepia_b = int(0.272 * r + 0.534 * g + 0.131 * b)

            # Limit values to 255
            sepia_r = min(sepia_r, 255)
            sepia_g = min(sepia_g, 255)
            sepia_b = min(sepia_b, 255)

            pixels[x, y] = (sepia_r, sepia_g, sepia_b)

    return image

def main():
    input_image_path = "input.jpg"
    output_image_path = "output.jpg"

    # Open image file
    try:
        with Image.open(input_image_path) as image:
            # Apply sepia filter
            sepia_image = apply_sepia_filter(image)

            # Save sepia-filtered image
            sepia_image.save(output_image_path)
            print("Sepia filter applied and saved successfully.")
    except IOError:
        print("Unable to open or process image file.")

if __name__ == "__main__":
    main()
