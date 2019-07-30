# Kolr

✨🎨🖌 Terminal independent colors, palettes and styles done right.

## Quickstart ⚡

**This library is still underdevelopment the below is the expected feature set for version 0.1.0**

### Terminal Style
```python
import kolr

# simple expression support
print(kolr.RED + 'This text is red!')
# style is restored
print(kolr.RED + 'This is Red' + kolr('This is green', style='green') + 'This is red')
# style can be nested and chained, strings are only generated when needed.
print(kolr('This is Red' + kolr('This is green', style='green')('This is default') + 'This is red', style='red'))
```

### Color Palettes
```python
import kolr.palette.xkcd as c

# palettes automatically render as monochrome, 3bit, 4bit,
# 8bit or 24bit colors depending on terminal support.
print(c['velvet'] + 'This is the closest color to velvet if the terminal does not support 24bit colors')

# code generation enabling autocompletion, even for custom palettes.
print(c.velvet + 'This is velvet in a terminal that supports 24bit colors')
```

## Why 💭

A quick search of `terminal color` on Github reveals over 150+ packages.
Why another one you ask for styling the terminal?

1. Kolr automatically simplifies any color palette depending on the terminal color support.
2. Kolr supports restoring the style after a styling sequence ends.
3. Kolr supports arbitrary color palettes *with* auto-completion for popular editors, through code generation.
    - (WIP) You can even publish or export your color palette to be used without Kolr.

## WIP ‍🚧

The rest of this readme is a WIP.