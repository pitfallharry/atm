# atm
## ATM (Azienda Trasporti Milanesi) Python Library

Initial Version

In [1]: from atm import Stop                                                                                            

In [2]: s = Stop(12125)                                                                                                 

In [3]: s.description()                                                                                                 
Fermata 12125 (P.za Emilia) | 2020-02-09 22:25:47.084090
-

In [4]: s.waitmessage()                                                                                                 
La linea 27 (V.le Ungheria - P.zza Fontana) arriverà tra 13 min
La linea 73 (Aeroporto Linate - Duomo M1 M3) arriverà tra 3 min
La linea N27 (NOTTURNA Viale Ungheria - Duomo M1 M3) arriverà tra ven - sab

In [5]: from atm import Line                                                                                            

In [6]: l = Line(73)                                                                                                    

In [7]: l.description()                                                                                                 
Linea Bus 73 Aeroporto Linate - Duomo M1 M3
-

In [8]: l.path()                                                                                                        
Linea Bus 73 Aeroporto Linate - Duomo M1 M3
-
12926 (Aeroporto di Linate  Segrate )
12921 (V.le Forlanini Via Circonvallazione  Segrate )
12854 (V.le Forlanini  Aeronautica Militare )
12852 (V.le Forlanini  Tangenziale Est )
18119 (V.le Forlanini P.za Artigianato)
12647 (Forlanini)
12405 (V.le Corsica Via Lomellina)
12400 (V.le Corsica Via Battistotti Sassi)
12391 (V.le Campania V.le Corsica)
12127 (P.za Grandi)
12125 (P.za Emilia)
12111 (Via Cadore C.so Ventidue Marzo)
12098 (P.za S.Maria del Suffragio)
12095 (P.za 5 Giornate)
11820 (C.so P.ta Vittoria  Camera del Lavoro )
17854 (Via Battisti)
18155 (L.go Augusto)
17769 (Via Larga)
17855 (P.za Velasca)
16929 (Duomo M1 M3)
