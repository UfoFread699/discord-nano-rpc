"""Discord Rich Presence – "Playing Nano" (the GNU nano text editor).

Note: the "Nano" name comes from your Discord application name, not from this
script. Create an application called "Nano" in the Developer Portal and put its
Application ID (Client ID) below.
"""

import time

from pypresence import Presence

# ============================================================
#  SETTINGS – adjust to your liking
# ============================================================

# Application ID from the Discord Developer Portal (the "Nano" app).
CLIENT_ID = "1569760843909038210"

# Asset keys uploaded at Developer Portal -> Rich Presence -> Art Assets.
LARGE_IMAGE = "nano"        # large image (nano logo)
LARGE_TEXT = "GNU nano"

SMALL_IMAGE = "tux"         # small image (Tux / Linux) – set to "" to disable
SMALL_TEXT = "Linux"

# Text shown below the name.
DETAILS = "Editing in nano"
STATE = "$ nano notes.txt"

# Buttons (max 2, URL must start with http:// or https://).
# Set BUTTONS = [] to disable buttons.
BUTTONS = [
    {"label": "GNU nano", "url": "https://www.nano-editor.org/"},
]

# ============================================================

def main():
    rpc = Presence(CLIENT_ID)
    rpc.connect()

    payload = {
        "details": DETAILS,
        "state": STATE,
        "start": time.time(),          # how long it has been running
        "large_image": LARGE_IMAGE,
        "large_text": LARGE_TEXT,
    }

    if SMALL_IMAGE:
        payload["small_image"] = SMALL_IMAGE
        payload["small_text"] = SMALL_TEXT

    if BUTTONS:
        payload["buttons"] = BUTTONS

    rpc.update(**payload)

    print("Rich Presence is running! Press Ctrl+C to stop.")
    print("Discord should now show: Playing Nano")

    try:
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        print("\nStopping, closing connection...")
        rpc.close()


if __name__ == "__main__":
    main()
