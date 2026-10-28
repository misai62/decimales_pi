#!/usr/bin/env python3
"""Calcule les décimales de pi avec la formule de Chudnovsky."""

from decimal import Decimal, getcontext
from pathlib import Path


def calculer_pi(nb_decimales: int) -> str:
    """Renvoie pi avec exactement ``nb_decimales`` chiffres après la virgule."""
    if nb_decimales < 0:
        raise ValueError("Le nombre de décimales doit être positif ou nul.")

    getcontext().prec = nb_decimales + 20

    m = 1
    l = 13_591_409
    x = 1
    k = 6
    somme = Decimal(l)

    # Chaque terme apporte environ 14 chiffres décimaux.
    for i in range(1, nb_decimales // 14 + 2):
        m = m * (k**3 - 16 * k) // i**3
        l += 545_140_134
        x *= -262_537_412_640_768_000
        somme += Decimal(m * l) / x
        k += 12

    pi = Decimal(426880) * Decimal(10005).sqrt() / somme
    return format(pi, f".{nb_decimales}f")


def main() -> None:
    nb_decimales = 10_000
    fichier = Path(__file__).with_name("pi_10000_decimales.txt")
    pi = calculer_pi(nb_decimales)
    partie_entiere, decimales = pi.split(".")
    lignes = [f"{partie_entiere}.{decimales[:50]}"]
    lignes.extend(
        decimales[i : i + 50] for i in range(50, len(decimales), 50)
    )
    fichier.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"{nb_decimales} décimales de pi enregistrées dans {fichier.name}")


if __name__ == "__main__":
    main()
