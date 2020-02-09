from datetime import datetime

try:
	import urllib.request, json
except ModuleNotFoundError:
	print('Non riesco ad importare i moduli.')

class Stop(object):
	"""
	Stop oggetto fermata
	"""
	def __init__(self, number=None, language='it'):
		"""
		Questo è il costruttore della classe.
		"""
		# controllo che number sia davvero un numero
		if not isinstance(number, int):
			raise ValueError("Inserire un numero per indicare la fermata!")
		if not isinstance(language, str):
			raise ValueError("Inserire una stringa che indichi la lingua!")
		url = 'https://giromilano.atm.it/TPPortalBackEnd/geodata/pois/stops/' + str(number) + '?lang=' + language
		try:
			r = urllib.request.urlopen(url).read().decode('utf-8')
		except urllib.error.HTTPError:
			print('La fermata {} non esiste.'.format(number))
		else:
			data = json.loads(r)
			self.data = data
		self.number = number
		self.language = language
		self.time = datetime.now()
	def description(self):
		print('Fermata {} ({}) | {}\n-'.format(self.data['CustomerCode'],self.data['Description'],self.time))
	def update(self):
		url = 'https://giromilano.atm.it/TPPortalBackEnd/geodata/pois/stops/' + str(self.number) + '?lang=' + self.language
		try:
			r = urllib.request.urlopen(url).read().decode('utf-8')
		except urllib.error.HTTPError:
			print('Non riesco ad aggionrare i dati della fermata {}.'.format(self.number))
		else:
			data = json.loads(r)
			self.data = data
			self.time = datetime.now()
	def waitmessage(self):
		a = []
		for record in self.data['Lines']:
			print('La linea {} ({}) arriverà tra {}'.format(record['Line']['LineCode'],record['Line']['LineDescription'],record['WaitMessage']))
			#a.append((record['Line']['LineCode'],record['Line']['LineDescription'],record['WaitMessage']))
		#return(a)

class Line(object):
	"""
	Stop oggetto linea
	"""
	def __init__(self, number=None, direction=0):
		"""
		Questo è il costruttore della classe.
		"""
		# controllo che number sia davvero un numero
		if not isinstance(number, int):
			raise ValueError("Inserire un numero per indicare la fermata!")
		if direction not in (0,1):
			raise ValueError("Indicare la direzione con 0 o 1!")
		url = 'https://giromilano.atm.it/TPPortalBackEnd/tpl/journeyPatterns/' + str(number) + '%7C' + str(direction)
		try:
			r = urllib.request.urlopen(url).read().decode('utf-8')
		except urllib.error.HTTPError:
			print('La fermata {} non esiste.'.format(number))
		else:
			data = json.loads(r)
		self.number = number
		self.data = data
		self.direction = direction
	def description(self):
		print('Linea {}\n-'.format(self.data['Line']['LineDescription']))
		#a.append((record['Line']['LineCode'],record['Line']['LineDescription'],record['WaitMessage']))
		#return(a)
	def path(self):
		self.description()
		for stop in self.data['Stops']:
			print('{} ({})'.format(stop['Code'],stop['Description']))
		#a.append((record['Line']['LineCode'],record['Line']['LineDescription'],record['WaitMessage']))
		#return(a)

#s = Stop(12125,'it')
#print(s.data)
#print(s.waitmessage())
#s.description()
#s.waitmessage()

#l = Line(73,0)
#print(l.data)
#l.path()