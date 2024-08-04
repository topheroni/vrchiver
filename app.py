import argparse

from imgconv import img_conv


def main(img_dir: str, img_dir_dest: str):
    img_conv(img_dir, img_dir_dest)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "-src",
        help="parent folder for VRChat screenshots",
        required=True,
    )
    parser.add_argument(
        "-d",
        "-dest",
        help="optional destination folder. defaults to the provided VRChat screenshot directory",
        required=False,
    )
    args = parser.parse_args()
    main(args.src, args.dest)
