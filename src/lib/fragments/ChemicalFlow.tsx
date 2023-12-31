import React, {useEffect, useState, useCallback} from 'react';
import PropTypes from 'prop-types';
import 'reactflow/dist/style.css';
import './ChemicalFlow.css'
import DownloadButton from './downloadButton';

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

const nodeWidth = 100;
const nodeHeight = 80;
// const nodeWidth = 172;
// const nodeHeight = 36;
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
    g.setGraph({ rankdir: direction , ranksep: 120, nodesep: 20, edgesep: 0, ranker: "longest-path"});
    // g.setGraph({ rankdir: direction});

    nodes.forEach((node) => {
        g.setNode(node.id, { width: nodeWidth, height: nodeHeight });
    });

    edges.forEach((edge) => {
        g.setEdge(edge.source, edge.target);
    });

    Dagre.layout(g);

    nodes.forEach((node: Node) => {

        const nodeWithPosition = g.node(node.id);
        // console.log("iterate node " + node.id + " rank " + nodeWithPosition.rank);

        if (!(node.sourcePosition)) {
            node.sourcePosition = isHorizontal ? 'right' as Position : 'bottom' as Position;
        }
        if (!(node.targetPosition)) {
            node.targetPosition = isHorizontal ? 'left' as Position : 'top' as Position;
        }

        // We are shifting the dagre node position (anchor=center center) to the top left
        // so it matches the React ChemicalFlow node anchor point (top left).
        // x: nodeWithPosition.x - nodeWidth / 2,
        node.position = {
            x: nodeWithPosition.x,
            y: nodeWithPosition.y - nodeHeight / 2,
        };
        if (node.type === "reaction") {
            // get previous node
            const previousNode = g.predecessors(node.id)[0];
            const previousNodeWithPosition = g.node(previousNode);

            // get next node
            const nextNode = g.successors(node.id)[0];
            const nextNodeWithPosition = g.node(nextNode);
            node.position.x = previousNodeWithPosition.x + 180;
            node.position.y = previousNodeWithPosition.y + nodeHeight / 2 + 10;

            const rank = nodeWithPosition.rank

            // get nodes with bigger rank
            const biggerRankNodes = g.nodes().filter((nodeId) => {
                return g.node(nodeId).rank === rank + 2 || g.node(nodeId).rank === rank;
            });

            // give bigger rank nodes a smaller x position
            biggerRankNodes.forEach((nodeId) => {
                const biggerRankNodesWithPosition = g.node(nodeId);
                biggerRankNodesWithPosition.x = biggerRankNodesWithPosition.x - 100;
                g.setNode(nodeId, biggerRankNodesWithPosition);
            });
        }

        return node;
    });
    return { nodes, edges };
}

const nodeTypes = {molecule: MoleculeNode, reaction: ReactionNode};
const edgeTypes = {
  molecule: MoleculeEdge,
};

// const defaultViewport = { x: 0, y: 0 };

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
    const [reactFlowInstance, setReactFlowInstance] = useState(null);

    useEffect(() => {
        window.initRDKitModule().then((rdkit) => {
            window.RDKit = rdkit;
            setRdkitLoaded(true);
        });
    }, []);

    // const onLoad = (rf) => {
    //     setReactFlowInstance(rf);
    // };

    useEffect(() => {
        if (reactFlowInstance) {
            setTimeout(() => reactFlowInstance.fitView( {padding: 100}), 0)
            setTimeout(() => reactFlowInstance.setViewport({x: -1000, y:0, zoom:1}), 0)
        }
    }, [reactFlowInstance]);

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
        <div style={{ width: '100%', height: height || '600px' }}>
            {rdkitLoaded ? <ReactFlow nodes={nodesStates}
                       edges={edgesStates}
                       onNodesChange={onNodesChange}
                       onEdgesChange={onEdgesChange}
                       onConnect={onConnect}
                       onNodeClick={onNodeClick}
                       onEdgeClick={onEdgeClick}
                       nodeTypes={nodeTypes}
                       edgeTypes={edgeTypes}
                       fitView
                       // onLoad={onLoad}
                       // defaultViewport={defaultViewport}
                       attributionPosition="top-left" >
                <Controls />
                <DownloadButton />
            </ReactFlow>: <span className="loading-span">Loading...</span>}
        </div>
    );

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
