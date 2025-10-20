import math

Yes_Answers = ["Y", "y", "Yes", "yes", "J", "j", "Ja", "ja"]

def ask(question):
    """Stelt een ja/nee vraag en retourneert True of False."""
    answer = input(question + " ").strip()
    return answer in Yes_Answers

def ask_val(question):
    """Vraagt om een numerieke waarde met foutafhandeling."""
    while True:
        try:
            return float(input(question))
        except ValueError:
            print("⚠ Ongeldige invoer, geef een numerieke waarde.")

def vraag_overbrenging(num, M_Cur, J_Cur, laatste=False):
    print(f"\n--- Overbrenging {num} ---")

    # --- Massatraagheden ---
    J = 0.0
    J += J_Cur
    if ask("Heb je Massatraagheden voor deze overbrenging? [Y/N]:"):
        while True:
            J += ask_val("Voer Massatraagheid in [kgm^2]: ")
            print(f"Huidige massatraagheden: {J:.6f} kgm^2")
            if ask("Waren dit alle Massatraagheden voor deze overbrenging? [Y/N]:"):
                break

    # --- Massas ---
    M = 0.0
    M += M_Cur
    if ask("Heb je Massas voor deze overbrenging? [Y/N]:"):
        while True:
            M += ask_val("Voer Massa in [kg]: ")
            print(f"Huidige massa's: {M:.6f} kg")
            if ask("Waren dit alle Massas voor deze overbrenging? [Y/N]:"):
                break

    # --- Overbrengingsverhouding ---
    if not laatste:
        I = ask_val("Voer de overbrengingsverhouding in: ")
        if I != 1 and I > 0:
            I2 = I * I
            M /= I2
            J /= I2

        print(f"\nOverbrenging {num} resultaten:")
        print(f"  Gecorrigeerde massa: {M:.6f} kg")
        print(f"  Gecorrigeerde massatraagheid: {J:.6f} kgm^2\n")

    return M, J

def main():
    print("Wat wil je berekenen?")
    print("1. Inertia Match")
    print("2. J* (totaal van overbrengingen)")
    print("3. Ideale I₀")

    Keuze = input("Maak een keuze (1/2/3): ").strip()

    # --- Optie 1: Inertia Match ---
    if Keuze == "1":
        J_star = ask_val("Wat is je J* in [kgm^2]?: ")
        J_motor = ask_val("Wat is je J_motor in [kgm^2]?: ")
        print(f"\nInertia Match = {J_star / J_motor:.3f}")

    # --- Optie 2: J* berekening ---
    elif Keuze == "2":
        ItotCount = int(ask_val("Hoeveel overbrengingen zijn er? (min 1): "))
        M_total, J_total = 0.0, 0.0
        M, J = 0.0, 0.0
        for n in range(ItotCount, 0, -1):
            M, J = vraag_overbrenging(n, M, J, laatste=(n == 0))
            M_total = M
            J_total = J

        print("\n--- TOTAALRESULTAAT ---")
        if ask("Is een van je overbrengingen niet dimensieloos? [Y/N]:"):
            J_total += M_total
            print(f"Totaal gecorrigeerde massatraagheid (J*): {J_total:.6f} kgm^2")
        else:
            print(f"Totaal gecorrigeerde massa: {M_total:.6f} kg")
            print(f"Totaal gecorrigeerde massatraagheid (J*): {J_total:.6f} kgm^2")

    # --- Optie 3: Ideale I₀ berekening ---
    elif Keuze == "3":
        if ask("Weet je je J*? [Y/N]:"):
            J_total = ask_val("Wat is je J* in [kgm^2]?: ")
        else:
            ItotCount = int(ask_val("Hoeveel overbrengingen zijn er? (min 1): "))
            M_total, J_total = 0.0, 0.0
            M, J = 0.0, 0.0
            for n in range(ItotCount, 0, -1):
                M, J = vraag_overbrenging(n, M, J, laatste=(n == 1))
                M_total = M
                J_total = J
            J_total += M_total  # toevoeging bij niet-dimensieloze delen

        J_motor = ask_val("Wat is je J_motor in [kgm^2]?: ")
        I_Ideal = math.sqrt(J_total / J_motor)
        print(f"\nIdeale overbrengingsverhouding (I₀) = {I_Ideal:.3f}")

    else:
        print("⚠ Ongeldige keuze. Start het programma opnieuw.")

# --- Hoofdprogramma ---
