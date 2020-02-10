# atm
## ATM (Azienda Trasporti Milanesi) Python Library

Initial Version

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

In [9]: from atm import Line

In [10]: l = Line(73)

In [11]: l.description()<br>
Linea Bus 73 Aeroporto Linate - Duomo M1 M3

In [12]: l.stops()                                                                                                       
Out[12]: 
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
 
In [13]: l.path('html')<br>
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

In [14]: s1 = Stop(12402)                                                                                                

In [15]: s2 = Stop(12400)                                                                                                

In [16]: distance(s1,s2)                                                                                                 
Out[6]: 0.1354349258943788
