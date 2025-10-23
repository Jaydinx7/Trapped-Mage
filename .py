import sys
import time
import threading
import os
import contextlib

# Suppress the "Hello from the pygame community" message
with open(os.devnull, "w") as devnull:
    with contextlib.redirect_stdout(devnull):
        import pygame

def play_sound_loop(sound_file, stop_event):
    """Continuously play the sound until stop_event is set."""
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_file)
    sound.set_volume(0.4)  # optional volume control

    # Loop until stopped
    while not stop_event.is_set():
        sound.play()
        time.sleep(sound.get_length())  # wait for sound duration before replaying

    # Ensure sound stops immediately
    pygame.mixer.stop()
    pygame.mixer.quit()

def typewriter(text, delay=0.03):
    """Print text like a typewriter."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # move to next line

if __name__ == "__main__":
    sound_file = "asd.wav"  # Use a short .wav typing/click sound
    stop_event = threading.Event()

    # Start sound loop in background
    sound_thread = threading.Thread(target=play_sound_loop, args=(sound_file, stop_event), daemon=True)
    sound_thread.start()

    try:
        typewriter("Typing sound will stop exactly when text finishes...", delay=0.05)
    finally:
        stop_event.set()
        sound_thread.join()
