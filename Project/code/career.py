import pygame

careers = [
    {
        "name": "Doctor",
        "x": 60, "y": 50,
        "color": (255,100,100),
       "scenarios": [

{
    "question": "A patient is panicking before surgery.",
    "skill_tested": "communication",

    "choices": {
        pygame.K_1: (
            "Calm the patient and explain the procedure",
            {"problem_solving": 5, "communication": 2}
        ),

        pygame.K_2: (
            "Tell the patient to stop overreacting",
            {"communication": -5}
        ),
    }
},

{
    "question": "Two emergency patients arrive at once.",
    "skill_tested": "problem_solving",

    "choices": {
        pygame.K_1: (
            "Prioritise based on severity",
            {"problem_solving": 5}
        ),

        pygame.K_2: (
            "Panic and treat randomly",
            {"problem_solving": -4}
        ),
    }
},

{
    "question": "You are exhausted after a long shift.",
    "skill_tested": "discipline",

    "choices": {
        pygame.K_1: (
            "Double-check prescriptions carefully",
            {"discipline": 5}
        ),

        pygame.K_2: (
            "Rush paperwork to leave early",
            {"discipline": -4}
        ),
    }
}
]
    },
    {
        "name": "Developer",
        "x": 230, "y": 30,
        "color": (100, 255, 100),
        "scenarios": [

{
    "question": "The app crashes before presentation day.",
    "skill_tested": "creativity",

    "choices": {
        pygame.K_1: (
            "Debug the code carefully",
            {"knowledge": 5, "problem_solving": 3}
        ),

        pygame.K_2: (
            "Pretend the issue doesn't exist",
            {"problem_solving": -5}
        ),
    }
},

{
    "question": "A teammate asks for coding help.",
    "skill_tested": "creativity",

    "choices": {
        pygame.K_1: (
            "Help explain the solution",
            {"creativity": 4, "communication": 2}
        ),

        pygame.K_2: (
            "Ignore them and focus only on yourself",
            {"creativity": -4}
        ),
    }
},

{
    "question": "A feature is taking longer than expected.",
    "skill_tested": "problem_solving",

    "choices": {
        pygame.K_1: (
            "Break the task into smaller steps",
            {"problem_solving": 5}
        ),

        pygame.K_2: (
            "Copy random code online",
            {"creativity": -3}
        ),
    }
}
]
    },
    {
    "name": "Designer",
    "x": 440, "y": 60,
    "color": (100,100,255),

    "scenarios": [

{
    "question": "A client rejects your first logo proposal.",
    "skill_tested": "creativity",

    "choices": {
        pygame.K_1: (
            "Develop a more original concept",
            {"creativity": 5, "communication": 2}
        ),

        pygame.K_2: (
            "Reuse an old design template",
            {"creativity": -4}
        ),
    }
},

{
    "question": "Your team needs a presentation design urgently.",
    "skill_tested": "discipline",

    "choices": {
        pygame.K_1: (
            "Organise tasks and finish professionally",
            {"discipline": 4, "communication": 2}
        ),

        pygame.K_2: (
            "Rush the work carelessly",
            {"discipline": -4}
        ),
    }
},

{
    "question": "A client gives harsh feedback on your project.",
    "skill_tested": "communication",

    "choices": {
        pygame.K_1: (
            "Accept feedback professionally",
            {"communication": 5}
        ),

        pygame.K_2: (
            "Argue emotionally with the client",
            {"communication": -5}
        ),
    }
}
]
},

        {
    "name": "Chef",
    "x": 40,
    "y": 330,
    "color": (255, 140, 0),

    "scenarios": [

{
    "question": "The kitchen becomes overcrowded during dinner rush.",
    "skill_tested": "discipline",

    "choices": {
        pygame.K_1: (
            "Stay organised and manage orders efficiently",
            {"discipline": 5, "problem_solving": 2}
        ),

        pygame.K_2: (
            "Rush meals without coordination",
            {"discipline": -4}
        ),
    }
},

{
    "question": "A customer reports a food safety issue.",
    "skill_tested": "knowledge",

    "choices": {
        pygame.K_1: (
            "Inspect hygiene procedures immediately",
            {"knowledge": 5}
        ),

        pygame.K_2: (
            "Ignore the complaint",
            {"discipline": -5}
        ),
    }
},

{
    "question": "Ingredients arrive late before an important event.",
    "skill_tested": "problem_solving",

    "choices": {
        pygame.K_1: (
            "Adapt the menu creatively",
            {"problem_solving": 5, "creativity": 2}
        ),

        pygame.K_2: (
            "Cancel dishes without warning",
            {"communication": -4}
        ),
    }
}
]
},

{
    "name": "Teacher",
    "x": 150,
    "y": 390,
    "color": (255, 255, 100),
    "scenarios": [

{
    "question": "A student does not understand the lesson.",
    "skill_tested": "communication",

    "choices": {
        pygame.K_1: (
            "Explain the topic differently",
            {"communication": 5, "knowledge": 2}
        ),

        pygame.K_2: (
            "Tell them to figure it out alone",
            {"communication": -4}
        ),
    }
},

{
    "question": "Students become noisy during class.",
    "skill_tested": "knowledge",

    "choices": {
        pygame.K_1: (
            "Regain control calmly",
            {"knowledge": 5}
        ),

        pygame.K_2: (
            "Yell angrily at everyone",
            {"discipline": -3, "communication": -2}
        ),
    }
},

{
    "question": "A student seems upset after class.",
    "skill_tested": "communication",

    "choices": {
        pygame.K_1: (
            "Ask if they need support",
            {"communication": 5}
        ),

        pygame.K_2: (
            "Ignore the situation",
            {"communication": -4}
        ),
    }
}
]
},

{
    "name": "Pilot",
    "x": 610,
    "y": 95,
    "color": (100, 200, 255),

    "scenarios": [

{
    "question": "A storm appears during your flight path.",
    "skill_tested": "problem_solving",

    "choices": {
        pygame.K_1: (
            "Reroute the aircraft safely",
            {"problem_solving": 5, "discipline": 2}
        ),

        pygame.K_2: (
            "Continue through dangerous turbulence",
            {"discipline": -5}
        ),
    }
},

{
    "question": "Passengers panic during turbulence.",
    "skill_tested": "communication",

    "choices": {
        pygame.K_1: (
            "Reassure passengers calmly",
            {"communication": 5}
        ),

        pygame.K_2: (
            "Ignore the cabin situation",
            {"communication": -4}
        ),
    }
},

{
    "question": "A technical warning appears before takeoff.",
    "skill_tested": "discipline",

    "choices": {
        pygame.K_1: (
            "Delay takeoff for safety checks",
            {"discipline": 5, "knowledge": 2}
        ),

        pygame.K_2: (
            "Proceed without inspection",
            {"discipline": -6}
        ),
    }
}
]
},

{
    "name": "Lawyer",
    "x": 245,
    "y": 390,
    "color": (180, 100, 255),

    "scenarios": [

{
    "question": "A client offers money to hide evidence.",
    "skill_tested": "discipline",

    "choices": {
        pygame.K_1: (
            "Reject the offer professionally",
            {"discipline": 5}
        ),

        pygame.K_2: (
            "Accept the unethical proposal",
            {"discipline": -6}
        ),
    }
},

{
    "question": "You must prepare for a difficult court case.",
    "skill_tested": "knowledge",

    "choices": {
        pygame.K_1: (
            "Research the case thoroughly",
            {"knowledge": 5, "problem_solving": 2}
        ),

        pygame.K_2: (
            "Improvise without preparation",
            {"knowledge": -5}
        ),
    }
},

{
    "question": "A client becomes aggressive during consultation.",
    "skill_tested": "communication",

    "choices": {
        pygame.K_1: (
            "Remain calm and professional",
            {"communication": 5}
        ),

        pygame.K_2: (
            "Respond emotionally",
            {"communication": -4}
        ),
    }
}
]
},

{
    "name": "YouTuber",
    "x": 505,
    "y": 480,
    "color": (255, 50, 50),
    "scenarios": [

{
    "question": "Your latest video suddenly goes viral.",
    "choices": {
        pygame.K_1: ("Focus on quality uploads", {"creativity": 4, "discipline": 5}),
        pygame.K_2: ("Use misleading clickbait", {"discipline": -8, "communication": -3}),
    }
},

{
    "question": "Viewers criticise your content heavily.",
    "choices": {
        pygame.K_1: ("Improve based on feedback", {"creativity": 4}),
        pygame.K_2: ("Start online drama", {"communication": -3, "problem_solving": -5}),
    }
},

{
    "question": "A sponsor offers money for dishonest promotion.",
    "choices": {
        pygame.K_1: ("Reject misleading sponsorship", {"communication": 3}),
        pygame.K_2: ("Accept for profit", {"knowledge": -7, "discipline": -4}),
    }
}
]
},

{
    "name": "Journalist",
    "x": 600,
    "y": 480,
    "color": (100, 255, 180),
    "scenarios": [

{
    "question": "You must interview a nervous witness.",
    "skill_tested": "communication",

    "choices": {
        pygame.K_1: (
            "Speak calmly and build trust",
            {"communication": 5, "discipline": 2}
        ),

        pygame.K_2: (
            "Interrupt constantly for quick answers",
            {"communication": -4}
        ),
    }
},

{
    "question": "Breaking news happens close to deadline.",
    "skill_tested": "knowledge",

    "choices": {
        pygame.K_1: (
            "Organise information quickly",
            {"knowledge": 5}
        ),

        pygame.K_2: (
            "Rush and publish unverified facts",
            {"knowledge": -3, "discipline": -2}
        ),
    }
},

{
    "question": "You must ask difficult questions during a live interview.",
    "skill_tested": "communication",

    "choices": {
        pygame.K_1: (
            "Ask professionally and confidently",
            {"communication": 5}
        ),

        pygame.K_2: (
            "Avoid important questions",
            {"communication": -4}
        ),
    }
}
]
},

{
    "name": "Scientist",
    "x": 350,
    "y": 350,
    "color": (150, 255, 255),

    "scenarios": [

{
    "question": "Your experiment fails after months of research.",
    "skill_tested": "problem_solving",

    "choices": {
        pygame.K_1: (
            "Analyse the failure and retry",
            {"problem_solving": 5, "discipline": 2}
        ),

        pygame.K_2: (
            "Fake successful results",
            {"discipline": -6}
        ),
    }
},

{
    "question": "Laboratory equipment breaks during testing.",
    "skill_tested": "knowledge",

    "choices": {
        pygame.K_1: (
            "Repair the setup safely",
            {"knowledge": 4}
        ),

        pygame.K_2: (
            "Ignore safety procedures",
            {"discipline": -5}
        ),
    }
},

{
    "question": "Another team publishes similar research first.",
    "skill_tested": "creativity",

    "choices": {
        pygame.K_1: (
            "Improve your research further",
            {"creativity": 5}
        ),

        pygame.K_2: (
            "Copy their findings dishonestly",
            {"discipline": -5}
        ),
    }
}
]
},

{
    "name": "Athlete",
    "x": 50,
    "y": 530,
    "color": (255, 255, 255),
    "scenarios": [

{
    "question": "A championship match is tomorrow morning.",
    "choices": {
        pygame.K_1: ("Train seriously", {"discipline": 5, "creativity": -2}),
        pygame.K_2: ("Skip practice for fun", {"knowledge": -2, "discipline": -3}),
    }
},

{
    "question": "You suffer a minor injury before competition.",
    "choices": {
        pygame.K_1: ("Recover properly", {"problem_solving": 3, "knowledge": 2}),
        pygame.K_2: ("Play while injured", {"problem_solving": -3, "knowledge": -5}),
    }
},

{
    "question": "A coach pressures you to use unfair advantages.",
    "choices": {
        pygame.K_1: ("Compete honestly", {"discipline": 4, "communication": 3}),
        pygame.K_2: ("Cheat to win", {"knowledge":-6, "discipline": -6}),
    }
}
]
},

{
    "name": "Photographer",
    "x": 445,
    "y": 350,
    "color": (200, 200, 200),

    "scenarios": [

{
    "question": "A client requests urgent photo edits.",
    "skill_tested": "creativity",

    "choices": {
        pygame.K_1: (
            "Edit the photos professionally",
            {"creativity": 5, "discipline": 2}
        ),

        pygame.K_2: (
            "Rush the edits carelessly",
            {"discipline": -4}
        ),
    }
},

{
    "question": "Lighting conditions suddenly change during a shoot.",
    "skill_tested": "problem_solving",

    "choices": {
        pygame.K_1: (
            "Adjust camera settings quickly",
            {"problem_solving": 5}
        ),

        pygame.K_2: (
            "Continue without adapting",
            {"knowledge": -3}
        ),
    }
},

{
    "question": "A customer dislikes your editing style.",
    "skill_tested": "communication",

    "choices": {
        pygame.K_1: (
            "Discuss improvements professionally",
            {"communication": 5}
        ),

        pygame.K_2: (
            "Argue with the customer",
            {"communication": -4}
        ),
    }
}
]
},

{
    "name": "Entrepreneur",
    "x": 325,
    "y": 30,
    "color": (255, 215, 0),
    "scenarios": [

{
    "question": "Your business sales suddenly drop.",
    "skill_tested": "decision_making",

    "choices": {
        pygame.K_1: (
            "Analyse the problem carefully",
            {"problem_solving": 5}
        ),

        pygame.K_2: (
            "Blame employees immediately",
            {"problem_solving": -4}
        ),
    }
},

{
    "question": "Employees suggest a new product idea.",
    "skill_tested": "communication",

    "choices": {
        pygame.K_1: (
            "Listen and discuss ideas together",
            {"creativity": 5, "communication": 2}
        ),

        pygame.K_2: (
            "Reject every suggestion instantly",
            {"communication": -4}
        ),
    }
},

{
    "question": "A competitor launches a better product.",
    "skill_tested": "creativity",

    "choices": {
        pygame.K_1: (
            "Innovate and improve your product",
            {"creativity": 5}
        ),

        pygame.K_2: (
            "Copy the competitor exactly",
            {"creativity": -3}
        ),
    }
}
]
}
]