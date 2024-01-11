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

        # game variables and images
        self.white_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook", 
                             "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
        self.white_positions = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
                                (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)]
        
        self.black_pieces = ["rook", "knight", "bishop", "king", "queen", "bishop", "knight", "rook", 
                             "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn", "pawn"]
        self.white_positions = [(0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7),
                                (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)]
        
        self.captured_pieces_white = []
        self.captured_pieces_black = []
        # 0 - whites turn, no selection: 1-whites turn, piece selected: 2- black turn no selected: 3- bkacj turn piece selected
        self.turn_step = 0
        self.selection = 100
        self.valid_moves = []

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