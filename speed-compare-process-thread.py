'''
File: speed-compare-process-thread.py
Author: Chuncheng Zhang
Purpose:
    Compare the speed between processes and threads.
'''

# %%
import sys
import time
import argparse
import pandas as pd

from pathlib import Path
from threading import Thread
from multiprocessing import Process
from multiprocessing.managers import SharedMemoryManager

from compute_pi import compute_pi

# %%


def monitor(sl, time_step=0.5):
    t = time.time()
    j = 0
    while True:
        print('M', j, time.time() - t, sl)
        time.sleep(time_step)
        j += 1


csv = Path('speed-compare-process-thread.csv')

table = None
if csv.is_file():
    table = pd.read_csv(csv, index_col=0)

# %%
if __name__ == '__main__':
    parse = argparse.ArgumentParser(__name__)
    parse.add_argument('-r', '--run', action='store_true', help='Run the jobs')
    parse.add_argument('-t', '--thread', action='store_false',
                       help='Run with thread')
    parse.add_argument('-p', '--process',
                       action='store_false', help='Run with process')
    parse.add_argument('-j', '--jobs', type=int,
                       default=5, help='Number of jobs in parallel')
    parse.add_argument('-d', '--duration', type=float,
                       default=10, help='Run for seconds')

    args = parse.parse_args()
    print(args)

    if not args.run:
        print('Not run anything')
        sys.exit(0)

    if args.thread == args.process:
        print('Only one mode is allowed, thread or process')
        sys.exit(1)

    if args.thread:
        method = Thread

    if args.process:
        method = Process

    method_name = '{}'.format(type(method()))

    duration = args.duration  # seconds

    num_jobs = args.jobs
    num_index = 4
    base_iterations = int(1e5)

    jobs = []
    for job_idx in range(num_jobs):
        jobs.append(dict(
            idx_session=int(job_idx*num_index),
            idx_pi=int(job_idx*num_index+1),
            idx_start=int(job_idx*num_index+2),
            idx_stop=int(job_idx*num_index+3),
            stop_session=-1,
            base_iterations=int((job_idx+1) * base_iterations),
            quite=True,
        ))

    print(jobs)

    with SharedMemoryManager() as smm:
        sl = smm.ShareableList([0 for _ in range(num_jobs * num_index + 2)])

        for job in jobs:
            p = method(target=compute_pi,
                       args=(sl,),
                       kwargs=job,
                       daemon=True)
            p.start()

        t = Thread(target=monitor, args=(sl,), daemon=True)
        t.start()

        # Run for 10 seconds
        time.sleep(duration)

        sl[-1] = -1

        for job in jobs:
            job['iteration'] = sl[job['idx_session']] * job['base_iterations']
            job['pi'] = sl[job['idx_pi']]
            job['start'] = sl[job['idx_start']]
            job['stop'] = sl[job['idx_stop']]
            job['method'] = method_name
            job['jobs'] = num_jobs

        print('Final', sl)

    result = pd.DataFrame(jobs)
    print(result)

    table = pd.concat([table, result])
    table.to_csv(csv)

    print('Done.')

# %%
