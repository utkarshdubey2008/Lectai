# Usage Guide

This guide provides an overview of how to use the LectAI Python library.

## Basic Usage

```python
from lectai import LectAI

client = LectAI()
response = client.get_response("Hello, Lect AI!")
print(response)
```

## Advanced Usage

You can customize the base URL if needed:

```python
client = LectAI(base_url="https://custom-api-url.com/")
response = client.get_response("Custom prompt")
print(response)
```

For more detailed examples and use cases, refer to our [API Reference](api_reference.md).