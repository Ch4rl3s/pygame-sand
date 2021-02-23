import pygame
import sys
import random
import time as tm
import phys as ph

mainClock = pygame.time.Clock()

screen_size = (600, 480)

black = (0, 0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0, 255)
blue = (0,0,255,255)
grey = (10,10,10,255)


pygame.init()

myfont = pygame.font.SysFont('timesnewroman',  12)

pygame.display.set_caption('sand testing')
screen = pygame.display.set_mode(screen_size)
screen.fill(white)

data = [[],[]]

mouse_down = False
draw_water = False
draw_stone = False
draw_brick = False
erase = False

# sand = pygame.Rect(300, 240, 1, 1)

sand_arr = []
water_arr = []
stone_arr=[]
brick_arr = []
tiles = [pygame.Rect(0, 440, 600, 2),pygame.Rect(6, 0, 2, 480), pygame.Rect(594, 0, 2, 480)]



while True:

	screen.fill(white)

	movement = [0, 1]


	for tile in tiles:
		pygame.draw.rect(screen, black, tile)

	for brick in brick_arr:
		pygame.draw.rect(screen, black, brick)

	for stone in stone_arr:
		stone = ph.stone_rule_set(stone, screen)
		pygame.draw.rect(screen, grey, stone)

	for sand in sand_arr:
		# sand = move(sand, movement, tiles, sand_arr)
		sand = ph.custom_sand_collision(sand, screen)
		pygame.draw.rect(screen, yellow, sand)


	rand_arr = [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]
	i=0
	start = tm.time()

	for water in water_arr:
		if i==len(rand_arr):
			i=0
		water = ph.custom_water_collision(water, rand_arr[i], screen)
		i+=1
		pygame.draw.rect(screen, blue, water)

	end = tm.time()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			f = open('text.txt')
			print(data)
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_down = True
			print("mouse down")
		if event.type == pygame.MOUSEBUTTONUP:
			mouse_down = False
			print("mouse up")
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				print(water_arr)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				draw_water = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				draw_water = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				draw_stone = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_s:
				draw_stone = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_b:
				draw_brick = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_b:
				draw_brick = False

	if draw_stone:
		x,y = pygame.mouse.get_pos()
		stone_arr.append(pygame.Rect(x, y, 1, 1))
		stone_arr.append(pygame.Rect(x-1, y+1, 1, 1))
		stone_arr.append(pygame.Rect(x+1, y, 1, 1))
		stone_arr.append(pygame.Rect(x-1, y, 1, 1))
		stone_arr.append(pygame.Rect(x, y+1, 1, 1))
		stone_arr.append(pygame.Rect(x, y-1, 1, 1))
		stone_arr.append(pygame.Rect(x+1, y-1, 1, 1))
		stone_arr.append(pygame.Rect(x+1, y+1, 1, 1))
		stone_arr.append(pygame.Rect(x-1, y-1, 1, 1))


	if draw_brick:
		x,y = pygame.mouse.get_pos()
		brick_arr.append(pygame.Rect(x, y, 10, 10))

	if draw_water:
		h_water = 20
		v_water = 20
		x,y = pygame.mouse.get_pos()
		for i in range(h_water):
			for j in range(v_water):
				if screen.get_at((x+i,y+j))==white:
					water_arr.append(pygame.Rect(x+i, y+j, 1, 1))


	if mouse_down:
		x,y = pygame.mouse.get_pos()
		sand_arr.append(pygame.Rect(x, y, 1, 1))
		sand_arr.append(pygame.Rect(x, y+1, 1, 1))
		sand_arr.append(pygame.Rect(x+1, y, 1, 1))
		sand_arr.append(pygame.Rect(x+1, y+1, 1, 1))



	data[1].append(round((end - start), 5))
	data[0].append(len(water_arr)+len(sand_arr)+len(stone_arr)+len(brick_arr))
	text = myfont.render(f"{round((end - start), 5)}", False, (0, 0, 0))
	text1 = myfont.render(f"entities {len(water_arr)+len(sand_arr)+len(stone_arr)+len(brick_arr)}", False, (0, 0, 0))
	screen.blit(text, (500,10))
	screen.blit(text1, (500,20))

	pygame.display.update()
	mainClock.tick(60)
