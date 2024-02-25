import tkinter as tk
# import pygetwindow as gw # do zbierania danych z okieneczka (nawet w tle)
import pyautogui
import threading
import time

def start():
    def press_m():
        while start_button["state"] == "disabled":
            pyautogui.keyDown('m')
            time.sleep(3)  # trzymanie przycisku przez 3 sekundy
            pyautogui.keyUp('m')
            time.sleep(0.02) # przerwa 0.02 sekundy

    def press_d():
        while start_button["state"] == "disabled":
            pyautogui.press('d')
            time.sleep(1000.1)  # opóźnienie 100 ms/1000,1 s

    def press_g():
        while start_button["state"] == "disabled":
            pyautogui.press('g')
            time.sleep(120)  # opóźnienie 120 sekund

    def press_c():
        while start_button["state"] == "disabled":
            pyautogui.press('c')
            time.sleep(0.03)  # opóźnienie 0.03 sekundy

    start_button["state"] = "disabled"
    stop_button["state"] = "normal"

    threading.Thread(target=press_m).start()
    threading.Thread(target=press_d).start()
    threading.Thread(target=press_g).start()
    threading.Thread(target=press_c).start()

def stop():
    start_button["state"] = "normal"
    stop_button["state"] = "disabled"

def exit_app(event=None):
    stop()
    root.destroy()

root = tk.Tk()      # tkinter i okieneczko
root.title("Automatyzacja przycisków")
root.bind("<Control-f>", exit_app)

start_button = tk.Button(root, text="START", command=start) # przyciski tu i ponizej
start_button.pack()

stop_button = tk.Button(root, text="STOP", command=stop, state="disabled")
stop_button.pack()

root.protocol("WM_DELETE_WINDOW", exit_app) # zamkniecie np. krzyzykiem
root.mainloop()
