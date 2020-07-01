import re

COMMENTS_NO_MACROS = (";", "/")
COMMENTS = (*COMMENTS_NO_MACROS, "#")

def is_comment(line):
    return line.strip().startswith(COMMENTS) or re.match(r"^\s*$", line)

def remove_comments(line, macro = False):
    characters = COMMENTS_NO_MACROS if macro else COMMENTS
    for character in characters:
        line = line.partition(character)[0]

    return line.strip()
    
def clean_raw(raw):
    return [remove_comments(line.strip()) for line in raw.splitlines() if not is_comment(line)]
    
def is_end(line):
    return line.lower().strip() == "end"
    
def read_file(path):
    for encoding in ["utf-8", "windows-1252", "latin-1"]:
        try:
            with open(path, "r", encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            pass
            
    raise UnicodeDecodeError
