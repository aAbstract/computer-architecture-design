import code
import inspect
import readline
from rlcompleter import Completer


def spawn_shell():
    caller_locals = inspect.currentframe().f_back.f_locals
    readline.set_completer(Completer(caller_locals).complete)
    readline.parse_and_bind("tab: complete")
    code.interact(local=caller_locals)
