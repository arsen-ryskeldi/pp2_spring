import pygame
import os

# Инициализация Pygame
pygame.init()

# Установка размера экрана (этот экран не будет отображаться, он используется для обработки событий клавиатуры)
screen = pygame.display.set_mode((100, 100))

# Путь к папке с музыкальными файлами
music_folder = "music"

# Убедимся, что папка существует
if not os.path.exists(music_folder):
    os.makedirs(music_folder)

# Загрузка музыкальных файлов
music_files = [os.path.join(music_folder, filename) for filename in os.listdir(music_folder) if filename.endswith('.mp3')]

# Проверяем, есть ли музыкальные файлы
if not music_files:
    print("Ошибка: Нет музыкальных файлов в папке 'music'")
    pygame.quit()
    quit()

# Инициализация плеера
pygame.mixer.init()

# Индекс текущего трека
current_track = 0

# Загрузка первого трека, если есть что играть
pygame.mixer.music.load(music_files[current_track])

# Функция воспроизведения следующего трека
def play_next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()

# Функция воспроизведения предыдущего трека
def play_previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                play_next_track()
            elif event.key == pygame.K_LEFT:
                play_previous_track()

    # Добавленная строка: обновление дисплея
    pygame.display.update()

pygame.quit()
