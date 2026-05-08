import pygame
import random
import sys

# ----------------------------
# SETTINGS
# ----------------------------
GRID_SIZE = 30
CELL_SIZE = 30

SCREEN_WIDTH = GRID_SIZE * CELL_SIZE
SCREEN_HEIGHT = 24 * CELL_SIZE

BUILDING_WIDTH = CELL_SIZE * 3
BUILDING_HEIGHT = CELL_SIZE * 2

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Career Path Simulation")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# COLORS
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# ----------------------------
# PLAYER
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
    {
        "name": "Chef",
    "x": 150,
    "y": 250,
    "color": (255, 140, 0),
    "scenario": {
        "question": "Customer says food is cold",
        "choices": {
            pygame.K_1: ("Cook again carefully", {"skill": 4, "happiness": -1}),
            pygame.K_2: ("Ignore complaint", {"money": 2, "happiness": -5}),
        },
    },
},

{
    "name": "Teacher",
    "x": 450,
    "y": 250,
    "color": (255, 255, 100),
    "scenario": {
        "question": "Student needs help after class",
        "choices": {
            pygame.K_1: ("Help student", {"skill": 3, "happiness": 3}),
            pygame.K_2: ("Leave early", {"happiness": -2}),
        },
    },
},

{
    "name": "Pilot",
    "x": 700,
    "y": 150,
    "color": (100, 200, 255),
    "scenario": {
        "question": "Bad weather during flight",
        "choices": {
            pygame.K_1: ("Land safely", {"skill": 5}),
            pygame.K_2: ("Rush landing", {"money": 3, "happiness": -4}),
        },
    },
},

{
    "name": "Lawyer",
    "x": 650,
    "y": 400,
    "color": (180, 100, 255),
    "scenario": {
        "question": "Client offers bribe",
        "choices": {
            pygame.K_1: ("Reject bribe", {"skill": 4, "happiness": 2}),
            pygame.K_2: ("Accept bribe", {"money": 8, "happiness": -6}),
        },
    },
},

{
    "name": "YouTuber",
    "x": 200,
    "y": 450,
    "color": (255, 50, 50),
    "scenario": {
        "question": "Video is getting attention",
        "choices": {
            pygame.K_1: ("Upload quality content", {"skill": 4, "money": 5}),
            pygame.K_2: ("Make clickbait", {"money": 8, "happiness": -3}),
        },
    },
},

{
    "name": "Game Dev",
    "x": 550,
    "y": 550,
    "color": (100, 255, 180),
    "scenario": {
        "question": "Game has many bugs before release",
        "choices": {
            pygame.K_1: ("Delay release and fix bugs", {"skill": 5}),
            pygame.K_2: ("Release unfinished game", {"money": 6, "happiness": -4}),
        },
    },
},

{
    "name": "Scientist",
    "x": 350,
    "y": 350,
    "color": (150, 255, 255),
    "scenario": {
        "question": "Experiment failed",
        "choices": {
            pygame.K_1: ("Try again carefully", {"skill": 5}),
            pygame.K_2: ("Fake results", {"money": 4, "happiness": -7}),
        },
    },
},

{
    "name": "Athlete",
    "x": 750,
    "y": 500,
    "color": (255, 255, 255),
    "scenario": {
        "question": "Big championship tomorrow",
        "choices": {
            pygame.K_1: ("Train hard", {"skill": 5, "happiness": -2}),
            pygame.K_2: ("Skip practice", {"happiness": 2, "skill": -3}),
        },
    },
},

{
    "name": "Photographer",
    "x": 100,
    "y": 550,
    "color": (200, 200, 200),
    "scenario": {
        "question": "Client wants edits quickly",
        "choices": {
            pygame.K_1: ("Edit professionally", {"skill": 4}),
            pygame.K_2: ("Rush edits", {"money": 4, "happiness": -2}),
        },
    },
},

{
    "name": "Entrepreneur",
    "x": 400,
    "y": 100,
    "color": (255, 215, 0),
    "scenario": {
        "question": "Business losing money",
        "choices": {
            pygame.K_1: ("Improve strategy", {"skill": 5}),
            pygame.K_2: ("Fire workers", {"money": 7, "happiness": -5}),
        }
    }
}

]

# ----------------------------
# EVENTS
# ----------------------------
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

def get_building_rect(career):
    return pygame.Rect(
        career["x"],
        career["y"],
        BUILDING_WIDTH,
        BUILDING_HEIGHT
    )

def draw_popup(career, stage):
    popup_width = 420
    popup_height = 200

    popup_rect = pygame.Rect(
        SCREEN_WIDTH // 2 - popup_width // 2,
        SCREEN_HEIGHT // 2 - popup_height // 2,
        popup_width,
        popup_height
    )

    pygame.draw.rect(screen, (30, 30, 40), popup_rect, border_radius=10)
    pygame.draw.rect(screen, WHITE, popup_rect, 2, border_radius=10)

    if stage == "ask":
        draw_text("Are you interested in this job?", popup_rect.x + 20, popup_rect.y + 50, YELLOW)
        draw_text("Press 1 = Yes", popup_rect.x + 20, popup_rect.y + 100)
        draw_text("Press 2 = No", popup_rect.x + 20, popup_rect.y + 130)

    elif stage == "scenario":
        draw_text(career["name"], popup_rect.x + 20, popup_rect.y + 15, YELLOW)
        draw_text(career["scenario"]["question"], popup_rect.x + 20, popup_rect.y + 60)

        draw_text("1: " + career["scenario"]["choices"][pygame.K_1][0],
                  popup_rect.x + 20, popup_rect.y + 110)

        draw_text("2: " + career["scenario"]["choices"][pygame.K_2][0],
                  popup_rect.x + 20, popup_rect.y + 140)

def get_rect(career):
    return pygame.Rect(
        career["x"],
        career["y"],
        BUILDING_WIDTH,
        BUILDING_HEIGHT
    )

# ----------------------------
# GAME
# ----------------------------
def game():
    player = Player()

    running = True
    current_career = None
    popup_active = False
    stage = None  # "ask" or "scenario"

    visited = set() 

    while running:
        dt = clock.tick(60) / 1000

        player_rect = pygame.Rect(player.pos.x - 10, player.pos.y - 10, 20, 20)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # KEY INPUT
            if event.type == pygame.KEYDOWN and popup_active:

                if stage == "ask":

                    if event.key == pygame.K_1:
                        stage = "scenario"

                    elif event.key == pygame.K_2:
                        popup_active = False
                        current_career = None
                        
                        

                elif stage == "scenario":

                    choices = current_career["scenario"]["choices"]

                    if event.key in choices:
                        _, effects = choices[event.key]
                        player.apply_effects(effects)
                        random_event(player)

                        popup_active = False
                        current_career = None

                         

            # CLOSE POPUP manually
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    popup_active = False
                    current_career = None

        # ----------------------------
        # MOVEMENT
        # ----------------------------
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

        # ----------------------------
        # COLLISION DETECTION
        # ----------------------------
        # ----------------------------
        # ----------------------------
        # COLLISION DETECTION
        # ----------------------------
        if not popup_active:

            for career in careers:

                rect = get_building_rect(career)

                if player_rect.colliderect(rect):

                    # ONLY TRIGGER IF NOT ALREADY VISITING
                    if career["name"] not in visited:

                        current_career = career
                        popup_active = True
                        stage = "ask"

                        visited.add(career["name"])
            
                           

        # bounds
        player.pos.x = max(10, min(SCREEN_WIDTH - 10, player.pos.x))
        player.pos.y = max(10, min(SCREEN_HEIGHT - 10, player.pos.y))

        # ----------------------------
        # DRAW
        # ----------------------------
        screen.fill((30, 30, 40))

        # grid
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
            pygame.draw.line(screen, (50, 50, 50), (0, y), (SCREEN_WIDTH, y))

        # careers
        for career in careers:
            rect = get_building_rect(career)

            pygame.draw.rect(screen, career["color"], rect, border_radius=6)
            pygame.draw.rect(screen, WHITE, rect, 2, border_radius=6)

            draw_text(career["name"], career["x"] + 5, career["y"] - 20)

        # player
        pygame.draw.circle(screen, YELLOW, player.pos, 10)

        # stats
        draw_text(f"Money: {player.money}", 10, 10)
        draw_text(f"Skill: {player.skill}", 10, 30)
        draw_text(f"Happiness: {player.happiness}", 10, 50)

        # popup
        if popup_active and current_career:
            draw_popup(current_career, stage)

        pygame.display.flip()

    pygame.quit()

# ----------------------------
# RUN
# ----------------------------
game()
