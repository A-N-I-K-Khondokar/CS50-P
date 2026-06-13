'''
1. A packages is a third party libraries
We can find this kind of libraries in websites
like : pypi.org

2. cowsay is a package in python we can find it 
in pypi.org/project/cowsay

3. pip (package manager) is a program by which 
we can install packages in our environment.

4.use pip install cowsasy 
5.import it

 
'''

import cowsay
import sys

if len(sys.argv)==2:
    cowsay.cow("hello "+sys.argv[1])