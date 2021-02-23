black = (0, 0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0, 255)
blue = (0,0,255,255)
grey = (10,10,10,255)



def custom_sand_collision(sand, screen):
	x = sand.x
	y = sand.y
	vel = 4
	if screen.get_at((x,y+1))==white:
		for i in range(vel):
			if screen.get_at((x,y+i))==white:
				sand.y = y+i
	elif screen.get_at((x-1,y+1))==white:
		sand.y = y+1
		sand.x -= 1
	elif screen.get_at((x+1,y+1))==white:
		sand.y+=1
		sand.x+=1
	elif screen.get_at((x,y+1))==black:
		pass
	return sand


def custom_water_collision(water, dir, screen):
    x = water.x
    y = water.y
    hor_spread = 3
    if screen.get_at((x, y-1)) == blue:
        return water
    elif screen.get_at((x, y+1)) == white:
        water.y = y+1
    elif screen.get_at((x-1,y+1))==white:
        water.x -= 1
        water.y +=1
    elif screen.get_at((x+1,y+1))==white:
        water.x+=1
        water.y+=1
    else:
        for i in range(1, hor_spread):
            if dir==1:
                if screen.get_at((x-i,y))==white:
                    water.x-=1
                elif screen.get_at((x+i,y))==white:
                    water.x+=1
            else:
                if screen.get_at((x+i,y))==white:
                    water.x+=1
                elif screen.get_at((x-i,y))==white:
                    water.x-=1
    return water

def stone_rule_set(stone, screen):
	x = stone.x
	y = stone.y
	vel = 4
	if screen.get_at((x,y+1))==white:
		for i in range(vel):
			if screen.get_at((x,y+i))==white:
				stone.y = y+i
	else:
		pass
	return stone
