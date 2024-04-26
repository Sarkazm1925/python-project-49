from .texts import welcome_user, request, conclusion, victory
from .logic import generator, is_valid_answer, even
from .logic import is_integer, calculate, get_gcd, prime
from .const import GAME_LIMIT, SIGNS
from .cli import welcome_user as welcome_user1

__all__ = ('welcome_user', 'request', 'conclusion', 'victory',
           'generator', 'is_valid_answer', 'even', 'prime',
           'is_integer', 'calculate', 'GAME_LIMIT', 'SIGNS',
           'get_gcd', 'welcome_user1')
