def safe_find(str, sym):
    idx = str.find(sym)
    if idx == -1:
        raise Exception('Error: Invalid html string')
    return idx


def parse_html(html_str,
               open_tag_callback=None,
               data_callback=None,
               close_tag_callback=None):
    cur_pos = 0
    while cur_pos < len(html_str)-1:
        if html_str[cur_pos] != '<':
            new_pos = cur_pos + safe_find(html_str[cur_pos:], '<')
            if data_callback:
                data_callback(html_str[cur_pos:new_pos])
            cur_pos = new_pos
        else:
            new_pos = cur_pos + safe_find(html_str[cur_pos:], '>') + 1
            if html_str[cur_pos+1] == '/':
                if close_tag_callback:
                    close_tag_callback(html_str[cur_pos:new_pos])
            else:
                tag, *attr_list = html_str[cur_pos:new_pos-1].split(' ')
                attributes = dict()
                for attr in attr_list:
                    key, val = attr.split('=')
                    attributes[key] = val
                if open_tag_callback:
                    open_tag_callback(tag + '>', attributes)
            cur_pos = new_pos
