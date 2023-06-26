class Matrix:
    def __init__(self, rows, columns):
        self._matrix = [[None for n in range(columns)] for i in range(rows)]
        self._rows_content = rows
        self._columns_content = columns
    
    def set_value(self, rows, columns, value):
        self._matrix[rows][columns] = value

    def get_value(self, rows, columns):
        return self._matrix[rows][columns]
    
    def get_rows_content(self):
        return self._rows_content
    
    def get_columns_content(self):
        return self._columns_content
    
import pprint

m = Matrix(5, 7)
for i in range(m.get_rows_content()):
    for n in range(m.get_columns_content()):
        m.set_value(i, n, 1)

pprint.pprint(m._matrix)