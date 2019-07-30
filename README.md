# Kolr

✨🎨🖌 Terminal independent colors, palettes and styles that work as expected.

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

## WIP

The rest of this readme is a WIP.