import random


class StoryTemplate:

    def __init__(self, name, pattern):

        self._name = name
        self._pattern = pattern

    @property
    def name(self):
        return self._name

    @property
    def pattern(self):
        return self._pattern

    def generate(self, words):

        sentence = []

        for token in self._pattern:

            if token.startswith("{") and token.endswith("}"):

                pos = token[1:-1]

                matching_words = words.filter_by_pos(pos)

                if len(matching_words) > 0:
                    random_word = random.choice(list(matching_words))
                    sentence.append(str(random_word))

            else:
                sentence.append(token)

        final_sentence = " ".join(sentence)

        return final_sentence.capitalize() + "."


TEMPLATES = [

    StoryTemplate(
        "Adventure",
        [
            "The",
            "{adj}",
            "{n}",
            "{v}",
            "{adv}",
            "{prep}",
            "the",
            "{adj}",
            "{n}"
        ]
    ),

    StoryTemplate(
        "Mystery",
        [
            "A",
            "{adj}",
            "{n}",
            "{adv}",
            "{v}",
            "while",
            "the",
            "{n}",
            "{v}",
            "{prep}",
            "the",
            "{n}"
        ]
    ),

    StoryTemplate(
        "Simple",
        [
            "The",
            "{adj}",
            "{n}",
            "{v}",
            "{adv}"
        ]
    )
]