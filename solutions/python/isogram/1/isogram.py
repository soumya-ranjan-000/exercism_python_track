def is_isogram(string):
    t_list = [x for x in string.lower() if not x.isspace() and not x == '-']
    t_set = set(t_list)
    if len(t_set) != len(t_list):
        return False
    else:
        return True


