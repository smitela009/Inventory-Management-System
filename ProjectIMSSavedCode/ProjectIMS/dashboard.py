

from itertools import product
from pickle import OBJ
from tkinter import*
from turtle import bgcolor, color, title
from unicodedata import category
from PIL import Image,ImageTk #pip install Pillow
from supplier import supplierClass
from employee import employeeClass
from category import categoryClass
from product import productClass
from sales import salesClass
from billing import BillClass
import sqlite3
from tkinter import messagebox
import os
import time
class IMS:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1350x700+0+0")
      self.root.title("Inventory Management System BY Smit Ela")
      
   #title
      self.icon_tile=PhotoImage(file="images/logo1.png")
      title=Label(self.root,text="Inventory Management System",image=self.icon_tile,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

      #button
      btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=50,width=150)

     #clock
      self.lbl_clock=Label(self.root,text="Welcome to IMS\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15,),bg="#4d636d",fg="white")
      self.lbl_clock.place(x=0,y=65,relwidth=1,height=30)



    #left menu
      self.MenuLogo=Image.open("images/menuimg.png")
      self.MenuLogo=self.MenuLogo.resize((200,200),Image.Resampling.LANCZOS)#Image.ANTIALIAS
      self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

      LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
      LeftMenu.place(x=-2,y=102,width=200,height=565)

      lbl_menulogo=Label(LeftMenu,image=self.MenuLogo)
      lbl_menulogo.pack(side=TOP,fill=X)

      self.icon_side=PhotoImage(file="images/side.png")
      lbl_menu=Label(LeftMenu,text="Menu",font=("times new roman",20,"bold"),bg="Green",).pack(side=TOP,fill=X)


      btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
      btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
      btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
      btn_Products=Button(LeftMenu,text="Products",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
      btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
      btn_billing=Button(LeftMenu,text="Billing",command=self.billing,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",15,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

 
      #Content 
      self.lbl_employee=Label(self.root,text="Total Employees\n [0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
      self.lbl_employee.place(x=250,y=120,height=150,width=300)

      self.lbl_supplier=Label(self.root,text="Total Supplier\n [0]",bd=5,relief=RIDGE,bg="orange",fg="white",font=("goudy old style",20,"bold"))
      self.lbl_supplier.place(x=600,y=120,height=150,width=300)

      self.lbl_products=Label(self.root,text="Total Products\n [0]",bd=5,relief=RIDGE,bg="Green",fg="white",font=("goudy old style",20,"bold"))
      self.lbl_products.place(x=950,y=120,height=150,width=300)

      self.lbl_category=Label(self.root,text="Total Categories\n [0]",bd=5,relief=RIDGE,bg="Brown",fg="white",font=("goudy old style",20,"bold"))
      self.lbl_category.place(x=350,y=300,height=150,width=300)

      self.lbl_sales=Label(self.root,text="Total Sales\n [0]",bd=5,relief=RIDGE,bg="blue",fg="white",font=("goudy old style",20,"bold"))
      self.lbl_sales.place(x=700,y=300,height=150,width=300)



 #footer
      lbl_footer=Label(self.root,text="Inventory Management System | Developed by Smit Ela \n Contact to Buy this Software 9682318133",font=("times new roman",15,),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
      
      
      self.update_content()
    #=======================================================================

    def employee(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=employeeClass(self.new_win)

    def supplier(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=supplierClass(self.new_win) 

    def category(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=categoryClass(self.new_win)

    def product(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=productClass(self.new_win) 

    def sales(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=salesClass(self.new_win)

    def billing(self):
      self.new_win=Toplevel(self.root)
      self.new_obj=BillClass(self.new_win)

    def update_content(self):
      con=sqlite3.connect(database=r'ims.db')
      cur=con.cursor()
      try:
        cur.execute("select * from product")
        product=cur.fetchall()
        self.lbl_products.config(text=f'Total Products\n [ {str(len(product))} ]')

        cur.execute("select * from supplier")
        supplier=cur.fetchall()
        self.lbl_supplier.config(text=f'Total Suppliers\n [ {str(len(supplier))} ]')

        cur.execute("select * from Category")
        category=cur.fetchall()
        self.lbl_category.config(text=f'Total Category\n [ {str(len(category))} ]')

        cur.execute("select * from employee")
        employee=cur.fetchall()
        self.lbl_employee.config(text=f'Total Employees\n [ {str(len(employee))} ]')
        bill=len(os.listdir('bill'))
        self.lbl_sales.config(text=f'Total Sales\n [{str(bill)}]')



        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-%m:%Y")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date:{str(date_)}\t\t Time: {str(time_)}")
        self.lbl_clock.after(200,self.update_content)


      except Exception as ex:
        messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def logout(self):
      self.root.destroy()
      os.system("python login.py")

if __name__=="__main__":
  root=Tk()
  OBJ=IMS(root)
  root.mainloop()