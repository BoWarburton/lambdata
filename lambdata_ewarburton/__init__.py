#!/usr/bin/env python
"""
lambdata - functions and code for EDI for Health Rosetta
"""

import pandas as pd
import numpy as np
# from lambdata_ewarburton.dataframe_helper import report_empty_fields # no value between the separators
# Y = example_module.mandel(5, 9)

from lambdata_soycode.dataframe_helper import report_missing_values

TEST = pd.DataFrame(np.ones(10))