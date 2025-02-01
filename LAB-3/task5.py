class RGBImage:
    def __init__(self, rows, cols):
        self.image = [[[0, 0, 0] for _ in range(cols)] for _ in range(rows)]

    def update_pixel(self, row, col, rgb):
        self.image[row][col] = rgb

    def get_pixel(self, row, col):
        return self.image[row][col]

image = RGBImage(2, 2)
image.update_pixel(0, 0, [255, 0, 0])
image.update_pixel(0, 1, [0, 255, 0])
print("Pixel RGB Value:", image.get_pixel(0, 1))
