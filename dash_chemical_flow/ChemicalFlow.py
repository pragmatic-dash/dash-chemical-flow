# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ChemicalFlow(Component):
    """A ChemicalFlow component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- edges (list; optional):
    The Edges to connect nodes. Example: [    {        'id': '1-2',
    'source': '1',        'target': '2',        'label': '+',
    'type': 'step',        'animated': True,    },    {        'id':
    '2-3',        'source': '2',        'target': '3',        'label':
    'expert',        'type': 'molecule',        'animated': True,
    'data': {'catalyst': 'CCO'},        'markerEnd': {'type': 'arrow',
    'color': '#000'},    } ].

- height (string; optional):
    Default height: 240px.

- label (string; required):
    A label that will be printed when this component is rendered.

- nodes (list; optional):
    Nodes to display. Example: [     {         'id': '1',
    'data': {'value': 'c1ccccc1', 'label': 'c1ccccc1'},
    'type': 'molecule',         'sourcePosition': 'right'     },     {
    'id': '2',         'type': 'molecule',         'data': {'value':
    'CCO', 'label': 'CCO'}     },     {         'id': '3',
    'type': 'molecule',         'data': {'value':
    'CC(=O)Oc1ccccc1C(=O)O', 'label': 'CC(=O)Oc1ccccc1C(=O)O'}     }
    ].

- value (string; optional):
    The value displayed in the input."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_chemical_flow'
    _type = 'ChemicalFlow'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, label=Component.REQUIRED, value=Component.UNDEFINED, nodes=Component.UNDEFINED, edges=Component.UNDEFINED, height=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'edges', 'height', 'label', 'nodes', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'edges', 'height', 'label', 'nodes', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['label']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(ChemicalFlow, self).__init__(**args)
