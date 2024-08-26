# VRChat Picture "Archiver"

Convert all VRChat screenshots from .png to .jpg. Mainly for reducing storage size and to preserve [VRCX](https://github.com/vrcx-team/VRCX) metadata, if it exists. The metadata is saved as a .json file with the same file name as the corresponding screenshot.

## Usage

`cd` to the directory of the cloned repo, and run the following command:

```
python app.py -s source_dir [-d destination_dir]
```

The `source_dir` is where your VRChat screenshots are being saved to (by default, your user Pictures folder). The `destination_dir` is an optional destination folder where the JPEGs will be saved to. Defaults to the screenshots source directory if not provided.

### Examples

```
python app.py -s C:\Users\user\Pictures\VRChat
python app.py -s C:\Users\user\Pictures\VRChat -d C:\Users\user\Pictures\VRChatCompressed
```

### Current features

- Converts screenshots from .png to .jpg
- Extract VRCX metadata if it exists. Saves it as a JSON with the same filename as the image

### Planned features

- Re-insert VRCX metadata into converted image
- Option to delete original screenshots
- Specify a resolution to downscale images to
- GUI
