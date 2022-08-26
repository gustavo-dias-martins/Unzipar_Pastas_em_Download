import zipfile
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_created(self, event):
        for arquivo in os.listdir(pasta_download):
            if ".zip" in arquivo:
                try:
                    with zipfile.ZipFile(r'{}\{}'.format(pasta_download, arquivo), 'r') as zip_ref:
                        zip_ref.extractall(r'{}'.format(pasta_download))
                    os.remove(r'{}\{}'.format(pasta_download, arquivo))
                except:
                    continue
            else:
                pass


unzipar = Handler()
pasta_download = os.path.join(r"C:\Users", os.getlogin(), "Downloads")
arquivos_download = os.listdir(pasta_download)
observer = Observer()
observer.schedule(unzipar, pasta_download, recursive=False,)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()