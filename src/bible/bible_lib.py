import os


def is_letter(char):
    return str.isalnum(char)


def write_index_file(filename, linenumber, val):
    filepath = os.path.dirname(filename)
    # create file path if it does not exist
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    # linebumber == 1, create a new file, or append new content to the file
    if linenumber == 1:
        f = file(filename, 'wb')
    else:
        f = file(filename, 'ab')
    content = "Line %d: %s %s" % (linenumber, ', '.join(val), os.linesep)
    f.write(content)
    f.close()


def process_line(linebumber, line):
    print "processing line %d" % linebumber
    words_hash = split_word(line)
    for (key, val) in words_hash.items():
        filename = os.path.join(os.getcwd(), 'index', key + '.txt')
        write_index_file(filename, linebumber, val)


def split_word(line):
    str_len = len(line)
    words_hash = {}
    word_start, word_start_pos, word_end_pos = False, 0, 0

    for i in range(0, str_len):
        # for a word's beginning
        if is_letter(line[i]) and (not word_start):
            word_start, word_start_pos = True, i

        # for a word's ending
        if (not is_letter(line[i])) and word_start:
            word_start, word_end_pos = False, i
            word = line[word_start_pos:word_end_pos]
            words_hash.setdefault(word.lower(), []).append(str(word_start_pos))

    return words_hash
