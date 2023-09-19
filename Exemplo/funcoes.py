def abc(a: int, s: str) -> int:
    print('abc', a, s)
    return a


def double_int(x: int) -> int:
    return x * 2


def say_hello() -> str:
    return 'Ola'


def half_float(x: float) -> float:
    return x/2


def favorite_number(x: int) -> bool:
    return_bool = False
    if x == 713:
        return_bool = True
    return return_bool


def doggo_test(s: str) -> str:
    string = s + s
    string_again = string + string
    return string_again


def rpc_test() -> str:
    print('Estou no servidor!')
    return 'Estou no cliente!'


def bye_basilio()-> str:
    return 'Bom descanso Basilio!'
