ProfileValue = 0
Vm = 0.25 # m/s
Sm = 0.2   # m
Tm = 1.0 # s
def ProfileValueCalc(ProfileValue, Vm, Sm, Tm):
    while True:
        T1 = Tm / ProfileValue
        A = Vm / T1
        Straveld = Vm * (Tm - (2 *T1)) +  0.5* A * T1**2 +  0.5* A * T1**2

        print(f"T1: {T1:.4f}[s] | A: {A:.4f}[m/s²] | S: {Straveld:.9f}[m] | P: {ProfileValue:.4f} [-]")

        if abs(Straveld - Sm) < 0.000000001:
            print("Exact")
            print(ProfileValue)
            break
        elif (Sm - 0.001) < Straveld < (Sm + 0.001):
            print("Bijna")
            ProfileValue = ProfileValue + 0.000000001
        elif Straveld < Sm:
            print("Te weinig")
            ProfileValue = ProfileValue + 0.0001
        else:
            print("Te veel")
            break

