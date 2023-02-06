from typing import List


def longer_word(word1: str, word2: str) -> str:
    """
    Returns the longer word when passed 2 words

    Args:
        word1 (str): First word
        word2 (str): Second word

    Returns:
        str: The longer word
    """
    if len(word1) > len(word2):
        return word1
    elif len(word2) > len(word1):
        return word2
    else:
        return word1


def longest_word(sentence: str | List[str]) -> str:
    """
    Computes longest word recursively given a sentence

    Args:
        sentence (str): the sentence we are given

    Returns:
        str: The longest word
    """
    # "This has the longest word." --> ['This', 'has', 'the', 'longest', 'word']
    # base case: 1 element in the list, then we just return it
    split_sentence = sentence.split(" ")
    if (
        len(split_sentence) == 1
    ):  # doing this, because we receive the sentence initially as a str, and if it is a list, testing if it only contains 1 element
        return sentence[0]
    else:
        # magic happens, we recursively call the longest_word, with a SHORTER argument, aka reducing the problem
        # that gives us an array of all the words in the sentence
        return longer_word(split_sentence[0], longest_word(" ".join(split_sentence)))


if __name__ == "__main__":
    example_sentence = "This has the longest word."
    print(longest_word(example_sentence))
    print(longest_word(example_sentence) == "longest")
