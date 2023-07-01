import re
def get_string(prompt):
    if not isinstance(prompt, str):
        raise TypeError("prompt must be of type str")
    try:
        return input(prompt)
    except EOFError:
        return None
def get_int(prompt):
    while True:
        s = get_string(prompt)
        if s is None:
            return None
        if re.search(r"^[+-]?\d+$", s):
            try:
                return int(s, 10)
            except ValueError:
                pass