/* eslint no-magic-numbers: 0 */
import React, { useState } from 'react';

import { ChemicalFlow } from '../lib';

const App = () => {
    const nodes = [
        {
            "id": "1",
            "data": {
                "value": "CC(C)(C)[Si](C)(C)Cl",
                "label": "CC(C)(C)[Si](C)(C)Cl",
                "commercial": true,
            },
            "type": "molecule",
        },
        {
            "id": "2",
            "data": {
                "value": "O=C1O[C@H](CO)[C@@H](O)[C@H]1O",
                "label": "O=C1O[C@H](CO)[C@@H](O)[C@H]1O",
                "commercial": true,
            },
            "type": "molecule",
        },
        {
            "id": "3",
            "data": {"value": "+", "label": "+"},
            "type": "reaction",
            "label": "+",
        },
        {
            "id": "4",
            "data": {
                "value": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "label": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "commercial": false,
            },
            "type": "molecule",
        },
        {
            "id": "5",
            "data": {
                "value": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "label": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "commercial": false,
            },
            "type": "molecule",
        },
        {
            "id": "6",
            "data": {
                "value": "CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "label": "CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "commercial": false,
            },
            "type": "molecule",
        },
        {
            "id": "7",
            "data": {"value": "CCC(CC)CO", "label": "CCC(CC)CO", "commercial": true},
            "type": "molecule",
        },
        {
            "id": "8",
            "data": {
                "value": "C[C@H](N)C(=O)O",
                "label": "C[C@H](N)C(=O)O",
                "commercial": true,
            },
            "type": "molecule",
        },
        {
            "id": "9",
            "data": {"value": "+", "label": "+"},
            "type": "reaction",
            "label": "+",
        },
        {
            "id": "10",
            "data": {
                "value": "CCC(CC)COC(=O)[C@H](C)N",
                "label": "CCC(CC)COC(=O)[C@H](C)N",
                "commercial": false,
            },
            "type": "molecule",
        },
        {
            "id": "11",
            "data": {
                "value": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1",
                "label": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1",
                "commercial": false,
            },
            "type": "molecule",
        },
        {
            "id": "12",
            "data": {"value": "+", "label": "+"},
            "type": "reaction",
            "label": "+",
        },
        {
            "id": "13",
            "data": {
                "value": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1",
                "label": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1",
                "commercial": false,
            },
            "type": "molecule",
        },
        {
            "id": "14",
            "data": {
                "value": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "label": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "commercial": false,
            },
            "type": "molecule",
        },
    ]
    
    const edges= [
        {"id": "1-3", "source": "1", "target": "3", "type": "step", "animated": true},
        {"id": "2-3", "source": "2", "target": "3", "type": "step", "animated": true},
        {
            "id": "3-4",
            "source": "3",
            "label": "transformer",
            "data": {"catalyst": "CCO"},
            "target": "4",
            "type": "molecule",
            "animated": true,
        },
        {
            "id": "4-5",
            "source": "4",
            "label": "database",
            "data": {"catalyst": "Nc1ncnn2c(I)ccc12"},
            "target": "5",
            "type": "molecule",
            "animated": true,
        },
        {
            "id": "5-6",
            "source": "5",
            "label": "database",
            "data": {"catalyst": "C[Si](C)(C)C#N.O=C(O)C(F)(F)F"},
            "target": "6",
            "type": "molecule",
            "animated": true,
        },
        {"id": "7-9", "source": "7", "target": "9", "type": "step", "animated": true},
        {"id": "8-9", "source": "8", "target": "9", "type": "step", "animated": true},
        {
            "id": "9-10",
            "source": "9",
            "label": "database",
            "data": {"catalyst": "CCO"},
            "target": "10",
            "type": "molecule",
            "animated": true,
        },
        {
            "id": "10-11",
            "source": "10",
            "label": "transformer",
            "data": {"catalyst": "O=P(Cl)(Cl)c1ccccc1.Oc1c(F)c(F)c(F)c(F)c1F"},
            "target": "11",
            "type": "molecule",
            "animated": true,
        },
        {"id": "6-12", "source": "6", "target": "12", "type": "step", "animated": true},
        {
            "id": "11-12",
            "source": "11",
            "target": "12",
            "type": "step",
            "animated": true,
        },
        {
            "id": "12-13",
            "source": "12",
            "label": "transformer",
            "data": {"catalyst": "CCO"},
            "target": "13",
            "type": "molecule",
            "animated": true,
        },
        {
            "id": "13-14",
            "source": "13",
            "label": "expert",
            "data": {"catalyst": "CCO"},
            "target": "14",
            "type": "molecule",
            "animated": true,
        },
    ]
    
    const [state, setState] = useState({value:'', label:'Type Here'});
    const setProps = (newProps) => {
            setState(newProps);
        };

    return (
        <div>
            <ChemicalFlow
                setProps={setProps}
                {...state}
                nodes={nodes}
                edges={edges}
            />
        </div>
    )
};


export default App;
