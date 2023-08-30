import os
import sys
from os.path import dirname, join
sys.path.append(join(dirname(__file__), '..'))
import testpy

def GetConfiguration(context, root):
  return testpy.SimpleTestConfiguration(context, root, 'internet')
