# atm
## ATM (Azienda Trasporti Milanesi) Python Library
This Library is intended for educational purpose.

- Free to use.
- No API Key needed.
- Daily useful.
- Functionality tested in real time.

Initial Version - 0.1
---------------------

In [1]: from atm import Stop

In [2]: s = Stop(11161)

In [3]: s.description()<br>
Fermata 11161 (Alzaia Nav. Pavese, 60) | 2020-02-10 23:04:32.617598

In [4]: s.waitmessage('grid')<br>
<pre>
11161 - Alzaia Nav. Pavese, 60
+---------+------------------------------+----------+
|   Linea | Descrizione                  | Attesa   |
+=========+==============================+==========+
|      59 | P.ta Lodovica - Famagosta M2 | no serv. |
+---------+------------------------------+----------+
|      71 | Famagosta M2 - Romolo M2     | 5 min    |
+---------+------------------------------+----------+
 - 2020-02-10 23:04:32.617598 - 
</pre>

In [5]: s.position()                                                                                                   
Out[5]: (9.176054951924698, 45.44497959284472)

In [6]: s.lines()                                                                                                      
Out[6]: ['59', '71']

In [7]: s.update()                                                                                                     

In [8]: s.waitmessage('html')   
<pre>
11161 - Alzaia Nav. Pavese, 60
<table>
<thead>
<tr><th style="text-align: right;">  Linea</th><th>Descrizione                 </th><th>Attesa  </th></tr>
</thead>
<tbody>
<tr><td style="text-align: right;">     59</td><td>P.ta Lodovica - Famagosta M2</td><td>no serv.</td></tr>
<tr><td style="text-align: right;">     71</td><td>Famagosta M2 - Romolo M2    </td><td>14 min  </td></tr>
</tbody>
</table>
 - 2020-02-10 23:16:08.537093 - 
</pre>

In [9]: from atm import distance

In [10]: s1 = Stop(12402)                                                                                                

In [11]: s2 = Stop(12400)                                                                                                

In [12]: distance(s1,s2)                                                                                                 
Out[12]: 0.1354349258943788

In [13]: from atm import Line

In [14]: l = Line(73)

In [15]: l.description()<br>
Linea Bus 73 Aeroporto Linate - Duomo M1 M3

In [16]: l.stops()                                                                                                       
Out[16]: 
['12926',
 '12921',
 '12854',
 '12852',
 '18119',
 '12647',
 '12405',
 '12400',
 '12391',
 '12127',
 '12125',
 '12111',
 '12098',
 '12095',
 '11820',
 '17854',
 '18155',
 '17769',
 '17855',
 '16929']
 
In [17]: l.path('html')<br>
<pre>
Bus 73 Aeroporto Linate - Duomo M1 M3
<table>
<thead>
<tr><th style="text-align: right;">  Fermata</th><th>Descrizione                                 </th></tr>
</thead>
<tbody>
<tr><td style="text-align: right;">    12926</td><td>Aeroporto di Linate  Segrate                </td></tr>
<tr><td style="text-align: right;">    12921</td><td>V.le Forlanini Via Circonvallazione  Segrate</td></tr>
<tr><td style="text-align: right;">    12854</td><td>V.le Forlanini  Aeronautica Militare        </td></tr>
<tr><td style="text-align: right;">    12852</td><td>V.le Forlanini  Tangenziale Est             </td></tr>
<tr><td style="text-align: right;">    18119</td><td>V.le Forlanini P.za Artigianato             </td></tr>
<tr><td style="text-align: right;">    12647</td><td>Forlanini                                   </td></tr>
<tr><td style="text-align: right;">    12405</td><td>V.le Corsica Via Lomellina                  </td></tr>
<tr><td style="text-align: right;">    12400</td><td>V.le Corsica Via Battistotti Sassi          </td></tr>
<tr><td style="text-align: right;">    12391</td><td>V.le Campania V.le Corsica                  </td></tr>
<tr><td style="text-align: right;">    12127</td><td>P.za Grandi                                 </td></tr>
<tr><td style="text-align: right;">    12125</td><td>P.za Emilia                                 </td></tr>
<tr><td style="text-align: right;">    12111</td><td>Via Cadore C.so Ventidue Marzo              </td></tr>
<tr><td style="text-align: right;">    12098</td><td>P.za S.Maria del Suffragio                  </td></tr>
<tr><td style="text-align: right;">    12095</td><td>P.za 5 Giornate                             </td></tr>
<tr><td style="text-align: right;">    11820</td><td>C.so P.ta Vittoria  Camera del Lavoro       </td></tr>
<tr><td style="text-align: right;">    17854</td><td>Via Battisti                                </td></tr>
<tr><td style="text-align: right;">    18155</td><td>L.go Augusto                                </td></tr>
<tr><td style="text-align: right;">    17769</td><td>Via Larga                                   </td></tr>
<tr><td style="text-align: right;">    17855</td><td>P.za Velasca                                </td></tr>
<tr><td style="text-align: right;">    16929</td><td>Duomo M1 M3                                 </td></tr>
</tbody>
</table>
</pre>

In [18]: l.reverse()

In [19]: l.path()
<pre>
Bus 73 Duomo M1 M3 - Aeroporto Linate
+-----------+----------------------------------------------+
|   Fermata | Descrizione                                  |
+===========+==============================================+
|     16929 | Duomo M1 M3                                  |
+-----------+----------------------------------------------+
|     11794 | Via Larga                                    |
+-----------+----------------------------------------------+
|     11798 | L.go Augusto                                 |
+-----------+----------------------------------------------+
|     11816 | Palazzo di Giustizia                         |
+-----------+----------------------------------------------+
|     11823 | C.so P.ta Vittoria  Camera del Lavoro        |
+-----------+----------------------------------------------+
|     12094 | P.za 5 Giornate                              |
+-----------+----------------------------------------------+
|     12099 | P.za S.Maria del Suffragio                   |
+-----------+----------------------------------------------+
|     12108 | Via Cadore C.so Ventidue Marzo               |
+-----------+----------------------------------------------+
|     12126 | P.za Emilia                                  |
+-----------+----------------------------------------------+
|     12390 | P.za Grandi                                  |
+-----------+----------------------------------------------+
|     12392 | V.le Campania V.le Corsica                   |
+-----------+----------------------------------------------+
|     12402 | V.le Corsica Via Lomellina                   |
+-----------+----------------------------------------------+
|     12407 | V.le Corsica Via Negroli                     |
+-----------+----------------------------------------------+
|     12646 | Forlanini                                    |
+-----------+----------------------------------------------+
|     12662 | V.le Forlanini P.za Artigianato              |
+-----------+----------------------------------------------+
|     12851 | V.le Forlanini  Tangenziale Est              |
+-----------+----------------------------------------------+
|     12853 | V.le Forlanini  Aeronautica Militare         |
+-----------+----------------------------------------------+
|     12922 | V.le Forlanini Via Circonvallazione  Segrate |
+-----------+----------------------------------------------+
|     12926 | Aeroporto di Linate  Segrate                 |
+-----------+----------------------------------------------+
</pre>
