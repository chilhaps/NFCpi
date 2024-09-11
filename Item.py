import os
music_formats = ['mp3', 'flac', 'wav', 'alac', 'ogg']

class Item:
    def __init__(self, dir, name):
        self.dir = dir
        self.name = name
        self.path = os.path.join(dir, name)
        self.format = os.path.splitext(name)[1][1:]
        self.is_playable = self.check_is_playable()
        self.is_subdirectory = self.check_is_subdir()

    def set_name(self, string):
        self.name = string

    def set_dir(self, string):
        self.path = string

    def set_format(self, string):
        self.format = string

    def set_is_playable(self, bool):
        self.is_playable = bool

    def set_is_subdirectory(self, bool):
        self.is_subdirectory = bool

    def get_name(self):
        return(self.name)

    def get_path(self):
        return(self.path)
    
    def get_format(self):
        return(self.format)
    
    def get_is_playable(self):
        return self.is_playable
    
    def get_is_subdirectory(self):
        return self.is_subdirectory
    
    def check_is_playable(self):
        return self.get_format() in music_formats
    
    def check_is_subdir(self):
        try:
            os.chdir(self.get_path())
            return True
        except:
            return False
