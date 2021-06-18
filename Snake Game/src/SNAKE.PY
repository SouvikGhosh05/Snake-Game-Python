import pygame
import random
import sys

y=0

class Snake():
  def __init__(self):
    self.position=[105,45]
    self.body=[[105,45],[90,45],[75,45],[60,45],[45,45],[30,45]]
    self.direction="RIGHT"
    self.tick= 5

  def changeDirTo(self,dir):
        
    if dir=="RIGHT" and not self.direction=="LEFT":
      self.direction="RIGHT"

    if dir=="LEFT" and not self.direction=="RIGHT": 
      self.direction="LEFT"

    if dir=="UP" and not self.direction=="DOWN":
      self.direction="UP"

    if dir=="DOWN" and not self.direction=="UP":
      self.direction="DOWN"

  def play_background_music(self):
        
    pygame.mixer.music.load("Background.mp3")
    pygame.mixer.music.play(-1)

  def play_sound(self,sound_name):
    if sound_name == "crash":
        sound = pygame.mixer.Sound("crash.mp3")
        sound.play()
    elif sound_name == "ding":
        sound = pygame.mixer.Sound("ding.mp3")
        sound.play()
    
  def move(self,foodPos):

    if y == 0:    
      if self.direction=="RIGHT":
        self.position[0] += 15
  
      if self.direction=="LEFT":
        self.position[0] -= 15
  
      if self.direction=="UP":
        self.position[1] -= 15
  
      if self.direction=="DOWN":
        self.position[1] += 15

    self.body.insert(0,list(self.position))
  
    if self.position==foodPos:
      self.play_sound("ding")
      self.tick+=1
      return 1
    else: 
      self.body.pop()
      return 0

  def checkCollision(self):
        
    if self.position[0] > 960 or self.position[0] <0:
      return 1
    elif self.position[1] > 775 or self.position[1] <0:
      return 1
  
    for bodypart in self.body[1:]:
          
      if self.position == bodypart:  
        return 1
  
  def getBody(self):
    return self.body

class FoodSpawer():
      
  def __init__(self):
    self.position=[random.randrange(1,65)*15,random.randrange(1,52)*15]
    self.isFoodonScreen=True

  def setFoodonScreen(self,b):
    self.isFoodonScreen=b

  def spawnFood(self):

    if self.isFoodonScreen==False:
      self.position=[random.randrange(1,65)*15,random.randrange(1,52)*15]
      self.isFoodonScreen=True
    return self.position

window=pygame.display.set_mode((975,780))
pygame.display.set_caption("Snake Game Python")

icon= pygame.image.load("snake_05.png").convert()
pygame.display.set_icon(icon)

fps=pygame.time.Clock()
snake=Snake()
foodSpawner=FoodSpawer()
duration =  100
background_image = pygame.image.load("background.jpg").convert()
food_image=pygame.image.load("apple.jpg").convert()
pygame.mixer.init()

def show_game_over(x):
    pygame.font.init()
    font = pygame.font.Font("Roasting.otf", 60)
    line1 = font.render(f"Game is over! Your score is {x}.", True, (244, 56, 241))
    window.blit(line1, (220, 325))
    pygame.mixer.music.stop()
    pygame.display.update()

snake.play_background_music()
x=1

def game():
  
  score=0
  global x,y
  
  while True:
      
    for event in pygame.event.get():
        
      if event.type==pygame.QUIT:
        pygame.quit()
        sys.exit()
      
      elif event.type==pygame.KEYDOWN:  

        if event.key==pygame.K_RIGHT:
          snake.changeDirTo('RIGHT')
  
        if event.key==pygame.K_LEFT:
          snake.changeDirTo('LEFT')
  
        if event.key==pygame.K_UP:
          snake.changeDirTo('UP')
  
        if event.key==pygame.K_DOWN:
          snake.changeDirTo('DOWN')

    foodPos=foodSpawner.spawnFood()
    if(snake.move(foodPos)==1):
      score+=5
      foodSpawner.setFoodonScreen(False)

    window.fill((0, 0, 0))
    window.blit(background_image, [0, 0])
    for pos in snake.getBody():

      if y==0:    
      
        pygame.draw.rect(window,pygame.Color(246, 156, 60),pygame.Rect(pos[0],pos[1],15,15))
        window.blit(food_image,[foodPos[0],foodPos[1]])
    
    if(snake.checkCollision()==1):
    
      if x==1:
          snake.play_sound("crash")
          x=0
      show_game_over(score)
      y=1
    
    pygame.display.set_caption("Snake Game | Your Score: " + str(score))
    pygame.display.update()
    fps.tick(snake.tick)

if __name__== "__main__":
    game()

# Coded by Souvik 💖