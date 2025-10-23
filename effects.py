# effects.py
import sys
import time
import threading
import os
import contextlib

# Hide pygame’s startup message
with open(os.devnull, "w") as devnull:
    with contextlib.redirect_stdout(devnull):
        import pygame


def _play_sound_loop(sound_file, stop_event, volume=0.4):
    """Loop sound in background until stop_event is set."""
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_file)
    sound.set_volume(volume)

    while not stop_event.is_set():
        sound.play()
        time.sleep(sound.get_length())

    pygame.mixer.stop()
    pygame.mixer.quit()


def typewriter_with_sound(text, sound_file, delay=0.03, volume=0.4):
    """Type text with a looping sound that stops automatically."""
    stop_event = threading.Event()
    sound_thread = threading.Thread(
        target=_play_sound_loop,
        args=(sound_file, stop_event, volume),
        daemon=True
    )
    sound_thread.start()

    try:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    finally:
        stop_event.set()
        sound_thread.join()
