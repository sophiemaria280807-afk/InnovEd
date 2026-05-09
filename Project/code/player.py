import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, groups,collision_sprites):
        super().__init__(groups)

        # load image
        self.load_images()
        self.state, self.frame_index = 'Girl',0
        image = pygame.image.load(join("..", "images", "player", "Girl", "1.png")).convert_alpha()

        # resize image
        self.image = self.frames[self.state][0]

        # rectangle
        self.rect = self.image.get_rect(center=pos)
        self.hitbox_rect = self.rect.inflate(-30,0)

        #movement
        self.direction = pygame.Vector2()
        self.speed = 200
        self.collision_sprites = collision_sprites

    def load_images(self):
        self.frames = {'Girl': []}

        folder_path = join('..', 'images', 'player', 'Girl')

        for i in range(3):

            full_path = join(folder_path, f'{i}.png')

            surf = pygame.image.load(full_path).convert_alpha()

            surf = pygame.transform.scale(surf, (64, 64))

            self.frames['Girl'].append(surf)

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
    
    def move(self,dt):
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')
        self.rect.center = self.hitbox_rect.center

    def collision(self,direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if direction == 'horizontal':
                    if self.direction.x > 0:self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0:self.hitbox_rect.left = sprite.rect.right
                else:
                    if self.direction.y < 0:self.hitbox_rect.top = sprite.rect.bottom
                    if self.direction.y > 0:self.hitbox_rect.bottom = sprite.rect.top

    def animate(self, dt):
        # animate only while moving
        if self.direction.x != 0 or self.direction.y != 0:
            self.frame_index += 5 * dt
        else:
            self.frame_index = 0

        frames = self.frames[self.state]

        self.image = frames[int(self.frame_index) % len(frames)]
    def update(self,dt):
        self.input()
        self.move(dt)
        self.animate(dt)