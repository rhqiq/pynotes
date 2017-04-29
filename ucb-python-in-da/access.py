public_var = 1
_private_var = 2

__all__ = ['public_var', '_private_fun', 'public_fun']


def public_fun():
    print('public ...')


def _private_fun():
    print('private...')   