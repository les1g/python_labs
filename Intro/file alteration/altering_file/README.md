# BMP Image Modifier

This program modifies the pixel data of a BMP image file by replacing a portion of the image's pixels with custom colors (red, green, and yellow). The program reads an existing BMP image file, extracts its pixel data, and overwrites it with a new sequence of pixels. The modified image is then saved as a new BMP file.

## Features

- **Reads** an existing BMP image file (`ball.bmp`).
- **Modifies** the pixel data in the BMP file by replacing it with a sequence of custom colors.
- The program creates a new image with 3000 red pixels, 3000 green pixels, and 3000 yellow pixels, which overwrite the original pixels in the BMP file.
- **Writes** the modified pixel data to a new BMP image file (`new_ball.bmp`).

## How It Works

1. **Read BMP File**: The program opens a BMP image (`ball.bmp`) in binary read mode and reads its content.
2. **Extract Pixel Data Location**: The program identifies the location of the pixel data in the BMP header by examining bytes 10 to 14, which store the offset to the pixel data.
3. **Generate New Pixel Data**: A new sequence of pixel data is created. Each pixel is represented by a single byte:
   - `0x02` for red
   - `0x02` for green
   - `0x03` for yellow
   The new sequence consists of 3000 red pixels, followed by 3000 green pixels, and then 3000 yellow pixels.
4. **Overwrite Pixel Data**: The program replaces the original pixel data with the new sequence of pixels.
5. **Write Modified Image**: The modified BMP data is written to a new file (`new_ball.bmp`), preserving the original image format.

## Requirements

- Python 3.x
- The program assumes the input BMP file follows the standard BMP format where pixel data is located starting at byte 10 and is represented by RGB values.

## File Structure

- `ball.bmp`: Original BMP image file (must be present in the working directory).
- `new_ball.bmp`: New BMP image file created with modified pixel data (output file).
- `altering_file.py`: Python script containing the image modification code.

## How to Run

1. Ensure that you have a BMP file named `ball.bmp` in the same directory as the Python script.
2. Run the script using Python 3:

```bash
python altering_file.py
