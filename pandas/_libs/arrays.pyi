from collections.abc import Sequence

import numpy as np

from pandas._typing import (
    AxisInt,
    DtypeObj,
    Self,
    Shape,
)

class NDArrayBacked:
    _dtype: DtypeObj
    _ndarray: np.ndarray
    def __init__(self, values: np.ndarray, dtype: DtypeObj) -> None: ...
    @classmethod
    def _simple_new(cls, values: np.ndarray, dtype: DtypeObj) -> Self: ...
    def _from_backing_data(self, values: np.ndarray) -> Self: ...
    def __setstate__(self, state) -> None: ...
    def __len__(self) -> int: ...
    @property
    def shape(self) -> Shape: ...
    @property
    def ndim(self) -> int: ...
    @property
    def size(self) -> int: ...
    @property
    def nbytes(self) -> int: ...
    def copy(self, order=...) -> Self: ...
    def delete(self, loc, axis=...) -> Self: ...
    def swapaxes(self, axis1, axis2) -> Self: ...
    def repeat(self, repeats: int | Sequence[int], axis: int | None = ...) -> Self: ...
    def reshape(self, *args, **kwargs) -> Self: ...
    def ravel(self, order=...) -> Self: ...
    @property
    def T(self) -> Self: ...
    @classmethod
    def _concat_same_type(
        cls, to_concat: Sequence[Self], axis: AxisInt = ...
    ) -> Self: ...
