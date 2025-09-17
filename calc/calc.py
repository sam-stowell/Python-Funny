import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import pygame
import splitter  # Automatically splits the video/audio

def main():
    input_file = splitter.input_file
    root = tk.Tk()
    root.title("Scrollable Number UI")
    root.geometry("1280x720")

    # First slider (0–100)
    tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=10, pady=10)
    slider1 = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200)
    slider1.grid(row=0, column=1, padx=10, pady=10)

    # Dropdown box
    tk.Label(root, text="Select Symbol:").grid(row=1, column=0, padx=10, pady=10)
    option_var = tk.StringVar(value="Option 1")
    options = ["+", "-", "*", "/"]
    dropdown = ttk.OptionMenu(root, option_var, options[0], *options)
    dropdown.grid(row=1, column=1, padx=10, pady=10)

    # Second slider (0–100)
    tk.Label(root, text="Number 2:").grid(row=2, column=0, padx=10, pady=10)
    slider2 = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200)
    slider2.grid(row=2, column=1, padx=10, pady=10)

    # Output box
    output_label = tk.Label(root, text="Result: ")
    output_label.grid(row=5, column=0, columnspan=2, pady=10)

    # Video display area
    video_label = tk.Label(root)
    video_label.grid(row=4, column=0, columnspan=2)

    # Function to play video using OpenCV and show in Tkinter
    def play_video(path, callback):
        cap = cv2.VideoCapture(path)
        fps = cap.get(cv2.CAP_PROP_FPS)

        def stream():
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (640, 360))
                img = ImageTk.PhotoImage(Image.fromarray(frame))
                video_label.img = img
                video_label.config(image=img)
                video_label.after(int(1000/fps), stream)
            else:
                cap.release()
                video_label.config(image="")
                callback()

        stream()

    def operate():
        num1 = slider1.get()
        num2 = slider2.get()
        symbol = option_var.get()

        # Original comedic logic
        if symbol == "+":
            output = num1 + num2
        if symbol == "-":
            output = num1 - num2
        if symbol == "*":
            output = num1 * num2
        elif symbol == "*":
            output = num1 * num2
        else:
            output = "Error (div by 0)" if num2 == 0 else num1 / num2

        def show_result():
            output_label.config(text=f"Result: {output}")

        # Play video-only file and audio simultaneously
        pygame.mixer.init()
        pygame.mixer.music.load(input_file+"_audio.mp3")
        pygame.mixer.music.play()
        play_video((input_file+"_video.mp4"), show_result)

    ttk.Button(root, text="Submit", command=operate).grid(
        row=3, column=0, columnspan=2, pady=10
    )

    root.mainloop()

if __name__ == "__main__":
    main()
