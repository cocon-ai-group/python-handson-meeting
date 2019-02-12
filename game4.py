import pygame

pygame.init()
scr = pygame.display.set_mode( (640, 480) )
clk = pygame.time.Clock()
x = 320
y = 240
vx = 5
vy = 3
while True:
	pygame.display.flip()
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			exit()
	key = pygame.key.get_pressed()
	if x + vx <= 0 or x + vx >= 640:
		vx = -vx
	if y + vy <= 0 or y + vy >= 480:
		vy = -vy
	x = x + vx
	y = y + vy
	scr.fill( (0,0,0) )
	pygame.draw.circle( scr, (255,0,0), (x,y), 30 )
	clk.tick(60)
	
