# -*- coding: utf-8 -*-

# Copyright (c) 2011, Kenneth Reitz <me@kennethreitz.com>

# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.

# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


from __future__ import absolute_import

import sys
import time

STREAM = sys.stderr
# Only show bar in terminals by default (better for piping, logging etc.)
try:
    HIDE_DEFAULT = not STREAM.isatty()
except AttributeError:  # output does not support isatty()
    HIDE_DEFAULT = True

BAR_TEMPLATE = '%s[%s%s] %i/%i - %s\r'
MILL_TEMPLATE = '%s %s %i/%i\r'

DOTS_CHAR = '.'
BAR_FILLED_CHAR = '#'
BAR_EMPTY_CHAR = ' '
MILL_CHARS = ['|', '/', '-', '\\']

#How long to wait before recalculating the ETA
ETA_INTERVAL = 1
#How many intervals (excluding the current one) to calculate the simple moving average
ETA_SMA_WINDOW = 9


class progress(object):

    def __new__(
        self, it, label='', width=32, hide=HIDE_DEFAULT,
        empty_char=BAR_EMPTY_CHAR, filled_char=BAR_FILLED_CHAR,
        expected_size=None
    ):

        def _show(_i):
            if (time.time() - self.etadelta) > ETA_INTERVAL:
                self.etadelta = time.time()
                self.ittimes = self.ittimes[-ETA_SMA_WINDOW:]+[-(self.start-time.time())/(_i+1)]
                self.eta = sum(self.ittimes)/float(len(self.ittimes)) * (count-_i)
                self.etadisp = time.strftime('%H:%M:%S', time.gmtime(self.eta))
            x = int(width*_i/count)
            if not hide:
                STREAM.write(BAR_TEMPLATE % (
                label, filled_char*x, empty_char*(width-x), _i, count, self.etadisp))
                STREAM.flush()

        count = len(it) if expected_size is None else expected_size

        self.start    = time.time()
        self.ittimes  = []
        self.eta      = 0
        self.etadelta = time.time()
        self.etadisp  = time.strftime('%H:%M:%S', time.gmtime(self.eta))

        if count:
            _show(0)

        for i, item in enumerate(it):

            yield item
            _show(i+1)

        if not hide:
            STREAM.write('\n')
            STREAM.flush()

    @classmethod
    def dots(cls, it, label='', hide=HIDE_DEFAULT):
        """Progress iterator. Prints a dot for each item being iterated"""

        count = 0

        if not hide:
            STREAM.write(label)

        for item in it:
            if not hide:
                STREAM.write(DOTS_CHAR)
                sys.stderr.flush()

            count += 1

            yield item

        STREAM.write('\n')
        STREAM.flush()

    @classmethod
    def mill(cls, it, label='', hide=HIDE_DEFAULT, expected_size=None):
        """Progress iterator. Prints a mill while iterating over the items."""

        def _mill_char(_i):
            if _i == 100:
                return ' '
            else:
                return MILL_CHARS[_i % len(MILL_CHARS)]

        def _show(_i):
            if not hide:
                STREAM.write(MILL_TEMPLATE % (
                    label, _mill_char(_i), _i, count))
                STREAM.flush()

        count = len(it) if expected_size is None else expected_size

        if count:
            _show(0)

        for i, item in enumerate(it):

            yield item
            _show(i+1)

        if not hide:
            STREAM.write('\n')
            STREAM.flush()
