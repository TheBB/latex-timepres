from math import *
from collections import namedtuple

R = 2
Eq = namedtuple('Eq', ['a', 'd'])

coords = [
    Eq(00.00, 00.00),
    Eq(13.81, 05.91),
    Eq(27.91, 11.48),
    Eq(42.53, 16.34),
    Eq(57.82, 20.16),
    Eq(73.72, 22.60),
    Eq(90.00, 23.45),
]

for c in coords[-2::-1]:
    coords.append(Eq(180 - c.a, c.d))
for c in coords[1:-1]:
    coords.append(Eq(180 + c.a, -c.d))

for c in coords:
    cx = -sin(pi/180*c.a) * cos(pi/180*c.d) * R
    cy = cos(pi/180*c.a) * cos(pi/180*c.d) * R
    cz = sin(pi/180*c.d) * R

    # print('({:.2f}, {:.2f})'.format(c.a, c.d))
    print(r'\tdplottransformmainscreen{%.4f}{%.4f}{%.4f}' % (cx, cy, cz))
