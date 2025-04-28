from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Funkcja celu (pamiętaj: linprog minimalizuje, więc zmieniamy znak)
c = [-800, -600, -900]  # - (zysk z herbaty I, II, III)

# Macierz ograniczeń A_ub * x <= b_ub
# Ograniczenia maszynowe:
# 1. Krojenie: 10 + x1 + 0.5x3 <= 40 -> x1 + 0.5x3 <= 30
# 2. Mieszanie: 20 + x2 + (2/3)x3 <= 40 -> x2 + (2/3)x3 <= 20
# 3. Paczkowanie: 16.67 + (1/3)x1 + (2/3)x2 + 0.5x3 <= 40 -> (1/3)x1 + (2/3)x2 + 0.5x3 <= 23.33

A_ub = [
    [1, 0, 0.5],        # krojenie
    [0, 1, 2/3],         # mieszanie
    [1/3, 2/3, 0.5]      # paczkowanie
]

b_ub = [
    30,       # krojenie
    20,       # mieszanie
    23.33     # paczkowanie
]

# Ograniczenia zmiennych: x1, x2, x3 >= 0
bounds = [(0, None), (0, None), (0, None)]

def solve_lp():
    """Rozwiązuje problem LP1"""
    try:
        result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
        if result.success:
            return result.x, -(result.fun + (10 * 800 + 20 * 600))
        else:
            raise ValueError("Problem optymalizacyjny nie został rozwiązany.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return None, None

def plot_results(times, save_path="wykres_lp1.png"):
    """Rysuje i zapisuje wykresy"""
    machines = ['Krojenie', 'Mieszanie', 'Paczkowanie']

    # Wykres słupkowy
    plt.figure(figsize=(8, 5))
    bars = plt.bar(machines, times, color=['skyblue', 'lightgreen', 'salmon'])
    plt.title('Wykorzystanie czasu maszyn w godzinach')
    plt.ylabel('Czas (godziny)')
    plt.grid(axis='y')
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}', ha='center', va='bottom')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.show()

    # Wykres kołowy
    plt.figure(figsize=(6, 6))
    plt.pie(times, labels=machines, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'salmon'])
    plt.title('Procentowe wykorzystanie czasu maszyn')
    plt.tight_layout()
    plt.savefig("wykres_kolowy_lp1.png")
    plt.show()

def save_results(x, zysk, save_path="wyniki_lp1.txt"):
    """Zapisuje wyniki do pliku"""
    with open(save_path, "w") as f:
        f.write("Optymalna produkcja (oprocz zakontraktowanych):\n")
        f.write(f"Herbata I: {x[0]:.2f} ton\n")
        f.write(f"Herbata II: {x[1]:.2f} ton\n")
        f.write(f"Herbata III: {x[2]:.2f} ton\n")
        f.write(f"\nMaksymalny tygodniowy zysk: {zysk:.2f} PLN\n")

if __name__ == "__main__":
    x, zysk = solve_lp()
    if x is not None:
        print("Optymalna produkcja (oprócz zakontraktowanych):")
        print(f"Herbata I: {x[0]:.2f} ton")
        print(f"Herbata II: {x[1]:.2f} ton")
        print(f"Herbata III: {x[2]:.2f} ton")
        print(f"\nMaksymalny tygodniowy zysk: {zysk:.2f} PLN")

        # Obliczenia zużycia czasu
        krojenie_time = 10*1 + x[0]*1 + x[2]*0.5
        mieszanie_time = 20*1 + x[1]*1 + x[2]*(2/3)
        paczkowanie_time = 10*(1/3) + 20*(2/3) + x[0]*(1/3) + x[1]*(2/3) + x[2]*0.5
        times = [krojenie_time, mieszanie_time, paczkowanie_time]

        # Rysowanie i zapisywanie wykresów
        plot_results(times)

        # Zapisywanie wyników do pliku
        save_results(x, zysk)
    else:
        print("Rozwiązanie nie zostało znalezione.")
