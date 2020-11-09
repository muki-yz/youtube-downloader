def kontrol():
    link = link_girdi.get()
     #ses ise 1 video ise 0
    try:
        global yt
        yt = YouTube(link)
        baslik = yt.title
        lbl_result["text"] = "Video: "+baslik
    except:
        lbl_result["text"] = "Bir hata oluştu,Linki kontrol et."
def indir():
    file_type = var1.get()
    global yt
    if file_type == 1:
        file_type = "audio"
        kaliteler = yt.streams.filter(type=file_type).all()

    elif file_type == 0:
        file_type = "video"
         
        if var2.get() ==1:
            res = "480p"
        elif var2.get() == 0:
            res="360p"
        kaliteler = yt.streams.filter(type=file_type, res = res).all()
    else:
        indir_buton["text"]="Bir sorun oluştu, dosya tipiyle ilgili"
    try:
    #Her şey yolunda ise indirsin
        indir_buton["text"]="Başladık!"
        lbl_result["text"] = str(kaliteler[0].filesize)+" indiriliyor"
        kaliteler[0].download(output_path = konum, filename = yt.title) # path, where to video download.
        indir_buton["text"]="Bitti!"
        lbl_result["text"] = " İndirme bitti\n" + str(kaliteler[0].filesize*0.000001) + "mb\n Dosya şurada >>>"+str(konum)
        print(f"İndirme Bitti! {kaliteler[0].filesize*0.000001}mb\nDosya şurada >>{konum}")
    except:
    #Hata verirse buraya gelecek, inş gelmez
        indir_buton["text"]="İndirme Gerçekleştirilemedi\nBir Hata oluştu!"


#import tkinter as tk
from pytube import YouTube
from tkinter import Frame,Entry,Label,Tk,Button,Checkbutton, IntVar
import os
konum = os.path.dirname(os.path.abspath(__file__))+"/Downloads"

# Set-up the window
window = Tk()
window.title("YouTube Video İndirici")
window.geometry("550x180")
window.wm_iconbitmap('favicon.ico')
window.configure(bg="light grey")
# Create the Fahrenheit entry frame with an Entry
# widget and label in it
#%%

link_frame = Frame(master=window)
link_girdi = Entry(master=link_frame, width=20)
link_label = Label(master=link_frame, text="Link     ",bg="grey",fg="black")

tur_frame = Frame(master=window)
var1 = IntVar()
tur_girdi = Checkbutton(master=tur_frame, variable = var1)
tur_label = Label(master=tur_frame, text="Ses doyası ise burayı işaretle",bg="grey",fg="black")

kalite_frame = Frame(master=window)
var2 = IntVar()
kalite_girdi = Checkbutton(master=kalite_frame, variable = var2)
kalite_label = Label(master=kalite_frame, text="480p olsun mu?\nDefault olarak 360'dır     ",bg="grey",fg="black")


# Layout the temperature Entry and Label in link_frame
# using the .grid() geometry manager
link_girdi.grid(row=0, column=1, sticky="w")
link_label.grid(row=0, column=0, sticky="w")

tur_girdi.grid(row=1, column=1, sticky="w")
tur_label.grid(row=1, column=0, sticky="w")

kalite_girdi.grid(row=2, column=1, sticky="w")
kalite_label.grid(row=2, column=0, sticky="w")
# Create the conversion Button and result display Label
indir_buton = Button(
    master=window,
    text="İndirmeye Başla!",
    command=indir
)
kontrol_buton = Button(
    master=window,
    text="Linki Kontrol Et",
    command=kontrol
)
cikis = Button(master=window,text='Uygulamadan Çık', command=window.quit)
lbl_result = Label(master=window, text="Girdiler Bekleniyor..\n-Link")
lbl_result.grid(row=3, columnspan=5, padx=10,sticky="e")

# Set-up the layout using the .grid() geometry manager
link_frame.grid(row=0, column=0, padx=10,sticky="w")
tur_frame.grid(row=1, column=0, padx=10,sticky="w")
kalite_frame.grid(row=2, column=0, padx=10,sticky="w")

kontrol_buton.grid(row=0, column=1, pady=10)
indir_buton.grid(row=1, column=1, pady=10)


cikis.grid(row=2, column =1, pady=10)

# Run the application
window.mainloop()