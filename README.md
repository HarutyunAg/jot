# Jot (ノ-_-)ノ ミ {...}

Jot can work with JSON \ TOML \ YAML \XML. This guy easily retrieve nested values using dot notation.
And when it comes to string formatting, Jot’s got your back — it safely replaces placeholders with values, so you can create templates using dot notation without worrying about missing data. 

## Usage example

```json
    {
        "user": {
            "name": "Jot",
            "pocket": {
                "box" : "🦎"
            }
        }
    }
```

```python
from jot import Jot

jot = Jot("path/to/dots.json")
jot.get("user.pocket.box")
# output --> 🦎
```

```python
template = "Hey {user.name}, what's in your pocket? {user.pocket.box}"
jot.format(template)
# Output: Hey Jot, what's in your pocket? 🦎
```