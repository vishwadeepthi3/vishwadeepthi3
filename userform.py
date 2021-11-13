from tkinter import *
root = Tk()
root.title('registration')
root.geometry('600x470')
root.resizable(False,False)
def register():
  name_info=name_value.get()
  phone_info=phone_value.get()
  gender_info=gender_value.get()
  email_info=email_value.get()
 
  file=open(name_info + ".txt","w")
  file.write(name_info+"\n")
  file.write(phone_info+'\n')
  file.write(gender_info+'\n')
  file.write(email_info+'\n')
  file.close()

  nameEntry.delete(0,END)
  phoneEntry.delete(0,END)
  genderEntry.delete(0,END)
  emailEntry.delete(0,END)
  
  Label(text="Registration success",fg='green',font=("Calibri",11)).place(x=250,y=430)
  

Label(root,text='Python rigistration Form',font='arial 25').pack(pady=50)
Label(text="Name",font=15).place(x=100,y=150)
Label(text="Phone",font=15).place(x=100,y=200)
Label(text="Gender",font=15).place(x=100,y=250)
Label(text="Email",font=15).place(x=100,y=300)

name_value=StringVar()
phone_value=StringVar()
gender_value=StringVar()
email_value=StringVar()

nameEntry=Entry(root,text=name_value,width=30,bd=2,font=20)
phoneEntry=Entry(root,text=phone_value,width=30,bd=2,font=20)
genderEntry=Entry(root,text=gender_value,width=30,bd=2,font=20)
emailEntry=Entry(root,text=email_value,width=30,bd=2,font=20)

nameEntry.place(x=200,y=150)
phoneEntry.place(x=200,y=200)
genderEntry.place(x=200,y=250)
emailEntry.place(x=200,y=300)

check_value=IntVar
checkbtn=Checkbutton(text='Remember me ?',variable=check_value).place(x=200,y=340)

Button(text='Register',font=20,width=11,height=2,command=register).place(x=250,y=380)






root.mainloop()
