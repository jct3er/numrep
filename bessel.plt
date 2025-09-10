# a simle gnuplot macro

set xlabel "x"
set ylabel "bessel_n(x)"

plot "bessel8.dat" using 1:2 pt 19 title "down calc", "bessel8.dat" using 1:3 pt 15 title "up calc"

