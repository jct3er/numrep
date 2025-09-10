# numrep

Starter code for numerical representation exercise

Add your files here.

Over and Underflows - over_under.cpp
Bessel Functions - plots.py
Numerical Derivatives - derivatives.py

Over and Underflows
1. Float overflow happens at 10^38 while underflow happens at 10^-45
2. Double overflow happens at 10^307 while underflow happens at 10^-324
3. Integer overflow happens at 2147483647 while underflow happens at -2147483648
4. Unsigned Integer overflow happends at 4294967295 while underflow happens at 0
5. Pythons integer is only limited by memory, so it is arbitrary precision.

Bessel Functions
1. The two methods for calculating the bessel functions give the same values.
The only difference is the first point on J8 is non-zero for the up method. So the down method is more accurate.

Numerical Derivatives
1. The max precision for: forward is about 10^-7, central is about 10^-10, and extrapolated is about 10^-13. The text estimates them to be about: 10^-8 for forward, 10^-11 for central, and 10^-15 for extrapolated. So forward and central are similar while extrapolated is a little off.
2. Forward should have a slope of O(h), while central is O(h^2), and extrapolated it O(h^4). In the range where algorithmic error dominates, forward has the smallest slope while extropated grows the fastest so this agrees with the model prediction.
3. Round off error dominates at h smaller than: 10^-8 for forward, 10^-5 for central, and 10^-2 for extrapolated. Beyond these points the error is dominated by algorithmic error.