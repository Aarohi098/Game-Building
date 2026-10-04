import pygame
import random

pygame.init()

SPRITE_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 1

MAGENTA = pygame.Color('magenta')
PINK = pygame.Color('pink')
YELLOW = pygame.Color('yellow')
WHITE = pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, colour, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.speed = 5
        
    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
            
        boundary_hit = False
        
        if self.rect.left < 0:
            self.rect.left = 0
            boundary_hit = True
        elif self.rect.right > 500:
            self.rect.right = 500
            boundary_hit = True
            
        if self.rect.top < 0:
            self.rect.top = 0
            boundary_hit = True
        elif self.rect.bottom > 400:
            self.rect.bottom = 400
            boundary_hit = True
            
        if boundary_hit == True:
            pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))
        
    def change_colour(self):
        self.image.fill(random.choice([MAGENTA, PINK, YELLOW, WHITE]))
    
all_sprites_list = pygame.sprite.Group()

sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randint(10, 450)
sp1.rect.y = random.randint(10, 350)
all_sprites_list.add(sp1)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Controlled Boundary Sprite")

exit_game = False
clock = pygame.time.Clock()

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        elif event.type == SPRITE_COLOUR_CHANGE_EVENT:
            sp1.change_colour()
            
    all_sprites_list.update()
    
    screen.fill('blue')
    all_sprites_list.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


    