#!/usr/bin/env python
# coding: utf-8

# In[27]:


import tkinter
from tkinter import *
from tkinter import messagebox
ent=['Celsius','Fahrenheit']
def cal(a,b,c):
    if a =='Celsius' and  b =='Fahrenheit':
       ans=(int(c)/100)*180+32
       label3.configure(text=str(ans)+' '+b)
       e.delete(0,END)
    elif a =='Fahrenheit' and  b =='Celsius':
       ans=((int(c)-32)/180)*100
       label3.configure(text=str(ans)+' '+b)
       e.delete(0,END)
    elif a =='Celsius' and  b =='Celsius':
       ans=int(c)
       label3.configure(text=str(ans)+' '+b)
       e.delete(0,END)
    elif a =='Fahrenheit' and  b =='Fahrenheit':
       ans=int(c)
       label3.configure(text=str(ans)+' '+b)
       e.delete(0,END)
    else:
        messagebox.showerror("missing box","Please Choose coversion units\nor Enter value to convert")
        #label3.configure(text='Please Choose coversion units\nor Enter value to convert')
        
font=('serif',15)       
root=Tk()
root.geometry("400x300")
root.title('Temperature Converter')
root.configure(bg='#394554')
fab=Label(root,text='Temperature Converter',font=font,fg='#61a045')
fab.place(x=100,y=10)
#=Label(root,text="From",font=font)
#lab.place(x=10,y=60)
a=StringVar()
a.set('Choose unit')
k=OptionMenu(root,a,*ent)
label=Label(root,text='To',font=font)
b=StringVar()
b.set('Choose unit')
l=OptionMenu(root,b,*ent)
k.place(x=30,y=60)
label.place(x=170,y=60)
l.place(x=230,y=60)
label1=Label(root,text="Enter Value",font=font)
e=Entry(root)
label1.place(x=30,y=120)
e.place(x=160,y=120)
but=Button(root,text='Convert',bg='#3aa1d8',command=lambda:cal(a.get(),b.get(),e.get()))
but.place(x=150,y=170)
label3=Label(root,text='ans',font=font)
label3.place(x=100,y=230)
dir(messagebox)



root.mainloop()




    


# In[ ]:





# In[ ]:




