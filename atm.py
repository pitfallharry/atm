from datetime import datetime

try:
	import urllib.request, json
except ModuleNotFoundError:
	print('Non riesco ad importare i moduli.')

class Stop(object):
	"""
	Classe fermata
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
	def lines(self):
		a = []
		for record in self.data['Lines']:
			a.append(record['Line']['LineCode'])
		return(a)
	def position(self):
		return (self.data['Location']['X'],self.data['Location']['Y'])
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
	def waitmessage(self,table_format='grid'):
		from tabulate import tabulate
		from termcolor import colored
		table = []
		title = self.data['CustomerCode'] + ' - ' + self.data['Description']
		headers =['Linea','Descrizione','Attesa']
		for record in self.data['Lines']:
			#print('La linea {} ({}) arriverà tra {}'.format(record['Line']['LineCode'],record['Line']['LineDescription'],record['WaitMessage']))
			table.append((record['Line']['LineCode'],record['Line']['LineDescription'],record['WaitMessage']))
		print(colored(title,'red'))
		print(tabulate(table,headers,tablefmt=table_format))
		print(' - {} - '.format(self.time))
		#return(a)


class Line(object):
	"""
	Classe linea
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
	def stops(self):
		a = []
		for record in self.data['Stops']:
			a.append(record['Code'])
		return(a)
	def path(self,table_format='grid'):
		from tabulate import tabulate
		from termcolor import colored
		table = []
		title = self.data['Line']['LineDescription']
		headers =['Fermata','Descrizione']
		for stop in self.data['Stops']:
			table.append([stop['Code'],stop['Description']])
		print(colored(title,'red'))
		print(tabulate(table,headers,tablefmt=table_format))

def distance(s1,s2):
	from math import sin, cos, sqrt, atan2, radians
	# approximate radius of earth in km
	R = 6373.0
	lat1 = radians(s1.position()[0])
	lon1 = radians(s1.position()[1])
	lat2 = radians(s2.position()[0])
	lon2 = radians(s2.position()[1])
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))
	d = R * c
	return d

#s = Stop(12125,'it')
#s.data
#s.waitmessage('grid')
#s.description()
#s.waitmessage()

#l = Line(73,0)
#l.data
#l.path()
