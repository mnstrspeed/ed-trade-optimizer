from itertools import repeat

def center(text=None, width=0, fill=' '):
    return ((width - len(text or '')) / 2) * fill + (text or '') + ((width - len(text or '') + 1) / 2) * fill
def right(text=None, width=0, fill=' '):
    return (width - len(text or '')) * fill + (text or '')
def left(text=None, width=0, fill=' '):
    return (text or '') + (width - len(text or '')) * fill

def line(width, text="", char=u'\u2500'):
    return center(text, width, fill=char)

def column(columns, separator=' ', width=0, align=repeat(left)):
    widths = [max(map(len, rows)) for rows in columns]
    iterators = map(iter, columns)
    separator = max(1, int((width - sum(widths)) / (len(columns) - 1))) * separator
    for _ in range(max(map(len, columns))):
        yield separator.join([a(text=next(r, None), width=w) for (r, w, a) in zip(iterators, widths, align)])
