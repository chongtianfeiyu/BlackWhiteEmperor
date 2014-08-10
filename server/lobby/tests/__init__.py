#!/usr/bin/env python
# coding=utf-8


import unittest, os, re, importlib


def test_suites(t):
    packages = ["models"]
    modules = []
    if t == 'all':
        for package in packages:
            modules.extend(test_modules(package))
    elif t not in packages:
        print "Tests not found"
        exit()
    else:
        modules.extend(test_modules(t))
    load = unittest.defaultTestLoader.loadTestsFromModule
    return unittest.TestSuite(map(load, modules))

def test_modules(package):
    path = os.path.split(os.path.realpath(__file__))[0]
    files = os.listdir(path + "/" + package)
    test = re.compile(r"^test.*.py$")
    files = filter(test.search, files)
    modules = []
    if len(files) > 0:
        filenameToModuleName = lambda f: "tests." + package + "." + os.path.splitext(f)[0]
        moduleNames = map(filenameToModuleName, files)
        modules = map(importlib.import_module, moduleNames)
    return modules

def run_tests(t):
    unittest.TextTestRunner(verbosity=2).run(test_suites(t))
