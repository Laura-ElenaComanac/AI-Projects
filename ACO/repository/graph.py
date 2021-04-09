import json
from model.utils import transform_input


class MyGraph:
    def __init__(self, txtFile, settingsFile):
        self._graph = transform_input(txtFile)

        with open(settingsFile) as file:
            self._settings = json.load(file)
            self._settings["noDim"] = len(self._graph)
            print(self._settings)

        self._trace = [[self.settings['Q'] for _ in line] for line in self._graph]

    @property
    def settings(self):
        return self._settings

    @property
    def nodes(self):
        return list(range(len(self._graph)))

    @property
    def trace(self):
        return self._trace

    def __len__(self):
        return len(self._graph)

    def __getitem__(self, node):
        return self._graph[node]

    def __setitem__(self, key, value):
        self._graph[key] = value

    def __str__(self):
        return "\n".join(
            ",".join([str(val) for val in line])
            for line in self._graph
        )


