"""Test all the modules."""
import os


def test_dualpal():
    with open('dualpal.in', 'w') as f:
        f.write('3 25\n')

    os.system('cp ../dualpal/dualpal.py .')
    __import__('dualpal')

    with open('dualpal.out') as f:
        assert (f.read() == """26\n27\n28\n""")

    os.remove('dualpal.py')
    os.remove('dualpal.in')
    os.remove('dualpal.out')
