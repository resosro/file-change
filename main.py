import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        url = "https://wil13465:11cb2a6e08a134e77e6fa7a4331f791c69@ragsauto01.esri.com/job/Mobile_Apps_Testing/job/test/build"
        response = requests.post(url, verify=False)
        print(response)


# Watching folder
def watch_folder(folder):
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, folder, recursive=False)
    observer.start()
    print(f"Watching folder: {folder}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folder_to_watch = r"\\redstorage3\devinfo\WRMResources\TestDocumentation\TestFramework\Apps"
    watch_folder(folder_to_watch)
    url = "https://wil13465:11cb2a6e08a134e77e6fa7a4331f791c69@ragsauto01.esri.com/job/Mobile_Apps_Testing/job/demo/build"
    response = requests.post(url, verify=False)
    print(response.reason)