# atm
## ATM (Azienda Trasporti Milanesi) Python Library

Initial Version

In [1]: from atm import Stop

In [2]: s = Stop(12125)

In [3]: s.description()<br>
Fermata 12125 (P.za Emilia) | 2020-02-09 22:25:47.084090

In [4]: s.waitmessage()<br>
La linea 27 (V.le Ungheria - P.zza Fontana) arriverà tra 13 min<br>
La linea 73 (Aeroporto Linate - Duomo M1 M3) arriverà tra 3 min<br>
La linea N27 (NOTTURNA Viale Ungheria - Duomo M1 M3) arriverà tra ven - sab<br>

In [5]: from atm import Line

In [6]: l = Line(73)

In [7]: l.description()<br>
Linea Bus 73 Aeroporto Linate - Duomo M1 M3

In [8]: l.path()<br>
Linea Bus 73 Aeroporto Linate - Duomo M1 M3

12926 (Aeroporto di Linate  Segrate)<br>
12921 (V.le Forlanini Via Circonvallazione  Segrate)<br>
12854 (V.le Forlanini  Aeronautica Militare)<br>
12852 (V.le Forlanini  Tangenziale Est)<br>
18119 (V.le Forlanini P.za Artigianato)<br>
12647 (Forlanini)<br>
12405 (V.le Corsica Via Lomellina)<br>
12400 (V.le Corsica Via Battistotti Sassi)<br>
12391 (V.le Campania V.le Corsica)<br>
12127 (P.za Grandi)<br>
12125 (P.za Emilia)<br>
12111 (Via Cadore C.so Ventidue Marzo)<br>
12098 (P.za S.Maria del Suffragio)<br>
12095 (P.za 5 Giornate)<br>
11820 (C.so P.ta Vittoria  Camera del Lavoro)<br>
17854 (Via Battisti)<br>
18155 (L.go Augusto)<br>
17769 (Via Larga)<br>
17855 (P.za Velasca)<br>
16929 (Duomo M1 M3)<br>
