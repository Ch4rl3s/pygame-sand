import pygame
import sys
import random
import time as tm

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
tiles = [pygame.Rect(0, 440, 600, 2),pygame.Rect(2, 0, 2, 480), pygame.Rect(597, 0, 2, 480)]
	
def collision_test(rect, tiles):
	collisions = []
	for tile in tiles:
		if rect.colliderect(tile):
			collisions.append(tile)
	return collisions


# def move(rect, movement, tiles, sand):
# 	rect.x += movement[0]
# 	collisions = collision_test(rect, tiles)
# 	for tile in collisions:
# 		if movement[0] > 0:
# 			rect.right = tile.left
# 		if movement[0] < 0:
# 			rect.left = tile.right

# 	rect.y += movement[1]
# 	collisions = collision_test(rect, tiles)
# 	for tile in collisions:
# 		if movement[1] > 0:
# 			rect.bottom = tile.top
# 		if movement[1] < 0:
# 			rect.top = tile.bottom
# 	collisions = collision_test(rect, sand)
# 	for tile in collisions:
# 		if rect.x!=tile.x and rect.y!=tile.y:
# 			if movement[1] > 0:
# 				rect.bottom = tile.top
# 			if movement[1] < 0:
# 				rect.top = tile.bottom
# 	return rect

def custom_sand_collision(sand):
	x = sand.x
	y = sand.y
	if screen.get_at((x,y+1))==white:
		sand.y = y+1
	elif screen.get_at((x-1,y+1))==white:
		sand.y = y+1
		sand.x -= 1
	elif screen.get_at((x+1,y+1))==white:
		sand.y+=1
		sand.x+=1
	elif screen.get_at((x,y+1))==black:
		pass
	return sand

def custom_water_collision(water, dir):
	x = water.x
	y = water.y
	if screen.get_at((x,y+1))==white:
		water.y = y+1
	elif screen.get_at((x-1,y+1))==white:
		water.x -= 1
		water.y +=1
	elif screen.get_at((x-1,y))==white and dir==1:
		water.x-=1
	elif screen.get_at((x+1,y))==white and dir==0:
		water.x+=1
	elif screen.get_at((x+1,y+1))==white:
		water.x+=1
		water.y+=1
	elif screen.get_at((x+1,y))==white and dir==1:
		water.x+=1
	elif screen.get_at((x-1,y))==white and dir==0:
		water.x-=1
	else:
		pass
	return water

def stone_rule_set(stone):
	x = stone.x
	y = stone.y
	if screen.get_at((x,y+1))==white:
		stone.y = y+1
	else:
		pass
	return stone


while True:

	screen.fill(white)

	movement = [0, 1]

	start = tm.time()

	for tile in tiles:
		pygame.draw.rect(screen, black, tile)

	for brick in brick_arr:
		pygame.draw.rect(screen, black, brick)

	for stone in stone_arr:
		stone = stone_rule_set(stone)
		pygame.draw.rect(screen, grey, stone)

	for sand in sand_arr:
		# sand = move(sand, movement, tiles, sand_arr)
		sand = custom_sand_collision(sand)
		pygame.draw.rect(screen, yellow, sand)

	rand_arr = [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]
	i=0

	for water in water_arr:
		if i==len(rand_arr):
			i=0
		water = custom_water_collision(water, rand_arr[i])
		i+=1
		pygame.draw.rect(screen, blue, water)

	end = tm.time()

	text = myfont.render(f"{round((end - start), 5)}", False, (0, 0, 0))
	text1 = myfont.render(f"entities {len(water_arr)+len(sand_arr)+len(stone_arr)+len(brick_arr)}", False, (0, 0, 0))
	screen.blit(text, (500,10))
	screen.blit(text1, (500,20))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
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
		x,y = pygame.mouse.get_pos()
		water_arr.append(pygame.Rect(x, y, 1, 1))
		water_arr.append(pygame.Rect(x+1, y, 1, 1))


	if mouse_down:
		x,y = pygame.mouse.get_pos()
		sand_arr.append(pygame.Rect(x, y, 1, 1))
		sand_arr.append(pygame.Rect(x, y+1, 1, 1))
		sand_arr.append(pygame.Rect(x+1, y, 1, 1))
		sand_arr.append(pygame.Rect(x+1, y+1, 1, 1))

	pygame.display.update()
	mainClock.tick(60)


