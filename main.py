import subprocess
import pytesseract
from game_source import apex_legends_gfn
from game_settings import capture_game
from game_settings import queue_pos
from game_source import apex_legends_gfn
from game_source import cyberpunk_gfn
from game_source import plague_tale_gfn

# Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def stylize_menu():
    print(".==================================================.")
    print("|       .-.   .-.     .--.                         |")   
    print("|      | OO| | OO|   / _.-' .-.   .-.  .-.   .''.  |")
    print("|      |   | |   |   \  '-. '-'   '-'  '-'   '..'  |")
    print("|      '^^^' '^^^'    '--'                         |")
    print("|.================.  .-.  .================.  .-.  |")
    print("||                | |   | |                |  '-'  |")
    print("||                | |   | |                |       |")
    print("||                | ':-:' |                |  .-.  |")
    print("||                |  '-'  |                |  '-'  |")
    print("|.================'       '================'       |")
    print(".==================================================.")
    print()
    print("╔════════════════════════════════════╗")
    print("║      Select a Game to Launch:      ║")
    print("╟────────────────────────────────────╢")
    print("║   [1] - Apex Legends on GFN        ║")
    print("║   [2] - Cyberpunk 2077 on GFN      ║")
    print("║   [3] - Plague Tale on GFN         ║")
    print("║                                    ║")
    print("╚════════════════════════════════════╝")
    
stylize_menu()
gfn_number = input("Select the game you want to launch: ")
    
def launch_game(gfn_number):
    if gfn_number == "1":
        print("Launching Apex Legends on GFN..\n")
        subprocess.call(apex_legends_gfn, shell=True)
    elif gfn_number == "2":
        print("Launching Cyberpunk on GFN..\n")
        subprocess.call(cyberpunk_gfn, shell=True)
    elif gfn_number == "3":
        print("Launching Plague Tale on GFN..\n")
        subprocess.call(plague_tale_gfn, shell=True)
    else:
        print("Invalid game selection.")
        
def main():
    launch_game(gfn_number)
    queue_pos()

if __name__ == "__main__":
    main()
