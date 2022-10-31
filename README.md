# Knee Finder
A simple tool to find the knee point of a 2-d curve.


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
from a line passing between the first and last point:

![Employee data](/imgs/sagitta.png?raw=true "Knee searching method")

Example:
