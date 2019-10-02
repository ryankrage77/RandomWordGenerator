# Random Word Generator
Generates random pronounceable strings.

~~Written in python 2.7 - does not yet run in python 3.x~~ Now supports python3!

## How do you know they're pronounceable?
Every time a new word is generated, it is sent to me for approval.

Nah, just make sure no no more than two consonants or three vowels appear together.

This results in words that are mostly possible to say, but you do get weird stuff like qx, db, etc.

## How do you know they're random?
I use Python's `Random` library/function/module thingy. The shorter the words you generate, the more likely they are to match an existing word.

### Future Plans
- tidy code up
- fix length 0 bug
- Better 'pronounceable' check
- Check generated words againsts a dictionary to see if they already exist.
- Allow for language-root specific generation, such as germanic or Japonic.
