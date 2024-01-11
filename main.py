import pygame

class Game:
    def __init__(self):    
        pygame.init()
        SCREEN_SIZE = (1000, 900)
        self.FPS = 60
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("chess")
        self.font = pygame.font.Font("freesansbold.ttf", 20)
        self.big_font = pygame.font.Font("freesansbold.ttf", 50)
        self.clock = pygame.time.Clock()

        self.run = True
    
    def start(self):
        while self.run:
            self.clock.tick(self.FPS)
            self.screen.fill("dark gray")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.flip()

        quit()

Game().start()