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


## Example

```python

import numpy as np
from KneeFinder import KneeFinder

data_x = np.linspace(1, 10, 15)
data_y = 10*(np.exp(-a) + 0.15 * np.random.rand(len(a)))

kf = KneeFinder(data_x=a, data_y=b)

knee_x, knee_y = kf.find_knee()

# plotting to check the results
kf.plot()

```

![clustering_data](https://raw.githubusercontent.com/vlavorini/kneefinder/main/imgs/knee.png?raw=true "Knee searching method")

## Methodology
KneeFinder define as knee the point which has the maximum distance 
from a line passing between the first and last point.

As example, take the following image: in blue you can see the data, 
in orange the segment which connect the first to the last data point, and
in red the distances between the data points. The big continuous red line points to our
knee point.

![clustering_data](https://raw.githubusercontent.com/vlavorini/kneefinder/main/imgs/sagitta.png?raw=true "Knee searching method")

This methodology is simpler with respect to other methods: no parameters are required, 
so it's easier to use in automated processes.

### Robustness
Since this tool does not rely on any assumption on the curve shape, 
it results as more robust with respect to other, more complicated, tools. 

As example, if you consider [Kneed](https://github.com/arvkevi/kneed) with the following data, 
and simulating a common mis-configuration in the parameters:

```python
# Finding the knee with the Kneed tool (not with our one)
from kneed import KneeLocator

x = [0.1       , 0.23571429, 0.37142857, 0.50714286, 0.64285714,
       0.77857143, 0.91428571, 1.05      , 1.18571429, 1.32142857,
       1.45714286, 1.59285714, 1.72857143, 1.86428571, 2.        ]
y = [ 1.17585897,  1.35051375,  1.836304  ,  2.20409812,  2.37060316,
        2.46157837,  3.28991099,  2.9927505 ,  3.44015722,  6.33212422,
        6.92051422,  5.28718862,  6.69129098,  6.67477275, 10.00921042]

kneedle = KneeLocator(x, y, curve="concave", direction="increasing")
kneedle.plot_knee()

```
Note that the curve is convex-like, while we configured Kneed as if the curve was concave-like. 
With this configuration, the package state the knee/elbow point to be the very first point, 
which is obviously wrong.

![kneed_wrong](https://raw.githubusercontent.com/vlavorini/kneefinder/main/imgs/wrong_knee.png?raw=true "Kneed mistake")

While using our tool you get:

![kneed_right](https://raw.githubusercontent.com/vlavorini/kneefinder/main/imgs/good_knee.png?raw=true "Kneed correct")

Moreover, our tool is also a bit faster:

```python
%%timeit
kf = KneeFinder(data_x=x, data_y=y)
kf.find_knee()
# 24 µs ± 268 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
```

```python
%%timeit
kneedle = KneeLocator(x, y, curve="concave", direction="increasing")
kneedle.find_knee()
# 91.8 µs ± 1.32 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
```



