import os
import sys
sys.path.append(os.path.dirname(__file__))

from altunityrunner import AltUnityDriver
import unittest
import pytest

class BaseTest(unittest.TestCase):
    platform = os.getenv('TESTS_PLATFORM')   
    altdriver = AltUnityDriver()

    @classmethod
    def setupClass(cls):
        print("INSIDE base_test.setupClass")        
        cls.altdriver = altdriver

    @classmethod
    def tearDownClass(cls):
        cls.altdriver.stop()
