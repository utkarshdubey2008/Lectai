# API Reference

## LectAI Class

### Initialization

```python
LectAI(base_url=None)
```

- `base_url` (str): The base URL for the API. Defaults to a hidden endpoint URL.

### Methods

#### `get_response(user_prompt)`

- `user_prompt` (str): The user's input prompt.
- Returns: A dictionary containing the API response.

### Example

```python
from lectai import LectAI

client = LectAI()
response = client.get_response("Hello, Lect AI!")
print(response)
```

For any questions or support, please contact us at [admin@lectai.io](mailto:admin@lectai.io).