# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MoleculeItem(Component):
    """A MoleculeItemReact component.


Keyword arguments:

- value (string; required)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_chemical_flow'
    _type = 'MoleculeItemReact'
    @_explicitize_args
    def __init__(self, value=Component.REQUIRED, **kwargs):
        self._prop_names = ['value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['value']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(MoleculeItem, self).__init__(**args)
