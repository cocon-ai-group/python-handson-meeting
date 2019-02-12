import pygame

pygame.init()
scr = pygame.display.set_mode( (640, 480) )
clk = pygame.time.Clock()
pygame.draw.line( scr, (255,0,0), (32,32), (240,240) )
while True:
	pygame.display.flip()
	for e in pygame.event.get():
		pass
	clk.tick(60)
	
