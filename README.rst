dummy_data
----------

Generates dummy data in various formats (currently only JSON implemented) based on user-defined model strings.

To use:

    >>> dd_model = '''
    ... {
    ...     "name": "{% first_name %} {% last_name %}",
    ...     "dob": "{% date %}"
    ... }'''
    >>> from dummy_data import json
    >>> json(dd_model)
    '\n{\n\t"name": "John Cleese",\n\t"dob": "10/27/1939"\n}'
