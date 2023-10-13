import React, { memo } from "react";
import { Handle, NodeProps, Position } from "reactflow";

import Molecule from "./Molecule";
// eslint-disable-next-line import/no-duplicates

const MoleculeNode = ({
                          data,
                          isConnectable,
                          targetPosition = Position.Right,
                          sourcePosition = Position.Left
                      }: NodeProps) => {
    const purpleMode = data?.commercial
    let className = "node-molecule"
    if (purpleMode===false) {
        className = "node-molecule-purple"
    }
    return (
        <div className={className}>
            <Handle
                type="target"
                position={targetPosition}
                isConnectable={isConnectable}
            />
            <div>
                <div style={{ width: '100%', height: '100%' }}>
                    <Molecule smiles={data?.value} />
                </div>
            </div>
            <Handle
                type="source"
                position={sourcePosition}
                isConnectable={isConnectable}
            />
        </div>
    );
};

MoleculeNode.displayName = "MoleculeNode";

export default memo(MoleculeNode);
