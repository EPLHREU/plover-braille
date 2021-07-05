> Plover plugin for Braille writing

A plugin allowing writing of Braille with plover, directly translating Braille input to english.
This system is based on Unified English Braille (UEB).

Due to a current limitation and [hard-coded value in plover](https://github.com/openstenoproject/plover/blob/6c5167f48476a499f2a0dbb973f6b77123bde429/plover/steno.py#L21) using numbers 1 to 6 for the cells lead to issues and inconsistencies with the dictionary.
To eliviate this issue, the references for the dots inside each cell line up with the qwerty keymap for the layout.

| cell    | layout  |
| ------- | ------- |
| `1 : f` | `4 : j` |
| `2 : d` | `5 : k` | 
| `3 : s` | `6 : l` | 

![Layout Diagram](img/layout.png)

![Braille Chart](img/braille-chart.png)

Made with Braille knowledge from: @a-lint thanks!


