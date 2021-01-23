from tkinter import *
from pytube import YouTube



#################### function #######################
def download():
    link = url.get()
    try:
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()
        video.download("/home/larry/Downloads/down")
        notification.config(fg="green",text = " video downloaded")
    except Exception as e:
        print(e)
        notification.config(fg="red",text = " failed to download the video")




#################################### gui part  ###########################################################

frame = Tk()
frame.title(" video downloader")

######### labels ##############

Label(frame,text="youtube video downloader",fg="red",font=("ariel",15)).grid(sticky=N,padx = 100,row =0)
Label(frame,text="please insert the link to your video",font=("ariel",12)).grid(sticky=N,pady = 15,row =1)
notification = Label(frame,font=("ariel",12))
notification.grid(sticky=N,pady =1, row = 4)

#####  variables  ###########

url = StringVar()
Entry(frame,width = 50, textvariable = url).grid(sticky=N,row=2)
######## Button   ##########
Button(frame,width=20,text = "Download!",font=("ariel",12),command = download).grid(sticky=N, row=3 , pady=15)

frame.mainloop()

