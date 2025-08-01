import tkinter as tk

class SupportWindow:
	def __init__(self, origin):
		#instancia de tk.
		self.root = tk.Toplevel(origin)

		#atributos da janela.
		self.root.title('Adicionar suporte')
		self.root.geometry('300x200')
		self.root.resizable(False, False)

		#elementos de root.
		self.text1 = tk.Label(self.root, text='x(mm):')
		self.text1.place(x=55, y=50)

		self.x = tk.Entry(self.root, width=100)
		self.x.place(x=145, y=50, width=100)

		self.buttonAddSupp = tk.Button(self.root, text='Adicionar')
		self.buttonAddSupp.place(x=20, y=140, width=120, height=30)

		self.buttonCancel = tk.Button(self.root, text='Cancelar', command = self.root.destroy)
		self.buttonCancel.place(x=160, y=140, width=120, height=30)

		self.controller = None

	def SetController(self, controller):
		self.controller = controller

