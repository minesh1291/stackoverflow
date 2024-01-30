## Python Dictionary

```python
def np_int_to_int(d:dict) -> None:
    """Converts np.int64 to int in a dict

    Parameters
    ----------
    d : dict
        dict to be converted
    """
    for k,v in d.items():
        if isinstance(v, np.int64):
            d[k] = int(v)
        if isinstance(v, dict):
            np_int_to_int(v)
```

```py
def print_type(d: dict) -> None:
    """Prints the type of each value in a dictionary.

    Parameters
    ----------
    d : dict
        Dictionary to print the types of.
    """
    for k,v in d.items():
        print(k, type(v))
        if isinstance(v, dict):
            print_type(v)
```
