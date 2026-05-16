import os
import pandas as pd
import s3fs

BUCKET = "bloc-grip-2026-kl"
LOCAL_DATA_DIR = "data"

def read_csv(key: str, use_s3: bool = True, **kwargs) -> pd.DataFrame:
    if use_s3:
        return pd.read_csv(f"s3://{BUCKET}/{key}", **kwargs)
    return pd.read_csv(os.path.join(LOCAL_DATA_DIR, key), **kwargs)

def read_parquet(key: str, use_s3: bool = True, **kwargs) -> pd.DataFrame:
    if use_s3:
        return pd.read_parquet(f"s3://{BUCKET}/{key}", **kwargs)
    return pd.read_parquet(os.path.join(LOCAL_DATA_DIR, key), **kwargs)

def write_parquet(df: pd.DataFrame, key: str, use_s3: bool = True, **kwargs) -> None:
    if use_s3:
        df.to_parquet(f"s3://{BUCKET}/{key}", index=False, **kwargs)
    else:
        df.to_parquet(os.path.join(LOCAL_DATA_DIR, key), index=False, **kwargs)
