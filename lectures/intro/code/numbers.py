#!/usr/bin/python2

logic   = True         # A boolean assignment
counter = 103          # An integer 
miles   = 1000.0       # A floating point
cmplx   = 1 + 1j        # A complex 
name    = "John"       # A string

print logic, not logic
print counter, counter * miles
print miles, miles / counter, miles // counter
print cmplx, cmplx.conjugate()
print name, '|'.join(name)
