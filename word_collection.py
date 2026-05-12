from word import Word


class WordCollection:

    def __init__(self):
        self._words = []

    @classmethod
    def from_file(cls, filepath):

        collection = cls()

        with open(filepath, "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                parts = line.split()

                if len(parts) != 2:
                    continue

                text, pos = parts

                try:
                    word = Word(text, pos)
                    collection.add(word)

                except ValueError:
                    continue

        return collection

    def add(self, word):

        if not isinstance(word, Word):
            raise TypeError("Must add a Word object")

        self._words.append(word)

    def filter_by_pos(self, part_of_speech):

        filtered = WordCollection()

        for word in self._words:

            if word.part_of_speech == part_of_speech:
                filtered.add(word)

        return filtered

    def sorted_words(self, reverse=False):

        sorted_collection = WordCollection()

        for word in sorted(self._words, reverse=reverse):
            sorted_collection.add(word)

        return sorted_collection

    def __len__(self):
        return len(self._words)

    def __getitem__(self, index):
        return self._words[index]

    def __contains__(self, item):
        return item in self._words

    def __iter__(self):
        return iter(self._words)

    def __repr__(self):
        return f"WordCollection({len(self)} words)"