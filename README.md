# RandomWordGenerator
Generates random pronounceable strings

## How do you know they're pronounceable?
Every time a new word is generated, it is sent to me for approval.
Nah, just make sure no no more than two consonants or three vowels appear together.

## How do you know they're random?
I use Python's `Random` library/function/module thingy. The shorter the words you generate, the more likely they are to match an existing word.

### Future Plans
- Check generated words againsts a dictionary to see if they already exist.
- Allow for language-root specific generation, such as germanic or Japonic.
