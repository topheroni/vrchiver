import argparse

from imgconv import img_conv


def main(args: argparse.Namespace):
    vrchat_dir = args.s
    dest_dir = args.d
    img_conv(vrchat_dir, dest_dir)


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
        help="optional destination folder. defaults to the provided VRChat screenshot directory if none provided",
        required=False,
    )
    args = parser.parse_args()
    main(args)
