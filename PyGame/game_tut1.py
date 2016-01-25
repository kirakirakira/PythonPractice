import pygame

pygame.init()

screen_width = 400
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
done = False
is_blue = True
x = 30 # x coord of top left corner of rectangle
y = 30 # y coord of top left corner of rectangle

rect_width = 25
rect_height = 40

clock = pygame.time.Clock()

while not done:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			is_blue = not is_blue

	pressed = pygame.key.get_pressed()

	if pressed[pygame.K_UP] and y > 3:
		y -= 3
	if pressed[pygame.K_DOWN] and y < (screen_height - rect_height - 3):
		y += 3
	if pressed[pygame.K_LEFT] and x > 3:
		x -= 3
	if pressed[pygame.K_RIGHT] and x < (screen_width - rect_width - 3):
		x += 3

	screen.fill((0, 0, 0))

	if is_blue:
		color = (0, 128, 255)
	else: 
		color = (255, 100, 0)

	pygame.draw.rect(screen, color, pygame.Rect(x, y, rect_width, rect_height))

	pygame.display.flip()

	clock.tick(60)