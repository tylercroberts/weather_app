class Mapper:
    def __init__(self):
        self._mapping = dict()

    def _add(self, source, dest):
        self._mapping[source] = dest

    def remap_key(self, source, dest):
        self._add(source, dest)

    def remap(self, itemslist):
        return [self._exec(item) for item in itemslist]

    def _exec(self, src_dict):
        dest = dict()

        if not src_dict:
            raise AttributeError("The source dictionary cannot be empty or None")

        for k, v in src_dict.items():
            try:
                new_key = self._mapping[k]
                dest[new_key] = v
            except KeyError:
                dest[k] = v

        return dest
