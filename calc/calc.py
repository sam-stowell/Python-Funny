import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
from ffpyplayer.player import MediaPlayer

def main():
    root = tk.Tk()
    root.title("Scrollable Number UI")
    root.geometry("1280x720")

    # First slider
    tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=10, pady=10)
    slider1 = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200)
    slider1.grid(row=0, column=1, padx=10, pady=10)

    # Dropdown
    tk.Label(root, text="Select Symbol:").grid(row=1, column=0, padx=10, pady=10)
    option_var = tk.StringVar(value="Option 1")
    options = ["+", "-", "*", "/"]
    dropdown = ttk.OptionMenu(root, option_var, options[0], *options)
    dropdown.grid(row=1, column=1, padx=10, pady=10)

    # Second slider
    tk.Label(root, text="Number 2:").grid(row=2, column=0, padx=10, pady=10)
    slider2 = tk.Scale(root, from_=0, to=100, orient="horizontal", length=200)
    slider2.grid(row=2, column=1, padx=10, pady=10)

    # Output label
    output_label = tk.Label(root, text="Result: ")
    output_label.grid(row=5, column=0, columnspan=2, pady=10)

    # Video display
    video_label = tk.Label(root)
    video_label.grid(row=4, column=0, columnspan=2)

    def play_video_with_audio(path, callback):
        cap = cv2.VideoCapture(path)
        player = MediaPlayer(path)
        stopped = False

        def stream():
            nonlocal stopped
            if stopped:
                return

            ret, frame = cap.read()
            audio_frame, val = player.get_frame()

            # Check if video frames ended
            video_ended = not ret
            # Check if audio ended
            audio_ended = val == 'eof'

            if not video_ended:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (640, 360))
                img = ImageTk.PhotoImage(Image.fromarray(frame))
                video_label.img = img
                video_label.config(image=img)

            if video_ended and audio_ended:
                stopped = True
                cap.release()
                video_label.config(image="")
                player.close_player()
                callback()
            else:
                video_label.after(30, stream)

        stream()

    def operate():
        print(f"Number 1: {slider1.get()}, Option: {option_var.get()}, Number 2: {slider2.get()}")
        num1 = slider1.get()
        num2 = slider2.get()
        symbol = option_var.get()

        # Comedic original logic
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

        play_video_with_audio("roidcat.mp4", show_result)

    ttk.Button(root, text="Submit", command=operate).grid(
        row=3, column=0, columnspan=2, pady=10
    )

    root.mainloop()


if __name__ == "__main__":
    main()
