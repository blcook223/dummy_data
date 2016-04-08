"""
Generators to read data and evaluate dummy data tags.
"""

from collections import OrderedDict
from json import loads, dumps

from .evaluators import evaluate_parsed


def generate_json(data):
    """
    Parse json and call evaluator.
    """
    return dumps(evaluate_parsed(loads(data, object_pairs_hook=OrderedDict)))
