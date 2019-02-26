#!python3

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

with open('Absentee Audit.ipynb') as f:
    nb = nbformat.read(f, as_version=4)
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(nb, {})

