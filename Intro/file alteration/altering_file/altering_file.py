import struct

# Open the original BMP image file in binary read mode
ball_file = open('ball.bmp', 'rb')

# Read all the data from the BMP file
ball_data = ball_file.read()

# Close the file after reading
ball_file.close()

# The BMP image file format stores the location of the pixel data
# starting at byte 10 and ending at byte 14 (4 bytes in total).
pixel_data_loc = ball_data[10:14]

# Convert the byte sequence representing the pixel data location into an integer.
# '<L' specifies the format: little-endian 4-byte unsigned long integer
pixel_data_loc = struct.unpack('<L', pixel_data_loc)[0]

# Create a new sequence of pixels to overwrite the original pixels
# The new sequence consists of 3000 red pixels (0x02), followed by 3000 green pixels (0x02),
# and 3000 yellow pixels (0x03).
new_pixels = b'\x02'*3000 + b'\x02'*3000 + b'\x03'*3000

# Create a new image data by combining the original data with the new pixels
# The image data before the pixel data is left unchanged, followed by the new pixel data,
# and then the remaining part of the original image data is appended.
new_ball_data = ball_data[:pixel_data_loc] + \
                new_pixels + \
                ball_data[pixel_data_loc + len(new_pixels):]

# Write the modified image data to a new file
new_ball_file = open('new_ball.bmp', 'wb')
new_ball_file.write(new_ball_data)
new_ball_file.close()
