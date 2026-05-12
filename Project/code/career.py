import pygame

careers = [
    {
        "name": "Doctor",
        "x": 60, "y": 50,
        "color": (255,100,100),
        "scenario": {
            "question": "Patient has fever",
            "choices": {
                pygame.K_1: ("Treat properly", {"skill": 5, "happiness": -2}),
                pygame.K_2: ("Ignore", {"happiness": -5}),
            }
        }
    },
    {
        "name": "Developer",
        "x": 230, "y": 30,
        "color": (100, 255, 100),
        "scenario": {
            "question": "Code has bug",
            "choices": {
                pygame.K_1: ("Debug it", {"skill": 5}),
                pygame.K_2: ("Copy online", {"money": 3}),
            }
        }
    },
    {
        "name": "Designer",
        "x": 440, "y": 60,
        "color": (100,100,255),
        "scenario": {
            "question": "Client wants logo urgently",
            "choices": {
                pygame.K_1: ("Original design", {"skill": 4}),
                pygame.K_2: ("Use template", {"money": 3}),
            }
        }
    },
        {
        "name": "Chef",
    "x": 40,
    "y": 330,
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
    "x": 150,
    "y": 390,
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
    "x": 610,
    "y": 95,
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
    "x": 245,
    "y": 390,
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
    "x": 505,
    "y": 480,
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
    "x": 600,
    "y": 480,
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
    "x": 50,
    "y": 530,
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
    "x": 445,
    "y": 350,
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
    "x": 325,
    "y": 30,
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
