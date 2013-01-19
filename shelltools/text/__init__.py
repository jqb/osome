from shelltools.text.progress import progress


def wrap(text, width):
    """
    A word-wrap function that preserves existing line breaks and most spaces in
    the text. Expects that existing line breaks are posix newlines.

    .. code-block:: python

        >>> print wrap("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis sollicitudin ", 30)
        Lorem ipsum dolor sit amet,
        consectetur adipiscing elit.
        Duis sollicitudin

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


def text_list(words, last_word='and'):
    """

    .. code-block:: python

        >>> get_text_list(['a', 'b', 'c', 'd'])
        'a, b, c and d'

        >>> get_text_list(['a', 'b', 'c'], 'or')
        'a, b or c'

        >>> get_text_list(['a', 'b'], 'or')
        'a or b'

        >>> get_text_list(['a'])
        'a'

        >>> get_text_list([])
        ''

    """
    if len(words) == 0: return ''
    if len(words) == 1: return words[0]
    return '%s %s %s' % (
        ', '.join([i for i in words][:-1]),
        last_word, words[-1])



if __name__ == "__main__":
    pass

