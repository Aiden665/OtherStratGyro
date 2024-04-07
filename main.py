import random, pygame, os, time, keyboard

# Initialize pygame
pygame.init()

# Set display properties
os.environ["SDL_VIDEO_CENTERED"] = "1"
info = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h

pygame.display.set_caption('stratagem hero')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT - 50), pygame.RESIZABLE)

# Load images

# lode arows
IMG_PATH_arow = "stratagem hero\\"

img_super_earth = pygame.image.load(os.path.join(IMG_PATH_arow, "cropped-super_earth2.png"))
img_super_earth = pygame.transform.scale(img_super_earth, (int(SCREEN_WIDTH / 3), int(SCREEN_HEIGHT / 2)))
img_arow_white = pygame.image.load(os.path.join(IMG_PATH_arow, "arow_white_resice.png"))
img_arow_white = pygame.transform.scale(img_arow_white, (100, 100))
img_arow_yellow = pygame.image.load(os.path.join(IMG_PATH_arow, "arow_yellow_resice.png"))
img_arow_yellow = pygame.transform.scale(img_arow_yellow, (100, 100))
img_arow_red = pygame.image.load(os.path.join(IMG_PATH_arow, "arow_red_resice.png"))
img_arow_red = pygame.transform.scale(img_arow_red, (100, 100))

"down" "up" "left" "right"

img_arow_white_up = pygame.transform.rotate(img_arow_white, 90)
img_arow_white_down = pygame.transform.rotate(img_arow_white, 270)
img_arow_white_left = pygame.transform.rotate(img_arow_white, 180)
img_arow_white_right = pygame.transform.rotate(img_arow_white, 0)

img_arow_yellow_up = pygame.transform.rotate(img_arow_yellow, 90)
img_arow_yellow_down = pygame.transform.rotate(img_arow_yellow, 270)
img_arow_yellow_left = pygame.transform.rotate(img_arow_yellow, 180)
img_arow_yellow_right = pygame.transform.rotate(img_arow_yellow, 0)

img_arow_red_up = pygame.transform.rotate(img_arow_red, 90)
img_arow_red_down = pygame.transform.rotate(img_arow_red, 270)
img_arow_red_left = pygame.transform.rotate(img_arow_red, 180)
img_arow_red_right = pygame.transform.rotate(img_arow_red, 0)


# lode stategums brige
IMG_PATH_brige = "Helldivers-2-Stratagems-icons-svg-master\Helldivers-2-Stratagems-icons-svg-master\Bridge"

HMG_Emplacement = pygame.image.load(os.path.join(IMG_PATH_brige, "HMG Emplacement.svg"))
Orbital_EMS_Strike = pygame.image.load(os.path.join(IMG_PATH_brige, "Orbital EMS Strike.svg"))
Orbital_Gas_Strike = pygame.image.load(os.path.join(IMG_PATH_brige, "Orbital Gas Strike.svg"))
Orbital_Precision_Strike = pygame.image.load(os.path.join(IMG_PATH_brige, "Orbital Precision Strike.svg"))
Orbital_Smoke_Strike = pygame.image.load(os.path.join(IMG_PATH_brige, "Orbital Smoke Strike.svg"))
Shield_Generator_Relay = pygame.image.load(os.path.join(IMG_PATH_brige, "Shield Generator Relay.svg"))
Tesla_Tower = pygame.image.load(os.path.join(IMG_PATH_brige, "Tesla Tower.svg"))


"down" "up" "left" "right"

Stratagems_list = [
 ["HMG Emplacement", ["down", "up", "left", "right", "right", "left"], HMG_Emplacement],
 ["Orbital EMS Strike", ["right", "right", "left", "down"], Orbital_EMS_Strike],
 ["Orbital Gas Strike", ["right", "right", "down", "right"], Orbital_Gas_Strike],
 ["Orbital Precision Strike", ["right", "right", "up"], Orbital_Precision_Strike],
 ["Orbital Smoke Strike", ["right", "right", "down", "up"], Orbital_Smoke_Strike],
 ["Shield Generator Relay", ["down", "down", "left", "right", "left", "right"], Shield_Generator_Relay],
 ["Tesla Tower", ["down", "up", "right", "up", "left", "right"], Tesla_Tower]]


def rnadom_numbers():
    while True:
        random_numbers = [random.randint(0, 6) for _ in range(difekulty)]
        print(random_numbers)
    # Check if there are any duplicates
        if len(random_numbers) != len(set(random_numbers)):
            pass
        else:
            break
    return random_numbers


def desplay_Stratagems(Stratagems_list,random_numbers,strategum_int):
    for i in range(len(random_numbers)-strategum_int):
        if i < 6:
            curent_Stratagem = Stratagems_list[random_numbers[i+strategum_int]][2]
            whithe_Stratagem = SCREEN_WIDTH // 20
            screen.blit(curent_Stratagem, ((((i+1)*2)+2) * whithe_Stratagem, SCREEN_HEIGHT // 3))
        else:
            break
def desplay_arows(Stratagems_list,random_numbers,strategum_int):
    whithe_arow = SCREEN_WIDTH // 20
    arow_list = Stratagems_list[random_numbers[strategum_int]][1]
    for J in range(len(arow_list)):
        arow = arow_list[J]
        if arow == "down":
            screen.blit(img_arow_white_down, ((((J + 1) * 2) + 2) * whithe_arow, SCREEN_HEIGHT // 2))
        elif arow == "right":
            screen.blit(img_arow_white_right, ((((J + 1) * 2) + 2) * whithe_arow, SCREEN_HEIGHT // 2))
        elif arow == "up":
            screen.blit(img_arow_white_up, ((((J + 1) * 2) + 2) * whithe_arow, SCREEN_HEIGHT // 2))
        elif arow == "left":
            screen.blit(img_arow_white_left, ((((J + 1) * 2) + 2) * whithe_arow, SCREEN_HEIGHT // 2))


def rong_buton(Stratagems_list,random_numbers,strategum_int):



    whithe_arow = SCREEN_WIDTH // 20
    arow_list = Stratagems_list[random_numbers[strategum_int]][1]
    for J in range(len(arow_list)):
        arow = arow_list[J]
        if arow == "down":
            screen.blit(img_arow_red_down, ((((J + 1) * 2) + 2) * whithe_arow, SCREEN_HEIGHT // 2))
        elif arow == "right":
            screen.blit(img_arow_red_right, ((((J + 1) * 2) + 2) * whithe_arow, SCREEN_HEIGHT // 2))
        elif arow == "up":
            screen.blit(img_arow_red_up, ((((J + 1) * 2) + 2) * whithe_arow, SCREEN_HEIGHT // 2))
        elif arow == "left":
            screen.blit(img_arow_red_left, ((((J + 1) * 2) + 2) * whithe_arow, SCREEN_HEIGHT // 2))
    pygame.display.update()
    time.sleep(0.1)
    desplay_arows(Stratagems_list, random_numbers, strategum_int)


def countdown_timer():
    global timer_value, start_time

    bar_height = SCREEN_HEIGHT // 20
    bar_border = 5
    bar_x = (SCREEN_WIDTH // 10)
    bar_y = SCREEN_HEIGHT - (SCREEN_HEIGHT // 3)
    bar_max_value = 15
    bar_width = SCREEN_WIDTH - (bar_x*2)


    if time.time() - start_time >= 1:
        print(timer_value)
        start_time = time.time()
        timer_value -= 1

    if timer_value > 0:
        bar_value = timer_value
    else:
        bar_value = 0

    # Draw loading bar background
    pygame.draw.rect(screen, (125, 125, 125),
                     (bar_x - bar_border, bar_y - bar_border, bar_width + bar_border * 2, bar_height + bar_border * 2))

    # Draw loading bar
    bar_fill_width = (bar_value / bar_max_value) * bar_width
    pygame.draw.rect(screen, (255, 255, 0), (bar_x, bar_y, bar_fill_width, bar_height))

    # Update the display
    pygame.display.flip()

    # Ensure timer doesn't go below 0

    pygame.time.Clock().tick(30)




# Set initial arrow image
curent_arow = img_arow_white

# Game loop
run = True
clock = pygame.time.Clock()
timer_value = 15
difekulty = 5
start_time = time.time()
random_numbers = rnadom_numbers()
screen.fill((0, 0, 0))
arow_int = 0
strategum_int = 0
screen.blit(img_super_earth, ((SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 3) / 2, (SCREEN_HEIGHT / 2) - (SCREEN_HEIGHT / 2) / 2))
desplay_Stratagems(Stratagems_list, random_numbers,strategum_int)
screen.blit(Tesla_Tower, (0, 0))
desplay_arows(Stratagems_list, random_numbers, strategum_int)
while run:
    num_temp = random_numbers[strategum_int]
    if arow_int < len(Stratagems_list[num_temp][1]):
        curent_arow = Stratagems_list[num_temp][1][arow_int]

    else:
        print("korekt")
        strategum_int += 1
        if timer_value < 14:
            timer_value += 1
        if not len(random_numbers) > strategum_int:
            print("your skore is 1000000")
            difekulty += 1
            start_time = time.time()
            random_numbers = rnadom_numbers()
            screen.fill((0, 0, 0))
            arow_int = 0
            strategum_int = 0
            timer_value = 15
            screen.blit(img_super_earth,
                        ((SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 3) / 2, (SCREEN_HEIGHT / 2) - (SCREEN_HEIGHT / 2) / 2))
            desplay_Stratagems(Stratagems_list, random_numbers, strategum_int)
            screen.blit(Tesla_Tower, (0, 0))
            desplay_arows(Stratagems_list, random_numbers, strategum_int)

        arow_int = 0
        screen.fill((0, 0, 0))
        screen.blit(img_super_earth,
                    ((SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 3) / 2, (SCREEN_HEIGHT / 2) - (SCREEN_HEIGHT / 2) / 2))
        desplay_Stratagems(Stratagems_list, random_numbers, strategum_int)
        desplay_arows(Stratagems_list, random_numbers, strategum_int)




    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if curent_arow == "up":
                    screen.blit(img_arow_yellow_up, ((((arow_int + 1) * 2) + 2) * (SCREEN_WIDTH / 20), SCREEN_HEIGHT // 2))
                    arow_int += 1
                    pygame.display.update()

                else:
                    arow_int = 0
                    rong_buton(Stratagems_list, random_numbers, strategum_int)
            if event.key == pygame.K_d:
                if curent_arow == "right":
                    screen.blit(img_arow_yellow_right, ((((arow_int + 1) * 2) + 2) * (SCREEN_WIDTH / 20), SCREEN_HEIGHT // 2))
                    arow_int += 1
                    pygame.display.update()

                else:
                    arow_int = 0
                    rong_buton(Stratagems_list, random_numbers, strategum_int)
            if event.key == pygame.K_s:
                if curent_arow == "down":
                    screen.blit(img_arow_yellow_down,
                                ((((arow_int + 1) * 2) + 2) * (SCREEN_WIDTH / 20), SCREEN_HEIGHT // 2))
                    arow_int += 1
                    pygame.display.update()

                else:
                    arow_int = 0
                    rong_buton(Stratagems_list, random_numbers, strategum_int)
            if event.key == pygame.K_a:
                if curent_arow == "left":
                    screen.blit(img_arow_yellow_left,
                                ((((arow_int + 1) * 2) + 2) * (SCREEN_WIDTH / 20), SCREEN_HEIGHT // 2))
                    arow_int += 1
                    pygame.display.update()

                else:
                    arow_int = 0
                    rong_buton(Stratagems_list, random_numbers, strategum_int)

    # Handle key presses


    # Update display
    countdown_timer()
    pygame.display.update()
# Quit pygame
pygame.quit()
