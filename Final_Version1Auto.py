import os
import pygame
from math import sin, radians, degrees, copysign
from pygame.math import Vector2
from pygame.locals import *
pygame.init()
#Bildschrimgrösse
screen = pygame.display.set_mode((1500, 920))


#Auto 360 Grad bewegung


#car 1 Daten zum Fahren
class Car1():
    def __init__(self, x, y, angle=0.0, length=2, max_steering=500, max_acceleration=30):
        self.x = x
        self.y = y
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = max_acceleration
        self.max_steering = max_steering
        self.max_velocity = 10
        self.brake_deceleration = 6000
        self.free_deceleration = 20
        self.acceleration = 2
        self.steering = 0.0

    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))

        if self.steering:
            turning_radius = self.length / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * dt
        self.angle += degrees(angular_velocity) * dt

    
#car 2 Daten zum Fahren
class Car2:
    def __init__(self, x, y, angle=0.0, length=2, max_steering=500, max_acceleration=30):
        self.position = Vector2(x, y)
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = max_acceleration
        self.max_steering = max_steering
        self.max_velocity = 10
        self.brake_deceleration = 6000
        self.free_deceleration = 20

        self.acceleration = 2
        self.steering = 0.0

    def update(self, dt):
        self.velocity += (self.acceleration * dt, 0)
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))

        if self.steering:
            turning_radius = self.length / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * dt
        self.angle += degrees(angular_velocity) * dt

#ingame sachen wegen Fenster
class Game:
    def __init__(self):
        pygame.display.set_caption("Rocked League 2d")
        width = 1280
        height = 720
        
        self.screen = pygame.display.set_mode((1500, 920))
        self.clock = pygame.time.Clock()
        self.ticks = 60
        self.exit = False

    def run(self):
        #Bilder und wichtige Rects/Postionen
        green1 = pygame.Color('blue') #für ori dann darkgreen
        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path1 = os.path.join(current_dir, "c:/Users/diA/workspace/python/modul404/sven/rocketleague-in-2d/Bilder/car1.png")
        image_path2 = os.path.join(current_dir,"c:/Users/diA/workspace/python/modul404/sven/rocketleague-in-2d/Bilder/car2.png")
        platz= pygame.image.load("c:/Users/diA/workspace/python/modul404/sven/rocketleague-in-2d/Bilder/fussballfeld.jpg")
        screen = pygame.display.set_mode((1500, 920))
        

        car1 = Car1(5,14.5)
        car2 = Car2(42,14.5)
        car_image1 = pygame.image.load(image_path1)
        car_image2 = pygame.image.load(image_path2)
        car1_rect = car_image1.get_rect()
        car2_rect = car_image2.get_rect()
        pygame.draw.rect(car_image1,red,(5-5,5,100,43,),2,10)
        pygame.draw.rect(car_image2,red,(5-5,5,100,43,),2,10)
        
        ppu = 32


        size = width, height = 1500, 920
        
        speed = [1, 1]
        screen = pygame.display.set_mode(size)
        ball = pygame.image.load("c:/Users/diA/workspace/python/modul404/sven/rocketleague-in-2d/Bilder/ball.png")
        ballrect = ball.get_rect()
        pygame.draw.circle(screen, (0,0,255), (150, 50), 15, 1)
        #physik geschichte für die beiden Autos
        while not self.exit:
            dt = self.clock.get_time() / 1000

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
            # Player input Car1
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_UP]:
                if car1.velocity.x < 0:
                    car1.acceleration = car1.brake_deceleration
                else:
                    car1.acceleration += 1 * dt
            elif pressed[pygame.K_DOWN]:
                if car1.velocity.x > 0:
                    car1.acceleration = -car1.brake_deceleration
                else:
                    car1.acceleration -= 1 * dt
            elif pressed[pygame.K_SPACE]:
                if abs(car1.velocity.x) > dt * car1.brake_deceleration:
                    car1.acceleration = -copysign(car1.brake_deceleration, car1.velocity.x)
                else:
                    car1.acceleration = -car1.velocity.x / dt
            else:
                if abs(car1.velocity.x) > dt * car1.free_deceleration:
                    car1.acceleration = -copysign(car1.free_deceleration, car1.velocity.x)
                else:
                    if dt != 0:
                        car1.acceleration = -car1.velocity.x / dt
            car1.acceleration = max(-car1.max_acceleration, min(car1.acceleration, car1.max_acceleration))
             
            if pressed[pygame.K_RIGHT]:
                car1.steering -= 30 * dt
            elif pressed[pygame.K_LEFT]:
                car1.steering += 30 * dt
            else:
                car1.steering = 0
            car1.steering = max(-car1.max_steering, min(car1.steering, car1.max_steering))

            #player Input Car2
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_s ]:
                if car2.velocity.x < 0:
                    car2.acceleration = car2.brake_deceleration
                else:
                    car2.acceleration += 1 * dt
            elif pressed[pygame.K_w]:
                if car2.velocity.x > 0:
                    car2.acceleration = -car2.brake_deceleration
                else:
                    car2.acceleration -= 1 * dt
            elif pressed[pygame.K_d]:
                if abs(car2.velocity.x) > dt * car2.brake_deceleration:
                    car2.acceleration = -copysign(car2.brake_deceleration, car2.velocity.x)
                else:
                    car2.acceleration = -car2.velocity.x / dt
            else:
                if abs(car2.velocity.x) > dt * car2.free_deceleration:
                    car2.acceleration = -copysign(car2.free_deceleration, car2.velocity.x)
                else:
                    if dt != 0:
                        car2.acceleration = -car2.velocity.x / dt
            car2.acceleration = max(-car2.max_acceleration, min(car2.acceleration, car2.max_acceleration))

            if pressed[pygame.K_a]:
                car2.steering -= 70 * dt
            elif pressed[pygame.K_d]:
                car2.steering += 70 * dt
            else:
                car2.steering = 0
            car2.steering = max(-car2.max_steering, min(car2.steering, car2.max_steering))
            # Logic
            car2.update(dt)

            # Logic
            car1.update(dt)
            car2.update(dt)
            # Drawing 
            screen.blit(platz, (0,0))
            #walls für collision mit autos
            wallup = pygame.draw.rect(screen,green1,[0,0,1500,10])
            walldown = pygame.draw.rect(screen,green1,[0,910,1500,10])
            wallleft = pygame.draw.rect(screen,green1,[0,0,10,920])
            wallright = pygame.draw.rect(screen,green1,[1490,0,10,920])

            #tor walls
            walltorleft = pygame.draw.rect(screen,green1,[10,347,34,227],6)
            walltorright = pygame.draw.rect(screen,green1,[1454,347,34,227],6)
            #Ball to auto


        

            if car1_rect.colliderect(wallup):
                print("ja")
                
               
            #physik geschichte auto rotation 360 grad
            rotated1 = pygame.transform.rotate(car_image1, car1.angle)
            rect = rotated1.get_rect()
            self.screen.blit(rotated1, car1.position * ppu - (rect.width / 2, rect.height / 2))
            
            rotated2 = pygame.transform.rotate(car_image2, car2.angle)
            rect2 = rotated2.get_rect()
            self.screen.blit(rotated2, car2.position * ppu - (rect2.width / 2, rect2.height / 2))
       
            
            screen.blit(ball,(720,425))
            pygame.display.flip()
            self.clock.tick(self.ticks)
        pygame.quit()

#########schrift für Knöpfe##################
font = pygame.font.SysFont('Roboto', 45)#####
#############################################


#3,2,1 Timer
'''def timer():
    clock = pygame.time.Clock()
    counter, text = 3, '3'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font1 = pygame.font.SysFont('Consolas', 600,)
   
    while True:
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter >0 else game.run()
            if e.type == pygame.QUIT: break
        else:
            screen.fill((255, 255, 255))
            screen.blit(font1.render(text, True, (0, 0, 0)), (-80, 140))
            pygame.display.flip()
            clock.tick(60)
            continue
        break
    '''

#farben

bg = pygame.image.load("c:/Users/diA/workspace/python/modul404/sven/rocketleague-in-2d/Bilder/back.jpg")
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#define global variable
clicked = False
counter = 0


#Menü
class button():
    #colours for button and text
    button_col = (255, 0, 0)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = black
    width = 280
    height = 80

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):

        global clicked
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)
        #check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)
        
        #add shading to button
        pygame.draw.line(screen, white, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, white, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
        #add text to button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action


#Was in den Knöpfe stehen soll und ihre Position
again = button(600, 400, 'Play')
quitt = button(600, 550, 'Quit')


###Titel inside Home
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)
X = 1550
Y = 400
display_surface = pygame.display.set_mode((X, Y))
font3 = pygame.font.Font('freesansbold.ttf', 80)
gamename = font3.render('Rocked League 2d', True, blue,)
textRect = gamename.get_rect()
textRect.center = (X // 2, Y // 2)


X1 = 1500
Y1 = 560

display_surface2 = pygame.display.set_mode((X1, Y1))
font4 = pygame.font.Font('freesansbold.ttf', 25)
unserenamen = font4.render('Sven Hayoz & Linus Schaub',True,blue)
textRect2 = unserenamen.get_rect()
textRect2.center = (X1 // 2, Y1 // 2)


game = Game()

#Ablauf ganzes Game!

def menu():
    run = True

    while run:
        screen.blit(bg,(0,0))
        
        display_surface.blit(gamename, textRect)
        display_surface.blit(unserenamen, textRect2)
        if again.draw_button():
            game.run()
        if quitt.draw_button():
            quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False	


        pygame.display.update()

menu()
