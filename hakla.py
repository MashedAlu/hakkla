import tkinter as tk

import mixer
import pygame

pygame.mixer.init()
def fade_in(alpha=0):
    if alpha <= 1:
        label.place(relx=0.5, rely=0.5, anchor="center")
        label.configure(alpha=alpha)  # needs tk >= 8.6 for transparency
        window.after(50, fade_in, alpha+0.05)
def playsound():
    pygame.mixer.music.load("E:/BRAC Tech/hakla/hakla.mp3")   # replace with your audio file
    pygame.mixer.music.play()
    fade_in()


    
window = tk.Tk()
window.title("Mental Health Update")

window.geometry("400x400")
bgimg = tk.PhotoImage(file='E:/BRAC Tech/hakla/images.png')
label = tk.Label(window, image=bgimg)
# don't pack yet, only after button press

button = tk.Button(window, text='Click me', command=playsound)
button.pack()

window.mainloop()