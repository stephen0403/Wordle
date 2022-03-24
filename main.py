## We end the game if:
## 1) The word is guessed 
## 2) All guesses are used
import pygame
import sys
import random
from words import *

pygame.init()

# Constants

WIDTH, HEIGHT = 633, 900

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("assets/Starting Tiles.png")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(317, 300))
ICON = pygame.image.load("assets/Icon.png")

pygame.display.set_caption("Wordle!")
pygame.display.set_icon(ICON)

GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

CORRECT_WORD = "coder"

ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

GUESSED_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 50)
AVAILABLE_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 25)

SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
pygame.display.update()

LETTER_X_SPACING = 85
LETTER_Y_SPACING = 12
LETTER_SIZE = 75
