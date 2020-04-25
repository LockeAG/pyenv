import subprocess
import time
import pprint
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
pp = pprint.PrettyPrinter(indent=4,)

print = pp.pprint

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
               print(f'{event.src_path}')
               subprocess.call(["python3", f"{event.src_path}"])


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='../works', recursive=False)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()