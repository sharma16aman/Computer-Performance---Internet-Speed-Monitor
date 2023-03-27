from tkinter import *
import psutil
import speedtest
import math
from PIL import Image,ImageTk

def usage():
    cpu_count = psutil.cpu_count()
    cpu_count_label.config(text=cpu_count,image=tk_image,compound='center',fg='#00ffff')

    cpu_usage = psutil.cpu_percent()
    cpu_usage_label.config(text=cpu_usage,image=tk_image,compound='center',fg='#00ffff')
    cpu_usage_label.after(100,usage)

    ram_count = format((psutil.virtual_memory()[0]/1000000000), ".0f")
    ram_count_text = str(ram_count) + "GB" 
    ram_count_label.config(text=ram_count_text,image=tk_image,compound='center',fg='#00ffff')

    ram_usage = format((psutil.virtual_memory()[2]), ".0f")
    ram_usage_text = str(ram_usage) + "%"
    ram_usage_label.config(text=ram_usage_text,image=tk_image,compound='center',fg='#00ffff')

    ram_available = format((psutil.virtual_memory()[1]/1000000000), ".0f")
    ram_available_text = str(ram_available) + "GB"
    ram_available_label.config(text=ram_available_text,image=tk_image,compound='center',fg='#00ffff')


def internet_speed():
    st = speedtest.Speedtest()

    download_speed = str(format(st.download()/1000000), ".0f") + "Mb/s"
    download_lable.config(text=download_speed)
    upload_speed = str(format(st.upload()/1000000), ".0f") + "Mb/s"
    upload_lable.config(text=upload_speed)
    ping = str(st.results.ping) + "ms"
    ping_lable.config(text=ping)

 
root = Tk()
root.config(bg="black")
image = Image.open('meter.png')
tk_image = ImageTk.PhotoImage(image)

root.geometry("1200x700")
root.title("CPU Status")

#code for CPU Count
cpu_count_label = Label(root,font=("Orbitron",40,'bold'),text="0",bd=-4)
cpu_count_label.grid(row=0,column=0)
l1 = Label(root,font=("Orbitron",20,'bold'),bg="black",fg="#fcba03",text="CPUs")
l1.grid(row=1,column=0)

#code for CPU Usage
cpu_usage_label = Label(root,font=("Orbitron",40,'bold'),text="0",bd=-4)
cpu_usage_label.grid(row=0,column=4)
l2 = Label(root,font=("Orbitron",20,'bold'),bg="black",fg="#fcba03",text="CPU usage")
l2.grid(row=1,column=4)

#code for RAM
ram_count_label = Label(root,font=("Orbitron",40,'bold'),text="0",bd=-4)
ram_count_label.grid(row=0,column=8)
l3 = Label(root,font=("Orbitron",20,'bold'),bg="black",fg="#fcba03",text="Total RAM")
l3.grid(row=1,column=8)

#RAM Usage
ram_usage_label = Label(root,font=("Orbitron",40,'bold'),text="0",bd=-4)
ram_usage_label.grid(row=0,column=12)
l4 = Label(root,font=("Orbitron",20,'bold'),bg="black",fg="#fcba03",text="RAM Usage")
l4.grid(row=1,column=12)

#RAM Available
ram_available_label = Label(root,font=("Orbitron",40,'bold'),text="0",bd=-4)
ram_available_label.grid(row=0,column=16)
l5 = Label(root,font=("Orbitron",20,'bold'),bg="black",fg="#fcba03",text="RAM Available")
l5.grid(row=1,column=16)

speed_button = Button(root,text="Test Internet Speed",font=("Orbitron",10,'bold'),command=internet_speed)
speed_button.grid(row=3,column=0)

download_lable = Label(root,font=("Orbitron",40,'bold'),text="0 Mb/s",image=tk_image,compound='center',fg='#00ffff',bd=-4)
download_lable.grid(row=3,column=4)
l6 = Label(root,font=("Orbitron",20,'bold'),bg="black",fg="#fcba03",text="Download Speed")
l6.grid(row=4,column=4)

upload_lable = Label(root,font=("Orbitron",40,'bold'),text="0 Mb/s",image=tk_image,compound='center',fg='#00ffff',bd=-4)
upload_lable.grid(row=3,column=8)
l7 = Label(root,font=("Orbitron",20,'bold'),bg="black",fg="#fcba03",text="Upload Speed")
l7.grid(row=4,column=8)

ping_lable = Label(root,font=("Orbitron",40,'bold'),text="0 ms",image=tk_image,compound='center',fg='#00ffff',bd=-4)
ping_lable.grid(row=3,column=12)
l8 = Label(root,font=("Orbitron",20,'bold'),bg="black",fg="#fcba03",text="Ping")
l8.grid(row=4,column=12)




usage()
root.mainloop()