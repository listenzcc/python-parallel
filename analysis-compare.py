# %%
import pandas as pd
import plotly.express as px

from pathlib import Path

# %%

csv = Path('speed-compare-process-thread.csv')

table = None
if csv.is_file():
    table = pd.read_csv(csv, index_col=0)

table['cost'] = table['stop'] - table['start']
table

# %%
df = table.copy()
df = df.sort_values(by='jobs')
df.index = range(len(df))
df = df[['iteration', 'pi', 'cost', 'method', 'jobs']]
df['method'] = df['method'].map(lambda e: e.split("'")[1].split('.')[-1])
df['speed_single'] = df['iteration'] / df['cost']
df['speed_total'] = df['speed_single'] * df['jobs']
df

# %%
px.box(df, x='method', y='iteration', color='jobs')
# %%
px.box(df, x='method', y='speed_single', log_y=True, color='jobs')

# %%
px.box(df, x='method', y='speed_total', log_y=True, color='jobs')

# %%
