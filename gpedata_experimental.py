import pathlib
import glob
import pandas as pd

class Params:
    requires = ()
    provides = ('baseline_before', 'baseline_after',
                'steady_after', 'steady_before', 'steady_cutoff',
                'falling_curve_window', 'rectification_window',
                'injection_start', 'injection_end',
                'injection_interval')

    injection_start = 0.050
    injection_end = 1.050

    injection_interval = injection_end - injection_start

    baseline_before = None
    baseline_after = injection_end

    steady_after = .250
    steady_cutoff = 80
    steady_before = injection_end

    falling_curve_window = 20
    rectification_window = 11

dirname = pathlib.Path(__file__).parent / 'gpedata-experimental'
csvs = sorted(glob.glob('{}/*.csv'.format(dirname)))
data = {name.split('/')[-1][:-4] : pd.read_csv(name, index_col=0)
        for name in csvs}
