from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler 
from json import loads
from os import listdir, path, mkdir, rename
from time import sleep as sleep
from sys import platform

class files(object):
    def __init__(self):
        self.data_array = None
        with open(f"config.json",'r') as file:
            self.data_array = loads(file.read())

class MyHandler(FileSystemEventHandler):
    def __init__(self, obj):
        self.data_array = obj.data_array

    def on_created(self,event):
        # Reads the json file for address based on file extension
        file_size:int = -1
        while file_size != path.getsize(event.src_path):
            file_size = path.getsize(event.src_path)
            sleep(5)
        try:
            for filename in listdir(self.data_array['folder_to_track']):
                try:
                    ext = path.splitext(filename)[1]
                    found:bool = False
                    for record in self.data_array['relocation_list']:
                        if ext in record["type"]:
                            address = f"{HOME}/{record['target_location']}"
                            new_dest = f"{HOME}/{record['target_location']}/{filename}"
                            found = True
                            break
                    if found:
                        src:str = f"{self.data_array['folder_to_track']}/{filename}"
                        if not path.exists(address):
                            mkdir(address)
                        rename(src,new_dest)
                except Exception as e:
                    print(e)
                    continue
            return True
        except Exception as e:
            print(e)
            return False

HOME = None
if platform == 'linux':
    HOME = path.expanduser("~")
elif platform == 'windows':
    HOME == ''
json = files()
eventHandler = MyHandler(json)
observer = Observer()
observer.schedule(eventHandler,json.data_array['folder_to_track'],recursive=False)
observer.start()
try:
    while True:
        sleep(20)
except KeyboardInterrupt:
    observer.stop()
observer.join()
