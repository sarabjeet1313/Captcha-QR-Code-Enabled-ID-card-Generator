from tkinter import *
from utility import *
from PIL import Image, ImageTk, ImageDraw, ImageFont



infoDic = {
     'name' : "",
     'id' : "",
     'dept_name' : "",
     'age' : "",
     'gender' : "",
     'blood' : "",
     'phn' : "",
     'capTxt' : ""
     }

color = 'rgb(255, 120, 120)'

def createID(info):
    image = Image.new('RGB', (1200,700), (51, 213, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('calibri.ttf', size=80)
    font1 = ImageFont.truetype('calibri.ttf', size=40)
    
    draw.rectangle(((30,30),(1170,670)), fill="white")
    draw.text((50, 50), info['name'], fill=color, font=font)
    draw.text((50, 150), info['id'], fill=color, font=font)
    draw.text((50, 250), info['dept_name'], fill=color, font=font)
    draw.text((50, 350), info['age'], fill=color, font=font)
    draw.text((150, 350), info['gender'], fill=color, font=font)
    draw.text((50, 450), info['blood'], fill=color, font=font)
    draw.text((50, 550), info['phn'], fill=color, font=font)

    draw.text((800,600), "Dal owned ID CARD", fill="black", font=font1)

    qrCode = createQrCode(info['id'])
    
    qrIm = Image.open(str(info['id']) + '.bmp')
    image.paste(qrIm,(800,50))

    image.save(str(info['name'] + "ID.png"))



mainWindow = Tk()
mainWindow.title("Dalhousie Captcha Enabled ID Card Generator")
mainWindow.geometry("1000x500")

""""""""" Frames """""""""

infoFrame = LabelFrame(mainWindow, text="Personal Information")
captchaFrame = LabelFrame(mainWindow, text="Additional Security")
buttonFrame = Frame(mainWindow)
messageFrame = LabelFrame(mainWindow, text="Message Pane")

infoFrame.pack(fill="both", expand=1)
infoFrame.pack_propagate(0)
captchaFrame.pack(fill="both", expand=1)
captchaFrame.pack_propagate(0)
buttonFrame.pack(fill="both", expand=1)
buttonFrame.pack_propagate(0)
messageFrame.pack(fill="both", expand=1)
messageFrame.pack_propagate(0)

""""""""""""""""""""""""""""""

""" Personal information pane """

l1 = Label(infoFrame, text="Enter Name : ")
l1.grid(row=0, column=0, sticky=W)
e1 = Entry(infoFrame)
e1.grid(row=0, column=1)

l2 = Label(infoFrame, text="Enter Student ID : ")
l2.grid(row=1, column=0, sticky=W)
e2 = Entry(infoFrame)
e2.grid(row=1, column=1)

l3 = Label(infoFrame, text="Enter Department Name : ")
l3.grid(row=2, column=0, sticky=W)
e3 = Entry(infoFrame)
e3.grid(row=2, column=1)

l4 = Label(infoFrame, text="Enter Age : ")
l4.grid(row=3, column=0, sticky=W)
e4 = Entry(infoFrame)
e4.grid(row=3, column=1)

l5 = Label(infoFrame, text="Enter Gender : ")
l5.grid(row=4, column=0,sticky=W)
e5 = Entry(infoFrame)
e5.grid(row=4, column=1)

l6 = Label(infoFrame, text="Enter Blood Group : ")
l6.grid(row=5, column=0, sticky=W)
e6 = Entry(infoFrame)
e6.grid(row=5, column=1)

l7 = Label(infoFrame, text="Enter Phone Number : ")
l7.grid(row=6, column=0, sticky=W)
e7 = Entry(infoFrame)
e7.grid(row=6, column=1)

""""""""""""""""""""""""""""""


def submit():
    
    infoDic['name'] = e1.get()
    infoDic['id'] = e2.get()
    infoDic['dept_name'] = e3.get()
    infoDic['age'] = e4.get()
    infoDic['gender'] = e5.get()
    infoDic['blood'] = e6.get()
    infoDic['phn'] = str(e7.get())

    capRead = str(e8.get())
 
    flag=1
    
 
    for val in infoDic.values():
        if val == "" :
            text.insert(INSERT, "All fields are mandatory. Please fill all of them")
            flag=0
            break

    if flag :
        if capRead != infoDic['capTxt'] :
            txt = "Captcha Failed, it was " + infoDic['capTxt'] + ". Please try again"
            text.delete(1.0,END)
            text.insert(INSERT, txt)
        else:
            text.delete(1.0,END)
            text.insert(INSERT, "Success !!!")
            createID(infoDic)



""" Captha Frame start ... """

cap_text = createTextForCaptcha()
infoDic['capTxt'] = str(cap_text)

cap_image = createCaptchaImage(cap_text)

image = Image.open(cap_image)
resized_image = image.resize((300, 100), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized_image)


lbl = Label(captchaFrame, image=img, width=300, height=100)
lbl.grid(row=0, column=0, sticky=N) 


def updateCaptcha():

    cap_text = createTextForCaptcha()
    infoDic['capTxt'] = str(cap_text)

    cap_image = createCaptchaImage(cap_text)


    image = Image.open(cap_image)
    resized_image = image.resize((300, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resized_image)

    lbl.configure(image=img)
    lbl.image = img


rImage = Image.open("Reset.png")
tImg = rImage.resize((30, 30), Image.ANTIALIAS)
rImg = ImageTk.PhotoImage(tImg)
btn = Button(captchaFrame,relief="raised", text="Reset", image=rImg, command=updateCaptcha)
btn.grid(row=0, column=1, sticky=S)

e8 = Entry(captchaFrame,width=30)
e8.grid(row=1, column=0, sticky=N)


""""""""""""""""""""""""

def close():
    txt = "Good Bye !!!"
    text.delete(1.0,END)
    text.insert(INSERT, txt)
    mainWindow.destroy()

""" Button Frame Start .... """

btn1 = Button(buttonFrame,relief="raised", text="Submit", command=submit)
btn1.grid(row=2, column=0, sticky=SW)

btn2 = Button(buttonFrame,relief="raised", text="Cancel", command=close)
btn2.grid(row=2, column=1, sticky=SW)

""""""""""""""""""""""""""""""""

""" Message Pane """
text = Text(messageFrame, width=700)
text.pack()

""""""




mainWindow.mainloop()
