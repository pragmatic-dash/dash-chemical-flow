# AUTO GENERATED FILE - DO NOT EDIT

export molecule

"""
    molecule(;kwargs...)

A Molecule component.

Keyword arguments:
- `smiles` (String; required)
"""
function molecule(; kwargs...)
        available_props = Symbol[:smiles]
        wild_props = Symbol[]
        return Component("molecule", "Molecule", "dash_chemical_flow", available_props, wild_props; kwargs...)
end

