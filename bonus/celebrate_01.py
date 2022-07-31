"""
@author Python La Paz
Llevas 33 dias programando te mereces un pastel
        Felicidades por seguir en el reto
                #100diasdepython
"""
pisos = 3
relleno = 4 * "-"
sabor = "  "
decorado = "+\n"
armado = (pisos - 1) * sabor
print(f"{armado}  (*)")
print(f"{armado} __|__")
print(f"{armado}| {sabor*2}|")
for i in range(2, pisos + 1):
    p = (pisos - i) * sabor
    d = f"+-{relleno*i}{decorado}"
    s = f"| {sabor*i*2}|"
    print(f"{p}{d}{p}{s}")
print(f"+-{pisos*relleno}{decorado}")
"""
Resultado:
      (*)
     __|__
    |     |
  +---------+
  |         |
+-------------+
|             |
+-------------+
"""
