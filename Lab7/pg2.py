import pygame
import os

pygame.init()

screen = pygame.display.set_mode((250, 250))
pygame.display.set_caption("Music Player")

music_dir = "/Users/yumi/Desktop/Songs"
songs = os.listdir(music_dir)
current_song_index = 0

pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))

def play_song():
    pygame.mixer.music.play()

def stop_song():
    pygame.mixer.music.stop()

def next_song():
    global current_song_index
    current_song_index = current_song_index + 1
    pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))
    play_song()

def prev_song():
    global current_song_index
    current_song_index = current_song_index - 1
    pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index]))
    play_song()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:            
            play_song()
            if event.key == pygame.K_LEFT: 
                prev_song()
            elif event.key == pygame.K_RIGHT:
                next_song()
            elif event.key == pygame.K_ESCAPE:
                stop_song()