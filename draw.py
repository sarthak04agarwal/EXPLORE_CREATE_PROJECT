
import pygame
from math import pi  

# Constructor for pygame
pygame.init()  

# Setting the width and the height of the screen
screen_Size = [500, 500]

# Setting the screen size 
screen = pygame.display.set_mode(screen_Size)    
   
# loop variable is using as flag     
loop = False      
while not loop:      
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:      
            loop = True    

    # Turns the whole screen into the color black   
    screen.fill((0, 0, 0))    
    
    # Draw on the screen a big circle
   
    # The big circle
    pygame.draw.circle(screen, (0, 255, 0), (250, 250), 200)
    #The two eyes
    pygame.draw.circle(screen, (255, 0, 0), (350, 200), 40)
    pygame.draw.circle(screen, (255, 0, 0), (150, 200), 40)
    # The nose
    pygame.draw.ellipse(screen, (0, 0, 255), [225, 250, 50, 60])

    # The mouth
    pygame.draw.circle(screen, "black", [250, 350], 50, 10, draw_bottom_left=True)
    pygame.draw.circle(screen, "black", [250, 350], 50, 10, draw_bottom_right=True)


    
    # This is required to project the image    
    pygame.display.flip()    
    
# Close the pop-up window when the user clicks on exit
pygame.quit()    