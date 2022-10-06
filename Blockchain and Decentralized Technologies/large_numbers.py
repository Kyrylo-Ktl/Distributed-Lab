import secrets
from time import time
from typing import Callable


def return_time(function: Callable) -> Callable:
    def wraps(*args, **kwargs):
        start = time()
        function(*args, **kwargs)
        return time() - start

    return wraps


def get_number_of_keys(bits: int) -> int:
    return 2 ** bits


def get_secret_token(bits: int) -> str:
    return '0x' + secrets.token_hex(bits // 8)


@return_time
def brute(bits: int, secret: str) -> bool:
    for candidate in range(0, get_number_of_keys(bits) + 1):
        if hex(candidate) == secret:
            return True
    return False


if __name__ == '__main__':
    N_BITS = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

    for n_bits in N_BITS:
        print(f'Number of bits: {n_bits}')
        print(f'Number of keys: {get_number_of_keys(n_bits)}')
        token = get_secret_token(n_bits)
        print(f'Generated secret: {token}')
        print(f'Seconds for a crack: {brute(n_bits, token)}\n')
