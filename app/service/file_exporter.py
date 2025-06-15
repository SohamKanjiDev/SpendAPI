import csv 
import io

class FileExporter:
    """
    This class is responsible for exporting tabular data to files such as .csv.
    """
    def __init__(self, field_names: list[str], data : list[list[str]]):
        """
        Initialise the exporter class.

        :param field_names: is the list of field names.
        :param data: is the list of corresponding row data.
        """
        self._field_names = field_names
        self._data = data 

    def getCSVString(self) -> str:
        """
        Get the csv string.

        :return: csv string from data.
        """
        with io.StringIO() as output:
            writer = csv.writer(output)
            writer.writerow(self._field_names)
            writer.writerows(self._data)
            return output.getvalue()