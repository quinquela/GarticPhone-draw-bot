# GarticPhone-draw-bot
A bot that draws the images you give it but in black and white.

# Black and White Drawing Bot

This bot creates black and white drawings from the images you provide. The ideal image size should be 500x500 or smaller, as larger images will be resized. The higher the threshold for the black and white conversion, the more resources your PC will use, and therefore, the program may freeze. The more white the image contains, the faster the bot will complete the drawing.

![image](https://github.com/user-attachments/assets/ddf996f3-aede-49ba-87a4-5d0003cae2ac)

## Usage

When you run the program, a message will appear in the console asking you to input the path of the image. After that, you'll need to provide the threshold for the black and white conversion. For example, if the image contains many dark colors, I would recommend a lower threshold, or else it will turn out too dark.

![image](https://github.com/user-attachments/assets/b079f311-ffcf-49fb-986c-3022aeb6040c)

## Important Notes

- The program will control your mouse to draw.
- If you want to cancel the drawing at any time and are having trouble stopping the execution, simply move the mouse quickly to one of the corners of your screen, and the program will automatically stop executing.

## Requirements

- Python 3.x
- Required libraries: `Pillow`, `pyautogui`, `Time`

## Installation

1. Clone the repository.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run the bot with `python draw_bot.py`.

Enjoy creating your black and white drawings!
