import pygame
import sys
import math

# Инициализация Pygame
pygame.init()

# Установка размера экрана
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Часы с Микки")

# Загрузка изображений
clock_image = pygame.image.load("mickey_clock.png")  # Изображение часов Микки
left_hand_image = pygame.image.load("left_hand.png")  # Изображение левой руки Микки (для секунд)
right_hand_image = pygame.image.load("right_hand.png")  # Изображение правой руки Микки (для минут)

# Определение центра часов
CLOCK_CENTER = (WIDTH // 2, HEIGHT // 2)

# Основной цикл программы
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Получение текущего времени
    current_time = pygame.time.get_ticks() // 1000  # Время в секундах

    # Вычисление углов для стрелок
    minutes_angle = -(current_time % 3600) / 3600.0 * 360.0  # 3600 секунд в часе
    seconds_angle = -(current_time % 60) / 60.0 * 360.0  # 60 секунд в минуте

    # Поворот и отрисовка стрелок
    clock_rect = clock_image.get_rect(center=CLOCK_CENTER)
    screen.blit(clock_image, clock_rect)

    # Поворот и отрисовка правой руки (минутная стрелка)
    right_hand_rotated = pygame.transform.rotate(right_hand_image, minutes_angle)
    right_hand_rect = right_hand_rotated.get_rect(center=CLOCK_CENTER)
    screen.blit(right_hand_rotated, right_hand_rect)

    # Поворот и отрисовка левой руки (секундная стрелка)
    left_hand_rotated = pygame.transform.rotate(left_hand_image, seconds_angle)
    left_hand_rect = left_hand_rotated.get_rect(center=CLOCK_CENTER)
    screen.blit(left_hand_rotated, left_hand_rect)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты кадров
    clock.tick(60)
