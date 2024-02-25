import tkinter as tk
import threading
import time
import pyautogui

def click_button():
    interval = float(time_entry.get())
    while start_clicked[0]:
        pyautogui.click()
        time.sleep(interval)

def start_clicking():
    start_clicked[0] = True
    click_thread = threading.Thread(target=click_button)
    click_thread.start()

def stop_clicking():
    start_clicked[0] = False
    window.destroy()        # zamkniecie krzyzykiem

# Tworzenie okna aplikacji
window = tk.Tk()
window.title("Clicker")
window.geometry("300x150")  #szer x wys

# pole tekstowe
time_label = tk.Label(window, text="Czas (sekundy):")
time_label.pack()

time_entry = tk.Entry(window)
time_entry.pack()

############################### Przyciski #######################################
start_clicked = [False]
start_button = tk.Button(window, text="START", command=start_clicking)  # START
start_button.pack()

stop_button = tk.Button(window, text="STOP", command=stop_clicking)     # STOP
stop_button.pack()

window.protocol("WM_DELETE_WINDOW", stop_clicking)  # STOP przy krzyzyku

window.mainloop() # petla
