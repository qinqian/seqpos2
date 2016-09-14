#!/usr/bin/env python

import os
import sys
from setuptools import setup, Extension
from Cython.Distutils import build_ext
from numpy.distutils.misc_util import get_numpy_include_dirs

cbw = Extension( '_motif',
                 sources = ['src/genomescan_Markov0_3.c', 'src/seq.c'],
                 extra_compile_args = ['-O3', '-std=c99', '-Wall'] )

bg = Extension('bgcount', ['lib/count.pyx'])

setup(name="seqpos2",
      version="1.0.0",
      description="Motif scan tool",
      author='Qian Alvin Qin',
      author_email='xx',
      url='http://liulab.dfci.harvard.edu/',
      ext_modules = [cbw, bg],
      cmdclass = {'build_ext':build_ext},
      scripts=['bin/seqpos2'],
      zip_safe=True,
      include_dirs=['src'] + get_numpy_include_dirs(),
      classifiers=[
        'Development Status :: 5 - productive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Artistic License',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        ])
