import pygame
import random
import sys

# ----------------------------
# SETTINGS
# ----------------------------
GRID_SIZE = 20
CELL_SIZE = 30
SCREEN_WIDTH = GRID_SIZE * CELL_SIZE
SCREEN_HEIGHT = GRID_SIZE * CELL_SIZE

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Career Path Simulation")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)

# ----------------------------
# PLAYER CLASS
# ----------------------------
class Player:
    def __init__(self):
        self.money = 0
        self.skill = 0
        self.happiness = 50
        self.pos = pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def apply_effects(self, effects):
        for stat, value in effects.items():
            setattr(self, stat, getattr(self, stat) + value)

# ----------------------------
# CAREERS
# ----------------------------
careers = [
    {
        "name": "Doctor",
        "x": 100,
        "y": 100,
        "color": (255, 100, 100),
        "scenario": {
            "question": "Patient has fever",
            "choices": {
                pygame.K_1: ("Treat properly", {"skill": 5, "happiness": -2}),
                pygame.K_2: ("Ignore", {"happiness": -5}),
            },
        },
    },
    {
        "name": "Developer",
        "x": 500,
        "y": 100,
        "color": (100, 255, 100),
        "scenario": {
            "question": "Code has bug",
            "choices": {
                pygame.K_1: ("Debug it", {"skill": 5}),
                pygame.K_2: ("Copy online", {"money": 3, "skill": -2}),
            },
        },
    },
    {
        "name": "Designer",
        "x": 300,
        "y": 500,
        "color": (100, 100, 255),
        "scenario": {
            "question": "Client wants logo urgently",
            "choices": {
                pygame.K_1: ("Original design", {"skill": 4}),
                pygame.K_2: ("Use template", {"money": 3}),
            },
        },
    },
]

events = [
    ("Promoted! +5 Money", {"money": 5}),
    ("Stressful day -5 Happiness", {"happiness": -5}),
    ("Learned new skill +5 Skill", {"skill": 5}),
]

# ----------------------------
# FUNCTIONS
# ----------------------------
def draw_text(text, x, y, color=WHITE):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def random_event(player):
    event = random.choice(events)
    player.apply_effects(event[1])
    return event[0]

def draw_popup(career):
    popup_width = 400
    popup_height = 200

    popup_rect = pygame.Rect(
        SCREEN_WIDTH//2 - popup_width//2,
        SCREEN_HEIGHT//2 - popup_height//2,
        popup_width,
        popup_height
    )

    pygame.draw.rect(screen, (20,20,30), popup_rect, border_radius=10)
    pygame.draw.rect(screen, WHITE, popup_rect, 2, border_radius=10)

    draw_text(career["name"], popup_rect.x + 20, popup_rect.y + 15, YELLOW)
    draw_text(career["scenario"]["question"], popup_rect.x + 20, popup_rect.y + 60)

    draw_text("1: " + career["scenario"]["choices"][pygame.K_1][0],
              popup_rect.x + 20, popup_rect.y + 110)

    draw_text("2: " + career["scenario"]["choices"][pygame.K_2][0],
              popup_rect.x + 20, popup_rect.y + 140)

# ----------------------------
# START MENU
# ----------------------------
def start_menu():
    start_btn = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 40, 200, 50)
    option_btn = pygame.Rect(SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 + 30, 200, 50)

    while True:
        screen.fill((20,20,30))

        draw_text("CAREER SIMULATOR", SCREEN_WIDTH//2 - 110, SCREEN_HEIGHT//2 - 120, YELLOW)

        mx, my = pygame.mouse.get_pos()

        hover_start = start_btn.collidepoint((mx,my))
        hover_option = option_btn.collidepoint((mx,my))

        pygame.draw.rect(screen, (50,50,50), start_btn)
        pygame.draw.rect(screen, GREEN if hover_start else WHITE, start_btn, 2)
        draw_text("START", start_btn.x + 70, start_btn.y + 15)

        pygame.draw.rect(screen, (50,50,50), option_btn)
        pygame.draw.rect(screen, GREEN if hover_option else WHITE, option_btn, 2)
        draw_text("OPTIONS", option_btn.x + 55, option_btn.y + 15)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if hover_start:
                    return
                if hover_option:
                    print("Options not implemented")

# ----------------------------
# MAIN GAME
# ----------------------------
def game():
    player = Player()
    running = True

    current_career = None
    popup_active = False

    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # CLICK interaction
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos

                if not popup_active:
                    for career in careers:
                        rect = pygame.Rect(career["x"]-20, career["y"]-20, 40, 40)

                        if rect.collidepoint((mx, my)):
                            current_career = career
                            popup_active = True

            # scenario choices
            if event.type == pygame.KEYDOWN and popup_active:
                choices = current_career["scenario"]["choices"]

                if event.key in choices:
                    text, effects = choices[event.key]
                    player.apply_effects(effects)
                    random_event(player)

                    popup_active = False
                    current_career = None

        # movement disabled if popup open
        if not popup_active:
            keys = pygame.key.get_pressed()
            speed = 220

            if keys[pygame.K_w]:
                player.pos.y -= speed * dt
            if keys[pygame.K_s]:
                player.pos.y += speed * dt
            if keys[pygame.K_a]:
                player.pos.x -= speed * dt
            if keys[pygame.K_d]:
                player.pos.x += speed * dt

        # keep inside screen
        player.pos.x = max(10, min(SCREEN_WIDTH - 10, player.pos.x))
        player.pos.y = max(10, min(SCREEN_HEIGHT - 10, player.pos.y))

        # DRAW
        screen.fill((30,30,40))

        # grid
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(screen, (50,50,50), (x,0), (x,SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(screen, (50,50,50), (0,y), (SCREEN_WIDTH,y))

        # careers
        for career in careers:
            pygame.draw.rect(screen, career["color"], (career["x"]-20, career["y"]-20, 40, 40))
            draw_text(career["name"], career["x"]-30, career["y"]-35)

        # player
        pygame.draw.circle(screen, YELLOW, player.pos, 10)

        # stats
        draw_text(f"Money: {player.money}", 10, 10)
        draw_text(f"Skill: {player.skill}", 10, 30)
        draw_text(f"Happiness: {player.happiness}", 10, 50)

        # popup
        if popup_active and current_career:
            draw_popup(current_career)

        pygame.display.flip()

    pygame.quit()

# ----------------------------
# RUN
# ----------------------------
start_menu()
game()