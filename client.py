import socket
import threading
from Tkinter import Tk, Entry, Frame, StringVar, Scrollbar, Listbox, END, X, BOTTOM, Y, RIGHT, LEFT, BOTH
from random import randint


def receive_data(sock):
    while True:
        try:
            data, addr = sock.recvfrom(4096)
            if data:
                msg_list.insert(END, '%s\n' % data)
        except OSError:
            continue


def enter_pressed(event):
    global sock
    input_get = input_field.get()
    name = name_field.get()
    if input_get:
        sock.sendto("{}: {}".format(name, input_get), server_host)
    input_user.set('')
    return


server_host = ('127.0.0.1', 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 0))

sock.sendto(" ", server_host)

threading.Thread(target=receive_data, args=(sock,)).start()

root = Tk()
root.title("Tkinter Chat")

messages_frame = Frame(root)
scrollbar = Scrollbar(messages_frame)
msg_list = Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()
messages_frame.pack()

input_name = StringVar()
name_field = Entry(root, text=input_name)
name_field.insert(0, 'Guest' + str(randint(1000, 9999)))
name_field.pack()

input_user = StringVar()
input_field = Entry(root, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

frame = Frame(root)
input_field.bind("<Return>", enter_pressed)
frame.pack()

root.mainloop()
