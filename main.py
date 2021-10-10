import math
import cmath

#I = V / R
def CTVR(Voltage, Resistance):
     Current = Voltage / Resistance
     return Current

#I = P / V
def CTPV(Power, Voltage):
    Current = Power / Voltage
    return Current

#I = √P / R
def CTPR(Power, Resistance):
    Current = math.sqrt(Power) / Resistance
    return Current

#I = P / (V x Cosθ)
def CTVR_SinglePhaseAC(Power, Voltage, Theta):
    Current = Power / (Voltage * math.cos(Theta))
    return Current

#I = V / Z
def CTVZ_SinglePhaseAC(Voltage, Impedance):
    Current = Voltage / Impedance
    return Current

#I = P / √3 x V x Cosθ
def CTPV_ThreePhaseAC(Power, Voltage, Theta):
    Current = Power / math.sqrt(3) * Voltage * math.cos(Theta)
    return Current

#V = I x R
def VTCR(Current, Resistance):
    Voltage = Current * Resistance
    return Voltage

#V = P / I
def VTPC(Power, Current):
    Voltage = Power / Current
    return Voltage

#V = √ (P x R)
def VTPR(Power, Resistance):
    Voltage = math.sqrt(Power * Resistance)
    return Voltage

#V = P/(I x Cosθ)
def VTPC_SinglePhaseAC(Power, Current, Theta):
    Voltage = Power / (Current * math.cos(Theta))
    return Voltage

#V = I x Z
def VTCZ_SinglePhaseAC(Current, Impedance):
    Voltage = Current * Impedance
    return Voltage

#Vl = √3 Vph or Vl = √3 Eph
def VStar_ThreePhaseAC(VoltagePH):
    VoltageL = math.sqrt(3) * VoltagePH
    return VoltageL

#Vl
def VDelta_ThreePhaseAC(VoltagePH):
    return VoltagePH

#P = V x I
def PTVC(Voltage, Current):
    Power = Voltage * Current
    return Power

#P =  I^2 x R
def PTCR(Current, Resistance):
    Power = math.pow(Current, 2) * Resistance
    return Power

#P = V^2/R
def PTVR(Voltage, Resistance):
    Power = math.pow(Voltage, 2) * Resistance
    return Power

#P = V x I x Cosθ
def PTVC_SinglePhaseAC(Voltage, Current, Theta):
    Power = Voltage * Current * math.cos(Theta)
    return Power

#P = I^2 x R x Cosθ
def PTCR_SinglePhaseAC(Current, Resistance, Theta):
    Power = math.pow(Current, 2) * Resistance * math.cos(Theta)
    return Power

#P = (V^2 / R) x Cosθ
def PTVR_SinglePhaseAC(Voltage, Resistance, Theta):
    Power = math.pow(Voltage, 2) / Resistance * math.cos(Theta)
    return Power

#P = √3 x Vl x Il x Cosθ
def PTVC_ThreePhaseAC_Line(Voltage, Current, Theta):
    Power = math.sqrt(3) * Voltage * Current * math.cos(Theta)
    return Power

#P = 3 x Vp x Ip x Cosθ
def PTVC_ThreePhase(Voltage, Current, Theta):
    Power = 3 * Voltage * Current * math.cos(Theta)
    return Power

#R = V / I
def RTVC(Voltage, Current):
    Resistance = Voltage / Current
    return Resistance

#R = P / I^2
def RTPC(Power, Current):
    Resistance = Power / math.pow(Current, 2)
    return Resistance

#R = V^2 / P
def RTVP(Voltage, Power):
    Resistance = math.pow(Voltage, 2) / Power
    return Resistance

#Z^2 = R^2 + X^2
def ZTRR_Squared(Resistance, Reactance):
    Impedance2 = math.pow(Resistance, 2) * math.pow(Reactance, 2)
    return Impedance2

#Z = √(R^2 + Xl^2) or #Z = √(R^2 + Xc^2)
def ZTRR(Resistance, Reactance):
    Impedance = math.sqrt(math.pow(Resistance, 2) + math.pow(Reactance,2))
    return Impedance

#Z = √(R^2 + (Xl - Xc)^2)
def ZTRR_CapacitiveInductive(Resistance, ReactanceL, ReactanceC):
    Impedance = math.sqrt(math.pow(Resistance, 2) + math.pow((ReactanceL - ReactanceC), 2))
    return Impedance

#Xl = 2πfL
def ITR(Frequency, Inductance):
    IReactance = 2 * math.pi * Frequency * Inductance
    return IReactance

#Xc = 1/2πfC
def CTR(Frequency, Capacitance):
    CReactance = 1 / (2* math.pi * Frequency * Capacitance)
    return CReactance

#G = 1 / R
def CTR_Conductance(Resistance):
    Conductance = 1 / Resistance
    return Conductance

#C = Q / V
def CTCV(Charge, Voltage):
    Capacitance = Charge / Voltage
    return  Capacitance

#f = 1 / T
def FTP(Period):
    Frequency = 1 / Period
    return Frequency

#T = 1 / f
def PTF(Frequency):
    Period = 1 / Frequency
    return Period

#𝜃ab = 𝜃a − 𝜃b
def PD(ThetaA, ThetaB):
    ThetaAB = ThetaA - ThetaB
    return ThetaAB

#𝑢(𝑡) = √2𝑈 ⋅ cos(𝜔𝑡 + 𝜃)
def TFV(Voltage, Frequency, Time, Theta):
    VoltageT = math.sqrt(2) * Voltage * math.cos(2 * math.pi * Frequency * Time + Theta)
    return VoltageT

#𝑖(𝑡) = √2𝐼 ⋅ cos (𝜔𝑡 + 𝜃 + 𝜓 )
def TFC(Current, Frequency, Time, Theta, Psi):
    CurrentT = math.sqrt(2) * Current * math.cos(2 * math.pi * Frequency * Time+ Theta + Psi)
    return CurrentT

#cos 𝜑 = cos(𝜃u − 𝜃i )
def PF(ThetaU, ThetaI):
    Phi = math.cos(ThetaU - ThetaI)
    return math.cos(Phi)

#𝑃 = √3 𝑈l 𝐼 𝑐𝑜𝑠𝜑.
def AP(Voltage, Current, Phi):
    ActiveP = math.sqrt(3) * Voltage * Current * math.cos(Phi)
    return ActiveP

#𝑄 = √3 ⋅ 𝑈l ⋅ 𝐼 ⋅ sin 𝜑
def RP(Voltage, Current, Phi):
    ReactiveP = math.sqrt(3) * Voltage * Current * math.sin(Phi)
    return ReactiveP

#𝑆 = 𝑃 + 𝑗 ⋅ 𝑄
def ApparentP(ActiveP, ReactiveP):
    S = complex(ActiveP, ReactiveP)
    return S

#|S| = √(P^2 + Q^2)
def ApparentP_Module(ActiveP, ReactiveP):
    S_module = math.sqrt(math.pow(ActiveP, 2) + math.pow(ReactiveP))
    return S_module

# Z = z * l or similar
def PTL(ParameterL, Length):
    Parameter = ParameterL * Length
    return Parameter

#Iload = k𝜃 * kp * kρ
def PCLC(k_theta, k_p, k_rho, CurrentLT):
    CurrentL = k_theta * k_p * k_rho * CurrentLT
    return CurrentL

#Ip = Sp / (√3 * Un)
def CTPpV(Power, Voltage):
    CurrentP = Power / (math.sqrt(3) * Voltage)
    return CurrentP

def CTPpV_Phase(Power, Voltage, Phi):
    CurrentP = Power / (math.sqrt(3) * Voltage * math.cos(Phi))
    return CurrentP




