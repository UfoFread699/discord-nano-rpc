"""Discord Rich Presence – "Hraje Nano" (textový editor GNU nano).

Pozor: název "Nano" se bere z názvu Discord aplikace, ne z tohoto skriptu.
Musíš tedy v Developer Portálu vytvořit DRUHOU aplikaci pojmenovanou "Nano"
a sem vložit její Application ID (Client ID).
"""

import time

from pypresence import Presence

# ============================================================
#  NASTAVENÍ – uprav si podle sebe
# ============================================================

# Application ID z Discord Developer Portálu (aplikace "Nano").
CLIENT_ID = "1569767990344556577"

# Klíče obrázků nahraných v Developer Portálu -> Rich Presence -> Art Assets.
LARGE_IMAGE = "nano"        # velký obrázek (logo nano)
LARGE_TEXT = "GNU nano"

SMALL_IMAGE = "tux"         # malý obrázek (Tux / Linux) – můžeš nechat prázdné ""
SMALL_TEXT = "Linux"

# Text, který se zobrazí pod názvem.
DETAILS = "BodyCam"
STATE = "Playing BodyCam"

# Odkazy na tlačítka (max 2, URL musí začínat http:// nebo https://).
# Pokud tlačítka nechceš, nastav BUTTONS = [].
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
        "start": time.time(),          # od kdy běží
        "large_image": LARGE_IMAGE,
        "large_text": LARGE_TEXT,
    }

    if SMALL_IMAGE:
        payload["small_image"] = SMALL_IMAGE
        payload["small_text"] = SMALL_TEXT

    if BUTTONS:
        payload["buttons"] = BUTTONS

    rpc.update(**payload)

    print("Rich Presence běží! Pro vypnutí stiskni Ctrl+C.")
    print("Na Discordu by se teď mělo zobrazit: Hraje BodyCam")

    try:
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        print("\nKonec, zavírám připojení...")
        rpc.close()


if __name__ == "__main__":
    main()
