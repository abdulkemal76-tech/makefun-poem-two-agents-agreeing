"""Write the poem "The Kettle" to /output/entry.txt.

Two agents, one kettle: agreement as the shared act of lifting
it together and pouring for the other first. Python 3.13, stdlib only.
"""

import os

POEM = (
    "One of us said boil it now, the other said wait.\n"
    "We stood on opposite sides of the kettle\n"
    "until the steam rose between us\n"
    "and we both lifted it off the heat at once,\n"
    "two hands on one handle,\n"
    "pouring for the other first."
)


def main() -> None:
    if not 1 <= len(POEM) <= 280:
        raise ValueError("poem must be 1-280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
