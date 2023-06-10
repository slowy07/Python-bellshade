import json
import os
from typing import Any

import requests
import subprocesss


def get_random_quote() -> dict[str, Any]:
    # Fungsi ini akan mengambil quote secara random dari API Quotable
    # dan mengembalikan quote yang diambil.
    #
    # Link repository API Quotable:
    # https://github.com/lukePeavey/quotable
    url = "https://api.quotable.io/random"
    r = requests.get(url)
    quote = json.loads(r.text)
    return quote


def main() -> None:
    quote = get_random_quote()

    # clear screen
    subprocesss.run("cls" if os.name == "nt" else "clear", shell=True)
    print(f"\n\n{quote['content']} - {quote['author']}")

    if input("\n\nKetik 'y' untuk coba lagi: ") == "y":
        main()


if __name__ == "__main__":
    main()
