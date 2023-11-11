#function that generates gif file with scrolling text
#input = text:str
#generate a 300x300 pixel file scrolling from bottom up
#if text is long the file should be longer

#import the ncessary librayies
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def gif(text):
    direction = 'up'
    image_height = 300
    image_width = 300
    text_colour = (225, 225, 225)
    background_colour = (0, 0, 0)
    font = ImageFont.load_default()

    #handling the text length and paragraph sorting
    text_lines = []  # Split text into lines to simulate a paragraph
    words = text.split()
    current_line = ''
    for word in words:
        test_line = current_line + word + ' '
        if font.getlength(test_line) <= image_width:
            current_line = test_line
        else:
            text_lines.append(current_line)
            current_line = word + ' '
    text_lines.append(current_line)

    line_height = font.getsize('A')[1]  # Height of a line of text
    total_text_height = len(text_lines) * line_height

    numframes = (total_text_height + image_height)
    speed = 10
    output_file = "gif.mp4"
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(output_file, fourcc, speed, (image_width, image_height))
    while True:
        for i in range(numframes):
            img = Image.new('RGB', (image_width, image_height), background_colour)
            draw = ImageDraw.Draw(img)

            if direction:
                y = image_height - i

            current_y = y

            for line in text_lines:
                draw.text((10, current_y), line, font=font, fill=text_colour)
                current_y += line_height

            frame = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            video_writer.write(frame)

        video_writer.release()

# Example usage:
gif("If you believe that deceivers are colorful folk who mislead with elaborate lies and tall tales, you are greatly mistaken. The best deceivers utilize a
bland and inconspicuous front that calls no attention to themselves")
