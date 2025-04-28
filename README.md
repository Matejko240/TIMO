# LP1 – Optymalizacja produkcji herbaty
_(na podstawie [Ch94] – A.C. Chiang, *Podstawy ekonomii matematycznej*, PWE, Warszawa, 1994)_

## Opis zadania

Zakład produkcyjny, składający się z trzech wydziałów (krojenie, mieszanie, paczkowanie), produkuje trzy rodzaje herbaty:  
- Herbata I,  
- Herbata II,  
- Herbata III.  

Każdy wydział dysponuje 40 godzinami pracy tygodniowo. Celem jest ustalenie optymalnej ilości produkcji każdego rodzaju herbaty w taki sposób, aby **zmaksymalizować tygodniowy zysk**, przy zachowaniu ograniczeń czasowych maszyn oraz uwzględnieniu zakontraktowanej minimalnej produkcji:
- Herbata I: co najmniej 10 ton,
- Herbata II: co najmniej 20 ton.

---

## Metodologia

Problem został rozwiązany metodą **programowania liniowego** (LP), przy pomocy funkcji `linprog` z pakietu `scipy.optimize`.  
Model zawiera:

- **Zmienne decyzyjne**: ilość ton produkcji poszczególnych herbat ponad zakontraktowane minimum,
- **Funkcję celu**: maksymalizacja łącznego zysku,
- **Ograniczenia**: dostępne czasy pracy maszyn dla krojenia, mieszania i paczkowania.

Dodatkowo:
- Wyniki rozwiązania są wizualizowane na wykresach,
- Wygenerowane wyniki i wykresy są zapisywane do plików.

---

## Wymagania

- Python 3.8+
- Biblioteki:
  - `scipy`
  - `matplotlib`

Instalacja zależności:
```bash
pip install scipy matplotlib
```

---

## Uruchomienie

Aby uruchomić program:
```bash
python main.py
```

Wynik zostanie wyświetlony w konsoli, a także zapisany do pliku:
- `wyniki_lp1.txt` – opis optymalnej produkcji i zysku,
- `wykres_lp1.png` – wykres słupkowy czasu pracy maszyn,
- `wykres_kolowy_lp1.png` – wykres kołowy wykorzystania maszyn.

---

## Wyniki (przykładowe)

- Herbata I: **x₁** ton
- Herbata II: **x₂** ton
- Herbata III: **x₃** ton
- Maksymalny zysk tygodniowy: **Z** PLN

Wyniki dokładne zależą od rozwiązania optymalizacyjnego.

---

## Notka teoretyczna

**Programowanie liniowe** (LP) jest metodą optymalizacji decyzji gospodarczych, w której zarówno funkcja celu, jak i ograniczenia są liniowe.  
Celem jest maksymalizacja (lub minimalizacja) funkcji celu przy zachowaniu dostępnych zasobów.

Typowe składniki modelu LP:
- Zmienne decyzyjne,
- Funkcja celu,
- Ograniczenia zasobowe.

W przypadku tego zadania programowanie liniowe pozwala na efektywną alokację czasu pracy maszyn w celu osiągnięcia maksymalnego zysku.

---

## Interpretacja wyniku

Rozwiązanie wskazuje, jaką dodatkową ilość każdego rodzaju herbaty powinno się wyprodukować, aby uzyskać największy możliwy zysk przy pełnym wykorzystaniu dostępnych zasobów maszynowych.  
Model uwzględnia obowiązkową produkcję zakontraktowaną oraz ograniczenia technologiczne wynikające z czasu pracy wydziałów produkcyjnych.

---
