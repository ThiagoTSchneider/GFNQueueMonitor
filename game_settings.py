import time
from PIL import Image
import pytesseract
import pyautogui
import telebot
from telebot import types

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

telegram_api = <Insert Here TelegramAPI>
chat_id = <Insert the ChatID>
bot = telebot.TeleBot(telegram_api)

print('✓ Successfully Connected to Telegram API\n')

queue_timeout = 0
in_queue = False
specific_text = ""
number = 0

def send_message(message):
    bot.send_message(chat_id, message)
    
def send_photo(image_path):
    with open(image_path, 'rb') as photo:
        photo = types.InputFile(photo)
        bot.send_photo(chat_id, photo)

def capture_game():
    global queue_timeout
    global in_queue
    global number
    x, y, width, height = 50, 200, 380, 130
    
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save('screenshot.png')
    image = Image.open('screenshot.png')
    text = pytesseract.image_to_string(image)
    
    search_pattern = "Jogadores na sua frente:"
    start_index = text.find(search_pattern)

    if start_index != -1:
        specific_text = text[start_index + len(search_pattern):].strip()
        parts = specific_text.split()
        if len(parts) >= 1:
            number = int(parts[0])
        if not in_queue:
            send_message(f"🕹️Você entrou na Fila!")
            print("🕹️Você está na Fila!")
            queue_timeout = 0
            in_queue = True
            queue_pos()
    else:
        send_message(f"🕹️ Você não está na Fila ({queue_timeout}/3)")
        print("🕹️Você não está na Fila(", queue_timeout, "/3)")
        time.sleep(3)
        queue_timeout += 1
        in_queue = False
        queue_pos()
        
def queue_pos():
    global number
    global queue_timeout
    while queue_timeout < 4:
        if queue_timeout == 3:
            time.sleep(3)
            send_message(f"🕹️Você saiu da Fila!")
            print("🕹️Você saiu da Fila!")
            exit()
        capture_game()
        if number < 150:
            time.sleep(20)
            print("Jogadores à Sua Frente ", number)
            image_path = "screenshot.png"
            send_photo(image_path)
            send_message(f"🎮Jogadores á sua Frente: 🚀 {number}")
            send_message(f"👀🕹️ Esteja alerta e mantenha um olho atento na fila, pois ela pode diminuir rapidamente! #FiqueNaFila")
        elif number < 75:
            time.sleep(15)
            print("Jogadores à Sua Frente", number)
            image_path = "screenshot.png"
            send_photo(image_path)
            send_message(f"🎮Jogadores á sua Frente: 🚀 {number}")
            send_message(f"👀🕹️ Esteja alerta e mantenha um olho atento na fila, pois ela pode diminuir rapidamente! #FiqueNaFila")
        elif number < 30:
            time.sleep(10)
            print("Jogadores à Sua Frente", number)
            image_path = "screenshot.png"
            send_photo(image_path)
            send_message(f"🎮Jogadores á sua Frente: 🚀 {number}")
            send_message(f"👀🕹️ Esteja alerta e mantenha um olho atento na fila, pois ela pode diminuir rapidamente! #FiqueNaFila")
        elif number < 15:
            time.sleep(5)
            print("Jogadores à Sua Frente", number)
            image_path = "screenshot.png"
            send_photo(image_path)
            send_message(f"🎮Jogadores á sua Frente: 🚀 {number}")
            send_message(f"Fique atento à fila! O programa encerrará automaticamente em 4 segundos após o início. 🕹️ Não deixe passar a sua vez! #FiqueNaFila")
        elif number > 150:
            time.sleep(25)
            print("Jogadores à Sua Frente", number)
            image_path = "screenshot.png"
            send_photo(image_path)
            send_message(f"🎮Jogadores á sua Frente: 🚀 {number}")
            send_message(f"👀🕹️ Esteja alerta e mantenha um olho atento na fila, pois ela pode diminuir rapidamente! #FiqueNaFila")