def safe_find(str, sym):
    idx = str.find(sym)
    if idx == -1:
        raise Exception('Error: Invalid html string')
    return idx


def parse_html(html_str,
               open_tag_callback=None,
               data_callback=None,
               close_tag_callback=None):
    while html_str:
        if html_str[0] != '<':
            idx = safe_find(html_str, '<')
            tag = html_str[:idx]
            html_str = html_str[idx:]
            if data_callback:
                data_callback(tag)
        else:
            idx = safe_find(html_str, '>')
            tag = html_str[:idx+1]
            if html_str[1] == '/':
                if close_tag_callback:
                    close_tag_callback(tag)
            else:
                if open_tag_callback:
                    open_tag_callback(tag)
            html_str = html_str[idx+1:]
