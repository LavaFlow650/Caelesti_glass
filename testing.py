import png



# reader = png.Reader(filename='initial shenanigan/test_img.png')
# width, height, pixels, metadata = reader.read()
# print(metadata)

# pixel_list = list(pixels)
# print(pixels)

# Create from array
image_2d = [[255, 0, 0, 255],    # Red pixel
            [0, 255, 0, 255],    # Green pixel
            [0, 0, 255, 255]]    # Blue pixel

# Save as PNG
#png.from_array(image_2d, 'RGBA;16').save("output.png")

# Write with more control
writer = png.Writer(width=1, height=3, bitdepth=8, greyscale=False, alpha=True)
with open('output.png', 'wb') as f:
    writer.write(f, image_2d)


# width = 255
# height = 255
# img = []
# for y in range(height):
#     row = ()
#     for x in range(width):
#         row = row + (x, max(0, 255 - x - y), y)
#     img.append(row)
# with open('gradient.png', 'wb') as f:
#     w = png.Writer(width, height, greyscale=False)
#     w.write(f, img)