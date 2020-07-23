from random import randint as rn
file1 = open("logs.txt","a") 

def log(logText, error=False, log=True):
    if error and not log:
        file1.write(f'The program logged an error. {logText}\n')
    elif not error and log:
        file1.write(f'Logging {logText}\n')
    elif error and log: 
        file1.write(f'There was an error and a log: {logText}\n')
    
import pygame

print("Welcome to paint program")
print("launching...")

dis_width = 720
dis_height = 500

log(logText = "set display")

pygame.init()
screen = pygame.display.set_mode([dis_width,dis_height])
pygame.display.set_caption("Paint")
log(logText = "set caption + init")

gameOn = True
mouse_down = False
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (200, 200, 200, 200)
BROWN = (255, 130, 65, 100)
WHITE = (225, 225, 225)
DARKGREY = (25,25,25,10)
currentColour = RED
radius = 15
bgColor = BLACK
fDown = False
log(logText = "variables")


rec_width = int(dis_width * 0.1)
rec_height = int(dis_height * 0.09)
log(logText = "set recw width + height")

redRectangle = pygame.Rect((0, 0), (rec_width, rec_height))
greenRectangle = pygame.Rect((rec_width, 0), (rec_width, rec_height))
blueRectangle = pygame.Rect((2*rec_width, 0), (rec_width, rec_height))
brownRectangle = pygame.Rect((3*rec_width, 0),(rec_width, rec_height))
greyRectangle = pygame.Rect((4*rec_width,0), (rec_width, rec_height))
blackRectangle = pygame.Rect((5*rec_width,0), (rec_width, rec_height))

maximize = pygame.image.load("maximize.png")
minimize = pygame.image.load("minimize.png")
randColor = pygame.image.load("random_color.png")
minusButton = pygame.image.load("minus.png")
plusButton = pygame.image.load("plus.png")
eraser = pygame.image.load("eraser.png")
clearButton = pygame.image.load("clear.png")
maximize = pygame.transform.scale(maximize, (rec_height, rec_height))
minimize = pygame.transform.scale(minimize, (rec_height, rec_height))
randColor = pygame.transform.scale(randColor, (rec_height, rec_height))
clearButton = pygame.transform.scale(clearButton, (rec_height, rec_height))
eraser = pygame.transform.scale(eraser, (rec_height, rec_height))
minusButton = pygame.transform.scale(minusButton, (rec_height, rec_height))
plusButton = pygame.transform.scale(plusButton, (rec_height, rec_height))
minusRect = minusButton.get_rect(topleft=(0, rec_height))
plusRect = minusButton.get_rect(topleft=(rec_height, rec_height))
eraserRect = eraser.get_rect(topleft=(2*rec_height, rec_height))
clearRect = clearButton.get_rect(topleft=(3*rec_height, rec_height))
randRect = randColor.get_rect(topleft=(4*rec_height, rec_height))
maxRect = maximize.get_rect(topleft=(6*rec_height, rec_height))
minRect = minimize.get_rect(topleft=(7*rec_height, rec_height))

screen.fill(bgColor)

topRectangle = pygame.Rect((0,0),(dis_width, 2 * rec_height))
log(logText = "init buttons")

log(logText = "game loop init!!")
while gameOn:

    fDown = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
            log(logText = "Program Exited")
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            spot = pygame.mouse.get_pos()
            if minusRect.collidepoint(spot):
                if radius > 5:
                    radius -= 5
                    log(logText = "smaller")
            elif plusRect.collidepoint(spot):
                if radius < 40:
                    radius += 5
                    log(logText = "enlarge")
            else:
                mouse_down = True

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(bgColor)
                log(logText = "clear")
            elif event.key == pygame.K_b or pygame.K_f:
                fDown = True
                log(logText = "fill")
    
    if fDown and mouse_down:
        spot = pygame.mouse.get_pos()
        if redRectangle.collidepoint(spot):
            bgColor = RED
            screen.fill(bgColor)
        elif greenRectangle.collidepoint(spot):
             bgColor = GREEN
             screen.fill(bgColor)
        elif blueRectangle.collidepoint(spot):
             bgColor = BLUE
             screen.fill(bgColor)
        elif brownRectangle.collidepoint(spot):
            bgColor = BROWN
            screen.fill(bgColor)
        elif greyRectangle.collidepoint(spot):
            bgColor = GREY
            screen.fill(bgColor)
        elif blackRectangle.collidepoint(spot):
            bgColor = BLACK
            screen.fill(bgColor)

    if mouse_down:
        # if the event is pressing the mouse
        # get the current position of the mouse
        spot = pygame.mouse.get_pos()
        if redRectangle.collidepoint(spot):
            # if the current position is within the red square, change the colour to red
            currentColour = RED
            log(logText = "change to RED")
        elif greenRectangle.collidepoint(spot):
            # if the current position is within the green square, change the colour to green
            currentColour = GREEN
            log(logText = "Change to GREEN")
        elif blueRectangle.collidepoint(spot):
            # if the current position is within the blue square, change the colour to blue
            currentColour = BLUE
            log(logText = "change to BLUE")
        elif brownRectangle.collidepoint(spot):
            # if the current position is within the brown square, change the colour to brown
            currentColour = BROWN
            log(logText = "change to BROWN")
        elif greyRectangle.collidepoint(spot):
            #if the current position is within the grey square, change the colour to grey
            currentColour = GREY
            log(logText = "change to GREY")
        elif blackRectangle.collidepoint(spot):
            #if the current position is within the black square, change the colour to black
            currentColour = BLACK
            log(logText = "change to BLACK")
        elif clearRect.collidepoint(spot):
            #If the current position is within the grey square, clear the screen
            screen.fill(bgColor)
            log(logText = "clear")
        elif eraserRect.collidepoint(spot):
            #if the current position is within the eraser, clear the screen
            currentColour = bgColor
            log(logText = "eraser")
        elif randRect.collidepoint(spot):
            #if the current position is within the rand color, choose a random color the screen
            choice = int(rn(0,5))
            if choice == 1:
                currentColour = RED
            elif choice == 2:
                currentColour = GREEN
            elif choice == 3:
                currentColour = BLUE
            elif choice == 4:
                currentColour = GREY
            elif choice == 5:
                currentColour = BROWN
        elif minRect.collidepoint(spot):
            #if we click on the minimize button...
            dis_width = 720
            dis_height = 500
            screen = pygame.display.set_mode([dis_width,dis_height])
            
        elif maxRect.collidepoint(spot):
            #if we click on the minimize button...
            dis_width = 1200
            dis_height = 700
            screen = pygame.display.set_mode([dis_width,dis_height])
            
        else:
            # if it's not within a button, place a circle at the spot the mouse was pressed
            pygame.draw.circle(screen, currentColour, spot, radius)
        
    pygame.draw.rect(screen, DARKGREY, topRectangle)
    pygame.draw.rect(screen, RED, redRectangle)
    pygame.draw.rect(screen, GREEN, greenRectangle)
    pygame.draw.rect(screen, BLUE, blueRectangle)
    pygame.draw.rect(screen, BROWN, brownRectangle)
    pygame.draw.rect(screen, GREY, greyRectangle)
    pygame.draw.rect(screen, BLACK, blackRectangle)
    
    pygame.draw.circle(screen, currentColour, (dis_width - radius, radius), radius)
    
    screen.blit(maximize, maxRect)
    screen.blit(minimize, minRect)
    screen.blit(plusButton, plusRect)
    screen.blit(minusButton, minusRect)
    screen.blit(eraser, eraserRect)
    screen.blit(clearButton, clearRect)
    screen.blit(randColor, randRect)
    pygame.display.update()

pygame.quit()
file1.close()