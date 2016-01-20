#!/usr/bin/python

import math;
import sys;

equation = input("Giv mig koefficienterne til en andengradsligning i denne format:\na b c\n");
equation = equation.split();

a = float(equation[0]);
b = float(equation[1]);
c = float(equation[2]);
d = pow(b, 2) - 4 * a * c;
print("d = " + str(b)+"^2 - 4*"+str(a)+"*"+str(c) + " = " + str(d));
if (d < 0):
	print("d < 0, no result!");
	exit();
print("x(es) = -" + str(b) + " +/- sqrt(" + str(d) + ") / (" + str(2) + "*" + str(a) + ") = ...");
print((-b + math.sqrt(d)) / (2 * a));
if (d != 0):
	print((-b - math.sqrt(d)) / (2 * a));