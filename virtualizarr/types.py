from typing import Any, Literal, NewType, Optional, Tuple, TypedDict

import numpy as np

ChunkKey = NewType("ChunkKey", str)  # a string of the form '1.0.1' etc.

# TODO replace these with classes imported directly from Zarr?
ZAttrs = NewType(
    "ZAttrs", dict[str, Any]
)  # just the .zattrs (for one array or for the whole store/group)


# TODO use a dataclass instead?
class ZArray(TypedDict):
    """Just the .zarray information"""

    chunks: Tuple[int, ...]
    compressor: Optional[str]
    dtype: np.dtype
    fill_value: Optional[float]  # float or int?
    filters: Optional[str]
    order: Literal["C"] | Literal["F"]
    shape: Tuple[int, ...]
    zarr_format: int


# Distinguishing these via type hints makes it a lot easier to keep track of what the opaque kerchunk "reference dicts" actually mean
# (idea from https://kobzol.github.io/rust/python/2023/05/20/writing-python-like-its-rust.html)
KerchunkStoreRefs = NewType(
    "KerchunkStoreRefs", dict[Literal["version"] | Literal["refs"], int | dict]
)  # top-level dict with keys for 'version', 'refs'
KerchunkArrRefs = NewType(
    "KerchunkArrRefs",
    dict[Literal[".zattrs"] | Literal[".zarray"] | str, ZArray | ZAttrs | dict],
)  # lower-level dict containing just the information for one zarr array
