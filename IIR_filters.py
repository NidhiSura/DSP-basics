#IIR Butterworth and Chebychev Filters

import math

#taking inputs
Ap = int(input('Enter pass-band attenuation: '))
As = int(input('Enter stop-band attenuation: '))
fp = int(input('Enter pass-band edge frequency: '))
fs = int(input('Enter stop-band edge frequency: '))
Fs = int(input('Enter sampling frequency: '))

#finding values of wp and ws
wp = (2*(math.pi)*fp)/Fs
ws = (2*(math.pi)*fs)/Fs

#FOR BUTTERWORTH
omegap = 2*Fs*math.tan(wp/2)
omegas = 2*Fs*math.tan(ws/2)

Nb = (math.log(((10**(0.1*As)-1)/(10**(0.1*Ap)-1))**(1/2)))/math.log(omegas/omegap)
Nb = math.ceil(Nb)

omegac = round(omegap/(10**(0.1*Ap)-1))

print('\nOrder of Butterworth Filter = ', Nb)

#CHEBYCHEV FILTER
Nc = math.acosh(((10**(0.1*As)-1)/(10**(0.1*Ap)-1))**(1/2))/math.acosh(omegas/omegap)
Nc = math.ceil(Nc)

print('\nOrder of Chebychev Filter = ', Nc)
print('\nCutoff frequency ~ ' + str(omegac/1000) + ' kHz')
