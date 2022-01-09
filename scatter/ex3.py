# Copyright (c) 2021 LMU Munich Geometry Processing Authors. All rights reserved.
# Created by Changkun Ou <https://changkun.de>.
#
# Use of this source code is governed by a GNU GPLv3 license that can be found
# in the LICENSE file.

import csv
import numpy as np
import matplotlib.pyplot as plt

with open('scatter.csv', 'r') as f:
    next(f) # skip first row
    data = list(csv.reader(f))
data = np.array(data, dtype=np.float)
print('mean:', data.mean(axis=0))
print('variance:', data.var(axis=0))

for i in range(4):
    print(f"pearson x{i}:")
    print(np.corrcoef(data[:, 2*i], data[:, 2*i+1]))
    plt.scatter(data[:, 2*i], data[:, 2*i+1])
    plt.savefig(f'x{i}.pdf')
    plt.clf()
