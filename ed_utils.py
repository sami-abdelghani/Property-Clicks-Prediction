"""
File name: ed_utils.py
Author: Edward Bujak
Date created: 2018.04.28
Date last modified: 2023.12.16
Python Version: 3.11.5 (that ed_utils was tested with)

collection of utility functions and classes

Functions:
    _inspector
    adder
    column_str
    five_number_summary
    five_number_summary2
    get_memory_info
    grep
    head
    inspector
    is_latitude
    is_longitude
    is_this_life_as_we_know_it
    ls_l - only available on unix-like Operating systems, not Windows
    meaning_of_life
    pp
    print_function_annotations
    speak
    tail
    tree
    versions
    wc

Classes:
    HiddenPrints
    DummyContextManager


Dependencies (aka requirements.txt)
    gtts
    playsound
for non-Windows OS:
    termcolor,
    xattr,
    pwd,
    grp


anytime ed_utils.py is changed, also need to restart kernel for all .IPYNB files that import ed_utils
or
you must reload it:

import importlib
importlib.reload(ed_utils)
ed_utils.__version__
"""

# module level dunder names
__version__ = '0.4.4'
version = __version__
__title__ = "ed_utils"
__summary__ = "Collection of useful utility functions and classes."
# __uri__ = "https://github.com/ebujak__/ed_utils" 
__author__ = "Edward Bujak"

# __copyright__ = "Copyright 2018-2023, The Edward Bujak Python Project"
__copyright__ = "Copyright 2018-2023 {0}".format(__author__)
__credits__ = ["Edward Bujak"]
__license__ = "GPL"
__maintainer__ = "Edward Bujak"
__email__ = "Edward_Bujak@hotmail.com"
__status__ = "Never Ending Development"

__dunders__ = ["__title__", "__summary__",
               # "__uri__",
               "__version__", "__author__",
               "__email__", "__license__", "__copyright__",
               '__classes__', '__functions__', '__all__', '__history__',
              ]
               
__classes__ = ['HiddenPrints', 'DummyContextManager']
__functions__ = ['_inspector', 'adder', 'column_str', 'five_number_summary', 'five_number_summary2',
                 'is_this_life_as_we_know_it', 'ls_l', 'meaning_of_life', 'pp',
                 'print_function_annotations', 'speak', 'tail',
                 'tree', 'versions', 'wc'
                 ]
#  __all__ list defines what will be imported from ed_utils.py when the statement
# from ed_utils import *
# is used. In this case, only those elements in the __all_ list will be imported from ed_utils.py.
__all__ = __functions__ + __classes__

__history__ = """
0.4.4 - 2023.12.16 - Edward Bujak - added print_function_annotations() function
0.4.3 - 2023.12.15 - Edward Bujak - changed __copyright__ attribute
                                    added __title__ attribute
                                    added __summary__ attribute
                                    added __dunders__ attribute
0.4.2 - 2023.12.14 - Edward Bujak - added versions() function
0.4.1 - 2023.12.13 - Edward Bujak - added is_latitude() function
                                    added is_longitude() function
                                    added __functions__ attribute
                                    added __classes__ attribute
                                    added __all__ attribute
0.4.0 - 2023.12.09 - Edward Bujak - corrected some documentation and comments
                                    rewrote wc() function; now takes optional arguments
0.3.9 - 2023.10.30 - Edward Bujak - handled conditional import of: termcolor (only in non-Windows OS,
                                    needed for ls_l() function) gtts, and playsound
0.3.8 - 2023.10.29 - Edward Bujak - added DummyContextManager
                                    enhaced tree() function to accept no arguments in which case it will act on
                                        the current working directory
                                    removed this lengthly "history" from module docstring and put into module
                                        variable "ed_utils.__history__"
0.3.7 - 2023.10.04 - Edward Bujak - added tree() function.  There is tree on the commmand line in Windows, macOS.
0.3.6 - 2023.09.28 - Edward Bujak - added code to handle Windows (not unix) issues with ls_l() function due to 
                                        xattr, termcolor, pwd
0.3.5 - 2023.05.06 - Edward Bujak - added grep() function
0.3.4 - 2023.04.22 - Edward Bujak - added ls_l() function
0.3.3 - 2023.04.21 - Edward Bujak - enhanced head() and tail(), and wc() functions with optional/default
                                    encoding='utf-8' to handle files with special characters; and
                                    Windows default not being "utf-8"
0.3.2 - 2023.04.18 - Edward Bujak - added speak() function
0.3.1 - 2023.03.04 - Edward Bujak - enhanced column_str() to handle empty str without raising exception
0.3.0 - 2023.03.03 - Edward Bujak - added head() function
                                    added tail() function
_._._ - 2023.02.__ - Edward Bujak - lost ~1.5 months coding (internal drive failure) ... so slowly recreating
0.2.0 - 2022.12.05 - Edward Bujak - added column_str() function
                                    added wc() function
                                    added "__version__" and "version" to all functions
                                        examples: column_str.__version__, column_str.version
                                    added type hints:
                                        Numeric = Union[float, int, complex, np.number]
                                        usage: from ed_utils import Numeric
0.1.9 - 2022.12.03 - Edward Bujak - corrected some misspellings
                                    changed
                                        FloatIntComplex = Union[float, int, complex]
                                    to
                                        Numeric = Union[float, int, complex, np.number]
0.1.8 - 2022.11.18 - Edward Bujak - added HiddenPrints class,
                                    added new inspector() function to take optional "verbose" parameter (default=False) calls                                         "old" inspector() now renamed _inspector()
                                    added type hints/annotations for all functions and HiddenPrints class
0.1.7 - 2021.02.0_ - Edward Bujak - added "Please wait ..." to _display_pip_list()
                                    improved printing of attributes, methods, classes to stand out more and removed space character on line
                                    enhanced "experimental" code to determine if input is iterable - multipe methods used - contradictory!
0.1.6 - 2021.02.04 - Edward Bujak - added "experimental" code for determining is input is iterable - uses collections.abc.Iterable
0.1.5 - 2021.01.26 - Edward Bujak - added get_memory_info() - currently only for Windows
0.1.4 - 2020.10.23 - Edward Bujak - added five_number_summary2()
0.1.3 - 2020.10.06 - Edward Bujak - generalized _display_pip_list()
0.1.2 - 2020.10.03 - Edward Bujak - fixed Windows bug on pip list
                                    only do memory size if an instance
0.1.1 - 2020.09.30 - Edward Bujak - fixed bug with supplying data types such as dict, list, int, ...
                                    fixed bug to not do length of data types that are iterable
                                    added memory size
0.1.0 - 2020.09.29 - Edward Bujak - fixed object --> object_
0.0.9 - 2020.09.29 - Edward Bujak - fixed bug in inspector() function, built-in modules (like time) have no attribute __file__ 
0.0.8 - 2020.09.28 - Edward Bujak - added inspector() function
0.0.7 - 2020.08.08 - Edward Bujak - changed meaning_of_life to properly return 42, added version, updated copyright
0.0.6 - 2020.07.18 - Edward Bujak - added five_number_summary()
0.0.5 - 2018.06.25 - Edward Bujak - added more test code __name__ == "__main__"
0.0.4 - 2018.05.09 - Edward Bujak - added pp() detection of ndarray returned message that ndarray is not yet suported
                                    put in code to deal with the specifc ndarray of 2 dimensions, aka matrix
0.0.3 - 2018.05.08 - Edward Bujak - added pp() detection of set and zip data types and returned
                                    informative message that these are not yet suported
0.0.2 - 2018.05.06 - Edward Bujak - added more pp() test cases
0.0.1 - 2018.04.28 - Edward Bujak - added __main__ driver with test cases
"""

# print('ed_utils: __name__ is {}'.format(__name__))
    
# -------------------------------------------------------------------------------------------------------

# Type hints/annotations used within ed_utils.py module
from typing import (
    Any,   # for column_str()
#     Callable,
#     Dict,
#     Generic,
#     Hashable,
#     Iterable,
#     Iterator,
#     IO,
#     List,
#     NoReturn,
    Optional,   # for head(), tail(), speak(), grep()
#     Sequence,
    Tuple,   # for wc()
    Union,
#     TypeVar,
#     cast,
#     overload,
#     TYPE_CHECKING,
)

from collections.abc import Iterable   # for column_str()
                                       # examples of Iterable: list, tuple, set

import numpy as np   # for .number

Numeric = Union[float, int, complex, np.number]
# usage:
#   from ed_utils impoyt Numeric

# -------------------------------------------------------------------------------------------------------

def meaning_of_life() -> int:
    """Test function that returns 42."""
    # print('ed_utils.meaning_of_life() test')
    return 42

meaning_of_life.__version__ = meaning_of_life.version = '0.1'

# -------------------------------------------------------------------------------------------------------

def is_this_life_as_we_know_it() -> None:
    '''Returns None.'''
    pass

is_this_life_as_we_know_it.__version__ = is_this_life_as_we_know_it.version = '0.1'
    
# -------------------------------------------------------------------------------------------------------

import os   # for getcwd(), listdir(), ...

class DirectoryNotFoundError(Exception):
    pass

def tree(path:  Optional[str] = None,
         indent: Optional[int] = 0,
         ignore_hidden: Optional[bool] = True) -> (int, int):
    """
    Recursively list the contents of a directory in a tree format.

    Parameters:
        path (str): The directory path to list.
        indent (int, optional): The current level of indentation for visual representation. Defaults to 0.
        ignore_hidden (bool, optional): Whether to ignore hidden files and directories. Defaults to True.

    Returns:
        None.

    Usage/Examples:
        >>> from ed_utils import list_directory
        >>> list_directory("/path/to/directory")
        |-- dir1
        |   |-- file1.txt
        |   `-- file2.txt
        |-- dir2
        |   |-- subdir1
        |   |   `-- file3.txt
        |   `-- subdir2
        |-- file4.txt
        `-- file5.txt

        2 directories, 5 files

    Raises:
        DirectoryNotFoundException: If the provided `path` does not exist.
    """
    # handle default path of None, to be interprted at the current working directory
    if path is None:
        # print("No 'path' specified.")
        path = '.'
        # print('path =', path)
        # if you want to indicate/show the cwd, rather than '.':
        # cwd = os.getcwd()
        # print('cwd =', cwd)
    
    # Ensure the path exists
    if not os.path.isdir(path):
        raise DirectoryNotFoundError(f"The path '{path}' does not exist.")
    
    print(path)
    
    def _list_directory(path: str,
                        indent: int = 0,
                        ignore_hidden: bool = True) -> (int, int):
        # Get the list of items in the directory
        items = sorted(os.listdir(path))

        # Optionally filter out hidden files and directories
        if ignore_hidden:
            items = [item for item in items if not item.startswith('.')]

        dir_count = 0
        file_count = 0

        for index, item in enumerate(items):
            full_path = os.path.join(path, item)

            # Use symbols and indentation to display the tree structure
            prefix = '|-- ' if index != len(items) - 1 else '`-- '
            print(' ' * indent + prefix + item)

            if os.path.isdir(full_path):
                dir_count += 1
                sub_dir_count, sub_file_count = _list_directory(full_path, indent + 4, ignore_hidden)
                dir_count += sub_dir_count
                file_count += sub_file_count
            else:
                file_count += 1

        if indent == 0:
            print(f"\n{dir_count} directories, {file_count} files")

        return dir_count, file_count
    
    return _list_directory(path, indent, ignore_hidden)
           
tree.__version__ = tree.version = '0.6'

# -------------------------------------------------------------------------------------------------------

import re
from typing import Optional

def grep(pattern: str,
         file_path: str,
         include_line_number: Optional[bool] = False,
         case_insensitive: Optional[bool] = False) -> None:
    """
    Search for lines matching a pattern in a file and print them.

    Parameters:
        pattern:str               The pattern to search for; can be a
                                  simple string or a regular expression.
        file_path:str             The path to the file to be searched.
        include_line_number:bool  Optional. If True, includes the line numbers in the output. Default is False.

        case_insensitive:bool     Optional. If True, performs a case-insensitive search. Default is False.

    Returns:
        None.
    
    Usage/Examples:
        import ed_utils

        print(ed_utils.grep.__doc__)   # docstring

        print(ed_utils.grep.__annotations__)   # type hints/annotations
        
        
        pattern = r'giraffe'
        file_path = 'animals.txt'
        
        ed_utils.grep(pattern, file_path)
        
        ed_utils.grep(pattern, file_path, include_line_number=True, case_insensitive=True)
    """

    if not isinstance(pattern, str):
        raise TypeError(f'pattern must be a str; {type(pattern) = }')

    if pattern.strip() == '':
        raise ValueError('pattern must be a non-blank string')

    if not isinstance(file_path, str):
        raise TypeError(f'file_path must be a str; {type(file_path) = }')

    if file_path.strip() == '':
        raise ValueError('file_path must be a non-blank string')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f'{file_path} does not exist')
    
    
    flags = re.IGNORECASE if case_insensitive else 0

    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if re.search(pattern, line, flags=flags):
                if include_line_number:
                    print(f"{line_number}: {line.rstrip()}")
                else:
                    print(line.rstrip())

grep.__version__ = grep.version = '0.1'

# -------------------------------------------------------------------------------------------------------

"""
gtts (gTTS - Google Text-to-Speech): gtts is a Python library that provides an easy way to convert text into speech using Google Text-to-Speech API. You can use it to generate audio files from text, which can be useful for creating automated voice responses or other text-to-speech applications.

playsound: The playsound library is a simple, platform-independent way to play audio files in Python. It allows you to play sound files, making it useful for basic audio playback functionality in your Python programs.
"""

import os   # in Python stdlib()

def speak(text: Optional[str]=None) -> None:
    """
    audibly reads text (TTS - Text To Speech)
    
    Parameter:
        text: str   optional text to audibly speak

    Returns:
        None.
        
    Usage/Examples:
        speak()   # None

        speak("dobry dzień")   # str

        speak(42)   # int
        
        speak(192.128)   # float
        
        speak(['abe', 'lincoln'])   # list

        speak(('abe', 'lincoln'))   # tuple

        speak({'abe', 'lincoln'})   # set: unordered

        speak({'abe':10, 'lincoln':20})   # dict    
    """
    try:
        from gtts import gTTS
    except ImportError:
        print(f"The 'gtts' module is not available. You might need to install it. 'pip install gtts'")
        return

    try:
        from playsound import playsound
    except ImportError:
        print(f"The 'playsound' module is not available. You might need to install it. 'pip install playsound'")
        return

    if text is None:
        return
    
    if not isinstance(text, str):  # check if text is a string
        text = str(text)  # convert to string if not already

    audio_filename = 'temp.test.mp3'

    clip = gTTS(text=text,
                lang='en',
                slow=False
                )

    clip.save(audio_filename)
    playsound(audio_filename)
    os.remove(audio_filename)

speak.__version__ = speak.version = '0.4'

# -------------------------------------------------------------------------------------------------------

def head(filename: str,
         num_lines: Optional[int]=10,
         encoding: Optional[str]='utf-8') -> None:
    """
    Prints the first `num_lines` lines (or less) from `filename`.

    Parameters:
        filename:str - A string representing the name of the file to read.
        num_lines:int - An optional integer representing the number of lines to print. Default is 10.
        encoding:str - An optional encoding. Default is 'utf-8'.
                    On Windows, the default encoding is usually 'cp1252', while on Linux or macOS,
                    it's typically 'utf-8'. However, it's always better to explicitly specify the
                    encoding to avoid any unexpected behavior caused by encoding mismatches.

    Returns:
        None.

    Usage/Examples:
        import ed_utils

        print(ed_utils.head.__doc__)   # docstring

        print(ed_utils.head.__annotations__)   # type hints/annotations

        ed_utils.head(r'data/Mall_Customers.csv')   # returns first 10 lines of file
        ed_utils.head(r'data/Mall_Customers.csv', 15)   # returns first 15 lines of file
        ed_utils.head(r'data/Mall_Customers.csv', 15, encoding='cp1252')   # returns first 15 lines of file, with encoding

    Raises:
        TypeError: If `filename` is not a string or `num_lines` is not an integer.
        ValueError: If `filename` is a blank string or `num_lines` is less than or equal to 0.
        FileNotFoundError: If `filename` does not exist.
    """

    if not isinstance(filename, str):
        raise TypeError(f'filename must be a str; {type(filename) = }')

    if filename.strip() == '':
        raise ValueError('filename must be a non-blank string')

    if not isinstance(num_lines, int):
        raise TypeError(f'num_lines must be an int; {type(num_lines) = }')

    if num_lines <= 0:
        raise ValueError('num_lines must be a positive integer')

    if not os.path.exists(filename):
        raise FileNotFoundError(f'{filename} does not exist')

    with open(filename, 'r', encoding=encoding) as file:
        for i in range(num_lines):
            line = file.readline()
            if not line:
                break
            print(line.rstrip())

head.__version__ = head.version = '0.2'

# -------------------------------------------------------------------------------------------------------

def tail(filename: str,
              num_lines: Optional[int]=10,
              encoding: Optional[str]='utf-8') -> None:
    """
    Prints the last `num_lines` lines (or less) from `filename`.

    Parameters:
        filename:str - A string representing the name of the file to read.
        num_lines:int - An optional integer representing the number of lines to print. Default is 10.
        encoding:str - An optional encoding. Default is 'utf-8'.
                    On Windows, the default encoding is usually 'cp1252', while on Linux or macOS,
                    it's typically 'utf-8'. However, it's always better to explicitly specify the
                    encoding to avoid any unexpected behavior caused by encoding mismatches.

    Returns:
        None.

    Usage/Examples:
        import ed_utils

        print(ed_utils.tail.__doc__)   # docstring

        print(ed_utils.tail.__annotations__)   # type hints/annotations

        ed_utils.tail(r'data/Mall_Customers.csv')   # returns last 10 lines of file
        ed_utils.tail(r'data/Mall_Customers.csv', 15)   # returns last 15 lines of file
        ed_utils.tail(r'data/Mall_Customers.csv', 15, encoding='cp1252')   # returns last 15 lines of file, with encoding

    Raises:
        TypeError: If `filename` is not a string or `num_lines` is not an integer.
        ValueError: If `filename` is a blank string or `num_lines` is less than or equal to 0.
        FileNotFoundError: If `filename` does not exist.
    """

    if not isinstance(filename, str):
        raise TypeError(f'filename must be a str; {type(filename) = }')

    if filename.strip() == '':
        raise ValueError('filename must be a non-blank string')

    if not isinstance(num_lines, int):
        raise TypeError(f'num_lines must be an int; {type(num_lines) = }')

    if num_lines <= 0:
        raise ValueError('num_lines must be a positive integer')

    if not os.path.exists(filename):
        raise FileNotFoundError(f'{filename} does not exist')

    try:
        with open(filename, 'r', encoding=encoding) as file:
            lines = file.readlines()
            for line in lines[-num_lines:]:
                print(line.rstrip())
    except UnicodeDecodeError:
        print(f'Error: {filename} has non-UTF-8 encoding')

tail.__version__ = tail.version = '0.2'

# -------------------------------------------------------------------------------------------------------

def wc(filename: str,
       encoding: Optional[str]='utf-8') -> Tuple[int, int, int]:
    """
    Calculates the number of lines, words, and characters in a file.

    Parameters:
        filename (str): Path of the file.
        encoding (str, optional): File encoding. Default is 'utf-8'.
                    On Windows, the default encoding is usually 'cp1252', while on Linux or macOS,
                    it's typically 'utf-8'. However, it's always better to explicitly specify the
                    encoding to avoid any unexpected behavior caused by encoding mismatches.

    Returns:
        Tuple[int, int, int]: Tuple containing line_count, word_count, char_count

    Usage/Examples:
        import ed_utils

        print(ed_utils.wc.__doc__)   # docstring

        print(ed_utils.wc.__annotations__)   # type hints/annotations

        ed_utils.wc(r'data/Mall_Customers.csv')   # returns (201, 205, 3780)

    Raises:
        TypeError: If 'filename' is not a string.
        ValueError: If 'filename' is a blank string.
        FileNotFoundError: If 'filename' does not exist.
        IOError: If there is an error opening the file.
    """
    if not isinstance(filename, str):
        raise TypeError(f'filename must be a string; {type(filename) = }')
    
    # if filename.strip() == '':
    if not filename.strip():
        raise ValueError('filename must be a non-blank string')

    if not os.path.exists(filename):
        raise FileNotFoundError(f'{filename} does not exist')

    line_count = word_count = char_count = 0

    try:
        with open(filename, 'r', encoding=encoding) as file:
            for line in file:
                line_count += 1
                word_count += len(line.split())
                char_count += len(line)
    except IOError as err:
        raise IOError(f'Error reading file: {err}')

    return line_count, word_count, char_count


wc.__version__ = wc.version = '0.4'

# -------------------------------------------------------------------------------------------------------

"""
xattr is a library for working with extended file attributes on Unix-like systems. Extended file attributes are metadata associated with files and directories beyond the traditional file permissions and timestamps. This library allows you to interact with these attributes programmatically.

termcolor is a Python library that provides a way to add colored output to text in terminal/console applications. It allows you to specify text color and style, making it easier to highlight or format text for better readability in terminal-based programs.
"""

import platform   # for ____() - part of Python's stdlib
    
from typing import Optional, Union
import os
import datetime

# use HTML for Jupyter Notebook output
from IPython.display import HTML, display

#file_or_dir_path = "data"
file_or_dir_path = "./"   # cwd - current working directory
# file_or_dir_path = "../"   # directory immediately above
# file_or_dir_path = "../../"   # directory immediately above
# file_or_dir_path = "/Users/chesirecat/_DEVELOPMENT"   # direct path
#file_or_dir_path = "../../../_DEVELOPMENT/E12.outlier_detect_quartile.ipynb"
#file_or_dir_path = SURNAMES_FULL_FILE_PATH
# errors:
#file_or_dir_path = "dog"
#file_or_dir_path = ""
#file_or_dir_path = "\\"
#file_or_dir_path = 42


def ls_l(file_or_dir_path: Optional[str] = './',
         output: Optional[str] = 'jupyter') -> Union[str, None]:
    """
    ls_l mimics the unix 'ls -l'
    Currently only accepts a directory name or a single file name.
    So it currently does not support wildcards, no any other ls options such a recursion, etc.

    Parameters:
        file_or_dir_path: str  optional file or directory path, default is cwd
        output: str            optional, default is 'jupyter'
                               'text' (any case) - simple text with color decorations is supported
                               'html' (any case) - html with color decorations (via CSS)
                               'jupyter' (any case) - 'html', but displayed in the Jupyter output cell
    Usage/Examples:
        ls_l()                        - long directory of cwd to the Jupyter Notebook otuput cell
        ls_l('../')                   - long directory of cwd to the Jupyter Notebook otuput cell
        ls_l('../', output='jupyter') - long directory of cwd to the Jupyter Notebook otuput cell
        ls_l(output='html')           - long directory of cwd as a str of html
        ls_l('/users/ebujak')         - long directory of /users/ebujak to the Jupyter Notebook otuput cell
        ls_l('data')                  - long directory of data to the Jupyter Notebook otuput cell
        ls_l('data', output='text')   - long directory of data as a str
        ls_l.__annotations__          - type hints/annotations
        print(ls_l.__doc__)           - docstring
        help(ls_l)
        
    Raises:
        TypeError   'file_or_dir_path' is not str
        TypeError   'output' is not str
        ValueError  'output' not in ('text', 'html', 'jupyter')
    """
    # get the name of the operating system
    os_name = platform.system()

    if os_name == "Windows":
        print('ls_l() function currently not implemented in Windows.')
        return

    if not (os_name == "Linux" or os_name == "Darwin"):   # if not Unix-like systems
        print(f"This is not a Unix-like or Windows operating system. Detected OS: {os_name}")
        print('ls_l() function currently not implemented for this OS.')
        return
        
    # print("This is a Unix-like operating system."
    # os_name == "Linux" or os_name == "Darwin":   # Unix-like systems

    try:
        from termcolor import colored   # if output is for the terminal - not part of Python stdlib
    except ImportError:
        print(f"Detected OS: {os_name}. The 'termcolor' module is not available. You might need to install it. 'pip install termcolor'")
        return

    try:
        import xattr   # for xattr.listxattr() method - only on unix-like OS
    except ImportError:
        print(f"Detected OS: {os_name}. The 'xattr' module is not available. You might need to install it. 'pip install xattr'")
        return
    
    try:
        import pwd   # for pwd.getpwuid(owner).pw_name - part of Python's stdlib
    except ImportError:
        print(f"Detected OS: {os_name}. The 'pwd' module is not available. 'pwd' should be part of Python's stdlib. You might need to install it.")
        return

    try:
        import grp   # for grp.getgrgid(group).gr_name - part of Python's stdlib
    except ImportError:
        print(f"Detected OS: {os_name}. The 'grp' module is not available. 'grp' should be part of Python's stdlib. You might need to install it.")
        return

    
    if not isinstance(file_or_dir_path, str):
        raise TypeError(f'file_or_dir_path must be a str, {file_or_dir_path = }, \
    {type(file_or_dir_path) = }')

    if not isinstance(output, str):
        raise TypeError(
            f'output must be a str, {output = }, {type(output) = }')

    output = output.lower()
    if output not in ('text', 'html', 'jupyter'):
        raise ValueError(
            f"output must be in ('text', 'html', 'jupyter'), {output = }")

    # helper function to print filesize using engineering prefixes for powers of 10**3, 10**6, 10**9, ...
    def get_file_size(size):
        if size < 1024:
            return f"{size:6d}B"
        size /= 1024
        if size < 1024:
            return f"{size:6.1f}K"
        size /= 1024
        if size < 1024:
            return f"{size:6.1f}M"
        size /= 1024
        return f"{size:6.1f}G"

    output_HTML_str = ''
    line_print = ''

    now = datetime.datetime.now()

    if os.path.isdir(file_or_dir_path):
        # it is a directory
        dir_path = file_or_dir_path
        filenames = sorted(os.listdir(file_or_dir_path))
    else:
        # it is a single file
        dir_path = ''
        # this will be a list of the one filename
        filenames = [''.join(file_or_dir_path)]

    # print(f'{filenames = }')

    for filename in filenames:
        file_path = os.path.join(dir_path, filename)
        file_stat = os.stat(file_path)
        file_size = file_stat.st_size

        # if the file is more than 1 year old:
        #     display 4 digit year with leading space in a field of 5
        # else
        #     display hh:mm with leading 0 for hours and minutes if single digit
        # file_stat.st_mtime   # e.g. 1680312070.7769566
        dt = datetime.datetime.fromtimestamp(file_stat.st_mtime)
        # d is leading '0' on single digit days
        # _d is leading space on single digit days   Note: may not work on all OS

        time_diff = now - dt

        # Check if the difference is greater than or equal to one year
        if time_diff >= datetime.timedelta(days=365):
            file_mtime = dt.strftime('%b %_d  %Y')
        else:
            file_mtime = dt.strftime('%b %_d %H:%M')

        file_mode = file_stat.st_mode

        permission_string = ""

        if os.path.isdir(file_path):
            permission_string += "d"
            is_dir_flag = True
        else:
            permission_string += "-"
            is_dir_flag = False
        
    #     if os.path.isdir(file_path):
    #         permission_string += 'd'
    #         file = f"<span style='color:blue'>{file}/</span>"
    #     elif os.path.isfile(file_path):
    #         permission_string += '-'
    # # TypeError: lstat: path should be string, bytes or os.PathLike, not int
    # #     elif os.path.islink(mode):
    # #         permission_string += 'l'
    #     else:
    #         permission_string += '?'

        # convert file_mode to a 9-bit binary string
        file_mode_str = f"{file_mode:09b}"

        for i, bit in enumerate(file_mode_str[-9:]):
            if i == 0:
                permission_string += "r" if bit == "1" else "-"
            elif i == 1:
                permission_string += "w" if bit == "1" else "-"
            elif i == 2:
                if os.path.isdir(file_path):
                    permission_string += colored("x",
                                                 "blue") if bit == "1" else "-"
                else:
                    permission_string += "x" if bit == "1" else "-"
            elif i == 3:
                permission_string += "r" if bit == "1" else "-"
            elif i == 4:
                permission_string += "w" if bit == "1" else "-"
            elif i == 5:
                if os.path.isdir(file_path):
                    permission_string += colored("x",
                                                 "blue") if bit == "1" else "-"
                else:
                    permission_string += "x" if bit == "1" else "-"
            elif i == 6:
                permission_string += "r" if bit == "1" else "-"
            elif i == 7:
                permission_string += "w" if bit == "1" else "-"
            elif i == 8:
                if os.path.isdir(file_path):
                    permission_string += colored("x",
                                                 "blue") if bit == "1" else "-"
                else:
                    permission_string += "-"  # "x" bit is not applicable for non-executable files

        # extended attributes on file or directory
        permission_string += "@" if len(xattr.listxattr(file_path)
                                        ) > 0 else " "
        # permission_string += "@" if has_xattr(file_path) else " "

        nlinks = file_stat.st_nlink

        owner = file_stat.st_uid
        group = file_stat.st_gid
        owner_name = ""
        group_name = ""

        try:
            import pwd
            owner_name = pwd.getpwuid(owner).pw_name
        except ImportError:
            owner_name = owner

        try:
            import grp
            group_name = grp.getgrgid(group).gr_name
        except ImportError:
            group_name = group

        if is_dir_flag:
            nlinks = '---'  # TEMPORARY
        else:
            nlinks = 1

        # simplier filesizes with engineering prefixes
        # line = f"{permission_string} {nlinks:2d} {owner_name} {group_name} \
        # {get_file_size(file_size):>10} {file_mtime}"
        # raw filesize
        line = f"{permission_string} {nlinks:3} {owner_name}  {group_name}  "

        # if is_dir_flag:
        #     line += f"{file_size:>8}"
        # else:
        #     line += f"{file_size:>8}"
        line += f"{file_size:>8}"

        line += f" {file_mtime}"

        # for directories: ---------------------------------------------------
        # place a black trailing "/" - some ls utilities do not place trailing "/" on dirctories since it is colored blue
        # and color the text blue

        # to stdout (for terminal output)
        # and
        # build up HTML string (for Jupyter Notebook or an HTML file or ...)
        if is_dir_flag:
            line_print += line + ' ' + colored(filename, 'blue') + '/\n'
            output_HTML_str += line + ' ' + '<span style="color:blue">' + \
                filename + '</span>' + '/' + '<br>'
        else:
            line_print += line + ' ' + filename + '\n'
            output_HTML_str += line + ' ' + filename + '</span>' + '<br>'

    # print(line_print)
    if output == 'text':
        return(line_print)
    
    output_HTML_str = f"<pre style='font-family: monospace'>{output_HTML_str}</pre>"

    if output == 'html':
        return(output_HTML_str)
    
    if output == 'jupyter':
        display(HTML(output_HTML_str))
        return

ls_l.__version__ = ls_l.version = '0.5'

# -------------------------------------------------------------------------------------------------------

def column_str(iterable: Iterable[Any],
               line_length: int=70,
               spaces_between_columns: int=5) -> str:
    """
    Parameters:
        iterable [Iterable[Any]]: iterable containing anything, 
        line_length [int=70] : line length
                               70 - default
        spaces_between_columns [int=5] : 0 or positiv integer number of padding spaces between columns
                                         5 - default
    
    Returns:
        Returns printable str of "iterable" elements formatted into columns
        with "spaces_between_columns" spaces between columsn and limited to
        "line_length" per line
    
    Usage/Examples:
        import ed_utils
        
        print(ed_utils.column_str.__doc__)   # docstring
        
        print(ed_utils.column_str.__annotations__)   # type hints/annotations

        animals = ['dog', 'cat', 'giraffe', 'lion', 'tiger', 'bear', 'wolf', 'python',
                   'Eastern Diamondback Rattlesnake', 'southern Titiwangsa bent-toed gecko',
                   'hippopotamus', 'gorilla', 'pirahna', 'yellow-bellied sapsucker',
                   'screaming hairy armadillo'
                  ]

        print(ed_utils.column_str(animals))

        print(ed_utils.column_str(animals, line_length=87))

        print(ed_utils.column_str(animals, line_length=10))

        print(ed_utils.column_str(animals, spaces_between_columns=2))

        print(ed_utils.column_str(animals, line_length=87, spaces_between_columns=2))
        
        print(ed_utils.column_str(animals, 87, 2))

    """
    if not isinstance(iterable, Iterable):
        raise TypeError(f'{type(iterable) = }; must be type Iterable, such as list, set, tuple')

    if not isinstance(line_length, int):
        raise TypeError(f'{type(line_length) = }; must be type int')

    if not isinstance(spaces_between_columns, int):
        raise TypeError(f'{type(spaces_between_columns) = }; must be type int')
        
    if spaces_between_columns < 0:
        raise ValueError(f'{spaces_between_columns = }; must be 0 or positive integer')

    if len(iterable) < 1:
        return ""
    
    longest_string = max(iterable, key=len)
    # print(longest_string)

    len_longest_string = len(longest_string)
    # print(len_longest_string)

    current_line_length = 0
    formatted_str = ''

    for element in iterable:
        formatted_str += element.ljust(len_longest_string + spaces_between_columns)
        current_line_length += len_longest_string + spaces_between_columns
        if current_line_length >= line_length:
            formatted_str += '\n'
            current_line_length = 0
            
    return formatted_str


column_str.__version__ = column_str.version = '0.6'

# -------------------------------------------------------------------------------------------------------

import subprocess   # for check_output()
import os   # for name

def get_memory_info() -> dict:
    '''Returns memory information from system in a dict.
    Currently only implemented on Windows.'''
    __version__ = '0.3'
    
    # validation -------------------------------------------------------------
#     if os.name == 'posix':   # 'posix' ==> unix ==> macOS
#         print('posix, unix, macOS')
#     elif os.name == 'nt':   # 'nt' ==> Windows
#         print('Windows')
    
    if os.name != 'nt':
        raise OSError(f'get_memory_info() only implemented for Windows.  Your OS is \"{os.name}\".')
            
    # traverse the info
    id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []

    # arrange the string into clear info
    for item in id:
        new.append(str(item.split("\r")[:-1]))

    memory = dict()

    for i in new:
        line = i[2:-2]   # remove leading 2 characters and trailing 2 characters
        # print(line)
        if line.startswith('Total Physical Memory'):
            _, value = line.split(':')
            # print(value)   # something like "   8,079 MB"
            value = value[:-3]  # strip off trailing " MB"
            value = value.replace(',', '')   # remove commas
            total_physical_memory = int(value)
            memory['total_physical_memory'] = total_physical_memory
        elif line.startswith('Available Physical Memory'):
            _, value = line.split(':')
            # print(value)   # something like "   2,751 MB"
            value = value[:-3]  # strip off trailing " MB"
            value = value.replace(',', '')   # remove commas
            available_physical_memory = int(value)
            memory['available_physical_memory'] = available_physical_memory        
        elif line.startswith('Virtual Memory: Max Size'):
            _, _, value = line.split(':')
            # print(value)   # something like "   32,655 MB"
            value = value[:-3]  # strip off trailing " MB"
            value = value.replace(',', '')   # remove commas
            virtual_memory_max_size = int(value)
            memory['virtual_memory_max_size'] = virtual_memory_max_size        
        elif line.startswith('Virtual Memory: Available'):
            _, _, value = line.split(':')
            # print(value)   # something like "   18,010 MB"
            value = value[:-3]  # strip off trailing " MB"
            value = value.replace(',', '')   # remove commas
            virtual_memory_available = int(value)
            memory['virtual_memory_available'] = virtual_memory_available        
        elif line.startswith('Virtual Memory: In Use'):
            _, _, value = line.split(':')
            # print(value)   # something like "   18,010 MB"
            value = value[:-3]  # strip off trailing " MB"
            value = value.replace(',', '')   # remove commas
            virtual_memory_in_use = int(value)
            memory['virtual_memory_in_use'] = virtual_memory_in_use        

#     print(f'{total_physical_memory = }')
#     print(f'{available_physical_memory = }')
#     print(f'{virtual_memory_max_size = }')
#     print(f'{virtual_memory_available = }')
#     print(f'{virtual_memory_in_use = }')

    return memory

# sample lines to parse
# Available Physical Memory: 2,751 MB)
# Total Physical Memory:     8,079 MB
# Virtual Memory: Max Size:  32,655 MB
# Virtual Memory: Available: 18,010 MB
# Virtual Memory: In Use:    14,645 MB

# Samples

'''
memory_info = get_memory_info()

# print(f'{memory_info = }')

for k,v in memory_info.items():
    print(f'{k:>27} {v:6}')
'''    

'''
physical_memory_percentage_free = memory_info['available_physical_memory'] \
                                / memory_info['total_physical_memory']

print(f'{physical_memory_percentage_free = }')

physical_memory_percentage_used = 1 - physical_memory_percentage_free

print(f'{physical_memory_percentage_used = }')
'''

'''
virtual_memory_percentage_free = memory_info['virtual_memory_available'] \
                               / memory_info['virtual_memory_max_size']
print(f'{virtual_memory_percentage_free = }')

virtual_memory_percentage_used = memory_info['virtual_memory_in_use'] \
                               / memory_info['virtual_memory_max_size']
print(f'{virtual_memory_percentage_used = }')
'''

get_memory_info.__version__ = get_memory_info.version = '0.1'


# -------------------------------------------------------------------------------------------------------

def five_number_summary(lst: list[Numeric]) -> tuple[Numeric, Numeric, Numeric, Numeric, Numeric]:
    '''Returns the 5-number summary of lst, i.e. (min, Q1, Q2, Q3, max)
    Q2 is the median'''
    
    def _list_split(lst):   # <--------- moved inside to be an inner/nested function,
                            # <--------- aka nested function
        mid_idx = len(lst) // 2
        # print('mid_idx= ', mid_idx)

        if len(lst) % 2 == 0:
            # print('even')
            median = (lst[mid_idx-1] + lst[mid_idx]) / 2
            low_lst = lst[:mid_idx]
            high_lst = lst[mid_idx:]
        else:
            # print('odd')
            median = lst[mid_idx]
            low_lst = lst[:mid_idx]
            high_lst = lst[mid_idx+1:]

        return median, low_lst, high_lst

    if len(lst) <= 1: 
        raise ValueError("input list must be of length >= 2")

    if not all(isinstance(e, (int, float)) for e in lst):
        raise TypeError("elements in lst must be int or float")
   
    lst = sorted(lst)

    Q2, low_lst, high_lst = _list_split(lst)                            
#     print(Q2)
#     print(low_lst)
#     print(high_lst)
    
    Q1, _, _ = _list_split(low_lst)                         
#    Q1, left_l_lst, left_h_lst = _list_split(low_lst)                         
#     print(Q1)
#     print(left_l_lst)
#     print(left_h_lst)
    
    Q3, _, _ = _list_split(high_lst)                         
#    Q3, right_l_lst, right_h_lst = _list_split(high_lst)                         
#     print(Q3)
#     print(right_l_lst)
#     print(right_h_lst)
    
    return lst[0], Q1, Q2, Q3, lst[-1]
 
assert five_number_summary([1, 2, 3, 7, 8, 8, 11, 15, 17]) == (1, 2.5, 8, 13, 17), \
                "failed 5-number summary"
assert five_number_summary([1, 1, 1, 1]) == (1, 1, 1, 1, 1), \
                "[1,1,1,1] failed 5-number summary"

five_number_summary.__version__ = five_number_summary.version = '0.1'

# -------------------------------------------------------------------------------------------------------

import numpy as np   # for numpy.quantile() method, .number
from typing import Union
Numeric = Union[float, int, complex, np.number]

def five_number_summary2(lst: list[Numeric]) -> tuple[Numeric, Numeric, Numeric, Numeric, Numeric]:
    '''Returns the 5-number summary of lst, i.e. (min, Q1, Q2, Q3, max)
    Q2 is the median'''

    if len(lst) <= 1: 
        raise ValueError("input list must be of length >= 2")

    if not all(isinstance(e, (int, float)) for e in lst):
        raise TypeError("elements in lst must be int or float")   

    # note that np.quantile() returns a list
    # this function, five_number_summary2() returns a tuple
    return tuple(np.quantile(lst, [0, 0.25, 0.5, 0.75, 1]))   # returns (min_, Q1, Q2, Q3, max_)

'''
# np.quantile() comes up with different Q1 and Q2 values
assert five_number_summary2([1, 2, 3, 7, 8, 8, 11, 15, 17]) == (1, 2.5, 8, 13, 17), \
                "failed 5-number summary"
'''
#                                                                     Q1       Q3
assert five_number_summary2([1, 2, 3, 7, 8, 8, 11, 15, 17]) == ( 1.,  3.,  8., 11., 17.), \
                "failed 5-number summary"

assert five_number_summary2([1, 1, 1, 1]) == (1, 1, 1, 1, 1), \
                "[1,1,1,1] failed 5-number summary"

five_number_summary2.__version__ = five_number_summary2.version = '0.1'

# -------------------------------------------------------------------------------------------------------

import json
import numpy as np   # for numpy.ndarray


def pp(obj):
    """ pp(obj) --> pretty prints obj
    
    does not work on datatypes which are not serializable, such as sets or complex
    
    TypeError: Object of type 'set' is not JSON serializable
    TypeError: Object of type 'zip' is not JSON serializable
    TypeError: Object of type 'ndarray' is not JSON serializable   
    """

    # print('pp(obj): type(obj) is {}'.format(type(obj)))

    if type(obj) == set:
          return "pp(): TEMPORARY - cannot handle 'set' data type yet"
    
    if type(obj) == zip:
          return "pp(): TEMPORARY - cannot handle 'zip' data type yet"

    # need to generalize printing out any dimension of numpy.ndarray
    # probably recursive since the dimension is unknown
    # code below is only the case for 2 dimensions
    if type(obj) == np.ndarray and obj.ndim == 2:
          print('obj.ndim -->', obj.ndim)
          print('obj.shape -->', obj.shape)
          
          indent = 4
          nrows = obj.shape[0]
          ncols = obj.shape[1]
          
          print('[')
 
          for r in range(nrows):
              print('{}{}'.format(' '*indent, '['))
              for c in range(ncols):
                  print('{}{}'.format(' '*indent*2, obj[r,c]), end='')
                  if c != ncols-1:
                      print(',')
                  else:
                      print()
              print('{}{}'.format(' '*indent, ']'), end='')
              if r != nrows-1:
                  print(',')
              else:
                  print()    
        
          print(']')
          return 'pp(): output is printed above, bad side affect, will be fixing this to return string, need to generalize for n-dimensions'

    if type(obj) == np.ndarray:  
          return "pp(): TEMPORARY - cannot handle 'numpy.ndarray' data type yet"
         
    return json.dumps(obj, indent=4, sort_keys=True)   # returns json string

pp.__version__ = pp.version = '0.1'

# -------------------------------------------------------------------------------------------------------
  
def adder(nums):
    """Returns the sum of the nums (int, float, complex, or mixed)."""
    # can easily do      return sum(nums)   (if you convert each element (i.e str) to a number) but this is for practice
    total = 0
    print('nums -->', nums)
    for i, num in enumerate(nums):
        print('nums[{}] --> {}  type --> {}'.format(i, num, type(num)))
        total += complex(num)
    return total

adder.__version__ = adder.version = '0.1'

# -------------------------------------------------------------------------------------------------------

def _inspector(object_):
    '''prints out information about object_
        Returns: 
            attributes - attributes of object_
            methods - methods of object_
            classes - classes of object_
            name - Python name of object_
            type_ - usually the type(name), but distinguishes between packages, modules, built-ins (from stdlib), and __ for math
        Usage:
            attributes, methods, classes, name, type_ = inspector(x)
            where x can be:
                Look at ed_utils.harness file
    '''

    print('ed_utils __version__ =', __version__)
          
    # dir(object_)   # has attributes -and- methods mixed


    def _display_pip_list(string):
        '''Prints the result of a "pip list" and search for the string, regardless of OS'''
        
        print('Please wait ...', end='\r')
        
        def _print_file(filename):
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    print(f.read(), end='')
                os.remove(filename)

        import os
        os_name = os.name
        filename = 'testtemptemptemptemp.txt'
        if os_name == 'nt':   # Windows
            _ = os.system(f"pip list | findstr -i {string} > {filename}")
            _print_file(filename)
        elif os_name == 'posix':   # macOS, unix, Linux
            _ = os.system(f"pip list | grep -i {string} > {filename}")
            _print_file(filename)
        else:
            print('OS not handled.')
   

    def _get_attributes_methods(obj):
        '''Returns the attributes and methods from the namespace for obj'''
        attrs = [a for a in dir(obj) if not callable(getattr(obj, a))]
        meths = [a for a in dir(obj) if callable(getattr(obj, a))]   # actually methods AND classes are callablee
        return attrs, meths

    attributes, methods = _get_attributes_methods(object_)
    print('object_ is', object_)

    # ---------------------------------------------------

#     BEWARE:
#         str.__name__   # 'str'
#         'sam'.__name__   # AttributeError: 'str' object has no attribute '__name__'

#     if hasattr(object_, __name__):   # I do not think this works same for example: 5 and int
#         name = object_.__name__
#     else:
#         name = object_
    try:
        name = object_.__name__
    except:
        print('object_ does not have __name__')
        name = object_   # this happens is 5, -7.23, ___
        print('name is assigned to ', name)

    # __name__ does not work on all objects, not for str

    t = type(object_)
    # print(t)
    tn = str(t).split("'")
    # print(tn)
    type_ = tn[-2]
    print(f'type({name}) is {type_}')
    
    # ----------------------------------------------------
    # memory size
    
    # the size of a data type is meaningless
    # actually:
    #     sys.getsizeof(any data type) ---> 416 bytes
    #     sys.getsizeof(any module or package or built-in) ---> 72 bytes
    
    if isinstance(object_, type):
        print(f'{object_} is not an instance of any data type')
    else:
        # then obj is an instance of some data type
        t = type(object_)
        print(f'{object_} is an instance of {t}')

        import sys

        size_object_ = sys.getsizeof(object_) 
        print(f'sys.getsizeof({object_}) = {size_object_:,} bytes')

        # sys.sizeof(any str variable) is its lenth + 49 bytes

        # size_name = sys.getsizeof(name)
        # print(f'sys.getsizeof({name}) = {size_name:,} bytes')  
    
    # ----------------------------------------------------
    if type_ == 'module':
        # print(name, 'is a package or a module or a built-in library')

        # print(f'44444 {object_=}')

        so = str(object_)
        # print(f'{so=}')
        if 'built-in' in so:
            type_ = 'built-in'
        elif '__init__.py' in so:
            type_ = 'package'
        else:
            type_ = 'module'
            # MAYBE endswith name.py --> module
            # SO WHAT IS THE OTHER KIND ... LIKE math

        print(name, 'is a', type_, end='  ')


        # get version of package/module.  Note that built-in libraries do not have version, such as time.
        version = None
        try:
            version = object_.__version__
        except:
            pass
        finally:
            print('version', version)


        # additional module (package or module or built-in) information
        # from installed "modules", i.e. packages/modules/built-in/other in this Python environment
        print('pip list', '--'*50)
        _display_pip_list(name)
        print('--'*55)
            
    # ---------------------------------------------------        
    if hasattr(object_, '__iter__'):
        print(f'{name} is iterable', end='')
        
        # _io.TextIOWrapper file handle is iterable, but cannot do len on it until it actually reads the file
        # data types do not have len(), even though some of them are iterable - such as list, tuple, ...        
        if type_ not in ['type', '_io.TextIOWrapper']:
            print(f'  len={len(object_)}')
        else:
            print()
    else:
        print(f'{name} is not iterable')   # this technique identifies nametuple as not iterable - WRONG!!!!

    # EXPERIMENTAL
    # this technique of checking is something is iterable is cleaner than the above "crazy" technique
    # but
    # this technique also catches namedtuple which is iterable
    
    print('EXPERIMENTAL')
    from collections.abc import Iterable   # Python 3.6+
    
    print(f'{name} is type {type(object_)} --- isinstance({name}, Iterable) == {isinstance(name, Iterable)}')
    print(f'{name = }')
    print(f'{object_ = }')
    print(f'{type_ = }')
    # print(f'{object_ = }')
    if type_ in ['module', 'package']:
        print(f'NOT iterable - do not pay attention to the above incorrect boolean from isinstance({name}, Iterable)')
    else:
        print('Above boolean is believable, but ....')


    print(f'has iter({name})? ==> {name}', end=' ')
    try:
        iterator = iter(name)
    except TypeError:
        print('is not iterable')
    else:
        print('is iterable')

    print('--name--')
    print(f"T/F hasattr({name}, '__iter__')? ==> {name}", end=' ')
    if hasattr(name, '__iter__'):
        print('is iterable')
    else:
        print('is not iterable')        

    print('--object_--')
    print(f"T/F hasattr({object_}, '__iter__')? ==> {object_}", end=' ')
    if hasattr(object_, '__iter__'):
        print('is iterable')
    else:
        print('is not iterable')        


    ########
    
    print('--'*55)

    # ---------------------------------------------------
    print('-- ', len(attributes), ' attributes -->\n', attributes, sep='')
    
    # methods is further separated into methods and classes
    # print(len(methods), 'methods/classes -->\n', methods)

    # Break up above methods into methods and classes
    m = [x for x in methods if x.islower()]
    print('-- ', len(m), ' methods -->\n', m, sep='')

    c = list(set(methods) - set(m))
    print('-- ', len(c), ' classes -->\n', c, sep='')
    
    # ---------------------------------------------------
    # docstring
    # getting the docstring to work reliably i stough!
    
    print('--'*55)
    # doc_str = f'{name}' + '.__doc__'
    # print(f'--- {doc_str} is ---')

#     print('++'*50)
#     print(f'DEBUG {name=}  {type(name)=}')
        
    try:
        # first try without () ... looks nicer, 5.__doc__, -7.62.__doc__ do not work
#         print('DEBUG_1 1st try --- no parentheses')
        doc_str = str(name) + '.__doc__'
        # doc_str = f'{name}' + '.__doc__'
        # doc_str = name + '.__doc__'   # works on all data type except classes
#         print(f'DEBUG_1 {doc_str=}')
        res = eval(doc_str)
#         print(f'DEBUG_1 eval({doc_str}) WORKED!')
    except:
        try:
            # ( ) are for (5)._doc__, (-7.62).__doc__, ... maybe others
#             print('DEBUG 2nd try --- with parentheses')
            doc_str = f'({name})' + '.__doc__'
#             print(f'DEBUG_2 {doc_str=}')
            res = eval(doc_str)
#             print(f'DEBUG_2 eval({doc_str}) WORKED!')
        except:
            res = None
#             print(f'DEBUG_1&2 except ... 1 and 2 did NOT work')

#     print('DEBUG_1&2 ---', doc_str, '---')
#     print(res)
#     # print(f'{name} does not have a __doc__ ... docstring')

    
    if res == None:
#         print('DEBUG res from steps 1 & 2 yield None ****************')
        
#         print('++'*50)
#         print(f'DEBUG {object_=}  {type(object_)=}')

        try:
#             print('DEBUG 3rd try --- no parentheses')
            # doc_str = str(name) + '.__doc__'
            doc_str = f'{object_}' + '.__doc__'
            # doc_str = name + '.__doc__'   # works on all data type except classes
#             print(f'DEBUG_3 {doc_str=}')
            res = eval(doc_str)
#             print(f'DEBUG_3 eval({doc_str}) WORKED!')
        except:
            try:
#                 print('DEBUG 4th try --- with parentheses')
                doc_str = f'({oject_})' + '.__doc__'
#                 print(f'DEBUG_4 {doc_str=}')
                res = eval(doc_str)
#                 print(f'DEBUG_4 eval({doc_str}) WORKED!')
            except:
                res = None
#                 print(f'DEBUG_3&4 except ... 3 and 4 did NOT work')
            
#         print('DEBUG_3&4 ---', doc_str, '---')
#         print(res)
#         # print(f'{name} does not have a __doc__ ... docstring')

    
    # ---------------------------------------------------
    return attributes, m, c, name, type_  # attributes, methods, classes, name, type_

_inspector.__version__ = _inspector.version = '0.1'

## -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# GIS
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

from typing import Union


def is_latitude(latitude: Union[int, float]) -> bool:
    """
    Check if a value is a valid latitude.

    A valid latitude is a number (integer or float) between -90 and 90, inclusive.

    Parameters:
        latitude (float or int): The value to check as a latitude.

    Returns:
        bool: True if the value is a valid latitude, False otherwise.

    Raises:
        TypeError: If the input is not a float or an integer.

    Example:
        >>> is_latitude(23.456)
        True
        >>> is_latitude(-90)
        True
        >>> is_latitude(90)
        True
        >>> is_latitude(91)
        False
        >>> is_latitude("invalid")
        TypeError: Latitude must be a float or an integer

    Usage:
        The function can be used to validate geographic coordinate data, ensuring that
        latitude values are within the acceptable range. This is particularly useful
        in applications dealing with mapping, GPS, and spatial data analysis.
    """
    # print(f'ed_utils: {latitude=}   {type(latitude)=}')
    if not isinstance(latitude, (float, int)):
        raise TypeError(f"Latitude must be a float or an integer; {type(latitude) = }")

    return -90 <= latitude <= 90


if __name__ == '__main__':
    print('ed_utils.py: is_latitude() testing entry.')
    # Assert statements with error messages for testing
    assert is_latitude(45.678) == True, "Expected True for a valid latitude"
    assert is_latitude(-90) == True, "Expected True for -90"
    assert is_latitude(90) == True, "Expected True for 90"
    assert is_latitude(91) == False, "Expected False for 91"

    try:
        is_latitude("invalid")
        assert False, "Expected a TypeError for invalid input type"
    except TypeError:
        pass  # This is expected

    print('ed_utils.py: is_latitude() testing passed.')


is_latitude.__version__ = is_latitude.version = '0.1'

# -------------------------------------------------------------------------------------------------------

from typing import Union


def is_longitude(longitude: Union[int, float]) -> bool:
    """
    Check if a value is a valid longitude.

    A valid longitude is a number (integer or float) between -180 and 180, inclusive.

    Parameters:
        longitude (float or int): The value to check as a longitude.

    Returns:
        bool: True if the value is a valid longitude, False otherwise.

    Raises:
        TypeError: If the input is not a float or an integer.

    Example:
        >>> is_longitude(45.678)
        True
        >>> is_longitude(-180)
        True
        >>> is_longitude(180)
        True
        >>> is_longitude(181)
        False
        >>> is_longitude("invalid")
        TypeError: Longitude must be a float or an integer

    Usage:
        The function can be used to validate geographic coordinate data, ensuring that
        longitude values are within the acceptable range. This is particularly useful
        in applications dealing with mapping, GPS, and spatial data analysis.
    """
    # print(f'ed_utils: {longitude=}   {type(longitude)=}')
    if not isinstance(longitude, (float, int)):
        raise TypeError(f"Longitude must be a float or an integer; {type(longitude) = }")

    return -180 <= longitude <= 180


if __name__ == '__main__':
    print('ed_utils.py: is_longitude() testing entry.')
    # Assert statements with error messages for testing
    assert is_longitude(45.678) == True, "Expected True for a valid longitude"
    assert is_longitude(-180) == True, "Expected True for -180"
    assert is_longitude(180) == True, "Expected True for 180"
    assert is_longitude(181) == False, "Expected False for 181"

    try:
        is_longitude("invalid")
        assert False, "Expected a TypeError for invalid input type"
    except TypeError:
        pass  # This is expected

    print('ed_utils.py: is_longitude() testing passed.')
    
    
is_longitude.__version__ = is_longitude.version = '0.1'

# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# CLASSES
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

import os   # for os.devnull
import sys   # for sys.stdout

from types import TracebackType
from typing import Optional, Type


class HiddenPrints:
    """
    Suppress print() output to stdout (default is screen).
    Code within HiddnPrints context manager will be interpreted.

    Notes:
        Uses context manager protocol of classes
        with __enter__() and __exit__() methods

    Usage/Example:
        # Import the DummyContextManager class if not already imported
        from ed_utils import DummyContextManager
    
        x = 7
        print('before')

        # Use the HiddenPrints context manager
        # Create an instance of HiddenPrints
        with HiddenPrints():
            print('This will not be printed, but code will be intepreted.')
            x_doubled = x * 2

        print("after")
        print('x_doubled =', x_doubled)
        
        Output is:
            before
            after
            x_doubled = 14
    """

    # NameError: name 'HiddenPrints' is not defined
    # def __enter__(self) -> HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')
        return self

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         sys.stdout.close()
#         sys.stdout = self._original_stdout
    
    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> bool:
        sys.stdout.close()
        sys.stdout = self._original_stdout
        return False

HiddenPrints.__version__ = HiddenPrints.version = '0.3'

# -------------------------------------------------------------------------------------------------------

class DummyContextManager:
    """
    A dummy context manager that does nothing and can be used as a template
    for creating custom context managers.

    Notes:
        Uses context manager protocol of classes
        with __enter__() and __exit__() methods

    Usage/Example:
        # Import the DummyContextManager class if not already imported
        from ed_utils import DummyContextManager

        x = 8
        print('before')
            
        # Using the dummy context manager
        # Create an instance of the DummyContextManager
        # with DummyContextManager() as dummy:
        # or
        with DummyContextManager():
            # Perform operations within the context
            print("Within DummyContextManager(): This code is interpreted within the 'with' context.")
            x_tripled = x * 3
            
        # Operations outside the context
        print("after")
        print('x_tripled =', x_tripled)
        
        # The __enter__ and __exit__ methods of DummyContextManager can be customized
        # to perform specific actions when entering and exiting the context, respectively.
        # For example, you can add resource management or error handling logic.

        Output is:
            before
            Within DummyContextManager(): This code is interpreted within the 'with' context.
            after
            x_tripled = 24
    """
    def __enter__(self):
        # You can optionally return an object if needed
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # You can optionally perform cleanup actions here
        pass

DummyContextManager.__version__ = DummyContextManager.version = '0.2'

# -------------------------------------------------------------------------------------------------------

from typing import Any

def inspector(obj: Any, verbose:bool = False) -> tuple[list[str], list[str], list[str], str, str]:
    """
    Parameters:
        obj: any class, variable, or data_type
        verbose [bool] : Verbose diagnostic information
                         False - default
    Returns:
        tuple containing:
            attributes [list] - attributes of object_
            methods [list] - methods of object_
            classes [list] - classes of object_
            name [str] - Python name of object_
            type_ [str] - usually the type(name), but distinguishes between packages,
                          modules, and built-ins (from stdlib)
            
    Usage/Examples:
        attributes, methods, classes, name, type_ = inspector(x)
        where x can be:
            Look at ed_utils.harness file

        import numpy
        inspector(numpy)

        import numpy as np
        inspector(np)
        
        inspector(np, verbose=True)

        inspector(sympy)
    """
    if verbose:
        return _inspector(obj)   # _inspector(obj) prints a lot of intermediate diagnostic information

    with HiddenPrints():
        return _inspector(obj)   # previous version, now inner function

inspector.__version__ = inspector.version = '0.2'


# -------------------------------------------------------------------------------------------------------

from typing import Optional, Union, List, Tuple, Set
import importlib

def versions(elements: Optional[Union[str, List[str], Tuple[str], Set[str] ]] = None) -> dict:
    """
    Retrieve the version information for a single element or all elements listed in the provided list. If no list is 
    provided, the function can optionally return the version of modules listed in a predefined list (e.g., __all__ 
    variable if defined in the context where this function is used). The function uses importlib to import modules 
    dynamically and checks for the __version__ attribute. It returns a dictionary with the module/package names as 
    keys and their version strings as values.

    Parameters:
        elements (Optional[Union[str, List[str]]]): A string or a list of strings where each string is the name of 
                                                    a module/package, or None. If None, the function uses a predefined 
                                                    list of modules/packages.

    Returns:
        dict: A dictionary with keys being the module/package names from the elements list and values
              being their respective version strings, if available. If a version string is not available
              or an element is not a valid module/package, it is excluded from the result.

    Raises:
        TypeError: If the elements argument is not a string, a list of strings, or None.

    Example:
        If elements = None    which is the default, the function could return:
        {'plot_bar_categorical': '0.2', 'plot_histogram': '0.4', 'versions': '0.8'}
        If elements = ['numpy', 'pandas'], the function could return:
        {'numpy': '1.18.5', 'pandas': '1.0.5'}
        If elements = 'numpy', the function could return:
        {'numpy': '1.18.5'}
        
    Note:
        This function assumes that all elements in the elements list are valid Python modules, packages,
        or object with __vervsion__ attribute.
        Elements without a __version__ attribute or that cannot be imported are ignored.
    """
    if elements is not None and not isinstance(elements, (str, list, tuple, set)):
        raise TypeError("The 'elements' parameter must be a string, a list of strings, a tuple of strings, or a set of strings, or None.")

    # If nothing was specified, return the versions of each element in a predefined list (__all__).
    if elements is None:
        versions_dict = {
            element: eval(element + '.__version__')
            for element in __all__
        }
        return versions_dict
    elif isinstance(elements, str):
        if len(elements) == 0:
            elements = ' '
        elements = [elements]

    versions_dict = {}
    
    for element in elements:
        if not isinstance(element, str):
            continue  # Skip non-string elements
        
        try:
            module = importlib.import_module(element)
            if hasattr(module, '__version__'):
                versions_dict[element] = module.__version__
        except ImportError:   # Ignore modules that do not exist or lack "__version__" attribute
            continue

    return versions_dict


versions.__version__ = versions.version = '0.8'

# -------------------------------------------------------------------------------------------------------

def print_function_annotations(func: callable) -> None:
    """
    Prints the type annotations of a function's parameters.

    Parameters:
        func (callable): The function whose type annotations are to be printed.

    Usage:
        Call this function with a function as its argument.
        It will print each parameter's name and type annotation in a formatted manner.

    Example:
        def example_function(a: int, b: float, c: str) -> bool:
            pass

        print_function_annotations(example_function)
        # Output:
        # a        int
        # b        float
        # c        str
        # return   bool
    """
    # Checking if the input is indeed a function
    if not callable(func):
        raise TypeError(f"The provided input is not a function.; it is {type(func)}")

    # Extracting the function's type annotations
    parameters = func.__annotations__.keys()

    if len(parameters) == 0:
        print('No type annotations.')
    else:
        # Finding the longest parameter name for formatting
        max_length_string = max(parameters, key=len)
        max_length = len(max_length_string)

        # Printing each parameter and its annotation
        for parameter, annotation in func.__annotations__.items():
            # print(f'{parameter:{max_length}}  {annotation.__name__}') 
            print(f'{parameter:{max_length}}  {annotation}') 


print_function_annotations.__version__ = print_function_annotations.version = '0.1'
            
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

def main(argv):
    """Start tests."""
    def _clear(): 
        import os
        # for Windows 
        if os.name == 'nt': 
            _ = os.system('cls') 
        # for Mac and linux(here, os.name is 'posix') 
        else: 
            _ = os.system('clear') 

    # test driver code here
    
    _clear()
    print('=====================================================')
    
    print('argv -->', argv)
    # print('json -->', json.dumps(argv, indent=4, sort_keys=True))
    print('argv ==>\n', pp(argv))
    
    _, *cmdline_arguments = argv
    result = adder(cmdline_arguments)
    print('ed_utils.py  main() --> {}'.format(result))

# -------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    # this is the main or testing cases to demonstrate functions in this file
    import sys
    main(sys.argv)
    
    print('----------------------------------------------')
    print(pp(5))
    print(pp(5.6))
    print(pp([3, 4, 5]))
    # print(ed_utils.pp({6, 'Helene', 5-7j, 'chromakey'}))   # TypeError: Object of type 'set' is not JSON serializable

    animals = {'Wally':'walrus', 'Ted':'giraffe', "Crazy":'snake', 'Arrogant':'cat'}
    print(pp(animals))

    animals2 = {'Wally':'walrus', 'Ted':'giraffe', "Menagerie": ['snake','lizard','salamander'],
                "Crazy":'snake', 'Arrogant':'cat'}
    print(pp(animals2))

    assert adder([1, 2, 3]) == 6, 'adder([1, 2, 3]) failed!'
