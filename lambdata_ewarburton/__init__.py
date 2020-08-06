#!/usr/bin/env python
"""
lambdata - functions and code for EDI for Health Rosetta
"""

import pandas as pd
import numpy as np
from . import example_module

TEST = pd.DataFrame(np.ones(10))

Y = example_module.mandel(5, 9)
