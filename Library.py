import json, os

class Library:
    def __init__(self, filename = 'library'):
        self.filename = filename + '.json'
        self.music_library = {}
        
        if os.path.exists(os.path.join(os.getcwd(), self.filename)):
            self.read()
        else:
            self.write()

    def get_lib(self):
        return self.music_library

    def update(self, key, value):
        self.music_library[key] = value
        self.write()

    def search(self, key):
        return self.music_library[key]
    
    def check_for(self, key):
        return key in self.music_library

    def read(self):
        with open(self.filename, 'r') as openfile:
            json_object = json.load(openfile)
            
        self.music_library = json_object

    def write(self):
        with open(self.filename, 'w') as outfile:
            json.dump(self.music_library, outfile)