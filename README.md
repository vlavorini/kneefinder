# Knee Finder
A simple tool to find the knee point of a 2-d curve.

This is useful for tune the parameters in several algorithms (clustering, etc.)


## Installation
you can install this package with pip:

```commandline
pip install kneefinder
```

## Definition of "Knee" point
The knee point is defined as the “relative costs to increase [or decrease, NdC] some tunable parameter is no longer worth 
the corresponding performance benefit” (Satopää, Albrecht, Irwin, and Raghavan, 2011, p.1)

## Methodology
KneeFinder define as knee the point which has the maximum distance 
from a line passing between the first and last point.

As example, take the following image: in blue you can see the data, 
in orange the segment which connect the first to the last data point, and
in red the distances between the data points. The big continuous red line points to our
knee point.

![clustering_data](/imgs/sagitta.png?raw=true "Knee searching method")

Note that this methodology is simpler with respect to other methods (no parameters required), 
so easier to use in an automated process.

## Example

```python

import numpy as np
import matplotlib.pyplot as plt
from KneeFinder import KneeFinder

data_x = np.linspace(1, 10, 15)
data_y = 10*(np.exp(-a) + 0.15 * np.random.rand(len(a)))

kf = KneeFinder(data_x=a, data_y=b)

knee_x, knee_y = kf.find_knee()

# plotting to check the results
kf.plot()

```

![clustering_data](/imgs/knee.png?raw=true "Knee searching method")
