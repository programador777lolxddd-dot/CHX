#!/usr/bin/env python3
"""
Ejemplo práctico de uso de Chrotrixurum (chx).

Escenario:
  - Tenemos títulos de artículos "sucios" y queremos normalizarlos.
  - Tenemos una lista de números y queremos filtrar primos.
  - Guardamos un reporte en disco.
  - Consultamos a los astros y firmamos con un sigilo.

Ejecuta:
    $ python ejemplo_chx.py
"""

from datetime import date, timedelta
from pathlib import Path

import chrotrixurum as chx


# ─────────────────────────────────────────────────────────────
# 1) Normalizar títulos de artículos
# ─────────────────────────────────────────────────────────────
TITULOS = [
    "Hola Mundo Ñandú: Introducción",
    "Cómo hacer Café en 5 Minutos",
    "Python Avanzado — Decoradores & Generadores",
    "Aprende  Álgebra   Lineal ¡Ya!",
]

print("=" * 60)
print("📝 TÍTULOS NORMALIZADOS")
print("=" * 60)

for titulo in TITULOS:
    slug = chx.slugify(titulo)
    snake = chx.snake_case(slug.replace("-", " "))
    corto = chx.truncate(titulo, 30)
    print(f"  original : {titulo}")
    print(f"  slug     : {slug}")
    print(f"  snake    : {snake}")
    print(f"  corto    : {corto}\n")


# ─────────────────────────────────────────────────────────────
# 2) Analizar una lista de números
# ─────────────────────────────────────────────────────────────
NUMEROS = [1, 2, 3, 4, 5, 7, 11, 13, 17, 20, 23, 29, 97, 100]

print("=" * 60)
print("🔢 ANÁLISIS NUMÉRICO")
print("=" * 60)

primos = [n for n in NUMEROS if chx.is_prime(n)]
print(f"  números   : {NUMEROS}")
print(f"  primos    : {primos}")
print(f"  proporción: {chx.percent(len(primos), len(NUMEROS))}")

# Interpolación: precio entre 100 y 500 al 35 %
precio = chx.lerp(100, 500, 0.35)
precio_limitado = chx.clamp(precio, 150, 400)
print(f"  lerp(100,500,0.35)         = {precio:.2f}")
print(f"  clamp(..., 150, 400)       = {precio_limitado:.2f}")

primeros_fib = list(chx.fibonacci(10))
print(f"  primeros 10 Fibonacci      = {primeros_fib}\n")


# ─────────────────────────────────────────────────────────────
# 3) Fechas legibles
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("📅 FECHAS")
print("=" * 60)

hoy = date.today()
ayer = hoy - timedelta(days=1)
en_una_semana = hoy + timedelta(days=7)

print(f"  hoy                 : {hoy}")
print(f"  days_between        : {chx.days_between(ayer, en_una_semana)} días entre ayer y +7d")
print(f"  humanize(-3h)       : {chx.humanize_delta(timedelta(hours=-3))}")
print(f"  humanize(+2d)       : {chx.humanize_delta(timedelta(days=2))}")
print(f"  ¿hoy es finde?      : {chx.is_weekend(hoy)}\n")


# ─────────────────────────────────────────────────────────────
# 4) Palíndromos: ¿cuáles merecen karma elevado?
# ─────────────────────────────────────────────────────────────
FRASES = [
    "Anita lava la tina",
    "Dábale arroz a la zorra el abad",
    "Chrotrixurum eterno",
    "Yo hago yoga hoy",
]

print("=" * 60)
print("✨ KARMA PALINDRÓMICO")
print("=" * 60)

for frase in FRASES:
    info = chx.palindrome_magic(frase)
    marca = "✅" if info["es_palindromo"] else "❌"
    print(f"  {marca} {frase!r}")
    print(f"     karma={info['karma']}  veredicto: {info['veredicto']}\n")


# ─────────────────────────────────────────────────────────────
# 5) Consultas a los astros (deterministas)
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("🔮 CONSULTAS A LOS ASTROS")
print("=" * 60)

preguntas = [
    "¿Aprobaré el examen?",
    "¿Debo refactorizar hoy?",
    "¿El bug está en producción?",
]

for p in preguntas:
    print(f"  {p}")
    print(f"    → {chx.divine(p, seed=42)}\n")


# ─────────────────────────────────────────────────────────────
# 6) Generar un reporte en disco
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("💾 GENERANDO REPORTE")
print("=" * 60)

reporte_dir = chx.ensure_dir("salida_chx")
reporte_path = reporte_dir / "reporte.txt"

with reporte_path.open("w", encoding="utf-8") as fh:
    fh.write(f"Reporte Chrotrixurum v{chx.__version__}\n")
    fh.write("=" * 40 + "\n\n")
    fh.write("Slugs generados:\n")
    for t in TITULOS:
        fh.write(f"  - {chx.slugify(t)}\n")
    fh.write("\nPrimos encontrados:\n")
    fh.write(f"  {primos}\n")
    fh.write("\nSigilo del día:\n")
    fh.write(f"  {chx.sigil(str(hoy))}\n")

tam = reporte_path.stat().st_size
print(f"  📄 Guardado en : {reporte_path}")
print(f"  📦 Tamaño      : {chx.human_size(tam)}\n")

# Leerlo línea a línea (streaming) y mostrar solo las 5 primeras
print("  Primeras 5 líneas:")
for i, linea in enumerate(chx.read_lines_safe(reporte_path)):
    if i >= 5:
        break
    print(f"    {linea}")

print("\n✅ Demo completada. Revisa la carpeta 'salida_chx/'.")