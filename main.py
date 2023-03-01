from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import pyautogui

sizex,sizey=tuple(pyautogui.size())

root = Tk()
root.title("IDEPY")
root.geometry(f"{sizex}x{sizey}+-9+0")
root.resizable(False,False)
root.configure(bg="#ffffff")
path=""



v=Scrollbar(root, orient='vertical')
v.pack(side=RIGHT, fill='y')



code_area = Text(root,width=(sizex//10)-3,height=sizey//33,yscrollcommand=v.set)

code_area.place(relx=0.00,rely=0.01)

v.config(command=code_area.yview)


code_output = Text(root,width=(sizex//10)-3,height=sizey//59)

code_output.place(relx=0.0,rely=0.60)



def new_file():
	code_area.delete(1.0,END)
	root.title("Untitled-IDEPY")
	path=""
def openf():
	global path
	path = askopenfilename(filetypes=[("Python Files","*.py")])
	with open(path,"r") as file:
		code = file.read()
		code_area.delete(1.0,END)
		code_area.insert(1.0,code)
		root.title(f"{path}-IDEPY")
def save(path,mode="save as"):
	if path=="" or mode=="save as":
		path = asksaveasfilename(filetypes=[("Python Files","*.py")])
		if not path:
			return
		with open(path, 'w') as file:
			code = code_area.get(1.0,END)
			file.write(code)
			return path
	elif path!="" or mode=="save":
		with open(path, 'w') as file:
			code = code_area.get(1.0,END)
			file.write(code)
			return path
def run(path1):
	exec(code_area.get(1.0,END))
	if path1=="":
		global path
		path=save(path1,mode="save")
		root.title(f"IDEPY {path}")
		return
	code_output.delete(1.0,END)
	command = f'python {path}'
	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output, error = process.communicate()
	code_output.insert('1.0', output)
	code_output.insert('1.0',  error)
	code_output.insert(END,  "\nRUN PROCESS COMPLETED!")
	
def cut():
    code_area.event_generate(("<<Cut>>"))

def copy():
    code_area.event_generate(("<<Copy>>"))

def paste():
    code_area.event_generate(("<<Paste>>"))

def dark():
	root.config(bg="#000000")
	code_area.config(bg="#00000a",fg="white",insertbackground='white')
	code_output.config(bg="#00000d",fg="gold",insertbackground='white')

def light():
	root.config(bg="#ffffff")
	code_area.config(bg="#ffffff",fg="black",insertbackground='black')
	code_output.config(bg="#ffffff",fg="black",insertbackground='black')


menubar = Menu(root)  
root.config(menu=menubar)



file_menu = Menu(menubar)

menubar.add_command(label="Run",command=lambda : run(path))
menubar.configure(fg="#00000f")

menubar.add_cascade(label='File',menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_separator()
file_menu.add_command(label="Open",command=openf)
file_menu.add_separator()
file_menu.add_command(label="Save",command=lambda : save(path,"save"))
file_menu.add_separator()
file_menu.add_command(label="Save As",command=lambda : save(path))

edit_menu=Menu(menubar)
menubar.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_separator()
edit_menu.add_command(label="Cut",command=cut)
edit_menu.add_separator()
edit_menu.add_command(label="Paste",command=paste)


theme_menu=Menu(menubar)
menubar.add_cascade(label="Theme",menu=theme_menu)
theme_menu.add_command(label="Light",command=light)
theme_menu.add_separator()
theme_menu.add_command(label="Dark",command=dark)



root.mainloop()