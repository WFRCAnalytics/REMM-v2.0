'''
Run model estimation functions.
Note: neighborhood_vars step must be run prior to estimation
'''

import datasources, models, variables, utils
import orca_wfrc.orca as sim
import pandas as pd
import numpy as np
import os


sim.run(["clear_cache",
         "travel_time_reset",
         "neighborhood_vars",
         "nrh_estimate_utah",
         "nrh_estimate_slc",
         "nrh_estimate_davis",
         "nrh_estimate_weber",
         "rsh_estimate_utah",
         "rsh_estimate_slc",
         "rsh_estimate_davis",
         "rsh_estimate_weber",
         "hlcm_estimate_slc",
         "hlcm_estimate_utah",
         "hlcm_estimate_dw",
         "elcm_estimate",
],iter_vars=[2015])

