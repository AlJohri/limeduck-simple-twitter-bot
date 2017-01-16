from utils import *
import itertools, textwrap

def test_remove_extra_spaces():

    input_text = textwrap.dedent("""
        Call me Ishmael. Some years ago- never mind how long precisely-
        having little or no money in my purse, and nothing particular to
        interest me on shore, I thought I would sail about a little and see
        the watery part of the world.""")

    output_text = (
        "Call me Ishmael. Some years ago- never mind how "
        "long precisely- having little or no money in my purse, "
        "and nothing particular to interest me on shore, I thought "
        "I would sail about a little and see the watery part of the world.")

    assert remove_extra_spaces(input_text) == output_text

def test_get_first_n_char():

    input_text = (
        "Call me Ishmael. Some years ago- never mind how "
        "long precisely- having little or no money in my purse, "
        "and nothing particular to interest me on shore, I thought "
        "I would sail about a little and see the watery part of the world.")

    output_text = (
        'Call me Ishmael. Some years ago- never mind how long precisely- '
        'having little or no money in my purse, and nothing particular to '
        'interest me')

    assert get_first_n_char(input_text, 140) == (output_text, 140)

    input_text2 = (
        "Whenever I find myself growing grim about the mouth; whenever "
        "it is a damp, drizzly November in my soul; whenever I find myself "
        "involuntarily pausing before coffin warehouses, and bringing up the "
        "rear of every funeral I meet; and especially whenever my hypos get "
        "such an upper hand of me, that it requires a strong moral principle "
        "to prevent me from deliberately stepping into the street, and "
        "methodically knocking people's hats off- then, I account it high "
        "time to get to sea as soon as I can.")

    output_text2 = (
        'Whenever I find myself growing grim about the mouth; whenever it '
        'is a damp, drizzly November in my soul; whenever I find myself')

    assert get_first_n_char(input_text2, 140) == (output_text2, 127)
