# %%
import os

# %%
jobs = [
    'python .\speed-compare-process-thread.py -r -t -j2',
    'python .\speed-compare-process-thread.py -r -t -j5',
    'python .\speed-compare-process-thread.py -r -t -j10',
    'python .\speed-compare-process-thread.py -r -t -j20',
    'python .\speed-compare-process-thread.py -r -t -j30',
    'python .\speed-compare-process-thread.py -r -t -j40',
    'python .\speed-compare-process-thread.py -r -p -j2',
    'python .\speed-compare-process-thread.py -r -p -j5',
    'python .\speed-compare-process-thread.py -r -p -j10',
    'python .\speed-compare-process-thread.py -r -p -j20',
    'python .\speed-compare-process-thread.py -r -p -j30',
    'python .\speed-compare-process-thread.py -r -p -j40',
]

for job in jobs:
    print('Running job', job)
    os.system(job)

# %%