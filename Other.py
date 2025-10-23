import math as m
from idlelib.zoomheight import WmInfoGatheringError
from os import supports_effective_ids


def PDR(pdr):
    calc = (2 * m.pi)/(pdr* 1e-3)
    print(calc)

def POWER(Speed, Force):
    print(Speed*Force)

def RMS_A():
    Tt = 2.6
    T1 = 0.055  #Begin trapezium 1
    T2 = 0.245 #Eind Versnelling trapezium 1
    T3 = 0.555 #Begin Vertaging trapezium 1
    T4 = 0.245 #Begin Piek 1, Eind Trapezium 1
    T5 = 0.08  #Midden Piek 1
    T6 = 0.08  #Eind Piek 1
    T7 = 0.09  #Begin Piek 2
    T8 = 0.08  #Midden Piek 2
    T9 = 0.08  #Eind Piek 2
    T10 = 0.09 #Begin trapezium 2
    T11 = 0.20 #Eind Versnelling trapezium 1
    T12 = 0.6  #Begin vertraging trapezium 1
    T13 = 0.2  #Eind

    V1 = pow(0, 2)
    V2 = pow(0.5 * 0.25, 2)
    V3 = pow(0.25, 2)
    V4 = pow(0.5 * 0.25, 2)
    V5 = pow(0.5 * 0.15, 2)
    V6 = pow(0.5 * 0.15, 2)
    V7 = pow(0.0, 2)
    V8 = pow(0.5 * 0.15 * -1, 2)
    V9 = pow(0.5 * 0.15 * -1, 2)
    V10 = pow(0, 2)
    V11 = pow(0.5 * 0.25 * -1, 2)
    V12 = pow(0.25 * -1, 2)
    V13 = pow(0.5 * 0.25 * -1, 2)

    F1 = pow(313.92, 2)
    F2 = pow(436.56, 2)
    F3 = pow(313.92, 2)
    F4 = pow(371.28, 2)
    F5 = pow(463.92, 2)
    F6 = pow(343.92, 2)
    F7 = pow(313.92, 2)
    F8 = pow(463.92, 2)
    F9 = pow(343.92, 2)
    F10 = pow(313.92, 2)
    F11 = pow(443.92, 2)
    F12 = pow(313.6, 2)
    F13 = pow(313.92, 2)

    Tm1 = pow(0.0573, 2)
    Tm2 = pow(0.0973, 2)
    Tm3 = pow(0.0573, 2)
    Tm4 = pow(0.0173, 2)
    Tm5 = pow(0.1308, 2)
    Tm6 = pow(-0.0163, 2)
    Tm7 = pow(0.0573, 2)
    Tm8 = pow(-0.0163, 2)
    Tm9 = pow(0.1308, 2)
    Tm10 = pow(0.0573, 2)
    Tm11 = pow(0.0083, 2)
    Tm12 = pow(0.0573, 2)
    Tm13 = pow(0.1063, 2)

    Kt = 0.73

    Kt = 0.73

    I1 = 0.0573 / Kt
    I2 = 0.0973 / Kt
    I3 = 0.0573 / Kt
    I4 = 0.0173 / Kt
    I5 = 0.1308 / Kt
    I6 = -0.0163 / Kt
    I7 = 0.0573 / Kt
    I8 = -0.0163 / Kt
    I9 = 0.1308 / Kt
    I10 = 0.0573 / Kt
    I11 = 0.0083 / Kt
    I12 = 0.0573 / Kt
    I13 = 0.1063 / Kt

    print("I1:", I1)
    print("I2:", I2)
    print("I3:", I3)
    print("I4:", I4)
    print("I5:", I5)
    print("I6:", I6)
    print("I7:", I7)
    print("I8:", I8)
    print("I9:", I9)
    print("I10:", I10)
    print("I11:", I11)
    print("I12:", I12)
    print("I13:", I13)

    I1 = pow(0.0573 / Kt, 2)
    I2 = pow(0.0973 / Kt, 2)
    I3 = pow(0.0573 / Kt, 2)
    I4 = pow(0.0173 / Kt, 2)
    I5 = pow(0.1308 / Kt, 2)
    I6 = pow(-0.0163 / Kt, 2)
    I7 = pow(0.0573 / Kt, 2)
    I8 = pow(-0.0163 / Kt, 2)
    I9 = pow(0.1308 / Kt, 2)
    I10 = pow(0.0573 / Kt, 2)
    I11 = pow(0.0083 / Kt, 2)
    I12 = pow(0.0573 / Kt, 2)
    I13 = pow(0.1063 / Kt, 2)

    Vrms = (m.sqrt((1/Tt)*((V1*T1) + (V2*T2) + (V3*T3) + (V4*T4) + (V5*T5) + (V6*T6) + (V7*T7) +
    (V8*T8) + (V9*T9) + (V10*T10) + (V11*T11) + (V12*T12) + (V13*T13))))
    print("Vrms: ", Vrms)

    Frms = (m.sqrt((1 / Tt) * ((F1 * T1) + (F2 * T2) + (F3 * T3) + (F4 * T4) + (F5 * T5) + (F6 * T6) + (F7 * T7) +
                               (F8 * T8) + (F9 * T9) + (F10 * T10) + (F11 * T11) + (F12 * T12) + (F13 * T13))))
    print("Frms: ", Frms)

    Tmrms = (m.sqrt((1 / Tt) * ((Tm1 * T1) + (Tm2 * T2) + (Tm3 * T3) + (Tm4 * T4) + (Tm5 * T5) + (Tm6 * T6) + (Tm7 * T7) +
                               (Tm8 * T8) + (Tm9 * T9) + (Tm10 * T10) + (Tm11 * T11) + (Tm12 * T12) + (Tm13 * T13))))
    print("Tmrms: ", Tmrms)

    Irms = (
        m.sqrt((1 / Tt) * ((I1 * T1) + (I2 * T2) + (I3 * T3) + (I4 * T4) + (I5 * T5) + (I6 * T6) + (I7 * T7) +
                           (I8 * T8) + (I9 * T9) + (I10 * T10) + (I11 * T11) + (I12 * T12) + (I13 * T13))))
    print("Irms: ",Irms)

    Prms = Vrms * Frms
    print("Prms: ", Prms)

def RMS_B():
    
        Jl = 0.190474
        Wl = 95
        Cosphi = 0.87
        Jm = 0.195
        I0 = 1.64

        
        Tt = 2.6
        T1 = 1.1875  # Begin trapezium 1
        T2 = 0.225  # Eind Versnelling trapezium 1
        T3 = 1.1875  # Begin Vertaging trapezium 1

        W1 = pow(0.5*(Wl*I0), 2)
        W2 = pow((Wl*I0), 2)
        W3 = pow(0.5*(Wl*I0), 2)
        A = (80*I0)
        TM = ((0.19/(I0**2))*(Wl*I0))+(18/I0)+((Jl+Jm)*A)
        #TM = ((D*/(I0^2))*(Wl*I0))+(Fw/I0)+((Jl+Jm)*Am)
        print("Tm: ",TM)

        TM1 = pow(TM, 2)
        A = (0 * I0)
        TM = ((0.19 / (I0 ** 2)) * (Wl * I0)) + (18 / I0) + ((Jl + Jm) * A)
        TM2 = pow(TM, 2)
        A = (80 * I0)
        TM = ((0.19 / (I0 ** 2)) * (Wl * I0)) + (18 / I0) + ((Jl + Jm) * A)
        TM3 = pow(TM, 2)

        PM = TM*(Wl*I0)
        print("PM: ", PM)
        I1 = (0.5*(Wl*I0)*TM)/(m.sqrt(3)*400*Cosphi)
        I3 = (0.5 * (Wl * I0) * TM) / (m.sqrt(3) * 400 * Cosphi)
        A = (0 * I0)
        TM = ((0.19 / (I0 ** 2)) * (Wl * I0)) + (18 / I0) + ((Jl + Jm) * A)
        I2 = ((Wl*I0)*TM)/(m.sqrt(3)*400*Cosphi)
        #I = (Wm*Tm)/(Sqrt(3)*Ueff*CosPhi)

        print("I1:", I1)
        print("I2:", I2)
        print("I3:", I3)


        I1 = pow(I1, 2)
        I2 = pow(I2, 2)
        I3 = pow(I3, 2)

        Wrms = (m.sqrt(
            (1 / Tt) * ((W1 * T1) + (W2 * T2) + (W3 * T3))))
        print("Wrms: ", Wrms)

        TMrms = (m.sqrt(
            (1 / Tt) * ((TM1 * T1) + (TM2 * T2) + (TM3 * T3))))
        print("TMrms: ", TMrms)

        Irms = (
            m.sqrt((1 / Tt) * ((I1 * T1) + (I2 * T2) + (I3 * T3))))
        print("Irms: ", Irms)

        Prms = Wrms * TMrms
        print("Prms: ", Prms)

        Nrms = Wrms * ((2*m.pi/60)**-1)
        print("Nrms: ", Nrms)