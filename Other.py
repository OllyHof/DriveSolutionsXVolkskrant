import math as m

def PDR(pdr):
    calc = (2 * m.pi)/(pdr* 1e-3)
    print(calc)

def POWER(Speed, Force):
    print(Speed*Force)

def RMS():
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

    Vrms = (m.sqrt((1/Tt)*((V1*T1) + (V2*T2) + (V3*T3) + (V4*T4) + (V5*T5) + (V6*T6) + (V7*T7) +
    (V8*T8) + (V9*T9) + (V10*T10) + (V11*T11) + (V12*T12) + (V13*T13))))
    print(Vrms)

    Frms = (m.sqrt((1 / Tt) * ((F1 * T1) + (F2 * T2) + (F3 * T3) + (F4 * T4) + (F5 * T5) + (F6 * T6) + (F7 * T7) +
                               (F8 * T8) + (F9 * T9) + (F10 * T10) + (F11 * T11) + (F12 * T12) + (F13 * T13))))
    print(Frms)

    Tmrms = (m.sqrt((1 / Tt) * ((Tm1 * T1) + (Tm2 * T2) + (Tm3 * T3) + (Tm4 * T4) + (Tm5 * T5) + (Tm6 * T6) + (Tm7 * T7) +
                               (Tm8 * T8) + (Tm9 * T9) + (Tm10 * T10) + (Tm11 * T11) + (Tm12 * T12) + (Tm13 * T13))))
    print(Tmrms)

    Prms = Vrms * Frms
    print(Prms)