import tkinter as tk

class CaracWindow:
	def __init__(self, origin):
		#instancia de tk.
		self.root = tk.Toplevel(origin)

		#atributos da janela.
		self.root.title('Adicionar força')
		self.root.geometry('500x300')
		self.root.resizable(False, False)

		#elementos de root.
		self.buttonAddCarac = tk.Button(self.root, text='Adicionar')
		self.buttonAddCarac.place(x=220, y=240, width=120, height=30)

		self.buttonCancel = tk.Button(self.root, text='Cancelar', command = self.root.destroy)
		self.buttonCancel.place(x=360, y=240, width=120, height=30)

		self.controller = None

	def SetController(self, controller):
		self.controller = controller

