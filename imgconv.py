import json
import logging
import os
import time

from PIL import Image
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

logging.getLogger().setLevel(logging.INFO)
start_string_vrcx = '{"application":"VRCX"'
folder_origin = r"C:\Users\chris\Pictures\VRChat\\"
folder = r"C:\Users\chris\MEGA\VRC\VRC paparazzi"


class Handler(FileSystemEventHandler):
    def created(self, event: FileSystemEvent):
        if event.is_directory:
            return
        filename = event.src_path
        if filename.endswith(".png"):
            logging.info(f"New VRChat screenshot: {filename}")
            png_to_jpeg(filename)
            return


def watch_folder():
    handler = Handler()
    observer = Observer()
    observer.schedule(
        handler,
        path=folder_origin,
        recursive=True,
    )
    observer.start()
    logging.info("Directory monitoring started")
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        logging.info("Terminating")
        observer.stop()
    observer.join()
    return


def png_to_jpeg(img_path: str):
    im = Image.open(img_path)
    with open(img_path, "rb") as f:
        img_binary = f.read()
    extract_metadata(img_binary, img_path)
    filesize_png = os.path.getsize(img_path) // 1000
    new_path = img_path.replace(".png", ".jpg")
    im_new = im.convert("RGB")
    im_new.save(new_path)
    filesize_new = os.path.getsize(new_path) // 1000
    logging.info(
        f"filesize for {img_path.split("\\")[-1]} reduced from {filesize_png} KB "
        f"to {filesize_new} KB ({round((1-filesize_new/filesize_png)*100,2)}%)"
    )
    os.remove(img_path)


def extract_metadata(img_binary: bytes, img_file: str) -> None:
    metadata_index = img_binary.find(start_string_vrcx.encode())
    metadata = img_binary[metadata_index : img_binary.find("}]}".encode()) + 3]
    metadata_string = metadata.decode()
    if metadata_index > -1:
        with open(img_file.replace(".png", ".json"), "w") as f:
            json.dump(json.loads(metadata_string), f, indent=2)


if __name__ == "__main__":
    # main()
    watch_folder()
