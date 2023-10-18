import React, {useEffect, useState, useCallback} from 'react';
import PropTypes from 'prop-types';
import 'reactflow/dist/style.css';

import Dagre from '@dagrejs/dagre';
import ReactFlow, {
    Node,
    Edge,
    Connection,
    addEdge,
    Controls,
    Position,
    NodeChange,
    EdgeChange,
} from 'reactflow';
import {applyEdgeChanges, applyNodeChanges, useNodesState,
    useEdgesState} from 'reactflow';
import "./molecule-edge.css";
import "./molecule-node.css";
import "./reaction-node.css"
import 'antd/dist/reset.css'
import MoleculeNode from "./MoleculeNode";
import ReactionNode from "./ReactionNode";
import MoleculeEdge from "./MoleculeEdge";

const nodeWidth = 172;
const nodeHeight = 36;
const g = new Dagre.graphlib.Graph().setDefaultEdgeLabel(() => ({}));

enum SelectionEventType {
    NODE = "node",
    EDGE = "edge"
}
interface SelectionEvent {
    type: SelectionEventType;
    nodes?: Node[],
    edges?: Edge[]
}
const getLayoutElements = (nodes: Node[], edges: Edge[], direction = 'LR') => {

    const isHorizontal = direction === 'LR';
    g.setGraph({ rankdir: direction });

    nodes.forEach((node) => {
        g.setNode(node.id, { width: nodeWidth, height: nodeHeight });
    });

    edges.forEach((edge) => {
        g.setEdge(edge.source, edge.target);
    });

    Dagre.layout(g);

    nodes.forEach((node: Node) => {
        const nodeWithPosition = g.node(node.id);
        if (!(node.sourcePosition)) {
            node.sourcePosition = isHorizontal ? 'right' as Position : 'bottom' as Position;
        }
        if (!(node.targetPosition)) {
            node.targetPosition = isHorizontal ? 'left' as Position : 'top' as Position;
        }

        // We are shifting the dagre node position (anchor=center center) to the top left
        // so it matches the React ChemicalFlow node anchor point (top left).
        node.position = {
            x: nodeWithPosition.x - nodeWidth / 2,
            y: nodeWithPosition.y - nodeHeight / 2,
        };

        return node;
    });
    return { nodes, edges };
}

const nodeTypes = {molecule: MoleculeNode, reaction: ReactionNode};
const edgeTypes = {
  molecule: MoleculeEdge,
};
const defaultViewport = { x: 0, y: 0, zoom: 0.25 };

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
const ChemicalFlow = (props) => {
    const {id, label, setProps, nodes, edges, height, selectionEvent} = props;
    const [rdkitLoaded, setRdkitLoaded] = useState(false);

    useEffect(() => {
        window.initRDKitModule().then((rdkit) => {
            window.RDKit = rdkit;
            setRdkitLoaded(true);
        });
    }, []);

    console.log("height:" + height)

    // def events
    const [
        nodesStates,
        setNodes,
    ] = useNodesState(nodes);
    const [
        edgesStates,
        setEdges,
    ] = useEdgesState(edges);

    const onNodesChange = useCallback(
        (changes: NodeChange[]) =>
            setNodes((nds) => applyNodeChanges(changes, nds)),
        [setNodes]
    );
    const onEdgesChange = useCallback(
        (changes: EdgeChange[]) =>
            setEdges((eds) => applyEdgeChanges(changes, eds)),
        [setEdges]
    );
    const onConnect = useCallback(
        (params: Edge | Connection) => setEdges((els) => addEdge(params, els)),
        [setEdges]
    );

    // return selection to streamlit
    const onNodeClick = (event: React.MouseEvent, node: any) => {
        // Handle node click event
        console.log('Node clicked:', node);
        if (node.type === "molecule") {
            console.log('Molecule clicked:', node);
            setProps({selectionEvent: {
                    type: SelectionEventType.NODE,
                    nodes: [node]
                }})
        } else {
            console.log("skip node event for type")

        }
    };

    const onEdgeClick = (event: React.MouseEvent, edge: any) => {
        // Handle node click event
        console.log('Edge clicked:', edge);
        setProps({selectionEvent: {
                type: SelectionEventType.EDGE,
                edges: [edge]
        }})
    };

    // auto layout
    getLayoutElements(
        nodes,
        edges,
        'LR'
    );

    return (
        <div style={{ width: '100%', height: height || '500px' }}>
            <ReactFlow nodes={nodesStates}
                       edges={edgesStates}
                       onNodesChange={onNodesChange}
                       onEdgesChange={onEdgesChange}
                       onConnect={onConnect}
                       onNodeClick={onNodeClick}
                       onEdgeClick={onEdgeClick}
                       nodeTypes={nodeTypes}
                       edgeTypes={edgeTypes}
                       fitView
                       defaultViewport={defaultViewport}
                       attributionPosition="top-left" >
                <Controls />
            </ReactFlow>
        </div>
    );
//     ------------------ original output -----------------
//         return (
//         <div id={id}>
//             ExampleComponent: {label}&nbsp;
//
//         <div>
//             {rdkitLoaded ? (
//                     <span
//                         dangerouslySetInnerHTML={{
//                     __html: window.RDKit.get_mol("CCO").get_svg(),
//                 }}
//     />
// ) : (
//         "Loading..."
//     )}
//         </div>
//             <label>bbbbbbbbbbb</label>
//             <div id="example-1-output" className="ml-6 column"></div>
//             <script>
//                console.log("aaa")
//             </script>
//
//             <input
//                 value={value}
//                 onChange={
//                     /*
//                         * Send the new value to the parent component.
//                         * setProps is a prop that is automatically supplied
//                         * by dash's front-end ("dash-renderer").
//                         * In a Dash app, this will update the component's
//                         * props and send the data back to the Python Dash
//                         * app server if a callback uses the modified prop as
//                         * Input or State.
//                         */
//                     e => setProps({value: e.target.value})
//                 }
//             />
//         </div>
//     );

}

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
     *     {
     *         'id': '1-2',
     *         'source': '1',
     *         'target': '2',
     *         'label': '+',
     *         'type': 'step',
     *         'animated': true
     *     },
     *     {
     *         'id': '2-3',
     *         'source': '2',
     *         'target': '3',
     *         'label': 'expert',
     *         'type': 'molecule',
     *         'animated': true,
     *         'data': {'catalyst': 'CCO'},
     *         'markerEnd': {'type': 'arrow', 'color': '#000'},
     *     }
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
