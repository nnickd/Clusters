class cluster:

    def __init__(self):
        self.ents = []

    def add(self, *ents):
        for ent in ents:
            self.ents.append(ent)

    def remove(self, *ents):
        for ent in ents:
            self.ents.remove(ent)
