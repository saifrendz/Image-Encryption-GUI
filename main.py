from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("300x250")


def encrypt_image():
    try:
        file1 = filedialog.askopenfile(mode='r', filetypes=[('Image Files', '*.png;*jpg;*.jpeg')])
        if file1 is not None:
            file_name = file1.name
            key = entry1.get(1.0, END)

            # Open file with read binary mode
            fi = open(file_name, 'rb')
            image = fi.read()
            fi.close()

            image = bytearray(image)
            for index, values in enumerate(image):
                image[index] = values ^ int(key)

            # Open file with write binary mode
            fi1 = open(file_name, 'wb')
            fi1.write(image)
            fi1.close()
    except Exception as e:
        print("An error occurred", e)


btn1 = Button(root, text="encrypt", command=encrypt_image)
btn1.place(x=70, y=10)

entry1 = Text(root, height=1, width=10)
entry1.place(x=50, y=50)

root.mainloop()
