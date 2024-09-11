import os, player, reader
from Queue import Queue
from Library import Library
    
if __name__ == '__main__':
    while True:
        user_lib = Library()
        music_uid = ''

        while not user_lib.check_for(music_uid):
            music_uid = reader.listen()

        music_dir = user_lib.search(music_uid)

        current_queue = Queue()
        current_queue.populate(music_dir)
        player.play_queue(current_queue, user_lib)
