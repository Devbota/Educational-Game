import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Main Menu')

background = pygame.image.load("Moon.png")
hbackground = pygame.transform.scale(background, (600,600))

f_temp = pygame.image.load("education.png")
f_background = pygame.transform.scale(f_temp, (400,400))
c_temp = pygame.image.load("Keyboard.png")
c_background = pygame.transform.scale(c_temp, (500,500))

mathsfilter = False
csfilter = False
physicsfilter = False
quizcheck = True


buttonpress = False
filter = False
controls = False

#initialise variables for game

charvel = 5

fps = 60
timer = pygame.time.Clock()
main_menu = False
colour = (100, 100, 255)
font = pygame.font.Font('freesansbold.ttf', 20)
#initalises information for pygame window
menu_value = 0
money = 80
skin = 0
items = [
    {'name': 'Wanderer', 'cost': 0},   
    {'name': 'Skullio', 'cost': 100},   
    {'name': 'Froggy', 'cost': 250}
]

mathQuestions = [
    {
        "question": "What is 19 x 19?",
        "options": ["352", "366", "361"],
        "answer": "361"
    },
    {
        "question": "Expand 5(x + 3)",
        "options": ["5x + 3", "5x + 15", "5x + 8"],
        "answer": "5x + 15"
    },
    {
        "question": "Simplify 4a + 5b + 6b + 11a",
        "options": ["26ab", "9a + 17b", "15a + 11b"],
        "answer": "15a + 11b"
    },
    {
        "question":"Is 66 a multiple of 3 and 11?",
        "options": ["Yes", "No", "Possibly"],
        "answer": "Yes"
    },
    {
       "question":"Express 32/50 as a percentage",
       "options": ["64%", "66%", "60%"],
       "answer": "64%"   
    },
    {
       "question":"Which one of these lines goes through the point (0, 1)",
       "options": ["y = x", "x = 1", "x + y = 1"],
       "answer": "x + y = 1"   
    },
    {
       "question":"Calculate: 578 ÷ (38.7 - 11.2) to 2 d.p",
       "options": ["21.02", "11.02", "17.02"],
       "answer": "21.02"   
    }
]

csQuestions = [
    {
        "question": "What does a rectangle in a flowchart show?",
        "options": ["Decision", "Process", "Input"],
        "answer": "Process"
    },
    {
        "question": "What does the acronym CPU stand for?",
        "options": ["Central Processing Unit", "Control Processing Unit", "Command Processing Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "What is a Synatx error",
        "options": ["A typo or incorrect spelling", "Arithmetic mistakes", "Logical mistakes"],
        "answer": "A typo or incorrect spelling"
    },
    {
        "question":"Which statement is used to specify a decimal number?",
        "options": ["int", "str", "float"],
        "answer": "float"
    },
    {
       "question":"How can strings and variables be told apart",
       "options": ["The data in a string is stored inside quotes", "By its name", "By its size"],
       "answer": "The data in a string is stored inside quotes"   
    },
    {
        "question":"What type of list does a Binary Search need?",
        "options": ["numerical", "ordered", "any"],
        "answer": "ordered"
    },
    {
       "question":"What language does a computer understand",
       "options": ["Binary", "English", "decimal numbers"],
       "answer": "Binary"   
    }

]

physicsQuestions = [
    {
        "question": "What is found at the Centre of the Solar system?",
        "options": ["The Earth", "The Sun", "The Moon"],
        "answer": "The Sun"
    },
    {
        "question": "What is a vector quantity?",
        "options": ["Has a magnitude and direction", "Has a direction", "Has a magnitude"],
        "answer": "Has a magnitude and direction"
    },
    {
        "question": "Which of these is a desirable property of a fuel for burning?",
        "options": ["Gives moderate amount of smoke", "Will not burn too steadily to be wasteful", "Gives bright clear flame"],
        "answer": "Gives bright clear flame"
    },
    {
        "question":"What energy transfer applies to infrared room heater?",
        "options": ["Heating", "Energy", "Radiation"],
        "answer": "Radiation"
    },
    {
       "question":"Which form of energy has a bullet fired from a gun?",
       "options": ["Kinetic", "Elastic/strain potential", "Nuclear"],
       "answer": "Kinetic"   
    },
    {
        "question":"Which is NOT true about how a loudspeaker works?",
        "options": ["The input source of energy is electrical", "Diaphragm vibrations cause air particles to vibrate", "It pushes and pulls the nearby air creating sound"],
        "answer": "The diaphragm vibrations cause air particles to vibrate up and down"
    },
    {
       "question":"Which is NOT true about how the human ear works?",
       "options": ["The vibrating ear bones causes the ear drum to vibrate", "Sound waves cause the ear drum to vibrate to and fro", "The ear system triggers nerve signals to the brain"],
       "answer": "Vibrating ear bones causes the ear drum to vibrate"   
    }
]


class Button:
  def __init__(self,txt,pos):
    self.text = txt
    self.pos = pos
    self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))
#constructor is used here to create objects in the button class
  def draw(self):
    pygame.draw.rect(screen, 'light gray', self.button, 0, 5)
    text = font.render(self.text, True, 'black')
    screen.blit(text, (self.pos[0] + 15, self.pos[1] + 7))
    
#method used to draw boxes for buttons

  def click_input(self):
    if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
      return True
    else:
      return False
#method used to check if the box has been pressed


def draw_home():
  pygame.display.set_caption("Home")
  button = Button('Main Menu', (330, 550))
  button.draw()
  return button.click_input()
#code used to enter the main menu
  
def draw_menu(): 
  value = -1
  ncolour = (100, 0, 255,)
  pygame.draw.rect(screen, ncolour, [100, 100, 400, 400])
  #exit menu button
  b1 = Button('Practice Quiz', (170, 120)) 
  b1.draw()
  b2 = Button('Main Game', (170, 202.5))
  b2.draw() 
  b3 = Button('Item Shop', (170, 285)) 
  b3.draw()
  b4 = Button('Contols', (170, 367.5))
  b4.draw()
#each of the 4 buttons is drawn
  home_btn = Button('Home', (170, 450))
  home_btn.draw()
  #home button is drawn
  if home_btn.click_input():
    value = 5
  if b1.click_input():
    value = 1
  if b2.click_input():
    value = 2
  if b3.click_input():
    value = 3
  if b4.click_input():
    value = 4
#assigns value to each button when it is clicked
  return value
  

def draw_shop():
    pygame.display.set_caption("Item Shop")
    global fps
    global money
    global skin
    #assigned to global variables to allow to change
    fps = 10
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
#Gets position of the mouse when pressed
        for i, item in enumerate(items):
            if pos[1] > (i * 50 + 100) and pos[1] < ((i + 1) * 50 + 100):    
            #Checks if click occured on any items
                if money >= item['cost']:
                    money -= item['cost']
                    print(item['name'],'Has been bought for £',item['cost'],'. You have £',money, 'left.') 
                    if item['name'] == 'Wanderer':
                       skin = 0
                    elif item['name'] == 'Skullio':
                       skin = 1
                    elif item['name'] == 'Froggy':
                       skin = 2
                    
                #comparison to see if money is enough to purchase item
                    #here is where you assign the character to use
                else:
                    print('Insufficient funds to buy',item['name'],'.')
    
    for i, item in enumerate(items):
        itext = f'{item["name"]} - £{item["cost"]}'
        t_surface = font.render(itext, True, (0, 255, 255))
        t_rect = t_surface.get_rect()
        t_rect.center = (300, (i + 1) * 50 + 100)
        screen.blit(t_surface, t_rect)
    #displays items on the screen
    mtext = f'Money: £{money}'
    msurface = pygame.font.Font(None, 24).render(mtext, True, (0, 255, 255))
    mrect = msurface.get_rect()
    mrect.topright = (500, 0)
    screen.blit(msurface, mrect)
    #displays current balance


def draw_quiz():
#initialisation of variables
  global main_menu
  global money
  global quizcheck
  questions = 0
  current_question = 0
  points = 0
  fps = 10
  earnt = 0
  running = True
#set quiz title
  pygame.display.set_caption("Practice Quiz")
#checks if a filter is active and which quiz to load
  if mathsfilter:
       quizcheck = True
       questions = mathQuestions
  elif csfilter:
       quizcheck = True
       questions = csQuestions
  elif physicsfilter:
       quizcheck = True
       questions = physicsQuestions
  else:
       quizcheck = False
       text = font.render("Please Select A Filter in Controls!", True, (255, 255, 255))
       screen.blit(text, (150, 125))
       

    
#enter game loop
  if quizcheck:
    while running:
        screen.blit(hbackground, (0,0))
#condition to exit code
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                  running = False
#gets position of mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                option_a = 50
#displays first question option
                for option in questions[current_question]["options"]:
                    optext = font.render(option, True, (0,0,0))
                    oprect = optext.get_rect()
                    oprect.left = 10
                    oprect.top = option_a
#checking condition for mouse + options
                    if oprect.collidepoint(pos):
                        if option == questions[current_question]["answer"]:
                            print("Right Answer, Well Done!")
                            points += 1
                            current_question += 1
                        else:
                            print("Wrong Answer!")
                            current_question += 1

                    option_a += 50
#checks if quiz has reached the end
                if current_question >= len(questions):
                    running = False
                    if points == 7: #determines rewards for points
                      earnt = 50
                      money += earnt
                    elif points == 6:
                      earnt = 40
                      money += earnt
                    elif points == 5:
                       earnt = 30
                       money += earnt                       
                    print("Quiz completed!")
                    print(f"You scored {points} out of {len(questions)}")
                    if earnt > 0:
                      print(f"You have earnt £{earnt}, enjoy your cash!")
                    else:
                      print("You unfortunately haven't earnt any money this time, try again!")

        if running:
            # Render the current question and options
            if current_question < len(questions):
                current_q = questions[current_question]
                qstext = font.render(current_q["question"], True, (0,255,255))
                screen.blit(qstext, (10, 10))
                option_a = 50

                for option in current_q["options"]:
                    optext = font.render(option, True, (0, 255, 255))
                    screen.blit(optext, (10, option_a))
                    option_a += 50

            # Update the display
            pygame.display.update()

            # Wait for a short amount of time to control the frame rate
            pygame.time.delay(int(1000/fps))

        

    main_menu = True




def draw_filter():
#change variables to global
    pygame.display.set_caption("Quiz Filters")
    global run
    global filter
    global buttonpress
    global fps
    global mathsfilter
    global csfilter 
    global physicsfilter 
    delaytime = 100
#checks if filter is active
    if filter:
#draws background for the buttons
        screen.blit(f_background, (100, 100))
#draws each of the buttons for filters
        ma1 = Button('Enable Maths', (170, 120)) 
        ma1.draw()
        cs2 = Button('Enable Computer Sci', (170, 202.5))
        cs2.draw() 
        ph3 = Button('Enable Physics', (170, 285)) 
        ph3.draw()
        r1 = Button('Reset', ((170, 455)))
        r1.draw()
#check for conditions to allow button to return correct filter
        if ma1.click_input() and csfilter is False and physicsfilter is False:
           mathsfilter = True
#Delay added to ensure text isn't too sensitive
           pygame.time.delay(delaytime)
           print("Maths Questions enabled")
        elif cs2.click_input() and mathsfilter is False and physicsfilter is False:
           csfilter = True
           pygame.time.delay(delaytime)
           print("Computer Science Questions enabled")
        elif ph3.click_input() and mathsfilter is False and csfilter is False:
           physicsfilter = True
           pygame.time.delay(delaytime)
           print("Physics Questions selected")
        elif r1.click_input():
           pygame.time.delay(delaytime)
           if physicsfilter or csfilter or mathsfilter:
              pygame.time.delay(delaytime)
              print("Question options Reset!")
           if not physicsfilter and not csfilter and not mathsfilter:
            pygame.time.delay(delaytime)
            print("Filters have already been reset!")
           mathsfilter = False
           csfilter = False
           physicsfilter = False
#get all events in pygame
        events = pygame.event.get()
        for event in events:
#check if escape is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
#update bool variables
                    filter = False
                    buttonpress = False
#Quit the programme
            elif event.type == pygame.QUIT:
               run = False
    else:
#return state
        return filter, buttonpress
    pygame.display.update()

def draw_controls():
    pygame.display.set_caption("Controls")
#global keyword to make these variables global varaibles
    global controls
    global buttonpress
#check if controls is active
    if controls is True:
#Fill screen
        screen.fill((255,255,255))
#insert keyboard image
        screen.blit(c_background, (80, 100))
        events = pygame.event.get()
        for event in events:
#detect if escape is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    controls = False
                    buttonpress = False
    else:
#return the state of filter and buttonpress
        return filter, buttonpress
    pygame.display.update()    
 


def background_set(name):
#loads file for purple tile
   pic = pygame.image.load(name)
#stores dimensions + position of purple.png
   _, _, width, height = pic.get_rect()
   tiles = []

#for loop which DIVS screen width from tile width
   for i in range(WIDTH // width + 1):
      #for loop which DIVS screen height from tile height
      for j in range(HEIGHT // height + 1):
        #if in range then note position of each tile to enter and add to tiles list
         pos = (i* width, j * height)
         tiles.append(pos)
#retuns created list and image being used
   return tiles, pic

#function for displaying background and any images on screen  
def drawbg(screen, background, bg_image, char, objects, xoffset):
   for tile in background:
      screen.blit(bg_image, tile)

   for object in objects:
      object.draw(screen, xoffset)
#utilises draw method    
   char.draw(screen, xoffset)

#update screen for any changes
   pygame.display.update()



def flip(sprites):
   return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def draw_sprites(dir1, dir2, width, height, direction = False):
   path = join("Characters", dir1, dir2)
   #loads every file inside of the directory
   pics = [f for f in listdir(path) if isfile(join(path, f))]

  #dictonary to store values
   sprites_total = {}

   for pic in pics:
      #loads the image and apprends path to directory 
      single_sprite = pygame.image.load(join(path, pic)).convert_alpha()

      sprites = []
      #code in order to split the different sprite states into a single sprite
      for i in range(single_sprite.get_width() // width):
         surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
         rect = pygame.Rect(i * width, 0, width, height)
         surface.blit(single_sprite, (0,0), rect)
         sprites.append(pygame.transform.scale2x(surface))

    #Adds two keys to dictionary for every single animation in order to change direction
      if direction:
         sprites_total[pic.replace(".png", "") + "_right"] = sprites
         sprites_total[pic.replace(".png", "") + "_left"] = flip(sprites)
      #otherwise direction is same
      else:
         sprites_total[pic.replace(".png", "")] = sprites

   return sprites_total      

def get_slab(size):
   path = join("Environment", "Terrain.png")
   #loads the terrain image and converts it to a pygame surface with alpha transparency.
   pic = pygame.image.load(path).convert_alpha()
   #creates a new pygame surface with a transparent alpha channel and sets its size to the size parameter passed to the function.
   surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
   rect = pygame.Rect(0,0, size, size)
   surface.blit(pic, (0,0), rect)
   return pygame.transform.scale2x(surface)




#Subclass of in-built sprite class for accurate collision 
class Char(pygame.sprite.Sprite):
   colour = (0, 255, 0)
   gravity = 1
   SPRITES = draw_sprites("Character Select", "Wanderer", 32, 32, True)
   delay = 8
  #use to create objects from the class
   def __init__(self, x, y, width, height):
      super().__init__()
      self.rect = pygame.Rect(x, y, width, height)
      self.x_velo = 0
      self.y_velo = 0
      self.mask = None
      self.direction = "right"
      self.a_count = 0
      self.fall_counter = 0
      self.jump_counter = 0

   def move(self,xdist, ydist):
      self.rect.x += xdist
      self.rect.y += ydist

   def jump(self): 
      self.y_velo = -self.gravity * 7
      self.a_count = 0 
      self.jump_counter += 1
      if self.jump_counter == 1:
         self.fall_counter = 0

   def leftm(self, velocity):
    self.x_velo = -velocity
    if self.direction != "left":
       self.direction = "left"
       self.a_count = 0

   def rightm(self,velocity):
    self.x_velo = velocity
    if self.direction != "right":
        self.direction = "right"
        self.a_count = 0

   def sprite_animate(self):
      #default animation of sprite is idle
      if skin == 0:
        single_sprite = "idle"
        if self.y_velo < 0:
            single_sprite = "jump"
      
        elif self.y_velo > 3:
          single_sprite = "fall"
          
      #when character is moving, use walk sprites
        if self.x_velo != 0:
           single_sprite = "walk"
      elif skin == 1:
       single_sprite = "idle1"
       if self.y_velo < 0:
            single_sprite = "jump1"
      
       elif self.y_velo > 3:
         single_sprite = "fall1"
          
       if self.x_velo != 0:
         single_sprite = "walk1"

      elif skin == 2:
       single_sprite = "idle2"
       if self.y_velo < 0:
            single_sprite = "jump2"
      
       elif self.y_velo > 3:
         single_sprite = "fall2"
          
       if self.x_velo != 0:
         single_sprite = "walk2"

      #changes the sprite picking new image from sheet
      single_sprite_name = single_sprite + "_" + self.direction
      sprites = self.SPRITES[single_sprite_name]
      s_index = (self.a_count // self.delay) % len(sprites)
      self.sprite = sprites[s_index]
      self.a_count += 1
      self.change()



   def loop(self,fps):
      #calcs acceleration downwards and sets y velocity to with 1 or that value
      self.y_velo += min(1, (self.fall_counter / fps) * self.gravity)
      #called each time for player movement
      self.move(self.x_velo, self.y_velo)
      
      self.fall_counter += 1
      self.sprite_animate()

   def change(self):
      self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
      self.mask = pygame.mask.from_surface(self.sprite)

   def draw(self, scr, xoffset):
      scr.blit(self.sprite,(self.rect.x - xoffset, self.rect.y))
    
   def landed(self):
      self.fall_counter = 0
      self.y_velo = 0
      self.jump_counter = 0

   def head_collide(self):
      self.count = 0
      self.y_velo *= -1



def vert_collision_manipulate(char, objects, ydist):
   objects_collide = []
   for object in objects:
      if pygame.sprite.collide_mask(char, object):
         if ydist < 0:
            char.rect.top = object.rect.bottom
            char.head_collide()
         elif ydist > 0:
            char.rect.bottom = object.rect.top
            char.landed()
        
   objects_collide.append(object)
   return objects_collide


def move_func(char, objects):
   #Gets currently pressed key
   keys = pygame.key.get_pressed()

   char.x_velo = 0
   #if left arrow is pressed, character moves left at charvel speed
   if keys[pygame.K_LEFT]:
    char.leftm(charvel)
  #if right arrow pressed, character moves right at charvel speed
   if keys[pygame.K_RIGHT]:
    char.rightm(charvel)

   vert_collision_manipulate(char, objects, char.y_velo)

#Base class to define all properties for a valid sprite
class Environment(pygame.sprite.Sprite):
   def __init__(self, x, y, width, height, name=None):
      super().__init__()
      self.rect = pygame.Rect(x, y, width, height)
      self.pic = pygame.Surface((width, height), pygame.SRCALPHA)
      self.width = width
      self.height = height
      self.name = name


   def draw(self,scr, xoffset):
      scr.blit(self.pic, (self.rect.x - xoffset, self.rect.y))     

#Slab class inherits from Environment creating blocks
class Slab(Environment):
   #constructor to initialise and create the blocks
   def __init__(self, x, y, size):
      super().__init__(x, y, size, size)
      slab = get_slab(size)
      self.pic.blit(slab, (0,0))
      self.mask = pygame.mask.from_surface(self.pic)
   


char = Char(200, 500, 50, 50)
background, bg_image = background_set("purple.png")  

slab_size = 96
slabs= [Slab(i * slab_size, HEIGHT - slab_size, slab_size) for i in range(-WIDTH // slab_size,( WIDTH * 2) // slab_size)]

xoffset = 0
scroll_width = 200

#main loop where pygame is running in
run = True
while run:
  screen.blit(hbackground, (0,0))
  timer.tick(fps)
#fills screen with colour and sets fos to 60
  if main_menu == True:
    menu_value = draw_menu()
    pygame.display.set_caption("Main Menu")
#returns main menu screen when true
    if menu_value != -1:
      main_menu = False
#returns home screen
  else:
    main_menu = draw_home()
    fps = 60
    if menu_value == 1:
        #text = font.render(f'Button{menu_value - 1}was clicked!', True, 'black')
        #screen.blit(text, (100, 200))
        draw_quiz()
    
    if menu_value == 2:
     #fps = 60
     char.loop(fps)      
     move_func(char, slabs)
     drawbg(screen, background, bg_image, char, slabs, xoffset)
    
    #checks if character is at oundary of screen
     if (char.rect.right - xoffset >= WIDTH - scroll_width and char.x_velo > 0) or (char.rect.left <= scroll_width and char.x_velo < 0):
        xoffset += char.x_velo
     


     for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          main_menu = True
          break
        elif event.key == pygame.K_SPACE or event.key == pygame.K_UP and char.jump_counter < 2:
          char.jump()


         

    if menu_value == 3:
        draw_shop()
    
    if menu_value == 4:

      c1 = Button('Question Filter', (170, 240)) 
      c1.draw()
      c2 = Button('Controls', (170, 300))
      c2.draw() 
      if c1.click_input() and buttonpress is False:
       buttonpress = True
       filter = True
      if filter == True:
        draw_filter()
      if c2.click_input() and buttonpress is False:
         controls = True
         buttonpress = True
      if controls == True:
         draw_controls()
    

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.flip()
pygame.quit()