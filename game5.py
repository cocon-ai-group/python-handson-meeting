import pygame

pygame.init()
scr = pygame.display.set_mode( (640, 480) )
clk = pygame.time.Clock()
x = 320
y = 240
vx = 5
vy = 3
wy1 = 240
wy2 = 240
while True:
	pygame.display.flip()
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			exit()
	key = pygame.key.get_pressed()
	if key[pygame.K_a]:
		wy1 = wy1 - 3
	elif key[pygame.K_z]:
		wy1 = wy1 + 3
	if key[pygame.K_UP]:
		wy2 = wy2 - 3
	elif key[pygame.K_DOWN]:
		wy2 = wy2 + 3
	if x + vx <= 20 and y - wy1 < 40 and y - wy1 > -40:
		vx = -vx
	if x + vx >= 620 and y - wy2 < 40 and y - wy2 > -40:
		vx = -vx
	if y + vy <= 0 or y + vy >= 480:
		vy = -vy
	if x + vx <= 0 or x + vx >= 640:
		x = 320
		y = 240
	x = x + vx
	y = y + vy
	scr.fill( (0,0,0) )
	pygame.draw.rect( scr, (0,255,0), (10,wy1-40,20,80) )
	pygame.draw.rect( scr, (0,0,255), (610,wy2-40,20,80) )
	pygame.draw.circle( scr, (255,0,0), (x,y), 30 )
	clk.tick(60)
	
