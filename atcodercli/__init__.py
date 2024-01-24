import gettext
import os
import pathlib

LOCALEDIR = pathlib.Path(__file__).parent / "locales"

# TODO: fix this DIRTY solution
LANG = os.environ.get("LANG", "en_US.utf-8").split(".")[0]

try:
    lang = gettext.translation(
        "atcodercli",
        languages=[
            LANG,
        ],
        localedir=LOCALEDIR,
    )
    lang.install()
except FileNotFoundError:
    gettext.install("atcodercli")
