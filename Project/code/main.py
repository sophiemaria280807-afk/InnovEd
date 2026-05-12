import pygame
import sys
from settings import *
from player import Player
from sprites import *
from buttons import Button
from pytmx.util_pygame import load_pygame
from os.path import join
from career import careers


class Game:
    def __init__(self):
        #setup
        pygame.init()
        
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Pathnova')
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'menu'
        self.font_path = join('..','data','font.ttf')
        

        #bg image
        self.background = pygame.image.load(join('..','data','maps','map.png')).convert()
        self.background = pygame.transform.scale(self.background,(WINDOW_WIDTH,WINDOW_HEIGHT))

        #menu background
        self.menu_bg = pygame.image.load(join('..','images','Example.jpg')).convert()
        self.menu_bg = pygame.transform.scale(self.menu_bg,(WINDOW_WIDTH,WINDOW_HEIGHT))
        self.button_image = pygame.image.load(join('..','images','button.png')).convert_alpha()
        self.button_image = pygame.transform.scale(self.button_image,(250, 80))
        self.stand_image = pygame.image.load(join('..', 'data', 'graphics', 'object22.png')).convert_alpha()
        self.stand_image = pygame.transform.scale(self.stand_image,(90, 60))

        #groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.setup()
        self.create_career_collisions()

        #sprites
        self.player = Player((700,300),self.all_sprites,self.collision_sprites)
        # career popup system
        self.popup_active = False
        self.current_career = None
        self.result_popup = False
        self.result_text = ""
        self.result_start_time = 0
    
    def get_font(self,size): 
        return pygame.font.Font(self.font_path,size)
    
    def show_result_popup(self):

        if self.result_popup:

            current_time = pygame.time.get_ticks()

            # show for 5 seconds
            if current_time - self.result_start_time < 5000:

                popup_rect = pygame.Rect(180, 470, 440, 90)

                pygame.draw.rect(
                    self.display_surface,
                    (20,20,20),
                    popup_rect
                )

                pygame.draw.rect(
                    self.display_surface,
                    "white",
                    popup_rect,
                    3
                )

                result_surface = self.get_font(20).render(
                    self.result_text,
                    True,
                    "white"
                )

                result_rect = result_surface.get_rect(center=popup_rect.center)

                self.display_surface.blit(
                    result_surface,
                    result_rect
                )

            else:
                self.result_popup = False
        
    def controls(self):
        mouse_pos = pygame.mouse.get_pos()
        self.display_surface.fill("white")

        lines = [
            "Use the arrow keys to move around",
            "and left click on the stands",
            "to interact with them"
        ]

        y = 180

        for line in lines:

            controls_text = self.get_font(25).render(line, True, "Black")
            controls_rect = controls_text.get_rect(center=(400, y))

            self.display_surface.blit(controls_text, controls_rect)

            y += 50

        back_button = Button(
            image=self.button_image,
            pos=(400, 550),
            text_input="BACK",
            font=self.get_font(30),
            base_colour="Black",
            hovering_colour="#8b8b8b"
        )

        back_button.changeColor(mouse_pos)
        back_button.update(self.display_surface)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if back_button.checkForInput(mouse_pos):
                    self.state = 'menu'

        pygame.display.update()

    def career(self):
        # DRAW CAREER STANDS
        for career in careers:

            self.display_surface.blit(
                self.stand_image,
                (career['x'], career['y'])
            )

            text = self.get_font(11).render(
                career["name"],
                True,
                "black"
            )

            self.display_surface.blit(
                text,
                (career["x"], career["y"] - 20)
            )

        # ----------------------------
        # DETECT PLAYER NEAR STAND
        # ----------------------------
        if not self.popup_active:

            player_rect = self.player.hitbox_rect

            for career in careers:

                stand_rect = pygame.Rect(
                    career["x"],
                    career["y"],
                    90,
                    60
                )

                # larger interaction zone
                interaction_rect = stand_rect.inflate(20, 20)

                if interaction_rect.colliderect(player_rect):

                    self.popup_active = True
                    self.current_career = career
                    break

        # ----------------------------
        # POPUP
        # ----------------------------
        if self.popup_active and self.current_career:
            stand_rect = pygame.Rect(
                self.current_career["x"],
                self.current_career["y"],
                90,
                60
            )

            interaction_rect = stand_rect.inflate(80, 80)

            if not interaction_rect.colliderect(self.player.hitbox_rect):

                self.popup_active = False
                self.current_career = None
                return

            popup_rect = pygame.Rect(120, 100, 560, 320)

            pygame.draw.rect(
                self.display_surface,
                (30,30,30),
                popup_rect
            )

            pygame.draw.rect(
                self.display_surface,
                "white",
                popup_rect,
                3
            )

            # TITLE
            title = self.get_font(32).render(
                self.current_career["name"],
                True,
                "white"
            )

            title_rect = title.get_rect(center=(400, 140))
            self.display_surface.blit(title, title_rect)

            # QUESTION
            question = self.current_career["scenario"]["question"]

            question_text = self.get_font(20).render(
                question,
                True,
                "white"
            )

            self.display_surface.blit(question_text, (150, 190))

            mouse_pos = pygame.mouse.get_pos()

            # CHOICES
            choice1 = self.current_career["scenario"]["choices"][pygame.K_1][0]
            choice2 = self.current_career["scenario"]["choices"][pygame.K_2][0]

            choice1_button = Button(
                image=self.button_image,
                pos=(400, 260),
                text_input=choice1,
                font=self.get_font(10),
                base_colour="black",
                hovering_colour="#8b8b8b"
            )

            choice2_button = Button(
                image=self.button_image,
                pos=(400, 340),
                text_input=choice2,
            
                font=self.get_font(10),
                base_colour="black",
                hovering_colour="#8b8b8b"
            )

            # DRAW BUTTONS
            for button in [choice1_button, choice2_button]:

                button.changeColor(mouse_pos)
                button.update(self.display_surface)

            # BUTTON CLICKS
            if pygame.mouse.get_pressed()[0]:

                if choice1_button.checkForInput(mouse_pos):

                    effects = self.current_career["scenario"]["choices"][pygame.K_1][1]

                    result_list = []

                    for stat, value in effects.items():

                        result_list.append(f"{stat} {'+' if value > 0 else ''}{value}")

                    self.result_text = "   ".join(result_list)
            
                    self.result_popup = True
                    self.result_start_time = pygame.time.get_ticks()

                    self.popup_active = False
                    self.current_career = None
                elif choice2_button.checkForInput(mouse_pos):

                    effects = self.current_career["scenario"]["choices"][pygame.K_2][1]

                    result_list = []

                    for stat, value in effects.items():

                        result_list.append(f"{stat} {'+' if value > 0 else ''}{value}")

                    self.result_text = "   ".join(result_list)

                    self.result_popup = True
                    self.result_start_time = pygame.time.get_ticks()

                    self.popup_active = False
                    self.current_career = None
    def menu(self):
        mouse_pos = pygame.mouse.get_pos()
        self.display_surface.blit(self.menu_bg, (0, 0))
        title = self.get_font(80).render("PATHNOVA",True,"White")
        title_rect = title.get_rect(center=(400,100))
        self.display_surface.blit(title,title_rect)
        
        play_button = Button(image=self.button_image, pos=(400, 250), text_input="PLAY", font=self.get_font(30), base_colour="black", hovering_colour="#8b8b8b")
        controls_button = Button(image=self.button_image, pos=(400, 400), text_input="CONTROLS", font=self.get_font(30), base_colour="black", hovering_colour="#8b8b8b")
        quit_button = Button(image=self.button_image, pos=(400, 550), text_input="QUIT", font=self.get_font(30), base_colour="black", hovering_colour="#8b8b8b")

        for button in [play_button,controls_button,quit_button]:
            button.changeColor(mouse_pos)
            button.update(self.display_surface)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                   if play_button.checkForInput(mouse_pos):
                       self.state = 'game'
                   if controls_button.checkForInput(mouse_pos):
                       self.state = 'controls'
                   if quit_button.checkForInput(mouse_pos):
                       self.running = False

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

    def create_career_collisions(self):

        for career in careers:

            collision_surface = pygame.Surface((90, 60), pygame.SRCALPHA)

            CollisionSprite(
                (career['x'], career['y']),
                collision_surface,
                [],
                self.collision_sprites
        )

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000

            if self.state == 'menu':
                self.menu()
            elif self.state == 'controls':
                self.controls()
            elif self.state == 'game':
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.popup_active = False
                #update
                self.all_sprites.update(dt) 

                # draw
                self.display_surface.blit(self.background, (0,0))
                self.all_sprites.draw(self.display_surface)
                self.career()
                self.show_result_popup()
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    
    game = Game()
    game.run()