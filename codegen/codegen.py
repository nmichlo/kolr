from pprint import pprint

from bs4 import BeautifulSoup
from kolr.util.util import fetch_url, overwrite_file
from terminaltables import AsciiTable


def _format_cell_text(text):
    import re
    text = text.strip().replace('\xa0', ' ')  # &nbsp; Non breaking space
    text = re.sub('\[.+?\]', '', text)
    try:
        return int(text)
    except:
        pass
    try:
        return tuple(int(d) for d in text.split(','))
    except:
        pass
    return text


def _format_table(table, postfix=None):
    table = [[_format_cell_text(cell.text) for cell in row] for row in table]
    from kolr.palette import ColorPalette
    names = ColorPalette.generate_unique_names(table[0])[0]
    postfix = postfix if postfix is not None else ""
    table = [[f'    T{postfix}(', *(f'{name}={cell.__repr__()}{", " if i < len(row) - 1 else ""}' for i, (name, cell) in enumerate(zip(names, row))), '),'] for row in table[1:]]
    table = AsciiTable(table)
    table.outer_border = False
    table.inner_column_border = False
    table.inner_heading_row_border = False
    table.padding_left = 0
    table.padding_right = 0
    table = f'T{postfix} = namedtuple(\'_NamedTuple{postfix}\', [{", ".join(n.__repr__() for n in names)}])\n' + f'L{postfix} = [\n{table.table}\n]'
    return table




def _expand_table(header, rows, skip_fullwidth=False, skip_malformed=True):
    def cspan(c): return int(c.get('colspan', 1))
    def rspan(c): return int(c.get('rowspan', 1))

    # Expand
    table, span_table = [header], [[1] * len(header)]
    for line in rows:
        # if must skip row
        fullwidth, skip = False, False
        if sum(cspan(cell) for cell in line) > len(header):
            fullwidth, skip = True, skip_malformed
            print('Malformed Line:', line)
        if skip or (skip_fullwidth and fullwidth and len(header) > 1):
            print('Skipping:', line)
            span_table[-1] = [min(i-1, 1) for i in span_table[-1]]  # adjust previous rows
            continue
        # Expand horr
        line = [cell for cell in line for i in range(cspan(cell))]
        # Expand vert from previous
        row, spans = [], []
        for prev_cell, prev_rowspan in zip(table[-1], span_table[-1]):
            if prev_rowspan > 1:
                cell, rowspan = prev_cell, prev_rowspan-1
            else:
                line, cell, rowspan = line[1:], line[0], rspan(line[0])
            row.append(cell)
            spans.append(rowspan)
        # append
        table.append(row)
        span_table.append(spans)
    return table

def _get_wikipedia_tables(url):
    soup = BeautifulSoup(fetch_url(url), "html.parser")
    elems = [
        soup.select_one('h1'),
        *(elem for elem in soup.select_one('div.mw-parser-output').children if elem.name in {'h2', 'h3', 'table'})
    ]
    def _elems_as_name(*elems):
        import re
        from kolr.palette import ColorPalette
        return '___'.join([ColorPalette.standardised_name(re.sub('\[[Ee]dit\]', '', elem.text.strip())).strip('_') for elem in elems if elem])
    # name stack
    h1, h2, h3, tables = None, None, None, []
    for elem in elems:
        if elem.name in {'h1'}:
            h1, h2, h3 = elem, None, None
        elif elem.name in {'h2'}:
            h2, h3 = elem, None
        elif elem.name in {'h3'}:
            h3 = elem
        elif elem.name in {'table'}:
            if 'wikitable' not in elem.attrs['class']:
                continue
            name = _elems_as_name(h1, h2, h3, elem.select_one('caption'))
            tables.append((name, elem))
    return tables


def _gen_python_from_wikipedia_tables(page, name=None):
    strings, url = [], f'https://en.wikipedia.org/wiki/{page}'
    name = (url if name is None else name)
    # imports & heading
    strings.append(f'\nfrom collections import namedtuple\n\n')
    strings.append(f'\n# {"="*73} #\n# {name}{" "*(73-len(name))} #\n# {"="*73} #\n\n\n')
    # get and append tables
    for (name, table) in _get_wikipedia_tables(url):
        # generate table
        header = table.select("tr th")
        entries = [row.find_all("td") for row in table.select("tr + tr")]
        table = _expand_table(header, entries)
        # append formatted table
        strings.append(str(_format_table(table, postfix=f'_{name}')))
        strings.append('\n\n')
    # return
    return ''.join(strings)


def _save_python_from_wikipedia_tables(page):
    python = _gen_python_from_wikipedia_tables(page)
    print(python)
    from kolr.palette import ColorPalette
    import os
    os.makedirs('gen', exist_ok=True)
    overwrite_file(f'gen/{ColorPalette.standardised_name(page)}.py', python)


if __name__ == '__main__':
    _save_python_from_wikipedia_tables('ANSI_escape_code')
    _save_python_from_wikipedia_tables('C0_and_C1_control_codes')