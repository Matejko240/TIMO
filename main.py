from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Funkcja celu (pamiętaj: linprog minimalizuje, więc zmieniamy znak)
c = [-800, -600, -900]  # - (zysk z herbaty I, II, III)

# Macierz ograniczeń A_ub * x <= b_ub
# Ograniczenia maszynowe:
# 1. Krojenie: 10 + x1 + 0.5x3 <= 40 -> x1 + 0.5x3 <= 30
# 2. Mieszanie: 20 + x2 + (2/3)x3 <= 40 -> x2 + (2/3)x3 <= 20
# 3. Paczkowanie: 16.67 + (1/3)x1 + (2/3)x2 + 0.5x3 <= 40 -> (1/3)x1 + (2/3)x2 + 0.5x3 <= 23.33

A = [
    [1, 0, 0.5],        # krojenie
    [0, 1, 2/3],         # mieszanie
    [1/3, 2/3, 0.5]      # paczkowanie
]

b = [
    30,       # krojenie
    20,       # mieszanie
    23.33     # paczkowanie
]

# Ograniczenia zmiennych: x1, x2, x3 >= 0
bounds = [(0, None), (0, None), (0, None)]

# Rozwiązanie
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

if result.success:
    x1, x2, x3 = result.x
    zysk = -(result.fun + (10 * 800 + 20 * 600))  # dodajemy zakontraktowane minimum
    print("Optymalna produkcja (oprócz zakontraktowanych):")
    print(f"Herbata I: {x1:.2f} ton")
    print(f"Herbata II: {x2:.2f} ton")
    print(f"Herbata III: {x3:.2f} ton")
    print(f"\nMaksymalny tygodniowy zysk: {zysk:.2f} PLN")

    # Obliczenia do wykresów
    krojenie = 10*1 + x1*1 + x3*0.5
    mieszanie = 20*1 + x2*1 + x3*(2/3)
    paczkowanie = 10*(1/3) + 20*(2/3) + x1*(1/3) + x2*(2/3) + x3*0.5

    maszyny = ['Krojenie', 'Mieszanie', 'Paczkowanie']
    czas = [krojenie, mieszanie, paczkowanie]

    # Wykres słupkowy
    plt.figure(figsize=(8, 5))
    plt.bar(maszyny, czas)
    plt.title('Wykorzystanie czasu maszyn w godzinach')
    plt.ylabel('Czas (godziny)')
    plt.grid(axis='y')
    plt.show()

    # Wykres kołowy
    plt.figure(figsize=(6, 6))
    plt.pie(czas, labels=maszyny, autopct='%1.1f%%', startangle=140)
    plt.title('Procentowe wykorzystanie czasu maszyn')
    plt.show()
else:
    print("Nie znaleziono rozwiązania.")
