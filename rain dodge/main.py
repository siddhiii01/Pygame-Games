import pygame
import time
import random

pygame.init()

WIDTH,HEIGHT=800,700
WIN = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("SPACE DODGE")

PLAYER_WIDTH=40
PLAYER_HEIGHT=60
PLAYER_VEC = 5

star_width=10
star_height=20
STAR_VEC=3

FONT=pygame.font.SysFont("comicsans",25)

BG=pygame.image.load('rain dodge/bg.jpeg').convert()

def draw(player,elapsed_time,stars):
  WIN.blit(BG,(0,0))
  pygame.draw.rect(WIN,"red",player)

  for star in stars:
    pygame.draw.rect(WIN,"white",star)

  time_text=FONT.render(f"Time is {round(elapsed_time)}s",1,"white")
  WIN.blit(time_text,(650,10))

  pygame.display.update()

def main():
  run=True
  start_time=time.time()
  elapsed_time=0

  star_add_increment=2000
  star_count=0

  stars =[]

  player = pygame.Rect(200,HEIGHT-PLAYER_HEIGHT,PLAYER_WIDTH,PLAYER_HEIGHT)

  clock=pygame.time.Clock()

  while run:
    star_count+=clock.tick(60)

    if star_count>star_add_increment:
      for _ in range(3):
        star_x = random.randint(0,WIDTH-10)
        star=pygame.Rect(star_x,-star_height,star_width,star_height)
        stars.append(star)

      star_add_increment = max(200,star_add_increment - 50)
      star_count=0

    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        run=False
        break
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x-PLAYER_VEC>=0:
      player.x-=PLAYER_VEC

    if keys[pygame.K_RIGHT] and player.x+PLAYER_VEC+player.width<=WIDTH:
      player.x+=PLAYER_VEC
        
    elapsed_time=time.time()-start_time 

    hit = False
    for star in stars[:]:
      star.y+=STAR_VEC
      if star.y>HEIGHT:
        stars.remove(star)
      elif star.y+star.height>=player.y and star.colliderect(player):
        stars.remove(star)
        hit = True
        break

    if hit:
      lost_text =  FONT.render("You Lost!",1,"yellow")
      WIN.blit(lost_text,(WIDTH/2-lost_text.get_width()/2,HEIGHT/2-lost_text.get_height()/2))
      pygame.display.update()
      pygame.time.delay(4000)
      break

    draw(player,elapsed_time,stars)
  pygame.quit()


if __name__=="__main__":
  main()