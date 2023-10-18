# AUTO GENERATED FILE - DO NOT EDIT

export chemicalflow

"""
    chemicalflow(;kwargs...)

A ChemicalFlow component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `edges` (Array; optional): The Edges to connect nodes.
Example:
[
   {
       'id': '1-2',
       'source': '1',
       'target': '2',
       'label': '+',
       'type': 'step',
       'animated': true,
   },
   {
       'id': '2-3',
       'source': '2',
       'target': '3',
       'label': 'expert',
       'type': 'molecule',
       'animated': true,
       'data': {'catalyst': 'CCO'},
       'markerEnd': {'type': 'arrow', 'color': '#000'},
   }
]
- `height` (String; optional): Default height: 240px
- `label` (String; required): A label that will be printed when this component is rendered.
- `nodes` (Array; optional): Nodes to display.
Example:
[
    {
        'id': '1',
        'data': {'value': 'c1ccccc1', 'label': 'c1ccccc1'},
        'type': 'molecule',
        'sourcePosition': 'right'
    },
    {
        'id': '2',
        'type': 'molecule',
        'data': {'value': 'CCO', 'label': 'CCO'}
    },
    {
        'id': '3',
        'type': 'molecule',
        'data': {'value': 'CC(=O)Oc1ccccc1C(=O)O', 'label': 'CC(=O)Oc1ccccc1C(=O)O'}
    }
]
- `selectionEvent` (Bool | Real | String | Dict | Array; optional): selectionEvent
type:
node:
edge:
"""
function chemicalflow(; kwargs...)
        available_props = Symbol[:id, :edges, :height, :label, :nodes, :selectionEvent]
        wild_props = Symbol[]
        return Component("chemicalflow", "ChemicalFlow", "dash_chemical_flow", available_props, wild_props; kwargs...)
end

