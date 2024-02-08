"""
File name: ed_data_viz.py
Author: Edward Bujak
Date created: 2023.12.13
Date last modified: 2023.12.19
Python Version: 3.11.5 (that ed_data_viz was tested with)

collection of data visualization functions and classes

For extensive examples of usage, go to ed_data_viz.demo.ipynb

Functions:
    plot_bar_categorical
    plot_histogram_
    plot_histogram
    plot_pie

Classes:
    none
    


anytime ed_data_viz.py is changed, also need to restart kernel for all .IPYNB files that import ed_data_viz
or
you must reload it:

import importlib
importlib.reload(ed_data_viz)
ed_data_viz.__version__
"""

# module level dunder names
__version__ = '0.1.4'
version = __version__
__title__ = "ed_data_viz"
__summary__ = "Collection of useful data visualization functions and classes."
# __uri__ = "https://github.com/ebujak__/ed_data_viz" 
__author__ = "Edward Bujak"

__copyright__ = "Copyright 2023-2023, The Edward Bujak Python Project"
__credits__ = ["Edward Bujak"]
__license__ = "GPL"
__maintainer__ = "Edward Bujak"
__email__ = "Edward_Bujak@hotmail.com"
__status__ = "Never Ending Development"
__classes__ = []
__functions__ = ['plot_bar_categorical', 'plot_histogram_', 'plot_histogram', 'plot_pie', 'versions',
                ]
#  __all__ list defines what will be imported from ed_data_viz.py when the statement
# from ed_data_viz import *
# is used. In this case, only those elements in the __all_ list will be imported from ed_data_viz.py.
__all__ = __functions__ + __classes__

__history__ = """

0.1.4 - 2023.12.19 - Edward Bujak - modified plot_bar_bar_categorical() function to call
                                        plt.tight_layout() before plt.savefig() to assure
                                        that saved images are not clipped
0.1.3 - 2023.12.17 - Edward Bujak - added plot_pie() function
0.1.2 - 2023.12.16 - Edward Bujak - added figsize, color, and alpha parameters to plot_histogram_() function
                                    added figsize, color, and alpha parameters to plot_histogram() function
                                    added color, and alpha parameters to plot_bar_categorical() function
0.1.1 - 2023.12.14 - Edward Bujak - added plot_histogram_() function
                                    added plot_histogram() function
                                    added versions() function
                                    changed plot_bar_bar_categorical() function to:
                                        take additional parameter to save as a file
0.1.0 - 2023.12.13 - Edward Bujak - added plot_bar_bar_categorical() function
                                    added __functions__ attribute
                                    added __classes__ attribute
                                    added __all__ attribute
"""

# print('ed_data_viz: __name__ is {}'.format(__name__))
    
# -------------------------------------------------------------------------------------------------------

# Type hints/annotations used within ed_data_viz.py module
from typing import (
#     Any,   # for column_str()
#     Callable,
#     Dict,
#     Generic,
#     Hashable,
#     Iterable,
#     Iterator,
#     IO,
    List,   # for versions()
    Tuple,   # for plot_bar_categorical(), versions()
    Set,   # for versions()
#     NoReturn,
    Optional,   # for plot_bar_categorical(), versions()
#     Sequence,
#    
    Union,   # for plot_bar_categorical(), versions()
#     TypeVar,
#     cast,
#     overload,
#     TYPE_CHECKING,
)


# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# UNIVARIATE
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from typing import Union, Optional


def plot_histogram_(
    s: Union[pd.Series, list, tuple, np.ndarray],
    figsize: Union[Tuple[Union[int, float], Union[int, float]],
               List[Union[int, float]]] = (6, 5),
    xlabel: Optional[str] = 'Value',
    title: Optional[str] = None,
    bins: Optional[int] = 20,
    kde: Optional[bool] = True,
    # color: Optional[str] = 'blue',
    color: Optional[str] = None,
    alpha: Optional[float] = 0.5,   # 0 .. 1
    file_path: Optional[str] = None,
    ) -> None:
    """
    Create and display a histogram plot of a given pandas Series, list, tuple, or numpy ndarray.

    Parameters:
        - s (Union[pd.Series, list, tuple, np.ndarray]): The data to be plotted as a histogram.
        - xlabel (Optional[str], optional): Label for the x-axis. Defaults to 'Value'.
        - title (Optional[str], optional): Title for the histogram plot. Defaults to None.

    Raises:
        - ValueError: If the input data 's' is not a pandas Series, list, tuple, or numpy ndarray.

    Returns:
        - None
    """
    # Validate input parameter
    if not isinstance(s, (pd.Series, list, tuple, np.ndarray)):
        raise ValueError(
            f"Input parameter 's' must be a pandas Series, list, tuple, or numpy ndarray; {type(s) = }")
        
    # Check for figsize to be a tuple or list of two positive integers or floats
    if not isinstance(figsize, (tuple, list)) or len(figsize) != 2:
        raise TypeError("figsize must be a tuple or list of two elements.")
    if not all(isinstance(n, (int, float)) and n > 0 for n in figsize):
        raise ValueError(
            "Both elements in figsize must be positive integers or floats.")

    plt.figure(figsize=figsize)

    sns.histplot(s,
                 bins=bins,
                 kde=kde,
                 color=color,
                 alpha=alpha,
                )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Count')

    # Optionally write the chart out as a file
    if file_path is not None:
        # Apply tight_layout to adjust subplot params on savefig()
        plt.tight_layout()
        print(f"Saving file '{file_path}'") 
        plt.savefig(file_path,
                    # dpi=1000
                    )
    
plot_histogram_.__version__ = plot_histogram_.version = '0.5'
    
# -------------------------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional


def plot_histogram(
    feature: str,
    dataframe: Optional[pd.DataFrame] = None,
    figsize: Union[Tuple[Union[int, float], Union[int, float]],
               List[Union[int, float]]] = (8, 7),
    xlabel: Optional[str] = None,
    title: Optional[str] = None,
    bins: Optional[int] = 20,
    kde: Optional[bool] = True,
    color: Optional[str] = None,
    alpha: Optional[float] = 0.5,   # 0 .. 1
    file_path: Optional[str] = None,
) -> None: 
    """
    Create and display a histogram plot of a specified feature in a pandas DataFrame.

    Parameters:
        - feature (str): The name of the feature to be plotted.
        - dataframe (Optional[pd.DataFrame]): The DataFrame containing the feature. 
              If None, the function tries to use a global DataFrame named 'df'.
        - file_path (Optional[str]): Path to save the plot image. If None, the plot is not saved.
        - TODO
        - MORE HERE
        
    Raises:
        - ValueError: If no DataFrame is provided and 'df' is not defined globally.
        - TypeError: If 'feature' is not a string or 'dataframe' is not a DataFrame (or None).
        - KeyError: If the 'feature' is not in the DataFrame.

    Returns:
        None

    Usage:
        - Call this function with the name of the feature and the DataFrame.
        - If no DataFrame is provided, the function will try to use a global DataFrame named 'df'.  

    Example:
        data = {
            'age': [25, 30, 35, 40, 45],
            'salary': [50000, 55000, 60000, 65000, 70000]
        }
        df = pd.DataFrame(data)

        # Plotting histogram for the 'age' feature
        plot_histogram('age', df)

        # If a global DataFrame 'df' is available, simply use:
        plot_histogram('salary')
"""    
    # Check if 'feature' is a string
    if not isinstance(feature, str):
        raise TypeError(f"Expected 'feature' to be a string, got {type(feature)} instead.")
        
    # Try to use a default global DataFrame if none is provided
    if dataframe is None:
        if 'df' not in globals():
            raise ValueError("No DataFrame provided and a global 'df' is not defined.")
        dataframe = globals()['df']
       
    # Check if the provided 'dataframe' is indeed a pandas DataFrame or None
    if not isinstance(dataframe, (pd.DataFrame, type(None))):
        raise TypeError("Expected 'dataframe' to be a pandas DataFrame or None.")
        
    # Check if the feature exists in the DataFrame
    if feature not in dataframe.columns:
        raise KeyError(f"Feature '{feature}' not found in the DataFrame.")

    # Check for figsize to be a tuple or list of two positive integers or floats
    if not isinstance(figsize, (tuple, list)) or len(figsize) != 2:
        raise TypeError("figsize must be a tuple or list of two elements.")
    if not all(isinstance(n, (int, float)) and n > 0 for n in figsize):
        raise ValueError(
            "Both elements in figsize must be positive integers or floats.")

    # Count non-NaN values and calculate percentage
    N = dataframe[feature].notna().sum()   # Number of non-NaN values
    num_records = len(dataframe)
    percentage_not_nan = N / num_records * 100

    # print(f'{N = :,}')
    # print(f'{num_records = :,}')
    # print(f'{percentage_not_nan = }')

    feature_latex = '$' + feature.replace('_', '\\_') + '$'
    
    # default title
    if not title:
        title = f'Distribution of {feature_latex}\n(Non-NaN Count: {N:,}, {percentage_not_nan:.1f}% Non-NaN)'

    # default xlabel is the feature name
    if not xlabel:
        xlabel = f'${feature}$'
       
    plot_histogram_(
        dataframe[feature],
        figsize=figsize,
        xlabel=feature_latex,
        title=title,
        bins=bins,
        kde=kde,
        color=color,
        alpha=alpha,
        file_path=file_path,
    )
    
plot_histogram.__version__ = plot_histogram.version = '0.5'

# -------------------------------------------------------------------------------------------------------

## Pie - Univariate - Categorical Variables

import matplotlib.pyplot as plt
from typing import List, Optional
import numpy as np


def plot_pie(
    x: List[float],
    labels: Optional[List[str]] = [],
    colors: Optional[List[str]] = [],
    startangle: Optional[float] = 140,
    figsize: Optional[Tuple[int, int]] = (10, 6),
    pie_type: Optional[str] = 'percentage',   # 'percentage' | 'count' | 'percentage_and_count' aka 'count_and_percentage'
    title: Optional[str] = '',
) -> None:
    """
    Plot a pie chart based on the input data.

    Parameters:
        - x (List[float]): A list of values for the pie chart slices.
        - labels (List[str], optional): A list of labels for the slices. Defaults to an empty list.
        - colors (List[str], optional): A list of color codes for the slices. Defaults to an empty list.
        - startangle (float, optional): The angle at which the first slice starts. Defaults to 140.
        - pie_type (str, optional): The type of information to display on the pie chart.
            Can be 'percentage', 'count', or 'percentage_and_count' (aka 'count_and_percentage').
            Defaults to 'percentage'.
         - title (str, optional): The title of the pie chart. Defaults to an empty string.

    Raises:
        - ValueError: If pie_type is not one of the allowed values.

    Returns:
        - None
    """
    plt.figure(figsize=figsize)
    
    def absolute(pct, allvals):
        absolute_count = int(pct/100.*np.sum(allvals))
        return "{:d}".format(absolute_count)

    def absolute_percent(pct, allvals):
        absolute_count = int(pct/100.*np.sum(allvals))
        return "{:d}\n({:.1f}%)".format(absolute_count, pct)

    if not isinstance(pie_type, str):
        raise TypeError(f"The pie_type parameter must be a str; you passed {type(pie_type)}.")

    if pie_type == 'percentage':
        autopct='%1.1f%%'
    elif pie_type == 'count':
        autopct=lambda pct: absolute(pct, x)
    elif pie_type in ('percentage_and_count', 'count_and_percentage'):
        autopct=lambda pct: absolute_percent(pct, x)
    else:
        raise ValueError("Invalid pie_type. Use 'percentage', 'count', or 'percentage_and_count'.")

    if len(x) != len(labels):
        raise ValueError("The length of x and labels must be the same.")

    if len(x) != len(colors):
        raise ValueError("The length of x and colors must be the same.")

    if not isinstance(title, str):
        raise TypeError(f"The title parameter must be a str; you pass {type(title)}.")
        
    # title = title.strip()
        
    plt.pie(x,
            labels=labels,
            autopct=autopct,
            startangle=startangle,
            colors=colors,
            )

    plt.title(title, fontsize=16)
    # plt.show()


plot_pie.__version__ = plot_pie.version = '0.1'

# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
# BIVARIATE
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from typing import Optional, Tuple, Union


def plot_bar_categorical(
    category_value_dict: dict,   # can be from pandas.Series.value_counts(), or collections.Counter()
    title: Optional[str] = None,
    xlabel: Optional[str] = 'Category',
    ylabel_on_left: Optional[str] = 'Count',
    ylabel_on_right: Optional[str] = 'Percentage',
    xtick_rotation: Optional[int] = 0,
    figsize: Optional[Tuple[int, int]] = (10, 6),
    fontsize_top_of_bar: Optional[int] = 11,
    # display y-axis ticks on the left; i.e. the count/frequency
    y_ticks_on_left_counts: Optional[bool] = True,
    # display y-axis ticks on the right; i.e. the percentage
    y_ticks_on_right_percentage: Optional[bool] = True,

    bar_annotation_type: Optional[Union[str, None]] = 'count_and_percentage',
    # can also be: [None, '', 'count', 'percentage', 'count_and_percentage']
    
    color: Optional[str] = None,
    alpha: Optional[float] = 0.5,   # 0 .. 1
    
    # if total==0 then this is a relative frequency, then this function will calculate total
    # if total!=0 then this is an absolute frequency, and needs to be provided
    total: Optional[int] = 0,   # CHANGE
    file_path: Optional[str] = None
) -> None:
    """
    Create and display a bar plot for categorical data. 
    The left y-axis will be the count. 
    The right y_axis will be the percentage.
    On the top of each bar will be the count and the percentage.
    The percentage is absolute if total is provided (i.e. not 0).
    The percentage is relative if total is not provided (i.e. default is 0).    
    
    Parameters:
        - category_value_dict: (dict): A dictionary containing category names as keys and their corresponding values.
        - title: Optional[str]: Title for the bar plot. Defaults to None.
        - xlabel: Optional[str]: Label for the x-axis. Defaults to 'Category'.
        - ylabel_on_left: Optional[str]: Label for the left y-axis. Defaults to 'Count'.
        - ylabel_on_right: Optional[str]: Label for the right y-axis. Defaults to 'Percentage'.
        - xtick_rotation: Optional[int]: Rotation angle for x-axis labels. Defaults to 0.
        - figsize: Optional[Tuple[int, int]]: Figure size. Defaults to (10, 6).
        - fontsize_top_of_bar: Optional[int]: Font size for text on top of the bars. Defaults to 11.
        - y_ticks_on_left_counts: Optional[bool]: display y-axis ticks on the left; i.e. the count/frequency.  Default is True.
        - y_ticks_on_right_percentage: Optional[bool]: display y-axis ticks on the right; i.e. the percentage.  Default is True.

        - bar_annotation_type: Optional[Union[str, None]]: Annotation at the top of each bar. Default is 'count_and_percentage'.
            Can also be: [None, '', 'count', 'percentage', 'count_and_percentage']
        
        - total: Optional[int]: Total value for calculating percentages. If set to 0, it will calculate the total
            from the values in the dictionary. Defaults to 0.
        - file_path: Optional[str]: file_path to save image to. Default is None, i.e. no image file is saved,

    Raises:
        - ValueError: If the input 'category_value_dict' is not a dictionary or if 'total' is not a non-negative integer.
    """
    if not isinstance(category_value_dict, dict):
        raise ValueError(f"Input 'category_value_dict' must be a dictionary; you passed a {type(category_value_dict)}.")
    
    if not isinstance(total, (int, np.int8, np.int16, np.int32, np.int64, np.uint8, np.uint16, np.uint32, np.uint64)):
        raise ValueError(f"{type(total) = }  total must be a non-negative integer.")

    if total < 0:
        raise ValueError(f"{total = }  total must be a non-negative integer.")

    # ------------------------------------
    
    # Convert to lower case for case-insensitive comparison
    if bar_annotation_type is not None:
        bar_annotation_type = bar_annotation_type.strip().lower()

    # print(f'{bar_annotation_type = }')
    
    # Check if the value is one of the allowed options
    if bar_annotation_type not in [None, '', 'count', 'percentage', 'count_and_percentage']:
        raise ValueError(f"{bar_annotation_type=} is not a valid.  It should be in [None, '', 'count', 'percentage', 'count_and_percentage'].")
    
    # ------------------------------------

    if total == 0:
        total = sum(category_value_dict.values())    
    
    fig, ax1 = plt.subplots(figsize=figsize)

    # Convert keys to strings - so the plotting of the x is exactly as
    # specified and not numeric order
    # - this is ingenious to prevent "visual" rearrangement of the various bars sorted numerically
    name_value_dict = {str(k): v
                       for k, v in category_value_dict.items()}
    # print(d_str)

    # First plot on ax1
    bars = plt.bar(
        name_value_dict.keys(),
        name_value_dict.values(),
        color=color,
        alpha=alpha,
    )
    ax1.set_ylabel(ylabel_on_left, fontsize=14)

    # Increase y-limit to add space
    max_y = max(name_value_dict.values())
    ax1.set_ylim(0, max_y * 1.06)

    # Second plot on ax2 (twin of ax1)
    ax2 = ax1.twinx()
    percentage = [value / total * 100
                  for value in name_value_dict.values()]
    ax2.set_ylabel(ylabel_on_right, fontsize=14)


    # Annotate bars
    # bar_annotation_type can be in [None, '', 'count', 'percentage', 'count_and_percentage']
    if bar_annotation_type not in [None, '']:
        for bar, count, pct in zip(bars, name_value_dict.values(), percentage):
            if bar_annotation_type == 'count_and_percentage':
                annotation_str = f'{count} ({pct:.1f}%)'
            elif bar_annotation_type == 'count':
                annotation_str = f'{count}'
            elif bar_annotation_type == 'percentage':
                annotation_str = f'{pct:.1f}%'
    
            ax1.text(bar.get_x() + bar.get_width() / 2,
                     count + max_y * 0.01,
                     # f'{count} ({pct:.1f}%)',
                     annotation_str,
                     ha='center',
                     color='black',
                     fontsize=fontsize_top_of_bar)


    # Add title and x-axis label
    ax1.set_title(title, fontsize=16)
    ax1.set_xlabel(xlabel, fontsize=14)

    # Set custom x-tick labels
    # the number of xticks
    # ax1.set_xticks(list(range(len(name_value_dict.keys()))))

    # ax1.set_xticks(list(name_value_dict.keys()))
    ax1.set_xticks(range(len(name_value_dict.keys())))
    ax1.set_xticklabels(list(name_value_dict.keys()), rotation=xtick_rotation)

    # ax1.set_xticklabels(['Not Cancelled', 'Cancelled'])   # the valus at the xticks

    if total != 0:
        # Need to slide/adjust the right y axis, i.e. percentage, to match
        # the left y axis, i.e. the absolute count
        lower_limit, upper_limit = ax1.get_ylim()
        # print("ax1 Lower Limit:", lower_limit)
        # print("ax1 Upper Limit:", upper_limit)
        ax2.set_ylim([lower_limit / total * 100, upper_limit / total * 100])

    # Optionally suppress y-ticks on the left y-axis (count/frequency)
    if not y_ticks_on_left_counts:
        ax1.set_yticks([])

    # Optionally suppress y-ticks on the right y-axis (percentage)
    if not y_ticks_on_right_percentage:
        ax2.set_yticks([])
    
    # Optionally write the chart out as a file
    if file_path is not None:
        # Apply tight_layout to adjust subplot params on savefig()
        plt.tight_layout()
        print(f"Saving file '{file_path}'") 
        plt.savefig(file_path,
                    # dpi=1000
                    )
        
    # plt.show()

plot_bar_categorical.__version__ = plot_bar_categorical.version = '0.3'

# -------------------------------------------------------------------------------------------------------
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
# -------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

def main(argv):
    """Start tests."""
    
    # test driver code here
    
    print('=====================================================')
    
    print('argv -->', argv)
    # print('json -->', json.dumps(argv, indent=4, sort_keys=True))
    
    _, *cmdline_arguments = argv

# -------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    # this is the main or testing cases to demonstrate functions in this file
    import sys
    main(sys.argv)
    
    print('----------------------------------------------')
