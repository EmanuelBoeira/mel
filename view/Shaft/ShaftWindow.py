import tkinter as tk
import tkinter.ttk as ttk
import SectionWindow as SWin
import ForceWindow as FWin
import SupportWindow as SupWin
import CaracWindow as CWin

class FirstWindow:
	def __init__(self):
		#instâcia de tk.
		self.root = tk.Tk()

		#atributos da janela.
		self.root.geometry('700x700')
		self.root.title('mel-eixo')
		self.root.resizable(False, False)

		#elementos de root.
		self.canvas = tk.Canvas(self.root, width=680, height=280, bg='white')
		self.canvas.place(x=10, y=10)

		self.text1 = tk.Label(self.root, text='Seções do eixo:')
		self.text1.place(x=10, y=300)

		self.tree_sections = ttk.Treeview(self.root)
		self.tree_sections.place(x=10, y=325, width=335, height=260)

		self.buttonOpenWinSection = ttk.Button(self.root, text='Adicionar', command = self.OpenSectionWindow)
		self.buttonOpenWinSection.place(x=10, y=590, width=165, height=25)

		self.buttonDelSection = ttk.Button(self.root, text='Remover', command = lambda :[self.RemoveSection(), self.controller.UpdateSectionTreeview(), self.controller.UpdateCanvas()])
		self.buttonDelSection.place(x=180, y=590, width=165, height=25)

		self.buttonOpenWinCarac = ttk.Button(self.root, text='Adicionar característica', command = self.OpenCaracteristicWindow)
		self.buttonOpenWinCarac.place(x=10, y=620, width=335, height=25)

		self.buttonOpenWinSupport = ttk.Button(self.root, text='Adicionar apoio', command = self.OpenSupportWindow)
		self.buttonOpenWinSupport.place(x=10, y=650, width=335, height=25)

		self.text2 = tk.Label(self.root, text='Foeças do eixo:')
		self.text2.place(x=355, y=300)

		self.tree_forces = ttk.Treeview(self.root)
		self.tree_forces.place(x=355, y=325, width=335, height=260)

		self.buttonOpenWinForce = ttk.Button(self.root, text='Adicionar', command = self.OpenForceWindow)
		self.buttonOpenWinForce.place(x=355, y=590, width=165, height=25)

		self.buttonDelForce = ttk.Button(self.root, text='Remover', command = lambda: [self.RemoveForce(), self.controller.UpdateForceTreeview(), self.controller.UpdateCanvas()])
		self.buttonDelForce.place(x=525, y=590, width=165, height=25)

		self.buttonCalc = ttk.Button(self.root, text='Calcular')
		self.buttonCalc.place(x=570, y=660, width=120, height=30)

		self.buttonCancel = ttk.Button(self.root, text='Voltar', command = self.root.quit)
		self.buttonCancel.place(x=430, y=660, width=120, height=30)

		#scrollbar do treeview
		self.treeviewScroll1 = tk.Scrollbar(self.tree_sections, orient=tk.VERTICAL)# command=self.tree_sections.yview)
		self.treeviewScroll1.pack(side=tk.RIGHT, fill=tk.Y)

		self.treeviewScroll2 = tk.Scrollbar(self.tree_forces, orient=tk.VERTICAL)# command=self.tree_sections.yview)
		self.treeviewScroll2.pack(side=tk.RIGHT, fill=tk.Y)

		#controller
		self.controller = None

	def SetController(self, controller):
		self.controller = controller

	def OpenForceWindow(self):
		self.ForceWindow = FWin.ForceWindow(self.root)
		self.ForceWindow.SetController(self.controller)

	def OpenSectionWindow(self):
		self.SectionWindow = SWin.SectionWindow(self.root)
		self.SectionWindow.SetController(self.controller)

	def OpenSupportWindow(self):
		self.SupportWindow = SupWin.SupportWindow(self.root)
		self.SupportWindow.SetController(self.controller)

	def OpenCaracteristicWindow(self):
		self.CaracWindow = CWin.CaracWindow(self.root)
		self.CaracWindow.SetController(self.controller)

	def RemoveSection(self):
		sec = self.tree_sections.focus()
		self.controller.RemoveSection(self.tree_sections.index(sec))

	def RemoveForce(self):
		f = self.tree_forces.focus()
		self.controller.RemoveForce(self.tree_forces.index(f))

	#executa o loop.
	def run(self):
		self.root.mainloop()
