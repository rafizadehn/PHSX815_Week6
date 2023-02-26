# PHSX 815: Week 6
## Numerical Integration Methods

This repository includes a script that compares the rectangle rule method and gaussian quadrature method of numerical integration. 

---

### Homework 6:

### Running the Code
The integration area measurements are made by the `Integration.py` python file. This file requires python3 to run, and includes the following packages listed at the top of the script:

```
  import numpy as np
  import sys
  import matplotlib.pyplot as plt
  from scipy import integrate
```

To run this script from the terminal in linux, run:

> $ python3 Integrate.py

This runs the file with the default parameters, which are: 100 subintervals for the rectangle sum and 1 evaluation point for the quadrature method calculation.

These values can be altered from the command line in the terminal by simply adding an argument after the file name. The arguments to change these include `-Nint` and `-Npoints`, respectively. 

For example, it may looks something like this in linux:

> $ python3 Integrate.py -Nint 1000 -Npoints 5

which would evaluate the rectangle sum with 1000 subintervals and the gaussian quadratures with 5 points.

### The Output

The first output is within the terminal and includes the values of the calculated integrals:

![pic1](https://user-images.githubusercontent.com/76142511/221339121-abdf50f0-f218-4972-816b-c536c3bc8b24.png)

The script also outputs the comparison of each method, along with the errors calculated:

![Figure_1](https://user-images.githubusercontent.com/76142511/221339149-c60c5aac-ef01-4ca7-8b3c-e66e7f5b769d.png)

![Figure_2](https://user-images.githubusercontent.com/76142511/221339152-2cfac7bb-9995-414b-8351-cfba09f22fd4.png)

![Figure_3](https://user-images.githubusercontent.com/76142511/221339154-bd40eaa0-3c6b-4522-b868-df63ec2735ea.png)

As you can see, both methods converge to the analytical solution quite quickly. In the future, I would choose a more complex integral to see if I can challenge these methods further.

[Rectangle Method code sourced from this site.](http://specminor.org/2017/01/05/numerical-integration-python.html)

---

### Homework 7:

### Running the Code
The monte carlo integration  measurements are made by the `MC_Integration.py` python file. This file requires python3 to run, and includes the following packages listed at the top of the script:

```
  import numpy as np
  import sys
  import matplotlib.pyplot as plt
  from scipy import integrate
```

To run this script from the terminal in linux, run:

> $ python3 MC_Integrate.py

This runs the file with the default parameters, which are: 100 subintervals for the rectangle sum, 1 evaluation point for the quadrature method calculation, and 1000 points in the monte carlo simulation.

These values can be altered from the command line in the terminal by simply adding an argument after the file name. The arguments to change these include `-Nint`, `-Nquads`, and `-Npoints`, respectively. 

For example, it may looks something like this in linux:

> $ python3 Integrate.py -Nint 1000 -Nquads 5 -Npoints 1000

which would evaluate the rectangle sum with 1000 subintervals, the gaussian quadratures with 5 points, and use 1000 randomly generated values for the monte carlo method.

### The Output

The first output is within the terminal and includes the values of the calculated integrals:


