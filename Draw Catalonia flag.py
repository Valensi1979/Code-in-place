from graphics import Canvas
import random

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 360

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)    
    
    for i in range(5):
        red_rectangle = canvas.create_rectangle(0, 80*i,CANVAS_WIDTH,(CANVAS_HEIGHT/9)*(2*i+1),'red')
        yellow_rectangle = canvas.create_rectangle(0,40*(2*i+1),CANVAS_WIDTH,(CANVAS_HEIGHT/9)*(2*i+1)+40,'yellow')
    
if __name__ == '__main__':
    main()