import json

# Permutation representation
from model.utils import transform_input


class MyGraph:
    def __init__(self, txtFile, settingsFile):
        self._graph = transform_input(txtFile)

        with open(settingsFile) as file:
            self._settings = json.load(file)
            self._settings["noDim"] = len(self._graph)
            print(self._settings)

    @property
    def settings(self):
        return self._settings

    @property
    def nodes(self):
        return list(range(len(self._graph)))

    def __len__(self):
        return len(self._graph)

    def __getitem__(self, node):
        return self._graph[node]
