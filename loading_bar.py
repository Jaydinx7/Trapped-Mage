import sys
import time


def loading_bar(message="Loading...", total=20, delay=0.1):
    print(message)
    for i in range(total + 1):
        bar = '█' * i + '-' * (total - i)
        percent = (i / total) * 100
        sys.stdout.write(f'\r[{bar}] {percent:.0f}%')
        sys.stdout.flush()
        time.sleep(delay)
    print("\nDone!")
