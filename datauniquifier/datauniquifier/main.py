"""Define the command-line interface for the datauniquifier program."""

from rich.console import Console

from pathlib import Path

import os
import psutil  # type: ignore

import typer

from datauniquifier import analyze
from datauniquifier import extract
from datauniquifier import uniquify

UNIQUE_FUNCTION_BASE = "unique"
UNDERSCORE = "_"

cli = typer.Typer()

console = Console()


@cli.command()
def main(
    approach: str = typer.Option(...),
    column: int = typer.Option(...),
    data_file: Path = typer.Option(...),
    display: bool = typer.Option(False, "--display"),
):
    """Create the list of data values in stored in the specified file and then uniquify the file contents."""
    # display the debugging output for the program's command-line arguments
    console.print("")
    console.print(f"The chosen approach to uniquify the file is: {approach}")
    console.print("")
    console.print(f"The data file that contains the input is: {data_file}")
    console.print("")
    # construct the full name of the function to call
    function = UNIQUE_FUNCTION_BASE + UNDERSCORE + approach
    # construct the requested function from the compute module
    # Reference: https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
    function_to_call = getattr(uniquify, function)
    # declare the variables that will store file content for a valid file
    data_text = ""
    data_column_text_list = []
    # --> the file was not specified so we cannot continue using program
    if data_file is None:
        console.print("No data file specified!")
        raise typer.Abort()
    # --> the file was specified and it is valid so we should read and check it
    if data_file.is_file():
        # read in the contents of the file and display welcome messages
        with open("input/data.txt", "r") as input_file:
            data_text = input_file.read()
        # read the example output in Discord to see what your program should
        # produce as output, ensuring that the program output matches exactly
        # display a final message and some extra spacing, asking a question
        # about the efficiency of the approach to computing the number sequence
        console.print()
        data_column_text_list = extract.extract_data_given_column(data_text, column)
        console.print (f" The data file contains {len(data_column_text_list)} data values in it!")
        console.print()
        console.print("Let's do some uniquification!")
        console.print()
        console.print(":mag: So, was this an efficient approach to uniquifying the data?")
        console.print()
        # use the extract_data_given_column function to get a data column text list
    # call the constructed function and capture the result
        uniquified_list = function_to_call(data_column_text_list)
    # display debugging information with the function's output
    # make sure to only take this step if the --display is specified
        if display:
            print(uniquified_list)
    # display the estimated overall memory use as reported by the operating system
    # Reference:
    # https://stackoverflow.com/questions/938733/total-memory-used-by-python-process
    # Note: you may need to adjust the implementation of the format_bytes function
    # in the analyze module depending on your operating system
    process = psutil.Process(os.getpid())
    console.print()
    console.print("Estimated overall memory according to the operating system:")
    console.print("   " + analyze.format_bytes(process.memory_info().vms))
    console.print()
    # display the reduction and percent reduction that is a result of the uniquification process
    console.print(":mag: So, did this remove a lot of duplicate data?")
    console.print()
    console.print(f"   The number of values removed from the data: {analyze.calculate_reduction(data_column_text_list, uniquified_list)}")
    console.print(f"   The percent reduction due to uniquification: {analyze.calculate_percent_reduction(data_column_text_list, uniquified_list)}")
    console.print()
    # make sure that your program output is exactly like the
    # output provided in the project description on the Proactive Programmers web site
    # once you finish implementing the program make sure that you evaluate:
    # --> Time efficiency and memory consumption and percent reduction for column 0 and column 1
    #     when running at least three of the uniquification algorithms in the uniquify module
