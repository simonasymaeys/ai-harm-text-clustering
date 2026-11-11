"""Combine independently obtained official AIM Excel exports; no network access.
Usage: python data/load_exports.py /path/to/exports --output /path/to/new_snapshot.csv
New snapshots require their own validation and study specification.
"""
from pathlib import Path
import argparse
import hashlib
import pandas as pd

FIELDS = ['id','title','date','summary','concepts','companies','country']

def combine(folder, output):
    files = sorted(Path(folder).glob('*.xlsx'))
    if not files:
        raise FileNotFoundError('No .xlsx exports found in the supplied folder.')
    tables=[]
    for path in files:
        frame=pd.read_excel(path,keep_default_na=False,dtype=str)
        if not set(FIELDS).issubset(frame.columns):
            raise ValueError(f'Unexpected export schema in {path.name}')
        frame=frame[FIELDS].copy()
        frame['date']=pd.to_datetime(frame.date,errors='raise').dt.strftime('%Y-%m-%d')
        tables.append(frame)
    merged=pd.concat(tables,ignore_index=True)
    repeated=merged[merged.id.duplicated(keep=False)]
    for report_id, rows in repeated.groupby('id'):
        if len(rows.drop_duplicates())>1:
            raise ValueError(f'Conflicting content for report ID {report_id}; review before combining.')
    merged=merged.drop_duplicates('id')
    merged=merged[merged.date.between('2026-07-01','2026-09-30')].sort_values(['date','id'])
    assert merged.id.is_unique
    if merged.empty or merged.id.eq('').any() or merged.summary.str.strip().eq('').any():
        raise ValueError('Empty dataset, missing IDs or missing summaries.')
    output=Path(output)
    if output.exists():
        raise FileExistsError('Output already exists; choose a new snapshot filename.')
    output.parent.mkdir(parents=True,exist_ok=True)
    merged.to_csv(output,index=False)
    print('Records:',len(merged),'distinct report dates:',merged.date.nunique())
    print('Monthly records:\n'+merged.groupby(merged.date.str[:7]).size().to_string())
    print('SHA-256:',hashlib.sha256(output.read_bytes()).hexdigest())
    print('Coverage must be reconciled with the monitor and boundary-day downloads.')
    return merged

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('export_directory')
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    combine(args.export_directory,args.output)
