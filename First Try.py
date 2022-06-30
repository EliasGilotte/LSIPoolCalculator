
pH = float(input('pH: '))
if pH == 7.0:
    pHf = float(.23)
    print(pH, 'pH =', pHf, 'pH Factor')
if pH == 7.2:
    pHf = float(.27)
    print(pH, 'pH =', pHf, 'pH Factor')
if pH == 7.4:
    pHf = float(.31)
    print(pH, 'pH =', pHf, 'pH Factor')
if pH == 7.6:
    pHf = float(.33)
    print(pH, 'pH =', pHf, 'pH Factor')
if pH == 7.8:
    pHf = float(.35)
    print(pH, 'pH =', pHf, 'pH Factor')
if pH == 8.0:
    pHf = float(.36)
    print(pH, 'pH =', pHf, 'pH Factor')

Temp = float(input('Temperature: '))
if 32 <= Temp <= 36:
    Tempf = float(0.0)
    print('The Temperature', Temp, 'F', '= The Temperature Factor', Tempf)
if 37 <= Temp <= 45:
    Tempf = float(0.1)
    print('The Temperature', Temp, 'F', '= The Temperature Factor', Tempf)
if 46 <= Temp <= 52:
    Tempf = float(0.2)
    print('The Temperature', Temp, 'F', '= The Temperature Factor', Tempf)
if 53 <= Temp <= 59:
    Tempf = float(0.3)
    print('The Temperature', Temp, 'F', '= The Temperature Factor', Tempf)
if 60 <= Temp <= 65:
    Tempf = float(0.4)
    print('The Temperature', Temp, 'F', '= The Temperature Factor', Tempf)
if 66 <= Temp <= 75:
    Tempf = float(0.5)
    print('The Temperature', Temp, 'F', '= The Temperature Factor', Tempf)
if 76 <= Temp <= 83:
    Tempf = float(0.6)
    print('The Temperature', Temp, 'F', '= The Temperature Factor', Tempf)
if 84 <= Temp <= 93:
    Tempf = float(0.8)
    print('The Temperature', Temp, 'F', '= The Temperature Factor', Tempf)
if 94 <= Temp <= 104:
    Tempf = float(0.8)
    print('The Temperature', Temp, 'F', '= The Temperature Factor', Tempf)
if Temp == 105:
    Tempf = float(0.9)
    print('The Temperature', Temp, 'F', '= The Temperature Factor', Tempf)


CaH = float(input('Calcium Hardness:'))
if 5 <= CaH <= 24:
    CaHf = float(0.3)
    print('The Calcium Hardness', CaH, '= The Calcium Hardness Factor', CaHf)
if 25 <= CaH <= 49:
    CaHf = float(1.0)
    print('The Calcium Hardness', CaH, '= The Calcium Hardness Factor', CaHf)
if 50 <= CaH <= 74:
    CaHf = float(1.3)
    print('The Calcium Hardness', CaH, '= The Calcium Hardness Factor', CaHf)
if 75 <= CaH <= 99:
    CaHf = float(1.5)
    print('The Calcium Hardness', CaH, '= The Calcium Hardness Factor', CaHf)
if 100 <= CaH <= 149:
    CaHf = float(1.6)
    print('The Calcium Hardness', CaH, '= The Calcium Hardness Factor', CaHf)
if 150 <= CaH <= 199:
    CaHf = float(1.8)
    print('The Calcium Hardness', CaH, '= The Calcium Hardness Factor', CaHf)
if 200 <= CaH <= 299:
    CaHf = float(1.9)
    print('The Calcium Hardness', CaH, '= The Calcium Hardness Factor', CaHf)
if 300 <= CaH <= 399:
    CaHf = float(2.1)
    print('The Calcium Hardness', CaH, '= The Calcium Hardness Factor', CaHf)
if 400 <= CaH <= 799:
    CaHf = float(2.2)
    print('The Calcium Hardness', CaH, '= The Calcium Hardness Factor', CaHf)
if CaH >= 800:
    CaHf = float(2.5)
    print('The Calcium Hardness', CaH, '= The Calcium Hardness Factor', CaHf)

TAl = float(input('Total Alkalinity:'))
if 5 <= TAl <= 24:
    TAlf = float(0.7)
    print('The Total Alkalinity', TAl, '= The Total Alkalinity Factor', TAlf)
if 25 <= TAl <= 49:
    TAlf = float(1.4)
    print('The Total Alkalinity', TAl, '= The Total Alkalinity Factor', TAlf)
if 50 <= TAl <= 74:
    TAlf = float(1.7)
    print('The Total Alkalinity', TAl, '= The Total Alkalinity Factor', TAlf)
if 75 <= TAl <= 99:
    TAlf = float(1.9)
    print('The Total Alkalinity', TAl, '= The Total Alkalinity Factor', TAlf)
if 100 <= TAl <= 149:
    TAlf = float(2.0)
    print('The Total Alkalinity', TAl, '= The Total Alkalinity Factor', TAlf)
if 150 <= TAl <= 199:
    TAlf = float(2.2)
    print('The Total Alkalinity', TAl, '= The Total Alkalinity Factor', TAlf)
if 200 <= TAl <= 299:
    TAlf = float(2.3)
    print('The Total Alkalinity', TAl, '= The Total Alkalinity Factor', TAlf)
if 300 <= TAl <= 499:
    TAlf = float(2.5)
    print('The Total Alkalinity', TAl, '= The Total Alkalinity Factor', TAlf)
if 500 <= TAl <= 799:
    TAlf = float(2.6)
    print('The Total Alkalinity', TAl, '= The Total Alkalinity Factor', TAlf)
if TAl >= 800:
    TAlf = float(2.9)
    print('The Total Alkalinity', TAl, '= The Total Alkalinity Factor', TAlf)

TDS = float(input('Total Dissolved Solids (TDS): '))
if 0 <= TDS <= 999:
    TDSf = float(12.10)
    print('The Total Dissolved Solids', TDS, '= The Total Dissolved Solids Factor', TDSf)
if 1000 <= TDS <= 1999:
    TDSf = float(12.19)
    print('The Total Dissolved Solids', TDS, '= The Total Dissolved Solids Factor', TDSf)
if 2000 <= TDS <= 2999:
    TDSf = float(12.29)
    print('The Total Dissolved Solids', TDS, '= The Total Dissolved Solids Factor', TDSf)
if 3000 <= TDS <= 3999:
    TDSf = float(12.35)
    print('The Total Dissolved Solids', TDS, '= The Total Dissolved Solids Factor', TDSf)
if TDS >= 4000:
    TDSf = float(12.41)
    print('The Total Dissolved Solids', TDS, '= The Total Dissolved Solids Factor', TDSf)

print('pH + Temperature Factor + Calcium Hardness Factor + Total Alkalinity - pH Factor - Total Dissolved Solids Factor =')

print(float(pH + Tempf + CaHf + TAlf - pHf - TDSf))












