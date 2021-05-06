import tkinter as tk 
from tkinter import *
from tkinter import messagebox, filedialog
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datetime


def sendmsg():
    global Time
    global Name
    global Msg
    present_time=datetime.datetime.now().time()
    current_time=str(present_time).rsplit(".")
    current_time=current_time[0]
    driver=webdriver.Chrome(r#add path for chromedriver.exe)
    #download the chromedriver and add the path 
    driver.get("https://web.whatsapp.com/")
    messagebox.showinfo("SUCCESSFULLY"," WHATSAPP LOGGED IN")
    while(Time.get()!=current_time):
        present_time=datetime.datetime.now().time()
        current_time=str(present_time).rsplit(".")
        current_time=current_time[0]
    driver.find_element_by_xpath('//span[@title="{}"][@dir="auto"]'.format(Name.get())).click()
    driver.find_element_by_xpath('//div[@dir="ltr"][@data-tab="6"][@spellcheck="true"]').send_keys(Msg.get(),Keys.ENTER)
    messagebox.showinfo("SUCCESSFULLY "," MESSAGE SENT")
root = tk.Tk()
root.geometry("500x300")
root.configure(bg='blue')
root.resizable(False, False) 
root.title("WHATSAPP MESSAGE") 
Time = StringVar() 
Name= StringVar()
Msg=StringVar()
Name_label = Label(root,  text="Name  :", bg="#E8D579") 
Name_label.grid(row=0, column=0, pady=5,padx=5)   
root.NameText = Entry(root, width=50, textvariable=Name) 
root.NameText.grid(row=0,  column=1, pady=5, padx=5)    
Time_label = Label(root,  text="Time    :", bg="#E8D579") 
Time_label.grid(row=1, column=0, pady=5, padx=5) 
root.TimeText = Entry(root, width=50, textvariable=Time) 
root.TimeText.grid(row=1,  column=1, pady=5, padx=5)
#root.TimeText.insert(0,"HH:MM:SS")
Time_inst=Label(root,text="(Time must be HH:MM:SS format and in 24 hrs format)",bg="white")
Time_inst.grid(row=2,column=1,pady=5,padx=5)
Msg_label=Label(root,text="Msg    :",bg="#E8D579")
Msg_label.grid(row=3,column=0,pady=5,padx=5)
root.MsgText=Entry(root,width=50,textvariable=Msg)
root.MsgText.grid(row=3,column=1,pady=5,padx=5)
Send= Button(root, text="SEND",  command=sendmsg,  width=20, bg="#05E8E0") 
Send.grid(row=4, column=1, pady=3, padx=3)  
root.mainloop()
