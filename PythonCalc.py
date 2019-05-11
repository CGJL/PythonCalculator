#Simple Calculator using tkinter and python


from tkinter import * 
from tkinter import ttk


class Calculator:

	result = 0.0

	division_bool = False
	mult_bool = False
	add_bool = False
	sub_bool  = False



	def buttonPressC(self):

		result = 0.0
		self.number_entered.delete(0,"end")


	def buttonPress(self, value):



		enteredvalue = self.number_entered.get()

		enteredvalue += value

		self.number_entered.delete(0, "end")

		self.number_entered.insert(0, enteredvalue)

	def isfloat(self, str_val):

		try: 
			float(str_val)
			return True
		except valueError:
			return Fase

	def buttonPressMath(self, value):

		if self.isfloat(str(self.number_entered.get())):
			self.division_bool = False
			self.mult_bool = False
			self.add_bool = False
			self.sub_bool  = False

			self.result = float(self.number_entered.get())

			if value == "/":
				print("/ pressed")
				self.division_bool = True
			elif value == "+":
				print("+ pressed")
				self.add_bool = True
			elif value == "-":
				print("- pressed")
				self.sub_bool = True
			else:
				print("* pressed")
				self.mult_bool = True

			self.number_entered.delete(0,"end")

	def buttonPressEquals(self):
		if self.add_bool or self.sub_bool or self.division_bool or self.mult_bool:
			if self.add_bool:
				answer = self.result + float(self.enteredvalue.get())
			elif self.sub_bool:
				answer = self.result - float(self.enteredvalue.get())
			elif self.division_bool:
				answer = self.result / float(self.enteredvalue.get())
			else:
				answer = self.result * float(self.enteredvalue.get())

			print(self.result, " ", float(self.enteredvalue.get())," ", answer)


			self.number_entered.delete(0, "end")
			self.number_entered.insert(0, answer)



	def __init__(self, root):

		self.enteredvalue = StringVar(root, value ="")

		root.title("Python Calculator")

		root.geometry("306x130")

		root.resizable(width = False, height = False)

		style = ttk.Style()

		style.configure("Tbutton", font = "Arial 16", padding = 5)
		style.configure("TEntry", font = "Arial 20", padding = 5)


		self.number_entered = ttk.Entry(root, textvariable = self.enteredvalue, width = 48)

		self.number_entered.grid(row = 0, columnspan = 4)



		self.button7 = ttk.Button(root, text="7", command=lambda: self.buttonPress('7')).grid(row=1, column =0)

		self.button8 = ttk.Button(root, text="8", command=lambda: self.buttonPress('8')).grid(row=1, column =1)

		self.button9 = ttk.Button(root, text="9", command=lambda: self.buttonPress('9')).grid(row=1, column =2)

		self.buttonDiv = ttk.Button(root, text="/", command=lambda: self.buttonPressMath('/')).grid(row=1, column =3)

		self.button4 = ttk.Button(root, text="4", command=lambda: self.buttonPress('4')).grid(row=2, column =0)

		self.button5 = ttk.Button(root, text="5", command=lambda: self.buttonPress('5')).grid(row=2, column =1)

		self.button6 = ttk.Button(root, text="6", command=lambda: self.buttonPress('6')).grid(row=2, column =2)

		self.buttonMul = ttk.Button(root, text="*", command=lambda: self.buttonPressMath('*')).grid(row=2, column =3)

		self.button1 = ttk.Button(root, text="1", command=lambda: self.buttonPress('1')).grid(row=3, column =0)

		self.button2 = ttk.Button(root, text="2", command=lambda: self.buttonPress('2')).grid(row=3, column =1)

		self.button3 = ttk.Button(root, text="3", command=lambda: self.buttonPress('3')).grid(row=3, column =2)

		self.buttonAdd = ttk.Button(root, text="+", command=lambda: self.buttonPressMath('+')).grid(row=3, column =3)

		self.buttonC = ttk.Button(root, text="C", command=lambda: self.buttonPressC()).grid(row=4, column =0)

		self.button0 = ttk.Button(root, text="0", command=lambda: self.buttonPress('0')).grid(row=4, column =1)

		self.buttonEq = ttk.Button(root, text="=", command=lambda: self.buttonPressEquals()).grid(row=4, column =2)

		self.buttonSub = ttk.Button(root, text="-", command=lambda: self.buttonPressMath('-')).grid(row=4, column =3)




root = Tk()
calculator = Calculator(root) 

root.mainloop()