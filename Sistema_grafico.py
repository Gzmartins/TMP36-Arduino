import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import random
import datetime
import winsound
import matplotlib.pyplot as plt
import serial.tools.list_ports
import requests

# === CONFIGURAÇÕES ===
MODO_SIMULACAO = True
BAUD_RATE = 9600
WHATSAPP_NUMERO = "+5521980629738"
WHATSAPP_APIKEY = "9571957"
TEMPO_ENTRE_ALERTAS = 120
ultimo_envio = 0

def detectar_arduino():
    portas = list(serial.tools.list_ports.comports())
    for p in portas:
        if "Arduino" in p.description or "CH340" in p.description:
            return p.device
    return None

PORTA_SERIAL = detectar_arduino()
try:
    if not MODO_SIMULACAO and PORTA_SERIAL:
        arduino = serial.Serial(PORTA_SERIAL, BAUD_RATE, timeout=1)
    else:
        MODO_SIMULACAO = True
except:
    MODO_SIMULACAO = True

# === VARIÁVEIS ===
temperatura_atual = 0
temperatura_anterior = None
tendencia = "➖ Estável"
limite_min = 2
limite_max = 8
historico_temperaturas = []

def enviar_alerta_whatsapp(mensagem):
    global ultimo_envio
    agora = time.time()
    if agora - ultimo_envio >= TEMPO_ENTRE_ALERTAS:
        try:
            mensagem_encoded = requests.utils.quote(mensagem)
            url = f"https://api.callmebot.com/whatsapp.php?phone={WHATSAPP_NUMERO}&text={mensagem_encoded}&apikey={WHATSAPP_APIKEY}"
            response = requests.get(url)
            if response.status_code == 200:
                print("✅ Alerta WhatsApp enviado com sucesso!")
                ultimo_envio = agora
            else:
                print("❌ Erro ao enviar mensagem:", response.text)
        except Exception as e:
            print("❌ Erro na conexão:", e)

# === INTERFACE TKINTER ===
root = tk.Tk()
root.title("Monitoramento de Temperatura com Arduino")
root.geometry("450x500")
root.resizable(False, False)

frame = ttk.Frame(root, padding=20)
frame.pack(fill='both', expand=True)

ttk.Label(frame, text="Temperatura Atual:", font=("Arial", 14)).pack()
temp_label = ttk.Label(frame, text="-- °C", font=("Arial", 24), foreground="blue")
temp_label.pack(pady=10)

status_label = ttk.Label(frame, text="Iniciando...", font=("Arial", 12))
status_label.pack(pady=5)

tendencia_label = ttk.Label(frame, text="Tendência: ➖ Estável", font=("Arial", 12))
tendencia_label.pack(pady=5)
