import pygame

pygame.init()
scr = pygame.display.set_mode( (640, 480) )
clk = pygame.time.Clock()
x = 320
y = 240
while True:
	pygame.display.flip()
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			exit()
	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT]:
		x = x - 10
	elif key[pygame.K_RIGHT]:
		x = x + 10
	if key[pygame.K_UP]:
		y = y - 10
	elif key[pygame.K_DOWN]:
		y = y + 10
	scr.fill( (0,0,0) )
	pygame.draw.circle( scr, (255,0,0), (x,y), 30 )
	clk.tick(60)
	
