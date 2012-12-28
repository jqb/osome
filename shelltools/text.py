
def wrap(text, width):
    """
    A word-wrap function that preserves existing line breaks and most spaces in
    the text. Expects that existing line breaks are posix newlines.

    https://github.com/django/django/blob/master/django/utils/text.py
    """
    def _generator():
        it = iter(text.split(' '))
        word = next(it)
        yield word
        pos = len(word) - word.rfind('\n') - 1
        for word in it:
            if "\n" in word:
                lines = word.split('\n')
            else:
                lines = (word,)
            pos += len(lines[0]) + 1
            if pos > width:
                yield '\n'
                pos = len(lines[-1])
            else:
                yield ' '
                if len(lines) > 1:
                    pos = len(lines[-1])
            yield word
    return ''.join(_generator())


def text_list(list_, last_word='or'):
    """
    >>> get_text_list(['a', 'b', 'c', 'd'])
    'a, b, c or d'
    >>> get_text_list(['a', 'b', 'c'], 'and')
    'a, b and c'
    >>> get_text_list(['a', 'b'], 'and')
    'a and b'
    >>> get_text_list(['a'])
    'a'
    >>> get_text_list([])
    ''

    https://github.com/django/django/blob/master/django/utils/text.py
    """
    if len(list_) == 0: return ''
    if len(list_) == 1: return list_[0]
    return '%s %s %s' % (
        ', '.join([i for i in list_][:-1]),
        last_word, list_[-1])


if __name__ == "__main__":
    text = \
"""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis sollicitudin lacinia risus,
"""
    print wrap(text, 30)
    print text_list(["black", "red", "blue", "green"])
    print text_list(["black", "red", "blue", "green"], "and")