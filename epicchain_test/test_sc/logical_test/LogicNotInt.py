from boa3.builtin.compile_time import public


@public
def Main(a: int) -> int:
    return ~a
