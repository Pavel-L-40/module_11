from pprint import pprint


def introspection_info(obj):
    dikt_ = {}
    dikt_['type'] = type(obj)
    dikt_['methods'] = dir(obj)
    return dikt_
number_info = introspection_info(42)
pprint(number_info)