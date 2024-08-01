from tkinter import*
from PIL import Image, ImageTk
import threading
root = Tk()
root.title("AI ASSISTANT")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#b5c2df")

#btn fns
def ask():
    print("ask")

def send():
    print("send")

def del_text():
    print("delete")

# frame

frame = LabelFrame(root, padx =100, pady=7, borderwidth=3 )
frame.grid(row=0,column=1,padx=55, pady=10)

# text label

text_label = Label(frame, text="Hey I'm Edith ", font = ("roboto",  14, "bold" ))
text_label.grid(row =0, column=0, padx=20,pady=10)

gif_frames = []
frame_delay = 0


def ready_gif():
    global frame_delay

    print('Started')
    gif_file = Image.open("image/orb.gif")
    for r in range(0,gif_file.n_frames):
        gif_file.seek(r)
        gif_frames.append(gif_file.copy())
    frame_delay = gif_file.info['duration']
    print('Completed')
    play_gif()

frame_count = -1

def play_gif():
    global frame_count, current_frame

    if frame_count >= len(gif_frames) - 1:
        frame_count = -1
        play_gif()

    else:
        frame_count += 1
        current_frame = ImageTk.PhotoImage(gif_frames[frame_count])
        gif_lb.config(image=current_frame)

        root.after(frame_delay,play_gif)

    

gif_lb = Label(root)
#gif_lb.pack(fill=Tk.BOTH)

threading.Thread(target=ready_gif).start()
    

ready_gif()




root.mainloop()