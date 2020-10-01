from PIL import Image


image = Image.open("Xdoubt.jpg")


image.show()

width = str(image.width)
height = str(image.height)


half_width = image.width // 2
half_height = image.height // 2


new_size = (half_width, half_height)


smaller_image = image.resize(new_size)


smaller_image.save('Xdoubt_small.jpg')

smaller_image.show()