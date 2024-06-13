import json
import os

from mon_package.ma_lib import count, get_words


def main():
    with open("song.txt", "rt", encoding="utf8") as f:
        stats = count(get_words(f.read))

        for word, counter in stats.items():
            print(f"- {word}: {counter}")


if __name__ == "__main__":
    main()
