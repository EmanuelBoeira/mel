class Shaft:
	sections = []   #conjunto de seções que compoem o eixo.
	forces = []     #conjunto de forças que atuam no eixo.
	supports = []   #um ou dois suportes para o eixo.
	mtot = []       #valores para montagem do gráfico de momento fletor total.

	#função de construção da classe.
	def __init__(self):
		self.name = 'Shaft'

	#adiciona coordenadas de dois pontos de uma seção do eixo.
	def AddSection(self, x1, y1, x2, y2):
		self.sections.append([[x1, y1],[x2, y2]])
		self.sections.sort()

	#adiciona coordenadas x e y de uma força no plano. rt indica se é radial(r) ou tangencial(t). F é a magnitude da força.
	def AddForce(self, x, y, rt, plano,  F):
		if rt == 't':
			if plano == 'xy':
				self.forces.append([x, y, 'xz', F])
			if plano == 'xz':
				self.forces.append([x, y, 'xy', F])
		else:
			self.forces.append([x, y, plano, F])
		self.forces.sort()

	#adiciona as coordenadas dos dois suportes do eixo.
	def AddSupport(self, x):
		self.supports.append(x)

	#adiciona os valores de momento fletor total ao longo do comprimento do eixo.
	def AddMoment(self, m):
		self.mtot.append(m)

	def RemoveSection(self, i):
		self.sections.remove(self.sections[i])

	def RemoveForce(self, i):
		self.forces.remove(self.forces[i])

#calcula e adiciona as reações dos dois suportes do eixo.
def Reactions(s):
	xy = []
	xz = []
	rxy1 = 0
	rxz1 = 0
	rxy2 = 0
	rxz2 = 0

	#adiciona as informações necessárias para o calculo da segunda reação(somatório de momento igual a zero).
	for force in s.forces:
		if force[0] < s.supports[0]:
			force[3] = -force[3]
		if force[2] == 'xy':
			xy.append([force[0], force[3]])
		else:
			xz.append([force[0], force[3]])

	#realiza os calculos do segundo apoio.
	for force in xy:
		rxy2 = rxy2 + (force[0] * force[1])
	rxy2 = (-1)*rxy2/s.supports[1]
	s.AddForce(s.supports[1], 0, 'r', 'xy', rxy2)

	for force in xz:
		rxz2 = rxz2 + (force[0] * force[1])
	rxz2 = (-1)*rxz2/s.supports[1]
	s.AddForce(s.supports[1], 0, 'r', 'xz', rxz2)

	#realiza os calculos do primeiro apoio.
	for force in s.forces:
		if force[2] == 'xy':
			rxy1 = rxy1 + force[3]
		if force[2] == 'xz':
			rxz1 = rxz1 + force[3]
	s.AddForce(s.supports[0], 0, 'r', 'xy', (-1)*rxy1)
	s.AddForce(s.supports[0], 0, 'r', 'xz', (-1)*rxz1)

	#organiza as forças em ordem crescente de x.
	s.forces.sort()


#calcula o momento fletor total.
def Bending_Moment(s):
	fxy = []
	fxz = []
	mxy = []
	mxz = []

	#separa as forças por plano.
	for f in s.forces:
		if f[2] == 'xy':
			fxy.append([f[0], f[3]])
		if f[2] == 'xz':
			fxz.append([f[0], f[3]])

	#mede as distâncias entre cada ponto e soma forças.
	for i in range(len(fxy)):
		if i+1 < len(fxy):
			fxy[i+1][1] = fxy[i+1][1] + fxy[i][1]
			fxy[i][0] = fxy[i+1][0] - fxy[i][0]

	fxy.remove(fxy[-1])

	for i in range(len(fxz)):
		if i+1 < len(fxz):
			fxz[i+1][1] = fxz[i+1][1] + fxz[i][1]
			fxz[i][0] = fxz[i+1][0] - fxz[i][0]

	fxz.remove(fxz[-1])

	#faz a multiplicação da distância pela força(integral por área).
	for f in fxy:
		mxy.append(f[0] * f[1])
	for f in fxz:
		mxz.append(f[0] * f[1])

	#faz a soma momentos.
	for i in range(len(mxy)-1):
		mxy[i+1] = mxy[i] + mxy[i+1]
		mxz[i+1] = mxz[i] + mxz[i+1]
	
	#calcula os valores de momento total.
	for i in range(len(mxy)-1):
		s.AddMoment(((mxy[i]**2) + (mxz[i])**2)**0.5)

#calcula o limite fadiga corrigido.
def Se(Sut, ka, kb, kc, kd, ke, kf):
	return (0.5*Sut)*ka*kb*kc*kd*ke*kf

#calcula o fator de fabricação ka.
def ka(Sut, x, y):
	return x*(Sut**y)

#calcula o fator de tamanho kb para flexão e torção.
def kb(d):
	if d <= 51 and d >= 2.8:
		return 1.24*(d**(-0.107))
	elif d > 51 and d <= 254:
		return 1.51 * (d*(-0.157))
	else:
		return 0

#calcula o diâmetro mínimo pelo critério de Von Misses.
def dmin(nf, Kf, Kfs, Ma, Tm, Se, Sy):
	return ((16*nf/3.1415)*(((4*((Kf*Ma/Se)**2))+(3*((Kfs*Tm/Sy)**2)))**(0.5)))**(1/3)

#exemplo
#shaft1 = Shaft()
#shaft1.AddSection(0,10,250,10)
#shaft1.AddSection(250,20,260,20)
#shaft1.AddForce(50, 10, 'r', 'xy', -876)
#shaft1.AddForce(50, 10, 'r', 'xz', 2400)
#shaft1.AddForce(195, 10, 'r', 'xy', -3937)
#shaft1.AddForce(195, 10, 'r', 'xz', -10814)
#shaft1.AddSupport(0)
#shaft1.AddSupport(250)

#print(shaft1.sections)
#shaft1.RemoveSection(250,20)
#print(shaft1.sections)

#Reactions(shaft1)
#Bending_Moment(shaft1)
#print(shaft1.mtot)
