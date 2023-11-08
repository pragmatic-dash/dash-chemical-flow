import type { RDKitModule } from "@rdkit/rdkit";
import React, {useEffect, useState} from "react";
import "./molecule.css"

declare global {
    // eslint-disable-next-line no-unused-vars
    interface Window {
        RDKit: RDKitModule;
    }
}
interface  MoleculeProps {
    smiles: string;
}
function Molecule(props: MoleculeProps) {
    const [rdkitLoaded, setRdkitLoaded] = useState(false);

    useEffect(() => {
        window.initRDKitModule().then((rdkit) => {
            window.RDKit = rdkit;
            setRdkitLoaded(true);
        });
    }, []);

    return (
        <div>
            {rdkitLoaded ? (
                    <span
                        dangerouslySetInnerHTML={{
                    __html: window.RDKit.get_mol(props.smiles).get_svg(80, 60).
                    replace("<rect style='opacity:1.0", "<rect style='opacity: 0").
                    replace("fill:#FFFFFF;", ""),
                }}
    />
) : (
                <span className="loading-span">Loading...</span>
    )}
        </div>
);
}

export default Molecule