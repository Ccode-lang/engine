# importing required library
import pygame
import os
# activate the pygame library .
pygame.init()
X = 600
Y = 600

# create the display surface object
# of specific dimension..e(X, Y).
scrn = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('image')

clock = pygame.time.Clock()

def texturein(textures):
    counter = 0
    texlist = []
    for tex, tpos in textures:
        print(tex)
        print(tpos)
        texlist += [[pygame.image.load(tex).convert(), tpos]]
        counter += 1
    return texlist
def loadplayerframes(textures):
    texlist = []
    for tex in textures:
        texlist += [pygame.image.load(tex).convert()]
    return texlist

map = open("map.map", "r")
lines = map.readlines()
map.close()

texturenames = []
for line in lines:
    data = line.split(":")
    texturenames += [[data[0], (int(data[1]), int(data[2]))]]
print(texturenames)
#texturenames = [["red.png", (0, 0)], ["red.png", (30, 0)]]

textures = texturein(texturenames)


pos = (0, 0)
speed = 1
player = [0, (X/2 - 20, Y/2 - 20)]
playerrect = pygame.Rect(player[1][0], player[1][1], 20, 20)
playertex = ["red.png"]
playerframes = loadplayerframes(playertex)

#collision
#noup = [pygame.Rect(0, 20, 20, 1)]
#nodown = [pygame.Rect(0, 0, 20, 1)]
#noright = [pygame.Rect(0, 0, 1, 20)]
#noleft = [pygame.Rect(20, 0, 1, 20)]
noup = []
nodown = []
noright = []
noleft = []
map = open("noup.col", "r")
lines = map.readlines()
map.close()
for line in lines:
    data = line.split(":")
    noup += [pygame.Rect(int(data[0]), int(data[1]), int(data[2]), int(data[3]))]
map = open("nodown.col", "r")
lines = map.readlines()
map.close()
for line in lines:
    data = line.split(":")
    nodown += [pygame.Rect(int(data[0]), int(data[1]), int(data[2]), int(data[3]))]
map = open("noright.col", "r")
lines = map.readlines()
map.close()
for line in lines:
    data = line.split(":")
    noright += [pygame.Rect(int(data[0]), int(data[1]), int(data[2]), int(data[3]))]
map = open("noleft.col", "r")
lines = map.readlines()
map.close()
for line in lines:
    data = line.split(":")
    noleft += [pygame.Rect(int(data[0]), int(data[1]), int(data[2]), int(data[3]))]
running = True
while running:
# iterate over the list of Event objects
# that was returned by pygame.event.get() method.
    for event in pygame.event.get():
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            running = False
        keys=pygame.key.get_pressed()
    counter = 0

    up = True
    down = True
    right = True
    left = True

    for rect in noup:
        if pygame.Rect.colliderect(playerrect, rect):
            up = False
    for rect in nodown:
        if pygame.Rect.colliderect(playerrect, rect):
            down = False
    for rect in noright:
        if pygame.Rect.colliderect(playerrect, rect):
            right = False
    for rect in noleft:
        if pygame.Rect.colliderect(playerrect, rect):
            left = False
    if keys[pygame.K_w] and up:
        pos = (pos[0], pos[1] - speed)
        player[1] = (player[1][0], player[1][1] - speed)
    if keys[pygame.K_s] and down:
        pos = (pos[0], pos[1] + speed)
        player[1] = (player[1][0], player[1][1] + speed)
    if keys[pygame.K_a] and left:
        pos = (pos[0] - speed, pos[1])
        player[1] = (player[1][0] - speed, player[1][1])
    if keys[pygame.K_d] and right:
        pos = (pos[0] + speed, pos[1])
        player[1] = (player[1][0] + speed, player[1][1])
    # Using blit to copy content from one surface to other
    #scrn.blit(, (0 - pos[0], 0 - pos[1]))
    

    scrn.fill((0,0,0))

    playerrect = pygame.Rect(player[1][0], player[1][1], 20, 20)

    for tex in textures:
        #print((tex[1][0] - pos[0], tex[1][1] - pos[1]))
        scrn.blit(tex[0], (tex[1][0] - pos[0], tex[1][1] - pos[1]))
    
    scrn.blit(playerframes[player[0]], (player[1][0] - pos[0], player[1][1] - pos[1]))
    # paint screen one time
    pygame.display.flip()
    clock.tick(120)

# deactivates the pygame library
pygame.quit()
