import modules.access_util.timer as timer

if __name__ == "__main__":
    p=timer.run(10,2,'wakeUpSong.mp3')
    print(p.is_alive())

