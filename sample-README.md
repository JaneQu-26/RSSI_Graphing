# pressure_studies - a suite of programs to study equations of state

## What is this?

pressure_studies is a simple set of programs to calculate and plot
pressure.  There is also a paper describing the physics in detail.

## Prerequisites

You will need a C compiler.  On a debian system you can install it
with:
```
sudo apt install gcc
```

You will also need the matplotlib library for python.  You can install
that with:
```
sudo apt install python3-matplotlib
```

Note that you might be using specific python packaging approaches, in
which case you will need to install matplotlib according to that
idiom.  Our use of it is rather simple, installation with apt might be
sufficient for most people.

## How to run the program and make plots

You can compile and run the program with:
```
gcc -o calculate_pressure calculate_pressure.c -lm
./calculate_pressure 14.1 4.8 > pressure_14.1-3_4.8.out
```

You can then make a sweep of temperatures and volumes, thus allowing
you to make plots, with:
```
for temp in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
    for vol in 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5; do
        out_fname=pressure_${temp}_${vol}.out
        echo "running temperature $temp and volume $vol - output in $out_fname"
        ./calculate_pressure $temp $vol > $out_fname
    done
done
```

After that sweep you now have enough output to make a plot with:
```
./plot_pressure.py pressure_*_*.out
```

This will create files called p_vs_T_and_V.png and p_vs_T_and_V.pdf

## Building the paper

Once you have made the plot you can build the paper with:
```
pdflatex pressure_studies.tex
```
and you will then be able to read it in the pdf file
pressure_studies.pdf

