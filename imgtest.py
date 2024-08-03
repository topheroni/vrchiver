import json
from pprint import pprint

start_string_vrcx = '{"application":"VRCX"'
img_path_metadata = (
    r"C:\Users\chris\MEGA\VRC\2023-08\VRChat_2023-08-31_23-40-52.751_2560x1440.png"
)
img_path_no_metadata = (
    r"C:\Users\chris\MEGA\VRC\2023-08\VRChat_2023-08-12_22-37-42.994_2560x1440.png"
)
img_path_jpg = (
    r"C:\Users\chris\MEGA\VRC\2023-08\VRChat_2023-08-12_22-37-42.994_2560x1440.jpg"
)

with open(img_path_metadata, "rb") as fm:
    img_metadata = fm.read()

with open(img_path_no_metadata, "rb") as fnm:
    img_no_meta = fnm.read()

with open(img_path_jpg, "rb") as fj:
    img_jpg = fj.read()

metadata_index = img_metadata.find(start_string_vrcx.encode())

metadata = img_metadata[metadata_index:]

brace_count = 0
metadata_string = ""
limit = -1
try:
    metadata_string = metadata.decode()
except UnicodeDecodeError as e:
    limit = e.args[2]
    metadata_string = img_metadata[metadata_index : metadata_index + limit - 2].decode()
else:
    for c in metadata_string:
        if c == "{":
            brace_count += 1
        elif c == "}":
            brace_count -= 1
        if brace_count == 0:
            metadata_string += c
            break
        metadata_string += c
print(metadata_string)
metadata_dict = json.loads(metadata_string)
with open(img_path_metadata.replace(".png", ".json"), "w") as f:
    json.dump(
        obj=metadata_dict,
        fp=f,
        indent=2,
    )
# pprint(metadata_dict, indent=2)
