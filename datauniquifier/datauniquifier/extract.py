"""Extract the data."""

from typing import List

# Sample of the data set:

# dana74@mahoney-perez.com,"Administrator, charities/voluntary organisations"
# nathanjohnson@davila.net,Software engineer
# pbush@gmail.com,"Journalist, newspaper"
# timothy75@chang.com,Osteopath
# gsparks@yahoo.com,"Psychologist, clinical"
# daniel39@gmail.com,Logistics and distribution manager
# jason85@ward.com,Logistics and distribution manager
# jacobwalton@hotmail.com,Television camera operator
# markmcgee@hernandez-roberts.com,IT sales professional
# shannon35@allen.com,Ecologist
# ksnyder@snow-brooks.net,Building surveyor


def extract_data_given_column(data: str, column: int) -> List[str]:
    """Extract a specified data column from the provided textual contents."""
    # create an empty list of the data
    data_collection = []
    # note that the data file:
    # --> contains two columns
    # --> each of which contains textual data
    # --> refer to the file called input/data.txt to learn more about
    # the format of the comma separated value (CSV) file that we must parse
    # --> iterate through each line of the file and extract the current job
    for row in data.splitlines():
        result = row.split(",")[column]
        data_collection.append(result)
    # ---> extract the specified column that contains the requested data
    # return the list of all of the specified column
    return data_collection
