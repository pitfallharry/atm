from datetime import datetime
import json
import requests
from math import sin, cos, sqrt, atan2, radians
from tabulate import tabulate
from termcolor import colored

# Imposta sessione globale per le richieste HTTP
session = requests.Session()
session.headers.update({
    "Origin": "https://giromilano.atm.it",
    "Referer": "https://giromilano.atm.it/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Dest": "document",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
})

BASE_URL = "https://giromilano.atm.it/proxy.tpportal/api/"


def fetch_json(endpoint):
    """Effettua una richiesta GET e restituisce il JSON."""
    try:
        response = session.get(BASE_URL + endpoint)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, json.JSONDecodeError):
        return None


class Stop:
    def __init__(self, code: str, language: str = 'it'):
        if not isinstance(code, str):
            code = str(code)
        if not isinstance(language, str):
            raise ValueError("Inserire una stringa che indichi la lingua!")
        
        if len(code) <= 6:
            result = fetch_json(f"tpPortal/tpl/stops/search/{code}")
            code = result[0]['Code'] if result else code
        
        self.data = fetch_json(f"tpPortal/geodata/pois/{code}?lang={language}")
        if not self.data:
            raise ValueError(f"Nessuna fermata trovata per il codice {code}")
        
        self.code = code
        self.ccode = self.data.get('CustomerCode')
        self.language = language
        self.time = datetime.now()

    def description(self):
        print(f"Fermata {self.ccode} ({self.data['Description']}) | {self.time}")

    def lines(self):
        return [record['Line']['LineCode'] for record in self.data.get('Lines', [])]

    def position(self):
        loc = self.data.get('Location', {})
        return loc.get('Y'), loc.get('X')

    def update(self):
        self.data = fetch_json(f"tpPortal/geodata/pois/{self.code}?lang={self.language}")
        self.time = datetime.now()

    def waitmessage(self, table_format='grid'):
        title = f"{self.ccode} - {self.data['Description']}"
        headers = ['Linea', 'Descrizione', 'Attesa']
        table = [(r['Line']['LineCode'], r['Line']['LineDescription'], r['WaitMessage'])
                 for r in self.data.get('Lines', [])]
        print(colored(title, 'red'))
        print(tabulate(table, headers, tablefmt=table_format))
        print(f' - {self.time} - ')


class Line:
    def __init__(self, code: str, direction: str = '0'):
        if not isinstance(code, str):
            code = str(code)
        if direction not in ('0', '1'):
            raise ValueError("Indicare la direzione con '0' o '1'!")
        
        self.data = fetch_json(f"tpportal/tpl/journeyPatterns/{code}|{direction}?alternativeRoutesMode=false")
        if not self.data:
            raise ValueError(f"Nessuna linea trovata per il codice {code}")
        
        self.code = code
        self.direction = direction

    def description(self):
        print(f"Linea {self.data['Line']['LineDescription']}")

    def stops(self):
        return [s['Code'] for s in self.data.get('Stops', [])]

    def path(self, table_format='grid'):
        headers = ['Fermata', 'Descrizione']
        table = [[s['Code'], s['Description']] for s in self.data.get('Stops', [])]
        print(colored(self.data['Line']['LineDescription'], 'red'))
        print(tabulate(table, headers, tablefmt=table_format))

    def reverse(self):
        self.direction = str((int(self.direction) + 1) % 2)
        self.data = fetch_json(f"tpportal/tpl/journeyPatterns/{self.code}|{self.direction}?alternativeRoutesMode=false")


def distance(s1, s2):
    """Calcola la distanza tra due fermate."""
    R = 6373.0  # raggio terrestre in km
    lat1, lon1 = map(radians, s1.position())
    lat2, lon2 = map(radians, s2.position())
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    return R * 2 * atan2(sqrt(a), sqrt(1 - a))


def from_customercode_to_code(ccode):
    """Trova il codice ATM dalla CustomerCode."""
    result = fetch_json(f"tpPortal/tpl/stops/search/{ccode}")
    if result:
        print(f"{ccode} -> {result[0]['Code']}")
    else:
        print(f"{ccode} -> None")
