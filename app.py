import argparse
import os

from imgconv import img_conv


def main(args):
    dir_source = args.s
    dir_dest = args.d
    if not dir_dest:
        dir_dest = dir_source
    if any(os.path.isfile(x) for x in [dir_source, dir_dest]):
        raise ValueError("arguments must be directories")
    img_conv(dir_source, dir_dest)


if __name__ == "__main__":
    dir_source_default = os.path.join(os.path.expanduser("~"), "Pictures", "VRChat")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "-src",
        help="parent folder for VRChat screenshots",
        default=dir_source_default,
        required=False,
    )
    parser.add_argument(
        "-d",
        "-dest",
        help="optional destination folder. defaults to the source directory if none provided",
        required=False,
    )
    args = parser.parse_args()
    main(args)
