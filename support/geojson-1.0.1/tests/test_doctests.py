# ============================================================================
# GeoJSON. Copyright (C) 2007 Sean C. Gillies
#
# See ../LICENSE.txt
# 
# Contact: Sean Gillies, sgillies@frii.com
# ============================================================================
import unittest
import glob
import os

import doctest

optionflags = (doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.NORMALIZE_WHITESPACE |
               doctest.ELLIPSIS)

def list_doctests():
    return [filename
            for filename
            in glob.glob(os.path.join(os.path.dirname(__file__), '*.txt'))]

def open_file(filename, mode='r'):
    """Helper function to open files from within the tests package."""
    return open(os.path.join(os.path.dirname(__file__), filename), mode)

def setUp(test):
    test.globs.update(dict(
            open_file = open_file,
            ))

def test_suite():
    return unittest.TestSuite(
        [doctest.DocFileSuite(os.path.basename(filename),
                              optionflags=optionflags,
                              setUp=setUp)
         for filename
         in list_doctests()])
