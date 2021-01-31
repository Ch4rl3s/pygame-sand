import pygame
import sys

mainClock = pygame.time.Clock()

screen_size = (600, 480)

black = (0, 0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0, 255)
blue = (0,0,255,255)

pygame.init()

pygame.display.set_caption('sand testing')
screen = pygame.display.set_mode(screen_size)
screen.fill(white)

mouse_down = False
draw_water = False

sand = pygame.Rect(300, 240, 1, 1)

sand_arr = [sand]
water_arr = []
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

def custom_water_collision(water):
	x = water.x
	y = water.y
	if screen.get_at((x,y+1))==white:
		water.y = y+1
	elif screen.get_at((x-1,y+1))==white:
		water.y = y+1
		water.x -= 1
	elif screen.get_at((x+1,y+1))==white:
		water.y+=1
		water.x+=1
	elif screen.get_at((x+1,y))==white:
		water.x+=1
	elif screen.get_at((x-1,y))==white:
		water.x-=1
	else:
		pass
	return water

while True:

	screen.fill(white)

	movement = [0, 1]

	for tile in tiles:
		pygame.draw.rect(screen, black, tile)

	for sand in sand_arr:
		# sand = move(sand, movement, tiles, sand_arr)
		sand = custom_sand_collision(sand)
		pygame.draw.rect(screen, yellow, sand)

	for water in water_arr:
		water = custom_water_collision(water)
		pygame.draw.rect(screen, blue, water)




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

	if draw_water:
		x,y = pygame.mouse.get_pos()
		water_arr.append(pygame.Rect(x, y, 1, 1))


	if mouse_down:
		x,y = pygame.mouse.get_pos()
		sand_arr.append(pygame.Rect(x, y, 1, 1))
		sand_arr.append(pygame.Rect(x, y+1, 1, 1))
		sand_arr.append(pygame.Rect(x+1, y, 1, 1))
		sand_arr.append(pygame.Rect(x+1, y+1, 1, 1))

	pygame.display.update()
	mainClock.tick(60)

