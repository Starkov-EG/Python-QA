import os.path

import cattr

from python_qa.utils.classes import is_attrs_class


class GraphQLBase:
    query: str = None
    variables: dict = {}
    name: str = None

    def __init__(self, query_file: str, name: str = None, **variables):
        self._load_from_file(query_file)
        self.variables = cattr.Converter().unstructure(self.variables) if is_attrs_class(self.variables) else variables
        self.name = name

    def _load_from_file(self, file: str):
        if os.path.exists(file):
            with open(file, "r", encoding="utf-8") as f:
                self.query = f.read()
        else:
            raise Exception("GraphQL file not found")

    @property
    def payload(self):
        return {
            "query": self.query,
            "variables": self.variables,
            "operationName": self.name
        }
