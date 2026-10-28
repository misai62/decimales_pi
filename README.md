# Calcul de 10 000 décimales de π

Ce projet contient un script Python qui calcule π avec **10 000 chiffres après la virgule** et enregistre le résultat dans un fichier texte.

## Contenu du projet

- `calcul_pi.py` : script de calcul utilisant la formule de Chudnovsky.
- `pi_10000_decimales.txt` : résultat du calcul, avec π suivi de ses 10 000 décimales.

## Prérequis

- Python 3 (aucune bibliothèque externe n’est nécessaire).

Le script utilise uniquement des modules fournis avec Python : `decimal` pour les calculs à haute précision et `pathlib` pour écrire le résultat.

## Utilisation

Depuis le répertoire du projet, exécutez :

```bash
python3 calcul_pi.py
```

Le script crée ou remplace `pi_10000_decimales.txt` dans le même répertoire que le script et affiche un message de confirmation. Le fichier contient une ligne commençant par :

```text
3.14159265358979323846264338327950288419716939937510...
```

## Méthode de calcul

Le calcul repose sur la formule de **Chudnovsky**, une série rapidement convergente pour π. Chaque terme apporte environ 14 chiffres décimaux. Le script effectue le calcul avec le module `decimal`, en réservant une précision supplémentaire pour limiter les effets des arrondis intermédiaires, puis formate le résultat avec exactement 10 000 chiffres après le point décimal.

## Modifier le nombre de décimales

Le nombre de décimales est défini par la variable `nb_decimales` dans la fonction `main` de `calcul_pi.py` :

```python
nb_decimales = 10_000
```

Vous pouvez modifier cette valeur, puis relancer le script. Le nom du fichier de sortie reste `pi_10000_decimales.txt` ; adaptez-le dans le script si vous souhaitez distinguer plusieurs résultats.
