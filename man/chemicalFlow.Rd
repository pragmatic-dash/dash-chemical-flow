% Auto-generated: do not edit by hand
\name{chemicalFlow}

\alias{chemicalFlow}

\title{ChemicalFlow component}

\description{
ExampleComponent is an example component. It takes a property, `label`, and displays it. It renders an input with the property `value` which is editable by the user.
}

\usage{
chemicalFlow(id=NULL, edges=NULL, height=NULL, label=NULL, nodes=NULL,
value=NULL)
}

\arguments{
\item{id}{Character. The ID used to identify this component in Dash callbacks.}

\item{edges}{Unnamed list. The Edges to connect nodes.
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
]}

\item{height}{Character. Default height: 240px}

\item{label}{Character. A label that will be printed when this component is rendered.}

\item{nodes}{Unnamed list. Nodes to display.
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
]}

\item{value}{Character. The value displayed in the input.}
}

\value{named list of JSON elements corresponding to React.js properties and their values}

