""" This module provides the Tree CLI """
# cli.py

import argparse
import pathlib
import sys

from . import __version__
from .mdltree import DirectoryTree

def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory doesn't exit")
        sys.exit()
    tree = DirectoryTree(root_dir, dir_only=args.dir_only, output_file=args.output_file) 
    tree.generate()


def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
            prog = "tree",
            description="Directory tree, a directory tree generator",
            epilog = "Fun",
            )

    parser.version = f"Directory tree generator v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
            "root_dir",
            metavar="ROOT_DIR",
            nargs="?",
            default=".",
            help="Generate a full directory tree starting at ROOT_DIR"
            )
    
    parser.add_argument(
            "-d",
            "--dir-only",
            action="store_true",
            help="Generate a directory-only tree"
            )

    parser.add_argument(
            "-o",
            "--output-file",
            nargs="?",
            default=sys.stdout,
            help="Generate a full directory tree and save it to a file"
            )
    return parser.parse_args()

