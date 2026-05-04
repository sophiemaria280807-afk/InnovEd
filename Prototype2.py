import pygame
import random

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
        "description": "Helps patients, high skill, stressful.",
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
        "description": "Builds software.",
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
        "description": "Creates visuals.",
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
def draw_text(text, x, y, color=(255,255,255)):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def random_event(player):
    event = random.choice(events)
    player.apply_effects(event[1])
    return event[0]

def near_stand(player, stand):
    distance = ((player.pos.x - stand["x"])**2 + (player.pos.y - stand["y"])**2)**0.5
    return distance < 50

# ----------------------------
# MAIN GAME
# ----------------------------
player = Player()
running = True
message = "Move with WASD. Stand near a career and press E."

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # interact
            if event.key == pygame.K_e:
                for career in careers:
                    if near_stand(player, career):
                        message = career["name"] + ": " + career["scenario"]["question"]
                        current_career = career

            # scenario choices
            if 'current_career' in locals():
                choices = current_career["scenario"]["choices"]

                if event.key in choices:
                    text, effects = choices[event.key]
                    player.apply_effects(effects)
                    result = random_event(player)
                    message = text + " | " + result
                    del current_career

    # movement
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

    # ---------------- DRAW ----------------
    screen.fill((30, 30, 40))

    # grid
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, (50,50,50), (x,0), (x,SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, (50,50,50), (0,y), (SCREEN_WIDTH,y))

    # stands
    for career in careers:
        pygame.draw.rect(screen, career["color"], (career["x"]-20, career["y"]-20, 40, 40))
        draw_text(career["name"], career["x"]-30, career["y"]-35)

    # player dot
    pygame.draw.circle(screen, (255, 255, 0), player.pos, 10)

    # stats
    draw_text(f"Money: {player.money}", 10, 10)
    draw_text(f"Skill: {player.skill}", 10, 30)
    draw_text(f"Happiness: {player.happiness}", 10, 50)

    # message
    draw_text(message, 10, SCREEN_HEIGHT - 30)

    # choice help
    if 'current_career' in locals():
        draw_text("Press 1 or 2", 10, SCREEN_HEIGHT - 55)

    pygame.display.flip()

pygame.quit()