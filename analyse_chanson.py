# analyse_chanson.py c:/toto/tata/titi.txt [--top 5]

import argparse
import os
import sys

from mon_package.ma_lib import count, get_words


def main(path, top):
    try:
        with open(path, "rt", encoding="utf8") as f:
            stats = count(get_words(f.read()))

            sorted_words = sorted(stats.items(), key=lambda e: e[1], reverse=True)

            for word, counter in sorted_words[:top]:
                print(f"- {word}: {counter}")
    except IOError:
        sys.exit(f"Unable to open file {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Un générateur de mot passe")

    parser.add_argument(
        "path",
        type=str,
        help="Path to the song",
    )

    parser.add_argument(
        "-t",
        "--top",
        type=int,
        default=int(os.environ.get("TOP_WORD_COUNT", "5")),
        help="Number of top words to show",
    )

    args = parser.parse_args()

    main(args.path, args.top)
