import pygame
import math
from random_words import RandomWords

pygame.init()
frame_width = 1100
frame_height = 700
frame = pygame.display.set_mode((frame_width, frame_height))
icon = pygame.image.load('32x32switch.png')
pygame.display.set_caption("Hangman")
pygame.display.set_icon(icon)

person_img = []
for i in range(11):
    person_img.append(pygame.image.load(str(i) + ".jpg"))
person_step = [0]

button_rad = 21
empty_fill = 40
alphabet = []
start_x = button_rad + empty_fill
a_mY = 500
m_zY = 600
letter = 65
font = pygame.font.SysFont("Helvetica", 15)

for i in range(26):
    if i == 0:
        alphabet.append([start_x, a_mY, chr(letter), False])
    elif i < 13:
        start_x = start_x + button_rad * 2 + empty_fill
        letter = letter + 1
        alphabet.append([start_x, a_mY, chr(letter), False])
    elif i == 13:
        start_x = button_rad + empty_fill
        letter = letter + 1
        alphabet.append([start_x, m_zY, chr(letter), False])
    else:
        start_x = start_x + button_rad * 2 + empty_fill
        letter = letter + 1
        alphabet.append([start_x, m_zY, chr(letter), False])

fps = 60
timer = pygame.time.Clock()
cont = True


def generate_word():
    letter_list = []
    rec_start = 250
    while True:
        rw = RandomWords()
        word = rw.random_word().upper()
        if 5 < len(word) < 10:
            for i in range(len(word)):
                rec_start = rec_start + 75
                letter_list.append([word[i], False, rec_start])
            return letter_list


game_word = generate_word()
font_lines = pygame.font.SysFont("Helvetica", 25)
print(game_word)


def distance(x1, x2, y1, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + (math.pow(y2 - y1, 2)))


def draw():
    frame.blit(pygame.image.load("back_img.jpg"), (0, 0))
    for button in alphabet:
        x, y, let, pressed = button
        pygame.draw.circle(frame, (204, 242, 244), (x, y), button_rad, 100)
        render = font.render(let, 1, (18, 110, 130))
        frame.blit(render, (x - render.get_width() / 2, y - render.get_height() / 2))
        if pressed:
            exists = False
            for game_word_letter in game_word:
                game_letter, picked, x_loc = game_word_letter
                if let == game_letter:
                    render = font_lines.render(let, 1, (18, 110, 130))
                    frame.blit(render, (x_loc + 15, 260))
                    game_word_letter[1] = True
                    exists = True
            if not exists:
                button[3] = False
                print(person_step[0])
                person_step[0] = person_step[0] + 1

    for game_word_letter in game_word:
        game_letter, picked, x_loc = game_word_letter
        pygame.draw.rect(frame, (0, 0, 0), (x_loc, 300, 50, 10))

    frame.blit(person_img[person_step[0]], (100, 50))
    pygame.display.update()


def button_press(loc_x, loc_y):
    pygame.draw.circle(frame, (0, 0, 0), (loc_x, loc_y), button_rad, 5)
    pygame.display.update()

def exit_game():
    if person_step[0] > 9:
        return True

    all_picked = True
    for game_word_letter in game_word:
        game_letter, picked, x_loc = game_word_letter
        if not picked:
            all_picked = False

    return all_picked


while cont:
    if exit_game():
        break

    timer.tick(fps)
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cont = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            in_x, in_y = pygame.mouse.get_pos()
            for button in alphabet:
                x, y, let, pressed = button
                if distance(in_x, x, in_y, y) < button_rad:
                    button_press(x, y)
                    button[3] = True


pygame.quit()
