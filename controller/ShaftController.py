import sys
sys.path.append('../model/')
sys.path.append('../view/Shaft')

import tkinter as tk

import Shaft as Shaft
import ShaftWindow as s_win

class ShaftController:
	#método construtor
	def __init__(self, model, view):
		self.model = model
		self.view = view

		#define quais botoẽs estarão disponíveis na inicialização
		if (self.model.sections == []):
			#self.view.buttonDelSection.state(['disabled'])
			#self.view.buttonOpenWinCarac.state(['disabled'])
			#self.view.buttonOpenWinSupport.state(['disabled'])
			#self.view.buttonOpenWinForce.state(['disabled'])
			#self.view.buttonDelForce.state(['disabled'])
			self.view.buttonCalc.state(['disabled'])

	#adiciona seção de eixo ao objeto
	def AddSectionToShaft(self, x1, y1, x2, y2):
		if self.model.sections == []:
			self.model.AddSection(x1, y1, x2, y2)
		else:
			x = 0
			for section in self.model.sections:
				x = section[1][0]

			self.model.AddSection(x, y1, (x+x2), y2)

	#atualiza informações das seções de eixo do objeto ao treeview
	def UpdateSectionTreeview(self):
		#limpa o treeview
		for i in self.view.tree_sections.get_children():
			self.view.tree_sections.delete(i)
		#caso haja seções de eixo, eles são adicionados no treeview
		if self.model.sections != []:
			for section in self.model.sections:
				self.view.tree_sections.insert('', tk.END, text='D: %s mm L: %s mm'%(((section[0][1])*2, (section[1][0]-section[0][0]))))

	#remove section
	def RemoveSection(self, i):
		self.model.RemoveSection(i)

	#adiciona força ao modelo
	def AddForceToTreeview(self, x, y, rt, plano, F):
		self.model.AddForce(x, y, rt, plano, F)

	#atualiza o treeview de forçãs
	def UpdateForceTreeview(self):
		for i in self.view.tree_forces.get_children():
			self.view.tree_forces.delete(i)
		if self.model.forces != []:
			for force in self.model.forces:
				self.view.tree_forces.insert('', tk.END, text='F: %s N'%(force[3]))

	#remove força
	def RemoveForce(self, i):
		self.model.RemoveForce(i)

	#atualiza o canvas com os desenhos das seções
	def UpdateCanvas(self):
		#limpa o canvas
		self.view.canvas.delete('all')
		fator = 1

		#verifica as dimenssões para que não ultrapasse os limites do canvas
		if int(self.model.sections[-1][1][0]) > 620:
				fator = 620/self.model.sections[-1][1][0]
		for section in self.model.sections:
			if int((section[0][1]*2)) > 220:
				if (220/int(section[0][1]*2)) < fator:
					fator = 220/int(section[0][1]*2)
		#comprimento total em x ao somar todas as seções
		Ltotal = int(self.model.sections[-1][1][0]*fator)

		#desenha as seções de eixo
		for section in self.model.sections:
			self.view.canvas.create_rectangle((int((340-(Ltotal/2))+(section[0][0]*fator)), int((140-(section[0][1]*fator)))), (int((340-(Ltotal/2))+(section[1][0]*fator)), int((140+(section[1][1]*fator)))), outline='black')

#teste
main_win = s_win.FirstWindow()
shaft = Shaft.Shaft()
control = ShaftController(shaft, main_win)

main_win.SetController(control)
main_win.run()

#print(shaft.sections)
#print(shaft.forces)
