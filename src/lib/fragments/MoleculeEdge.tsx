import React from 'react';
import { BaseEdge, EdgeLabelRenderer, EdgeProps, getBezierPath } from 'reactflow';
import Molecule from "./Molecule";

export default function CustomEdge({
  // eslint-disable-next-line no-unused-vars
  id,
  data,
  label,
  sourceX,
  sourceY,
  targetX,
  targetY,
  sourcePosition,
  targetPosition,
  style = {},
  markerEnd,
}: EdgeProps) {
  const [edgePath, labelX, labelY] = getBezierPath({
    sourceX,
    sourceY,
    sourcePosition,
    targetX,
    targetY,
    targetPosition,
  });

  return (
    <>
      <BaseEdge path={edgePath} markerEnd={markerEnd} style={style} />
        {/* eslint-disable-next-line no-undefined */}
      <EdgeLabelRenderer children={undefined}>
        <div
          style={{
            position: 'absolute',
            transform: `translate(-50%, -50%) translate(${labelX}px,${labelY - 50}px) `,
            fontSize: 12,
            // everything inside EdgeLabelRenderer has no pointer events by default
            // if you have an interactive element, set pointer-events: all
            pointerEvents: 'all',
          }}
          className="nodrag nopan">
            <div style={{ width: '100%', height: '100%' }}>
              <Molecule smiles={data?.catalyst} />
            </div>
        </div>
        <div style={{
            position: 'absolute',
            transform: `translate(-50%, -50%) translate(${labelX}px,${labelY}px) `,
            fontSize: 12,
            // everything inside EdgeLabelRenderer has no pointer events by default
            // if you have an interactive element, set pointer-events: all
            pointerEvents: 'all',
          }}
          className="nodrag nopan">
          <label>{label}</label>
        </div>
      </EdgeLabelRenderer>
    </>
  );
}
