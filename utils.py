import re

TWEET_LENGTH = 140

def remove_extra_spaces(s):
    regexes = [
        (r"\n", " "),
        (r"\s\s+", " ")
    ]
    x = s.strip()
    for reg, repl in regexes:
        x = re.sub(reg, repl, x)
    return x

def get_first_n_char(source_text, n):
    while 0 < n < len(source_text) and source_text[n] != " ":
        n -= 1
    return source_text[:n].strip(), n

def tweet_generator(source_text):
    start_index = 0
    username = yield
    while True:
        text, text_length = get_first_n_char(
            source_text[start_index:], TWEET_LENGTH-len(f".@${username} "))
        if not text: # restart generator
            text = source_text
            start_index = 0
        else:
            start_index += text_length
            username = yield text
