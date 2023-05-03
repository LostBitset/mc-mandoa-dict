# mandoacreator-dict
The dictionary as taken from mandoacreator.com

This generates a nice Python object for each entry from the JSON provided by [mandocreator.com](mandocreator.com).

To obtain `capture.json`:

1. Go to [https://www.mandocreator.com/tools/dictionary.html#](https://www.mandocreator.com/tools/dictionary.html#).
2. Open the JS console (Firefox: Ctrl+Shift+K).
3. Type `copy(JSON.stringify(dict))` and press enter.

The contents should now be copied to your clipboard. Paste them into `capture.json`.

