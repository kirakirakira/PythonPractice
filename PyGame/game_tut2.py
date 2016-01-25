import pygame
import os

_image_library = {}

def get_image(path):
	global _image_library
	image = _image_library.get(path)
	if image == None:
		canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
		image = pygame.image.load(canonicalized_path)
		_image_library[path] = image
	return image

pygame.init()

screen_width = 600
screen_height = 450

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

done = False

font = pygame.font.SysFont("comicsansms", 36)

text = font.render("Welcome to Tux's Game to the Death", True, (0, 128, 0))

x = 20
y = 20

rect_width = 143
rect_height = 170

pygame.mixer.music.load('ping.wav')
pygame.mixer.music.play(-1)

def check_position(x,y):
	if x >= 200 and y >= 200:
		screen.blit(get_image('windows.png'), (200, 200))

while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill((255, 255, 255)) 

	screen.blit(text,
        (screen_width/2 - text.get_width() // 2, screen_height/2 - text.get_height() // 2))

	check_position(x,y)

	pressed = pygame.key.get_pressed()

	if pressed[pygame.K_UP] and y > 3:
		y -= 3
	if pressed[pygame.K_DOWN] and y < (screen_height - rect_height - 3):
		y += 3
	if pressed[pygame.K_LEFT] and x > 3:
		x -= 3
	if pressed[pygame.K_RIGHT] and x < (screen_width - rect_width - 3):
		x += 3

	screen.blit(get_image('tux.png'), (x, y))

	pygame.display.flip()

	clock.tick(60)