# Jot
**Jot** is a lightweight Python library for accessing nested strings in JSON files using dot notation.  
I often frustrated having many static strings spread all over code. 
With Jot, I can centralize my string resources in JSON files, allowing for cleaner code and easier updates.

## Usage example

To use Jot, first create a JSON file with your strings, for example:

```json
{
    "en": {
        "title": {
            "label": "Hi!",
            "description": "Welcome to Jot"
        }
    }
}

```

Then, you can access values as follows:

```python
from jot import Jot

jot = Jot("path/to/dots.json")
label: str = jot.get("en.title.label", default="not found")
```
