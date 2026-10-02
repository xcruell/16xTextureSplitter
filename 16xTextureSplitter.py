from PIL import Image
from pathlib import Path
import msvcrt
import time
import os

os.system("")

INPUT_DIR = Path(__file__).parent
OUTPUT_DIR = INPUT_DIR / "output"

MAX_SIZE = 64
TILE_SIZE = 16

RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
GRAY = "\033[90m"

print(f"{CYAN}╔═════════════════════════════════════════════╗{RESET}")
print(f"{CYAN}║         Python - 16xTextureSplitter         ║{RESET}")
print(f"{CYAN}║               Made by xcruell               ║{RESET}")
print(f"{CYAN}╚═════════════════════════════════════════════╝{RESET}")
print(f"│")

OUTPUT_DIR.mkdir(exist_ok=True)

processed = 0

for file in INPUT_DIR.glob("*.png"):
    img = Image.open(file)
    width, height = img.size

    source = f"{YELLOW}{file.name}{RESET} {GRAY}({width}x{height}){RESET}"

    if width > MAX_SIZE or height > MAX_SIZE:
        print(f"├─ {RED}[SKIP]{RESET} ┬ {source}")
        print(f"│         └─ {GRAY}{width}x{height} is too large{RESET}")
        print(f"│")
        continue

    if width % TILE_SIZE != 0 or height % TILE_SIZE != 0:
        print(f"├─ {RED}[SKIP]{RESET} ┬ {source}")
        print(f"│         └─ {GRAY}{width}x{height} is not divisible by 16{RESET}")
        print(f"│")
        continue

    if width == 16 and height == 16:
        print(f"├─ {RED}[SKIP]{RESET} ┬ {source}")
        print(f"│         └─ {GRAY}already 16x16{RESET}")
        print(f"│")
        continue

    if width == 16 and height == 32:
        top_file = OUTPUT_DIR / f"{file.stem}_top.png"
        bottom_file = OUTPUT_DIR / f"{file.stem}_bottom.png"

        img.crop((0, 0, 16, 16)).save(top_file)
        img.crop((0, 16, 16, 32)).save(bottom_file)

        print(f"├─ {GREEN}[OK]{RESET} ┬ {source}")
        print(f"│       ├─ {BLUE}{top_file.name}{RESET}")
        print(f"│       └─ {BLUE}{bottom_file.name}{RESET}")
        print(f"│")
        
        processed += 1
        continue

    if width == 32 and height == 16:
        left_file = OUTPUT_DIR / f"{file.stem}_left.png"
        right_file = OUTPUT_DIR / f"{file.stem}_right.png"

        img.crop((0, 0, 16, 16)).save(left_file)
        img.crop((16, 0, 32, 16)).save(right_file)

        print(f"├─ {GREEN}[OK]{RESET} ┬ {source}")
        print(f"│       ├─ {BLUE}{left_file.name}{RESET}")
        print(f"│       └─ {BLUE}{right_file.name}{RESET}")
        print(f"│")
        processed += 1
        continue

    tile_number = 1

    for y in range(0, height, TILE_SIZE):
        for x in range(0, width, TILE_SIZE):
            tile = img.crop((
                x,
                y,
                x + TILE_SIZE,
                y + TILE_SIZE
            ))

            output_file = OUTPUT_DIR / f"{file.stem}_{tile_number}.png"
            tile.save(output_file)

            tile_number += 1

    print(f"├─ {GREEN}[OK]{RESET} ┬ {source}")

    for number in range(1, tile_number):
        prefix = "└─" if number == tile_number - 1 else "├─"
        print(f"│       {prefix} {BLUE}{file.stem}_{number}.png{RESET}")

    processed += 1
    print("│")

print(f"{CYAN}╔═════════════════════════════════════════════╗{RESET}")
print(f"{CYAN}║        Done! {processed} texture(s) processed.        ║{RESET}")
print(f"{CYAN}╚═════════════════════════════════════════════╝{RESET}")
print()
print("Closing automatically in 4 seconds...")
print("Press any key to close now.")

start_time = time.time()

while time.time() - start_time < 4:
    if msvcrt.kbhit():
        msvcrt.getch()
        break

    time.sleep(0.05)