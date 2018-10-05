import re

# refactored for python3
# 
# I can't take credit for this, credit belongs to Michael Urman https://codereview.stackexchange.com/users/32004/michael-urman
# I have extended this to account for other issues that I have found
#
# https://codereview.stackexchange.com/questions/62435/robustly-dealing-with-malformed-unicode-files


def find_encoding_problems(line, line_number, counter):
    try:
        line.encode('ascii')
    except UnicodeEncodeError:
        print("WARNING: Encoding error in line", i+1)
        counter += 1

def find_tab_characters(line, line_number):
    if (re.search(r'\t', line) is not None):
        print("WARNING: tab character located on line", line_number)

def find_backslash_characters(line, line_number):
    if (re.search(r"\\", line) is not None):
        print("WARNING: backslash character located on line", line_number)

def find_single_tick_characters(line, line_number):
    if (re.search(r"[^\']\'[^\']", line) is not None):
        print("WARNING: single tick character located on line",line_number)

if __name__ == "__main__":
    filename = "file.json"
    unicodeerror = 0
    for i, line in enumerate(open(filename, "r", encoding="latin")):
        # calculate line number
        line_number = i+1
        # search for unicode characters
        find_encoding_problems(line, line_number, unicodeerror)
        # search for tabs
        find_tab_characters(line, line_number)
        # search for backslash
        find_backslash_characters(line, line_number)
        # search for single ticks
        find_single_tick_characters(line, line_number)

    # raise error if unicode is just atrocious
    if unicodeerror > 5:
        raise StandardError("ERROR: Too many Unicode errors")