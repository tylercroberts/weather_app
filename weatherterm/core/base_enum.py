from enum import Enum


class BaseEnum(Enum):
    def _generate_next_value_(self, name, start, count, last_value):
        return name