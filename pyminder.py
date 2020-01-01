import time
from pygame import mixer


def reminder(t):
    while t:
        mins, secs = divmod(t, 60)
        time.sleep(1)
        t -= 1
        print(t)

    if t == 0:
        mixer.init()
        mixer.music.load(r"C:\Users\mturo\Desktop\pyminder\vader.mp3 ")
        mixer.music.play()


while True:
    reminder(1220)
