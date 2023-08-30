import random
class Sniffer:

    def CodeAnalysis(self, jcode):

        dimensions = ["readability", "consistency", "modularity", "maintainability", "testability", "performance"]
        reveal_dimensions = {}
        for d in dimensions:

            reveal_dimensions[d] = random.uniform(0, 1)
        return reveal_dimensions

Sniffer = Sniffer()