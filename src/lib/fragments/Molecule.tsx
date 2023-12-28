import type {RDKitModule} from '@rdkit/rdkit';
import React, {useEffect, useState} from 'react';
import './molecule.css';

declare global {
    // eslint-disable-next-line no-unused-vars
    interface Window {
        RDKit: RDKitModule;
    }
}

interface MoleculeProps {
    smiles: string;
}

function Molecule(props: MoleculeProps) {

    return (
        <div>
            <span
                dangerouslySetInnerHTML={{
                    __html: window.RDKit.get_mol(props.smiles).get_svg(100, 80)
                        .replace('<rect style=\'opacity:1.0', '<rect style=\'opacity: 0')
                        .replace('fill:#FFFFFF;', '')
                        .replace(/stroke-width:2\.0px;/g, 'stroke-width:0.5px;'),
                }}
            />
        </div>
    );
}

export default Molecule;