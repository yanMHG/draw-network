from typing import Callable, Optional

import pandas as pd

from .geodraw import geoBrazilUFDrawNetwork


def _draw(
    df: pd.DataFrame,
    decorator: Callable,
    src_col: Optional[str] = None,
    dest_col: Optional[str] = None,
    ij_col: Optional[str] = None,
    jk_col: Optional[str] = None,
    **kwargs,
):
    df_reindexed = df.set_index([src_col, dest_col])
    try:
        ij = df_reindexed[ij_col].to_dict()
    except KeyError:
        ij = {}
    try:
        jk = df_reindexed[jk_col].to_dict()
    except KeyError:
        jk = {}
    return decorator(ij, jk, **kwargs)


def geoBrazilUFDrawDataframe(
    df: pd.DataFrame,
    src_col: Optional[str] = None,
    dest_col: Optional[str] = None,
    ij_col: Optional[str] = None,
    jk_col: Optional[str] = None,
    **kwargs,
):
    return _draw(
        df, geoBrazilUFDrawNetwork, src_col, dest_col, ij_col, jk_col, **kwargs
    )
