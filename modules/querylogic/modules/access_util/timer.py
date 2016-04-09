import sys
import multiprocessing
import time
import pyglet
import os


def exiter(dt):
    pyglet.app.exit()

def timer_run(mins,timerNo,songTitle):
    print('Timer' + str(timerNo) + ' set for ' + str(mins) + ' minute(s)')
    minutes=int(mins)
    while minutes > 0:
        time.sleep(60)
        minutes = minutes - 1
        print (str(minutes) + " minute(s) left on timer" + str(timerNo))


    print('wake up')

    currentDir = os.path.dirname(os.path.abspath(__file__))
    pathToSong = os.path.join(currentDir, songTitle)

    song = pyglet.media.load(pathToSong)
    player = pyglet.media.Player()
    player.queue(song)
    player.volume = 1.0
    player.play()

    pyglet.clock.schedule_once(exiter, song.duration)
    pyglet.app.run()


def run(mins,timerNo,songTitle):
    p = multiprocessing.Process(target=timer_run, args=(mins,timerNo,songTitle,))
    p.start()
    return p


