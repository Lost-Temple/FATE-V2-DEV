#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import enum
import os


class TaskMode(enum.Enum):
    SIMPLE = "SIMPLE"
    DEEPSPEED = "DEEPSPEED"

    def __str__(self):
        return self.value


def is_deepspeed_mode():
    return os.getenv("FATE_TASK_TYPE", "").upper() == TaskMode.DEEPSPEED.value


def is_root_worker():
    if is_deepspeed_mode():
        return os.getenv("RANK", "0") == "0"
    return True
