# VRChat Picture "Archiver"

Convert all VRChat screenshots from .png to .jpg. Mainly for reducing storage size. Also pulls the [VRCX](https://github.com/vrcx-team/VRCX) metadata, if it exists, from the image and saves it as a .json file with the same file name as the corresponding screenshot.

## Usage
```
python app.py -s source_dir [-d destination_dir]
```

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
 - GUI option
 - Option to delete original screenshots