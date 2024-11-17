from cProfile import label
import email
from os import closerange
from pickle import OBJ
import sqlite3
from sre_parse import expand_template
from textwrap import fill
from tkinter import*
from turtle import bgcolor, color, tilt, title
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
class supplierClass:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1050x500+220+130")
      self.root.title("Inventory Management System BY Smit Ela 5001")
      self.root.focus_force()
             #all varialbles
      self.var_searchby=StringVar()
      self.var_searchtxt=StringVar()

      self.var_sup_invoice=StringVar()
      self.var_name=StringVar()
      self.var_contact=StringVar()
     
      
#       self.var_sup_invoice=StringVar()

            
             

                #search options
      lbl_search=Label(self.root,text="Search by Invoice",bg="white",font=("goudy old style",15)) 
      lbl_search.place(x=600,y=80,)  
      

      txt_search=Entry(self.root,textvariable=self.var_searchby,font=("goudy old style",15),bg="lightyellow").place(x=750,y=80,width=140,height=30)  
       
      btn_Search=Button(self.root,text="Search",command=self.search,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=900,y=80,width=100,height=30)  

      #title
      title=Label(self.root,text="Supplier Details",font=("goudy style old",20,"bold"),bg="blue",fg="white").place(x=50,y=10,width=1000,height=40)

      #content
      #row1

      lbl_supplier_invoice=Label(self.root,text="Invoice No.",font=("goudy style old",15),bg="white",).place(x=50,y=80)
     

      txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy style old",15),bg="lightyellow",).place(x=180,y=80,width=180)

     

#      row2
      lbl_name=Label(self.root,text="Name",font=("goudy style old",15),bg="white",).place(x=50,y=120)
      txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy style old",15),bg="lightyellow",).place(x=180,y=120,width=180)

     

#row3
      lbl_contact=Label(self.root,text="Contact",font=("goudy style old",15),bg="white",).place(x=50,y=160)
      txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy style old",15),bg="lightyellow",).place(x=180,y=160,width=180)

      #row 4
      lbl_desc=Label(self.root,text="Description",font=("goudy style old",15),bg="white",).place(x=50,y=200)
      self.txt_desc=Text(self.root,font=("goudy style old",15),bg="lightyellow",)
      self.txt_desc.place(x=180,y=200,width=300,height=60)



#buttons
      btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=80,y=320,width=110,height=28)
      btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="Blue",fg="white",cursor="hand2").place(x=200,y=320,width=110,height=28) 
      btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=320,y=320,width=110,height=28) 
      btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=440,y=320,width=110,height=28) 


      #tree view from employe data

      emp_frame=Frame(self.root,bd=3,relief=RIDGE)
      emp_frame.place(x=600,y=120,width=400,height=350)

      scrolly=Scrollbar(emp_frame,orient=VERTICAL)
      scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

      self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
      scrollx.pack(side=BOTTOM,fill=X)
      scrolly.pack(side=RIGHT,fill=Y)
      scrollx.config(command=self.supplierTable.xview)
      scrolly.config(command=self.supplierTable.yview)

      self.supplierTable.heading("invoice",text="Invoice No.")
      self.supplierTable.heading("name",text="Name")
      self.supplierTable.heading("contact",text="Contact")
      self.supplierTable.heading("desc",text="Description")
     
      self.supplierTable["show"]="headings"

      self.supplierTable.column("invoice",width=90)
      self.supplierTable.column("name",width=100)
      self.supplierTable.column("contact",width=100)
      self.supplierTable.column("desc",width=100)
     
      self.supplierTable.pack(fill=BOTH,expand=1)
      self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
      #self.show()
#=====================================================================
    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                  messagebox.showerror("Error","Invoice is Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                  messagebox.showerror("Error","Invoice Number is already assigned, try Different",parent=self.root)
                else:
                  cur.execute("Insert into supplier(invoice,name,contact,desc) values(?,?,?,?)",(
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0',END),
                      
                  ))
                  con.commit()
                  messagebox.showinfo("Success","Supplier added successfully",parent=self.root)
                  self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                  self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
      #  print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END),
        self.txt_desc.insert(END,row[3]),
     

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                  messagebox.showerror("Error","Invoice is Required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                  messagebox.showerror("Error","This Invoice is invalid, try Different",parent=self.root)
                else:
                  cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                       
                        self.var_name.get(),
                       
                        self.var_contact.get(),
                       
                        self.txt_desc.get('1.0',END),
                       
                        self.var_sup_invoice.get(),
                  ))
                  con.commit()
                  messagebox.showinfo("Success","Supplier updated successfully",parent=self.root)
                  self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)



    def delete(self):
      con=sqlite3.connect(database=r'ims.db')
      cur=con.cursor()
      try:
         if self.var_sup_invoice.get()=="":
                  messagebox.showerror("Error","Invoice is Required",parent=self.root)
         else:
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                  messagebox.showerror("Error","This Invoice is invalid, try Different",parent=self.root)
                else:
                  op=messagebox.askyesno("Confirm","Do you want to delete?",parent=self.root)
                  if op == True:
                     cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                     con.commit()
                     messagebox.showinfo("Delete","Supplier Deleted Successfully",parent=self.root)
                    
                     self.clear()

      except Exception as ex:
         messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        
        self.var_contact.set("")
       
        self.txt_desc.delete('1.0',END),
        
        self.var_searchtxt.set("")
       
        self.show()



    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                 messagebox.showerror("Error","Invoice is required",parent=self.root)
            else:
                  cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                  row=cur.fetchone()
                  if row!=None:
                      self.supplierTable.delete(*self.supplierTable.get_children())
                      self.supplierTable.insert('',END,values=row)
                  else:
                        messagebox.showerror("Error","No record Found",parent=self.root) 
        except Exception as ex:
                  messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


if __name__=="__main__":
   root=Tk()
   OBJ=supplierClass(root)
   root.mainloop()
