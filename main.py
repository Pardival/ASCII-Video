import cv2 as cv
import pygame
from PIL import Image
import sys

def resize_img(image, new_width) :
    width, height = image.size
    scale = height / width
    new_height = int(new_width * scale)
    return image.resize((new_width,new_height)).convert('L')
    
def convert_pixels_to_ascii(image) :
    # Ñ@#W$9876543210?!abc;:+=-,._
    ELEMENT_DRAW1 = ["Ñ","@","#","W","$","9","8","7","6","5","4","3","2","1","0","?","!","a","b","c",";",":","+","=","-",",",".","_", "'"]
    ELEMENT_DRAW = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    pixels = image.getdata()
    ascii_image = "".join([ELEMENT_DRAW1[pixel // 9] for pixel in pixels])
    return ascii_image

def draw(image, new_width) :
    ascii_image_resized = convert_pixels_to_ascii(resize_img(image, new_width))
    total_pixels = len(ascii_image_resized)

    to_out = "\n".join([ascii_image_resized[index:(index + new_width)] for index in range(0, total_pixels, new_width)])
    sys.stdout.write(to_out)

    #TODO TO RENDER IN PYGAME
    # display_surface = pygame.display.set_mode((400, 400))
    # font = pygame.font.SysFont('didot.ttc', 25)
    # text = font.render(to_out, True, (255, 255, 255))
    # display_surface.fill((0, 0, 0))
    # textRect = text.get_rect()
    # display_surface.blit(text, textRect)
    # pygame.display.update()
            
def main() :
    cam = cv.VideoCapture(0)
    pygame.init()
    while True:
        # Capture frame-by-frame
        ret, frame = cam.read()
        # operation on the frame
        #ret = cam.set(cv.CAP_PROP_FRAME_WIDTH,320) 
        #ret = cam.set(cv.CAP_PROP_FRAME_HEIGHT,240)
        #greyFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #COLOR_HSV2BGR

        # Display the resulting frame
        cv.imshow('frame', frame)
        draw(Image.fromarray(frame), 140)
        if cv.waitKey(1) == ord('q'):
            break
    cam.release()
    cv.destroyAllWindows()

main()