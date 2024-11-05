# Jot

I feel bad when many static strings spread all over the code.  
So I create this little boy called **Jot** to centralize my resources in JSON and easily access nested values using dot notation.

## Usage example

To use Jot, first create a JSON file with your strings, for example:

```json
{
    "en": {
        "title": {
            "label": "Hi!",
            "description": "I'm Jot. What u want ? (ノ-_-)ノ ミ ┴┴"
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
