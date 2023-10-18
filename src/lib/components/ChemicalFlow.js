import React from 'react';
import PropTypes from 'prop-types';
import { ChemicalFlow as RealComponent } from '../LazyLoader';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
const ChemicalFlow = (props) => {
    return (
        <React.Suspense fallback={null}>
            <RealComponent {...props}/>
        </React.Suspense>
    );
};

ChemicalFlow.defaultProps = {};

ChemicalFlow.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * A label that will be printed when this component is rendered.
     */
    label: PropTypes.string.isRequired,

    /**
     * Nodes to display.
     * Example:
     * [
     *     {
     *         'id': '1',
     *         'data': {'value': 'c1ccccc1', 'label': 'c1ccccc1'},
     *         'type': 'molecule',
     *         'sourcePosition': 'right'
     *     },
     *     {
     *         'id': '2',
     *         'type': 'molecule',
     *         'data': {'value': 'CCO', 'label': 'CCO'}
     *     },
     *     {
     *         'id': '3',
     *         'type': 'molecule',
     *         'data': {'value': 'CC(=O)Oc1ccccc1C(=O)O', 'label': 'CC(=O)Oc1ccccc1C(=O)O'}
     *     }
     * ]
     * */
    nodes: PropTypes.array,

    /**
     * The Edges to connect nodes.
     * Example:
     * [
     *    {
     *        'id': '1-2',
     *        'source': '1',
     *        'target': '2',
     *        'label': '+',
     *        'type': 'step',
     *        'animated': true,
     *    },
     *    {
     *        'id': '2-3',
     *        'source': '2',
     *        'target': '3',
     *        'label': 'expert',
     *        'type': 'molecule',
     *        'animated': true,
     *        'data': {'catalyst': 'CCO'},
     *        'markerEnd': {'type': 'arrow', 'color': '#000'},
     *    }
     * ]
     * */
    edges: PropTypes.array,

    /**
     * Default height: 240px*/
    height: PropTypes.string,

    /**
     * selectionEvent
     * type:
     * node:
     * edge:
     */
    selectionEvent: PropTypes.any,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default ChemicalFlow;

export const defaultProps = ChemicalFlow.defaultProps;
export const propTypes = ChemicalFlow.propTypes;
