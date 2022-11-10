# firestoreのやりとりにおいて不要な物や必要なもの(date)などを操作する。
# todo: このファイルをserializerとし後日実装。

from . import config
from datetime import datetime
from typeing import List, Optional
from pydantic import BaseModel


class Record(BaseModel):
    name: string
