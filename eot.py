from math import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def eot(dn):
    omega = 2 * pi / 365.25
    lmd = 23.44 * pi / 180
    alpha = omega * ((dn + 10) % 365)
    beta = alpha + 0.0333 * sin(omega * ((dn - 2) % 365))
    gamma = (alpha - atan(tan(beta) / cos(lmd))) / pi
    return 43200 * (gamma - round(gamma)) / 60


def mode(x, n):
    freq = np.fft.rfft(x)
    freq[:n] = 0
    freq[n+1:] = 0
    return np.fft.irfft(freq)


dns = np.linspace(0, 365, 5000, endpoint=False)
eots = [eot(dn) for dn in dns]

m1 = mode(eots, 1)
m2 = mode(eots, 2)

d1 = np.diff(np.hstack((m1, [m1[0]])))
d2 = np.diff(np.hstack((m2, [m2[0]])))

d1 *= 7.9 / max(np.abs(d1))
d2 *= 20.3 / max(np.abs(d2))

print('Periapsis:', dns[np.argmin(d1)])
print('Apoapsis:', dns[np.argmax(d1)])
print('Vernal equinox:', dns[np.argmax(d2[:2500])])
print('Autumnal equinox:', dns[2500 + np.argmax(d2[2500:])])
print('Summer solstice:', dns[np.argmin(d2[:2500])])
print('Winter solstice:', dns[2500 + np.argmin(d2[2500:])])

data = np.vstack((dns, -d1, -d2, -d1 - d2, [-e for e in eots])).T
df = pd.DataFrame(data=data, columns=['Day number', 'Length due to ellipticity',
                                      'Length due to obliquity of ecliptic',
                                      'Length of day', 'EoT'])
df.to_csv('eot.csv', sep=' ')
