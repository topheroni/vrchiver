import json
import logging
import os
import time

from PIL import Image
from send2trash import send2trash
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

logging.getLogger().setLevel(logging.INFO)
start_string_vrcx = '{"application":"VRCX"'.encode("utf-8")


class Handler(FileSystemEventHandler):
    def created(self, event: FileSystemEvent):
        if event.is_directory:
            return
        filename = event.src_path
        if filename.endswith(".png"):
            logging.info(f"New VRChat screenshot: {filename}")
            png_to_jpeg(filename)
            return


def img_conv(dir_src: str, dir_dest: str) -> None:
    os.makedirs(dir_dest, exist_ok=True)
    for dir, _, files in os.walk(dir_src):
        for file in files:
            if not file.endswith(".png"):
                continue
            path_full = os.path.join(dir, file)
            png_to_jpeg(path_full)


# TODO implement optional watchdog to auto-compress images
# def watch_folder():
#     # TODO pass user provided folder
#     handler = Handler()
#     observer = Observer()
#     observer.schedule(
#         handler,
#         path=folder_origin,
#         recursive=True,
#     )
#     observer.start()
#     logging.info("Directory monitoring started")
#     try:
#         while True:
#             time.sleep(5)
#     except KeyboardInterrupt:
#         logging.info("Terminating")
#         observer.stop()
#     observer.join()
#     return


def png_to_jpeg(path_png: str, del_original: bool = False) -> None:
    """Perform the actual conversion.

    Args:
        path_png (str): full path of the PNG image
        del_original (bool, optional): whether to delete the original PNG file. Defaults to False.
    """
    img_png = Image.open(path_png)
    with open(path_png, "rb") as f:
        img_binary = f.read()
    extract_metadata(img_binary, path_png)
    filesize_png = os.path.getsize(path_png) // 1000
    path_jpg = path_png.replace(".png", ".jpg")
    img_jpg = img_png.convert("RGB")
    img_jpg.save(path_jpg)
    filesize_jpg = os.path.getsize(path_jpg) // 1000
    logging.info(
        f"filesize for {path_png.split("\\")[-1]} reduced from {filesize_png} KB "
        f"to {filesize_jpg} KB ({round((1-filesize_jpg/filesize_png)*100,2)}%)"
    )
    if del_original:
        send2trash(path_png)


def extract_metadata(img_binary: bytes, img_file: str) -> None:
    """Extract VRCX metadata, if it exists, from the screenshot.

    Args:
        img_binary (bytes): binary string of image contents
        img_file (str): full image path
    """
    metadata_index = img_binary.find(start_string_vrcx)
    # only if VRCX metadata exists in the image
    if metadata_index > -1:
        metadata = img_binary[metadata_index : img_binary.find("}]}".encode()) + 3]
        metadata_string = metadata.decode()
        with open(img_file.replace(".png", ".json"), "w") as f:
            json.dump(json.loads(metadata_string), f, indent=2)


# if __name__ == "__main__":
#     # main()
#     watch_folder()
