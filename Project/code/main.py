import pygame
from settings import *
from player import Player
from sprites import *
from pytmx.util_pygame import load_pygame

class Game:
    def __init__(self):
        #setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Pathnova')
        self.clock = pygame.time.Clock()
        self.running = True

        #bg image
        self.background = pygame.image.load(join('..','data','maps','map.png')).convert()
        self.background = pygame.transform.scale(self.background,(WINDOW_WIDTH,WINDOW_HEIGHT))

        #groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.setup()

        #sprites
        self.player = Player((400,300),self.all_sprites,self.collision_sprites)
        
    def setup(self):

    # load map
        game_map = load_pygame(join('..', 'data', 'maps', 'world2.tmx'))

        # original map size
        map_width = game_map.width * game_map.tilewidth
        map_height = game_map.height * game_map.tileheight

        # scale ratios
        scale_x = WINDOW_WIDTH / map_width
        scale_y = WINDOW_HEIGHT / map_height
        

        # loop through objects
        for obj in game_map.get_layer_by_name('Object1'):

            # scale object image
            scaled_image = pygame.transform.scale(
                obj.image,
                (
                    int(obj.image.get_width() * scale_x),
                    int(obj.image.get_height() * scale_y)
                )
            )

            # scale object position
            CollisionSprite(
                (
                    obj.x * scale_x,
                    obj.y * scale_y
                ),
                scaled_image,
                self.all_sprites,
                self.collision_sprites
            )

        for obj in game_map.get_layer_by_name('Object2'):

                scaled_image = pygame.transform.scale(
                    obj.image,
                    (
                        int(obj.image.get_width() * scale_x),
                        int(obj.image.get_height() * scale_y)
                    )
                )

                CollisionSprite(
                    (
                        obj.x * scale_x,
                        obj.y * scale_y
                    ),
                    scaled_image,
                    self.all_sprites,
                    self.collision_sprites
                )

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            #update
            self.all_sprites.update(dt) 

            #draw
            # draw
            self.display_surface.blit(self.background, (0,0))
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()