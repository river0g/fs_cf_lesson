# firestoreのやりとりにおいて不要な物や必要なもの(date)などを操作する。
# todo: このファイルをserializerとし後日実装。
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class Record(BaseModel):
    name: str
