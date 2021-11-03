#! /usr/bin/env python

import sys

import magic


def detect_mime(input_filename: str) -> str:
    return magic.from_file(input_filename, mime=True)

def main() -> None:
    if len(sys.argv) != 2:
        print(f"{sys.argv[0]} <input file>")
        sys.exit(1)
    input_filename = sys.argv[1]
    print(detect_mime(input_filename))

if __name__ == "__main__":
    main()
