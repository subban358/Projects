from tkinter import *   
import mysql.connector

def show_signup(e2):
	top.c1+=1
	if top.c1 %2 != 0:
		e2.config(show="")
	else:
		e2.config(show="*")	
		
def show_login(e2):
	top.c+=1
	if top.c %2 != 0:
		e2.config(show="")
	else:
		e2.config(show="*")	

def sign_db(e1,e2,e3,e4,sign):
	s="*/_-=+*?.<>&?%$#@^!"
	s1="1234567890"
	s2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	res=any(elem in list(s) for elem in list(e2.get()))
	res1=any(elem in list(s1) for elem in list(e2.get()))
	res2=any(elem in list(s2) for elem in list(e2.get()))
	
	if res and res2 and res2:
		if len(list(e4.get()))==10:
			l=[]
			l.append(e1.get())
			l.append(e2.get())
			l.append(e3.get())
			l.append(e4.get())
			l1=tuple(l)
			quary1="insert into auth (u_id,paswrd,Name,phone) values (%s,%s,%s,%s)"
			mycursor.execute(quary1,l1)
			mydb.commit()
			w = "Welcome"+" "+e3.get()
			l = Label(sign,text=w).place(x=90,y=280)
		else:
			l2 = Label(sign,text="Entered Invalid Mobile number").place(x=90,y=260)
			
	else:
		l1 = Label(sign,text="Give stronger password").place(x=90,y=260)
		
def signup():
	sign = Tk()
	sign.geometry("600x350")
	uname = Label(sign, text = "Username").place(x = 30,y = 50)  
	password = Label(sign, text = "Password").place(x = 30, y = 90)
	name = Label(sign, text = "Name").place(x = 30, y = 130)
	phn = Label(sign, text = "Mobile no.").place(x = 30, y = 170)
	label = Label(sign,text="Password should cointain upper & lower case and \nspecial characters").place(x=270,y=90)
	
	e1 = Entry(sign,width = 20)
	e1.place(x = 100, y = 50)  
	e2 = Entry(sign,show="*", width = 20)
	e2.place(x = 100, y = 90)  
	bt = Button(sign,text="show",width = 5,command=lambda:show_signup(e2))
	bt.place(x=220,y=90)
	e3 = Entry(sign,width = 20)
	e3.place(x = 100, y = 130)
	e4 = Entry(sign,width = 20)
	e4.place(x = 100, y = 170)
	sbmitbtn = Button(sign, text = "Submit",command = lambda:sign_db(e1,e2,e3,e4,sign))
	sbmitbtn.place(x = 90, y = 220)
	sign.mainloop()

def login_db(e1,e2,login):
	quary2="select paswrd from auth where u_id LIKE "+ "'"+e1.get()+"'"
	mycursor.execute(quary2)
	result=mycursor.fetchall()
	i=len(result)
	if i> 0:
		if result[0][0] == e2.get():
			shop()
		else:
			l2 = Label(login,text="Wrong password").place(x=90,y=150)
	else:
		l3 = Label(login,text="Wrong Username").place(x=90,y=150)

def login():
	login = Tk()	
	login.geometry("500x300")
	uname = Label(login, text = "Username").place(x = 30,y = 50)  
	password = Label(login, text = "Password").place(x = 30, y = 90)
	e1 = Entry(login,width = 20)
	e1.place(x = 100, y = 50)  
	e2 = Entry(login,show="*", width = 20)
	e2.place(x = 100, y = 90)
	sh = Button(login,text="show",width=4,command=lambda:show_login(e2))
	sh.place(x=200,y=90)
	sbmitbtn = Button(login, text = "Log in",command = lambda:login_db(e1,e2,login))
	sbmitbtn.place(x = 90, y = 120)
	login.mainloop()

def shop():
	shop = Tk()
	shop.geometry("500x400")
	b1 = Button(shop,text="Sell",width=20,command=sell)
	b2 = Button(shop,text="Update Stock",width=20,command=update)
	b1.place(x=20,y=150)
	b2.place(x=280,y=150)
	shop.mainloop()

def sell():
	sell = Tk()
	v = IntVar()
	sell.geometry("500x500")
	l1 = Label(sell,text="Enter name of product")
	l2 = Label(sell,text="Enter amount of product")
	e1 = Entry(sell,width=20)
	e2 = Entry(sell,width=20)
	l = Label(sell,text="Discount Rates")
	r1 = Radiobutton(sell,text="10%",variable=v,value=0)
	r2 = Radiobutton(sell,text="17%",variable=v,value=1)
	r3 = Radiobutton(sell,text="20%",variable=v,value=2)
	b = Button(sell,text="Print Bill",width=25,command= lambda: sold(e1.get(),e2.get(),v.get(),sell))
	l1.place(x=20,y=130)
	e1.place(x=180,y=130)
	l2.place(x=20,y=170)
	e2.place(x=180,y=170)
	b.place(x=80,y=250)
	l.place(x=340,y=130)
	r1.place(x=340,y=150)
	r2.place(x=340,y=170)
	r3.place(x=340,y=190)
	sell.mainloop()

def update():
	pass	
def sold(a,b,c,sell):
	sell.destroy()
	sold = Tk()
	q="select price from stock where product LIKE "+ "'"+a+"'"
	q2 = "select quantity from stock where product LIKE "+ "'"+a+"'"
	mycursor.execute(q)
	result=mycursor.fetchall()
	mycursor.execute(q2)
	res = mycursor.fetchall()

	q1 = "update stock set quantity= "+ "'"+str(int(res[0][0])-int(b))+"'"+"where product="+"'"+a+"'"
	mycursor.execute(q1)
	p=int(result[0][0])
	p1 = int(b)*p
	if c == 0:
		l = Label(sold,text="You have to pay"+" "+str(int(p1-p1*0.1))).pack()
	elif c == 1:
		l1 = Label(sold,text="You have to pay"+" "+str(int(p1-p1*0.17))).pack()
	elif c == 2:
		l2 = Label(sold,text="You have to pay"+" "+str(int(p1-p1*0.2))).pack()
	sold.mainloop()	



  
if __name__ == '__main__':
	top = Tk()
	top.c=0
	top.c1=0
	top.geometry("400x400")
	top.title("User Login")
	l = Label(top,text="Welcome to Login portal").place(x=120,y=90)
	mydb = mysql.connector.connect(host="localhost",user="root",passwd="159753",database="login")
	mycursor = mydb.cursor()
	b1 = Button(top,text = "Sign up",padx=30,command=signup)
	b2 = Button(top,text="Log in",padx=30,command=login)  
	b1.place(x=25,y=150)  
	b2.place(x=275,y=150)
	top.mainloop()  