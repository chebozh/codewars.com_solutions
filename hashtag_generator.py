"""The marketing team is spending way too much time typing in hashtags.
Let's help them with out own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""


# solution
def generate_hashtag(s):
    if not s:
        return False
    words = s.split()
    words = [word.capitalize() for word in words]
    result = '#{}'.format("".join(words))
    return result if len(result) <= 140 else False


# examples
print(generate_hashtag("    Hello     World   "))
print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag(''))
