from tkinter import*
from tkinter import messagebox,simpledialog



import schedule
import time



root = Tk()
root.geometry("500x500")

##def has_more_than1(input_string):
##    return len(input_string) > 1
##def has_more_than2(input_string):
##    return len(input_string) > 2
##def has_more_than3(input_string):
##    return len(input_string) > 3
##def has_more_than4(input_string):
##    return len(input_string) > 4
##T="0"


##a=has_more_than1(T)
##b=has_more_than2(T)
##c=has_more_than3(T)
##d=has_more_than4(T)


##while a==True:
##    if c == True:
##        running()
##        break
##    elif  c == False:
##        messagebox.RETRY = "password must be more that 4 characters"
##        break
T=0
T= Text(root,height=1,width=8)
T.place(x=200,y=50)
T.pack()
label90=Label(root,text="Enter the password")
label90.place(x=10,y=50)
T=int(T)
content=0
def indexcount():
    global abcd
    
    abcd=T.index(END)
def checktextbox ():
    global T
    content=T.get("1.0",END).strip()
    indexcount()
    if content:
        if abcd<4:
            messagebox.RETRY = "password must be more that 4 characters"
            T=0
        elif abcd>3:
            running()

        


def running():
    def quittt1():
        label2=Label(root,text="2")
        label2.place(x=20,y=100)
        root.destroy()


    def shoroo_va_payan():


        def provide_password():
             user_result=simpledialog.askstring("Password",'enter ur password')
             label88=Label(root,text=user_result)
        
           
             if T == user_result:
                 label89=Label(root,text="2345")
                 quittt1()
             else:
                 label3=Label(root,text=user_result)
                 label3.place(x=20,y=60)
                
             
                

        global root
        root.geometry('500x500')
        root.overrideredirect(True)#قفل کردن صفحه

        quit_button = Button(root,text='quit',command=provide_password)
        quit_button.pack()
        root.mainloop()


       
    def block_off():
        global root
        root.overrideredirect(False)#باز کردن

    schedule.every().day.at("19:13").do(shoroo_va_payan())
    schedule.every().day.at("19;14").do(block_off())


    while True:
       schedule.run_pending()
       time.sleep(1)



coni_button = Button(root,text='coniform',command=checktextbox)
coni_button.place(x=100,y=100)







