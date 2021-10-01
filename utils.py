
def call_if_value_is_callable(a_dict: dict) -> None:
    """Call values from a dictionary if they are callable

    :param a_dict: a dict
    """

    if isinstance(a_dict, dict):
        for key, value in a_dict.items():
            if callable(value):
                a_dict[key] = value()
