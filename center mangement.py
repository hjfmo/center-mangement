 
from tkinter import *
from tkinter import ttk

root =Tk()

root.title('CENTER MANGEMENT SYSTEM')
root.geometry('1240x515+100+100')
root.resizable(False,False)
root.configure(bg='white')


#======= ENTRIES FRAME =====
entries_frame= Frame(root,bg='red')
entries_frame.place(x=1,y=1,width=360,height=510) 

title=Label(entries_frame,text='CENTER SYSTEM',font=('calibri',16,'bold'),bg='white',fg='green'   )
title.place(x=10,y=1) 

#enter name
lblname=Label(entries_frame,text="Name",font=('calibri',17,'bold'),bg='white',fg='green')
lblname.place(x=10,y=50)
txtname = Entry(entries_frame,width=20,font=('calibri',16))
txtname.place(x=100,y=50)

#enter school year

lbljob=Label(entries_frame,text="S year",font=('calibri',17,'bold'),bg='white',fg='green')
lbljob.place(x=10,y=90)
txtjob = Entry(entries_frame,width=20,font=('calibri',16))
txtjob.place(x=100,y=90)

#enter gender

lblgender=Label(entries_frame,text="gender",font=('calibri',17,'bold'),bg='white',fg='green')
lblgender.place(x=10,y=130)
combogender=ttk.Combobox(entries_frame,state='readonly',width=18,font=('calibri',12))
combogender['values']=("male","famele")
combogender.place(x=120,y=130)

#enter age


lblage=Label(entries_frame,text="age",font=('calibri',17,'bold'),bg='white',fg='green')
lblage.place(x=10,y=170)
txtage = Entry(entries_frame,width=20,font=('calibri',16))
txtage.place(x=100,y=170)

#enter Email


lblEmail=Label(entries_frame,text="Email",font=('calibri',17,'bold'),bg='white',fg='green')
lblEmail.place(x=10,y=210)
txtEmail = Entry(entries_frame,width=20,font=('calibri',16))
txtEmail.place(x=100,y=210)

#enter mobile 

lblmobile=Label(entries_frame,text="mobile",font=('calibri',17,'bold'),bg='white',fg='green')
lblmobile.place(x=10,y=250)
txtmobile = Entry(entries_frame,width=20,font=('calibri',16))
txtmobile.place(x=100,y=250)


#enter address
 

lbladdress=Label(entries_frame,text="address:",font=('calibri',17,'bold'),bg='white',fg='green')
lbladdress.place(x=10,y=290)
txtaddress= Text(entries_frame,width=30,height=2,font=('calibri',16))
txtaddress.place(x=10,y=330)
             

#======= Buttons FRAME =====

btn_frame=Frame(entries_frame,bg='black',bd=1,relief=SOLID)
btn_frame.place(x=10,y=400,width=335,height=100)
 # first button
btnAdd = Button(btn_frame,
                text= 'Add details',
                width=14,
                height=1,
                font=('calibri',16),
                fg='green',
                bg='red',
                bd=0
                ).place(x=4,y=5)

#second button


btnupdate = Button(btn_frame,
                text= 'update details',
                width=14,
                height=1,
                font=('calibri',16),
                fg='green',
                bg='blue',
                bd=0
                ).place(x=4,y=50)

#3 button

btndelete = Button(btn_frame,
                text= 'delete details',
                width=14,
                height=1,
                font=('calibri',16),
                fg='green',
                bg='cyan',
                bd=0
                ).place(x=170,y=5)


#4 button

btnClear = Button(btn_frame,
                text= 'clarification',
                width=14,
                height=1,
                font=('calibri',16),
                fg='green',
                bg='yellow',
                bd=0
                ).place(x=170,y=50)


#=========[table frame]========

tree_frame = Frame(root,bg='white')
tree_frame.place(x=365,y=1,width=875,height=610)
style=ttk.Style()
style.configure("mystyle.treeview", front=('calibri',13),rowheight=50)
style.configure("mystyle.treeview.heading" ,front=('calibri',13) )

tv = ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),show='headings')
tv.heading("1",text="ID")
tv.column ("1",width="40")

tv.heading("2",text="Name")
tv.column ("2",width="140")


tv.heading("3",text="Age")
tv.column ("3",width="50")

tv.heading("4",text="S year")
tv.column ("4",width="120")

tv.heading("5",text="Email")  
tv.column ("5",width="150")

tv.heading("6",text="Gender")
tv.column ("6",width="90")


tv.heading("7",text="Mobile")
tv.column ("7",width="150")


tv.heading("8",text="Address")
tv.column ("8",width="150")





tv.place(x=1,y=1,height=610)













root.mainloop()