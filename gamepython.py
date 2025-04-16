"""import pygame
# Ініціалізуємо Pygame
pygame.init()
# Зберігаємо у змінних розміри вікна (ширина, висота)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
# Зберігаємо у змінній основний колір фону (RGB)
background_color = (135, 206, 250) # Небесно-блакитний
# Створюємо вікно
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# Встановлюємо назву вікна
pygame.display.set_caption("Моя перша гра")
# Заповнюємо фон кольором
screen.fill(background_color)
# Оновлюємо дисплей
pygame.display.flip()
# Затримка перед виходом
pygame.time.delay(5000)"""


"""import pygame
import random
# Ініціалізація бібліотеки pygame
pygame.init()
# Створюємо ігрове вікно
screen = pygame.display.set_mode((500, 400)) # Ширина 400, висота 300
pygame.display.set_caption("Мій перший ігровий цикл")
# Основний колір фону
background_color = (173, 216, 230) # Світло-блакитний
# Ігровий цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Перевірка на натискання закриття вікна
            running = False
        if event.type == pygame.KEYDOWN: # Перевірка на натискання клавіші
            if event.key == pygame.K_RETURN: # Якщо натиснута клавіша Enter
                random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                screen.fill(random_color)
# Оновлюємо екран
        pygame.display.flip()
# Завершуємо роботу pygame
pygame.quit()"""


"""#1
import pygame

position = pygame.math.Vector2(100, 150)
print(f"X: {position.x}, Y: {position.y}")

#2
import pygame
# Ініціалізація pygame
pygame.init()
# Встановлення розміру вікна
screen = pygame.display.set_mode((800, 600))
# Створення об'єкта: прямокутник
rect_position = pygame.math.Vector2(200, 300) # Початкова позиція
# Основний цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Очищуємо екран
        screen.fill((255, 255, 255))
# Малюємо прямокутник
        pygame.draw.rect(screen, (0, 0, 255), (rect_position.x, rect_position.y, 50, 50))
# Оновлення екрана
        pygame.display.flip()
pygame.quit()


import pygame
# Ініціалізація pygame
pygame.init()
# Встановлення розміру вікна
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Рух об'єкта за допомогою Enter")
rect_position = pygame.math.Vector2(200, 300) # Початкова позиція
object_size = 50
object_color = (255,0,0)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                rect_position.x +=50
                rect_position.y +=20
    screen.fill((255,255,255))
    pygame.draw.rect(screen, object_color, (rect_position.x, rect_position.y, object_size, object_size))
    pygame.display.flip()
pygame.quit()"""



"""import pygame
# Ініціалізація pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
t = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.time.get_ticks() - t > 2000:
            print("Час іде...")
            t = pygame.time.get_ticks()"""




"""import pygame
import random
# Ініціалізація бібліотеки pygame
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim trainer")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
x,y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
RADIUS = 30
font = pygame.font.SysFont("Arial", 30)
start_time = pygame.time.get_ticks()
last_move_time = 0
MOVE_INTERVAL = 1000
score = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x - x)**2 + (mouse_y - y)**2)**0.5
            if distance <= RADIUS:
                score+=1
                print("Є влучення!")
    corrent_time = pygame.time.get_ticks()
    if corrent_time - last_move_time >- MOVE_INTERVAL:
        x,y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
        last_move_time = corrent_time
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), RADIUS)
    score_text = font.render(f"Влучань: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    elapset_time = (corrent_time - start_time)//1000
    time_text = font.render(f"Час: {elapset_time} c", True, (0, 0, 0))
    screen.blit(time_text,(10,40))
    pygame.draw.rect(screen, (0, 255, 0), (0,0,500,500),10)
    pygame.display.flip()
pygame.quit()"""



"""import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Хтось натиснув стрілочку вгору!")
            elif event.key == pygame.K_DOWN:
                print("Хтось натиснув стрілочку вниз!")
            elif event.key == pygame.K_s:
                print("s")
            elif event.key == pygame.K_w:
                print("w")
            elif event.key == pygame.K_a:
                print("a")
            elif event.key == pygame.K_SPACE:
                print("Space")
            elif event.key == pygame.K_LSHIFT:
                print("LEFT SHIFT")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                print("Хтось відпустив стрілочку вгору!")

pygame.quit()"""







"""import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            message = "Клавіша ліворуч натиснута"
            print(message)
        elif keys[pygame.K_RIGHT]:
            message = "Клавіша праворуч натиснута"
            print(message)
        elif keys[pygame.K_UP]:
            message = "Клавіша вгору натиснута"
            print(message)
        elif keys[pygame.K_DOWN]:
            message = "Клавіша вниз натиснута"
            print(message)
        
pygame.quit()"""



"""import pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
# Кольори
YELLOW = (253, 253, 150)
GREEN = (5, 244, 120)
# Початкові координати квадратика
x, y = 300, 200
width, height = 50, 50
speed = 5 # Швидкість руху квадратика
# Основний цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
# Отримання стану клавіш
    keys = pygame.key.get_pressed()
# Рух квадратика
    if keys[pygame.K_LEFT] or keys[pygame.K_a]: # Ліворуч
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: # праворуч
        x += speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]: # вниз
        y += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]: # вгору
        y -= speed
# ...
# Очищення екрану
    screen.fill(YELLOW)
# Малюємо квадратик
    pygame.draw.rect(screen, GREEN, (x, y, width, height))
# Оновлення екрану
    pygame.display.update()
# Кадри на секунду
    clock.tick(60)"""


"""import pygame
import random 
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
# Кольори
GREY = (125, 125, 125)
GREEN = (0, 163, 108)  
# Завантаження зображення кота та фону
cat_img = pygame.image.load("dog.png") # Завантажуєpngзображення кота
cat_img = pygame.transform.smoothscale(cat_img, (50, 50)) # Використовуємо smoothscale для кращої якості
cat = cat_img.get_rect() # Отримуємо розміри зображення кота
cat.topleft = (100, 100) # Встановлюємо початкову позицію кота
# Завантаження фону
background_img = pygame.image.load("background.jpg") # Завантажуємо фонове зображення
background_img = pygame.transform.scale(background_img, (800, 600)) # Масштабуємо його під розмір екрану
# Параметри швидкості, вони знадобляться пізніше
speed = 0 # Початкова вертикальна швидкість (кіт стоїть на місці)
gravity = 0.5 # Значення нашої сили тяжіння
jump_speed = -8 # Швидкість стрибка (зверни увагу, що вона від'ємна, бо напрямлена вгору)

obstacle_timer = 0 # Таймер для контролю інтервалу часу між перешкодами
obstacles = [] # Список перешкод
obstacle_width = 50 # Ширина перешкоди
gap_height = 150 # Відстань між верхньою та нижньою перешкодами
min_distance = 250
score = 0
font = pygame.font.Font(None, 36)
# Основний цикл
while True:
    screen.blit(background_img, (0, 0)) # Малюємо фонове зображення на екрані
    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            speed = jump_speed # Встановлюємо швидкість стрибка
# Ефект гравітації (швидкість поступово збільшується)
    speed += gravity
# Поступово збільшуємо швидкість, додаючи гравітацію
    cat.y += speed
    if cat.y > 500:
        cat.y = 550
        speed = 0
    if cat.y < -70:
        cat.y = 550
        speed = 0
    obstacle_timer += 1
    if obstacle_timer > min_distance:
        top_obstacle_height = random.randint(100, 400) # Випадкова висота верхньої перешкоди
        bottom_obstacle_height = screen.get_height() - top_obstacle_height - gap_height # Рахуємо висоту нижньої перешкоди  
        top_obstacle = pygame.Rect(800, 0, obstacle_width, top_obstacle_height)
        bottom_obstacle = pygame.Rect(800, screen.get_height() - bottom_obstacle_height, obstacle_width, bottom_obstacle_height)
        obstacles.append((top_obstacle, bottom_obstacle))
        obstacle_timer = 0
# Далі переміщаємо перешкоди та перевіряємо на зіткнення:
    for top_obstacle, bottom_obstacle in obstacles:
        top_obstacle.x -= 5 # Переміщаємо перешкоду трохи вліво
        bottom_obstacle.x -= 5 # Переміщаємо нижню перешкоду трохи вліво
# Перевірка на зіткнення з перешкодою
        if cat.colliderect(top_obstacle) or cat.colliderect(bottom_obstacle):
            print("Game Over!")
            pygame.quit()
            exit()
        if top_obstacle.x < -obstacle_width: # Видаляємо перешкоду, якщо вона вийшла за межі екрану
            obstacles.remove((top_obstacle, bottom_obstacle))
            score += 1
# (!) Приблизно тут ми пізніше додамо логіку стрибків
# Малюємо кота
    screen.blit(cat_img, cat.topleft)
    for top_obstacle, bottom_obstacle in obstacles:
        pygame.draw.rect(screen, GREEN, top_obstacle) # Верхня перешкода
        pygame.draw.rect(screen, GREEN, bottom_obstacle) # Нижня перешкода
# Оновлюємо екран
    score_text = font.render(f"Рахунок: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.update
# Оновлюємо частоту кадрів
    clock.tick(60)"""


"""import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
# Кольори
YELLOW = (253, 253, 150)
GREEN = (5, 244, 120)
# Початкові координати квадратика
x, y = 300, 200
width, height = 50, 50
speed = 5 # Швидкість руху квадратика

# Основний цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
# Отримання стану клавіш
    keys = pygame.key.get_pressed()
# Рух квадратика
    if keys[pygame.K_LEFT] or keys[pygame.K_a]: # Ліворуч
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: # праворуч
        x += speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]: # вниз
        y += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]: # вгору
        y -= speed
# ...
# Очищення екрану
    screen.fill(YELLOW)
# Малюємо квадратик
    pygame.draw.rect(screen, GREEN, (x, y, width, height))
# Оновлення екрану
    pygame.display.update()
# Кадри на секунду
    clock.tick(60)"""


"""import pygame
import random 

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 163, 108)  

cat_img = pygame.image.load("dog.png")
cat_img = pygame.transform.smoothscale(cat_img, (80, 80))
cat = cat_img.get_rect()
cat.topleft = (100, 100)

background_img = pygame.image.load("space.jpg")
background_img = pygame.transform.scale(background_img, (800, 600))

speed = 0
gravity = 0.5
jump_speed = -8

obstacle_timer = 0
obstacles = []
obstacle_size = 80
min_distance = 200
score = 0
font = pygame.font.Font(None, 36)

while True:
    screen.blit(background_img, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            speed = jump_speed
    
    speed += gravity
    cat.y += speed

    if cat.y > 550:
        cat.y = 550
        speed = 0
    if cat.y < -50:
        cat.y = -50
        speed = 0

    obstacle_timer += 1
    if obstacle_timer > min_distance:
        obstacle1 = random.randint(100, 500)
        obstacle2 = random.randint(120, 450)
        obstacle3 = random.randint(50, 400)  
        obstacle4 = random.randint(150, 550) 

        # Додаємо третю та четверту перешкоди
        obstacle1 = pygame.Rect(800, obstacle1, obstacle_size, obstacle_size)
        obstacle2 = pygame.Rect(800, obstacle2, obstacle_size, obstacle_size)
        obstacle3 = pygame.Rect(800, obstacle3, obstacle_size, obstacle_size)
        obstacle4 = pygame.Rect(800, obstacle4, obstacle_size, obstacle_size)

        obstacles.append((obstacle1, obstacle2, obstacle3, obstacle4))
        obstacle_timer = 0

    for obstacle1, obstacle2, obstacle3, obstacle4 in obstacles:
        obstacle1.x -= 5
        obstacle2.x -= 5
        obstacle3.x -= 5
        obstacle4.x -= 5
        
        if (cat.colliderect(obstacle1) or 
            cat.colliderect(obstacle2) or 
            cat.colliderect(obstacle3) or 
            cat.colliderect(obstacle4)):
            print("Game Over!")
            pygame.quit()
            exit()
        
        if obstacle1.x < -obstacle_size and obstacle2.x < -obstacle_size \
            and obstacle3.x < -obstacle_size and obstacle4.x < -obstacle_size:
            obstacles.remove((obstacle1, obstacle2, obstacle3, obstacle4))
            score += 1

    screen.blit(cat_img, cat.topleft)

    for obstacle1, obstacle2, obstacle3, obstacle4 in obstacles:
        pygame.draw.rect(screen, WHITE, obstacle1)
        pygame.draw.rect(screen, WHITE, obstacle2)
        pygame.draw.rect(screen, WHITE, obstacle3)
        pygame.draw.rect(screen, WHITE, obstacle4)
    
    title_font = pygame.font.Font(None, 48)
    title_text = title_font.render("Спробуй упіймати цей обєкт", True, (255, 255, 255))
    screen.blit(title_text, (200, 10))

    score_text = font.render(f"Рахунок: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
      
    pygame.display.update()
    clock.tick(60)"""

import pygame
import random 

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREEN = (0, 163, 108)  

cat_img = pygame.image.load("dog.png")
cat_img = pygame.transform.smoothscale(cat_img, (80, 80))
cat = cat_img.get_rect()
cat.topleft = (100, 100)

background_img = pygame.image.load("space.jpg")
background_img = pygame.transform.scale(background_img, (800, 600))

speed = 0
gravity = 0.5
jump_speed = -8

obstacle_timer = 0
obstacles = []
obstacle_size = 80
min_distance = 200
score = 0
font = pygame.font.Font(None, 36)

# Додаємо "невідомий об'єкт"
mystery_object = pygame.Rect(random.randint(0, 760), random.randint(0, 560), 40, 40)
mystery_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
mystery_speed = [random.choice([-3, 3]), random.choice([-3, 3])]

while True:
    screen.blit(background_img, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            speed = jump_speed
    
    speed += gravity
    cat.y += speed

    if cat.y > 550:
        cat.y = 550
        speed = 0
    if cat.y < -50:
        cat.y = -50
        speed = 0

    obstacle_timer += 1
    if obstacle_timer > min_distance:
        obstacle1 = random.randint(100, 500)
        obstacle2 = random.randint(120, 450)
        obstacle3 = random.randint(50, 400)  
        obstacle4 = random.randint(150, 550) 

        obstacle1 = pygame.Rect(800, obstacle1, obstacle_size, obstacle_size)
        obstacle2 = pygame.Rect(800, obstacle2, obstacle_size, obstacle_size)
        obstacle3 = pygame.Rect(800, obstacle3, obstacle_size, obstacle_size)
        obstacle4 = pygame.Rect(800, obstacle4, obstacle_size, obstacle_size)

        obstacles.append((obstacle1, obstacle2, obstacle3, obstacle4))
        obstacle_timer = 0

    for obstacle1, obstacle2, obstacle3, obstacle4 in obstacles:
        obstacle1.x -= 5
        obstacle2.x -= 5
        obstacle3.x -= 5
        obstacle4.x -= 5
        
        if (cat.colliderect(obstacle1) or 
            cat.colliderect(obstacle2) or 
            cat.colliderect(obstacle3) or 
            cat.colliderect(obstacle4)):
            print("Game Over!")
            pygame.quit()
            exit()
        
        if obstacle1.x < -obstacle_size and obstacle2.x < -obstacle_size \
            and obstacle3.x < -obstacle_size and obstacle4.x < -obstacle_size:
            obstacles.remove((obstacle1, obstacle2, obstacle3, obstacle4))
            score += 1

    mystery_object.x += mystery_speed[0]
    mystery_object.y += mystery_speed[1]
    if mystery_object.x <= 0 or mystery_object.x >= 760:
        mystery_speed[0] *= -1
    if mystery_object.y <= 0 or mystery_object.y >= 560:
        mystery_speed[1] *= -1

    if cat.colliderect(mystery_object):
        print("Ви спіймали невідомий об'єкт!")
        score += 10
        mystery_object.topleft = (random.randint(0, 760), random.randint(0, 560))

    pygame.draw.ellipse(screen, mystery_color, mystery_object)

    screen.blit(cat_img, cat.topleft)

    for obstacle1, obstacle2, obstacle3, obstacle4 in obstacles:
        pygame.draw.rect(screen, WHITE, obstacle1)
        pygame.draw.rect(screen, WHITE, obstacle2)
        pygame.draw.rect(screen, WHITE, obstacle3)
        pygame.draw.rect(screen, WHITE, obstacle4)
    
    title_font = pygame.font.Font(None, 48)
    title_text = title_font.render("Спробуй упіймати цей об'єкт", True, (255, 255, 255))
    screen.blit(title_text, (200, 10))

    score_text = font.render(f"Рахунок: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
      
    pygame.display.update()
    clock.tick(60)
