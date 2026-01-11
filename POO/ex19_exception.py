
class MeuError(Exception):
    ...


def lancando():
    exception_ = MeuError("Meu Erro")
    exception_.add_note("Você errou nisso")
    raise exception_

try:
    #1/0
    lancando()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    print(type(error))
    print(error.__notes__)
