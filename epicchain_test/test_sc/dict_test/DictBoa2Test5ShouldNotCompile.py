from typing import Any

from boa3.builtin.compile_time import public


@public
def main() -> Any:
    d = {
        'a': 1,
        'b': {'a': 2},
    }
    return d['b']
