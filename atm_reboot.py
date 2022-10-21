from datetime import datetime

try:
    import json, requests
except ModuleNotFoundError:
    print('Non riesco ad importare i moduli.')

URL = "https://giromilano.atm.it/proxy.ashx"
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "HIGH:!DH:!aNULL"
headers = {"Origin": "https://giromilano.atm.it", "Referer": "https://giromilano.atm.it/",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}


class Stop(object):
    """
    Classe fermata
    """

    def __init__(self, code: str = None, language: str = 'it') -> object:
        """
        Questo è il costruttore della classe Fermata (Stop)
        """
        # controllo che code sia davvero una stringa ed eventualmente lo converto
        if not isinstance(code, str):
            code = str(code)
        if not isinstance(language, str):
            raise ValueError("Inserire una stringa che indichi la lingua!")
        digits = len(str(code))
        #print(digits)
        if digits > 6:  # tests if code is Code or CustomerCode
            print("Code")
        else:  # if code is CustomerCode, search the Code and give it to code var *
            #print("CustomerCode")
            data = {"url": f"tpPortal/tpl/stops/search/{code}"}
            try:
                r = requests.post(URL, data=data, headers=headers)
            except requests.exceptions.ConnectionError as e:
                raise ConnectionError(e, request=request)
            try:
                code = r.json()[0]['Code']  # *
            except json.decoder.JSONDecodeError as e:
                print(f"Nessuna fermata con il codice {code}")
                #raise SystemExit(f"Nessuna fermata con il codice {code}")
        data = {"url": f"tpPortal/geodata/pois/{code}?lang=it"}
        r = requests.post(URL, data=data, headers=headers)
        self.data = r.json()
        self.code = code
        self.ccode = r.json()['CustomerCode']
        self.language = language
        self.time = datetime.now()

    def description(self):
        print(f"Fermata {self.data['CustomerCode']} ({self.data['Description']}) | {self.time}\n-")

    def lines(self):
        a = []
        for record in self.data['Lines']:
            a.append(record['Line']['LineCode'])
        return (a)

    def position(self):
        return (self.data['Location']['Y'], self.data['Location']['X'])

    def showonmap(self):
        try:
            from ipyleaflet import Map, Marker
        except ModuleNotFoundError:
            print('Non riesco ad importare i moduli.')
        poi = (self.data['Location']['Y'], self.data['Location']['X'])
        m = Map(center=poi, zoom=15)
        marker = Marker(location=poi, draggable=True)
        m.add_layer(marker);
        display(m)

    def update(self):
        data = {"url": f"tpPortal/geodata/pois/{self.code}?lang=it"}
        r = requests.post(URL, data=data, headers=headers)
        self.data = r.json()
        self.time = datetime.now()

    def waitmessage(self, table_format='grid'):
        from tabulate import tabulate
        from termcolor import colored
        table = []
        title = f"{self.data['CustomerCode']} - {self.data['Description']}"
        headers = ['Linea', 'Descrizione', 'Attesa']
        for record in self.data['Lines']:
            # print('La linea {} ({}) arriverà tra {}'.format(record['Line']['LineCode'],record['Line']['LineDescription'],record['WaitMessage']))
            table.append((record['Line']['LineCode'], record['Line']['LineDescription'], record['WaitMessage']))
        print(colored(title, 'red'))
        print(tabulate(table, headers, tablefmt=table_format))
        print(f' - {self.time} - ')

    def waitmessage_plus(self, direction='0', table_format='html'):
        from tabulate import tabulate
        from termcolor import colored
        table = []
        title = f"{self.data['CustomerCode']} - {self.data['Description']}"
        headers = ['Linea', 'Descrizione', 'Attesa']
        for record in self.data['Lines']:
            link = f"<a href=\"?l={record['Line']['LineCode']}&d={direction}\">{record['Line']['LineCode']}</a>"
            table.append((link, record['Line']['LineDescription'], record['WaitMessage']))
        print(title)
        print(tabulate(table, headers, tablefmt=table_format))


class Line(object):
    """
	Classe linea
	"""

    def __init__(self, code: str = None, direction: str = '0') -> object:
        """
		Questo è il costruttore della classe Linea (Line)
		"""
        # controllo che code sia davvero una stringa ed eventualmente lo converto
        if not isinstance(code, str):
            code = str(code)
        if direction not in ('0', '1'):
            raise ValueError("Indicare la direzione con '0' o '1'!")
        if not isinstance(direction, str):
            direction = str(direction)
        requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "HIGH:!DH:!aNULL"
        data = {"url": f"tpportal/tpl/journeyPatterns/{code}|{direction}?alternativeRoutesMode=false"}
        r = requests.post(URL, data=data, headers=headers)
        self.data = r.json()
        self.code = code
        self.direction = direction

    def description(self):
        print(f"Linea {self.data['Line']['LineDescription']}\n-")

    def stops(self):
        a = []
        for record in self.data['Stops']:
            a.append(record['Code'])
        return (a)

    def path(self, table_format='grid'):
        from tabulate import tabulate
        from termcolor import colored
        table = []
        title = self.data['Line']['LineDescription']
        headers = ['Fermata', 'Descrizione']
        for stop in self.data['Stops']:
            table.append([stop['Code'], stop['Description']])
        print(colored(title, 'red'))
        print(tabulate(table, headers, tablefmt=table_format))

    def path_plus(self, direction='0', table_format='html'):
        from tabulate import tabulate
        from termcolor import colored
        table = []
        title = self.data['Line']['LineDescription']
        link_description = f"<a href=\"?l={self.code}&d={direction}\">Descrizione</a>"
        headers = ['Fermata', link_description]
        for stop in self.data['Stops']:
            link = f"<a href=\"?s={stop['Code']}\">{stop['Code']}</a>"
            table.append([link, stop['Description']])
        print(title)
        print(tabulate(table, headers, tablefmt=table_format))

    def reverse(self):
        self.direction = str((int(self.direction) + 1) % 2)
        data = {f"url": f"tpportal/tpl/journeyPatterns/{self.code}|{self.direction}?alternativeRoutesMode=false"}
        r = requests.post(URL, data=data, headers=headers)
        self.data = r.json()


def distance(s1, s2: int) -> int:
    from math import sin, cos, sqrt, atan2, radians
    # approximate radius of earth in km
    R = 6373.0
    lat1 = radians(s1.position()[0])
    lon1 = radians(s1.position()[1])
    lat2 = radians(s2.position()[0])
    lon2 = radians(s2.position()[1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    d = R * c
    return d


def from_customercode_to_code(ccode: int) -> int:
    data = {"url": f"tpPortal/tpl/stops/search/{ccode}"}
    r = requests.post(URL, data=data, headers=headers)
    try:
        data = {"url": f"tpPortal/geodata/pois/{r.json()[0]['Code']}?lang=it"}
    except json.decoder.JSONDecodeError as e:
        print(f"{ccode} -> None")
    else:
        print(f"{ccode} -> {r.json()[0]['Code']}")
