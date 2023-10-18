import dash_chemical_flow
from dash import Dash, callback, html, Input, Output

app = Dash(__name__)

DRY_RUN_DATA = {
    "nodes": [
        {
            "id": "1",
            "data": {
                "value": "CC(C)(C)[Si](C)(C)Cl",
                "label": "CC(C)(C)[Si](C)(C)Cl",
                "commercial": True,
            },
            "type": "molecule",
        },
        {
            "id": "2",
            "data": {
                "value": "O=C1O[C@H](CO)[C@@H](O)[C@H]1O",
                "label": "O=C1O[C@H](CO)[C@@H](O)[C@H]1O",
                "commercial": True,
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
                "commercial": False,
            },
            "type": "molecule",
        },
        {
            "id": "5",
            "data": {
                "value": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "label": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "commercial": False,
            },
            "type": "molecule",
        },
        {
            "id": "6",
            "data": {
                "value": "CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "label": "CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "commercial": False,
            },
            "type": "molecule",
        },
        {
            "id": "7",
            "data": {"value": "CCC(CC)CO", "label": "CCC(CC)CO", "commercial": True},
            "type": "molecule",
        },
        {
            "id": "8",
            "data": {
                "value": "C[C@H](N)C(=O)O",
                "label": "C[C@H](N)C(=O)O",
                "commercial": True,
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
                "commercial": False,
            },
            "type": "molecule",
        },
        {
            "id": "11",
            "data": {
                "value": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1",
                "label": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1",
                "commercial": False,
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
                "commercial": False,
            },
            "type": "molecule",
        },
        {
            "id": "14",
            "data": {
                "value": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "label": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "commercial": False,
            },
            "type": "molecule",
        },
    ],
    "edges": [
        {"id": "1-3", "source": "1", "target": "3", "type": "step", "animated": True},
        {"id": "2-3", "source": "2", "target": "3", "type": "step", "animated": True},
        {
            "id": "3-4",
            "source": "3",
            "label": "transformer_network",
            "data": {"catalyst": "CCO"},
            "target": "4",
            "type": "molecule",
            "animated": True,
        },
        {
            "id": "4-5",
            "source": "4",
            "label": "database",
            "data": {"catalyst": "Nc1ncnn2c(I)ccc12"},
            "target": "5",
            "type": "molecule",
            "animated": True,
        },
        {
            "id": "5-6",
            "source": "5",
            "label": "database",
            "data": {"catalyst": "C[Si](C)(C)C#N.O=C(O)C(F)(F)F"},
            "target": "6",
            "type": "molecule",
            "animated": True,
        },
        {"id": "7-9", "source": "7", "target": "9", "type": "step", "animated": True},
        {"id": "8-9", "source": "8", "target": "9", "type": "step", "animated": True},
        {
            "id": "9-10",
            "source": "9",
            "label": "database",
            "data": {"catalyst": "CCO"},
            "target": "10",
            "type": "molecule",
            "animated": True,
        },
        {
            "id": "10-11",
            "source": "10",
            "label": "transformer_network",
            "data": {"catalyst": "O=P(Cl)(Cl)c1ccccc1.Oc1c(F)c(F)c(F)c(F)c1F"},
            "target": "11",
            "type": "molecule",
            "animated": True,
        },
        {"id": "6-12", "source": "6", "target": "12", "type": "step", "animated": True},
        {
            "id": "11-12",
            "source": "11",
            "target": "12",
            "type": "step",
            "animated": True,
        },
        {
            "id": "12-13",
            "source": "12",
            "label": "transformer_network",
            "data": {"catalyst": "CCO"},
            "target": "13",
            "type": "molecule",
            "animated": True,
        },
        {
            "id": "13-14",
            "source": "13",
            "label": "expert_system",
            "data": {"catalyst": "CCO"},
            "target": "14",
            "type": "molecule",
            "animated": True,
        },
    ],
    "backup_reactions": {
        "CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C": [
            {
                "smiles": "CC(C)(C)[Si](C)(C)Cl.CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O)[C@@H]1O[Si](C)(C)C(C)(C)C>>CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "reaction_type": "transformer_network",
                "confidence_score": -0.07182464748620987,
                "probability": -0.06447131931781769,
            },
            {
                "smiles": "CC(C)(C)[Si](C)(C)Cl.O=C1O[C@H](CO)[C@@H](O)[C@H]1O>>CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "reaction_type": "transformer_network",
                "confidence_score": -0.07855594903230667,
                "probability": -0.08524945378303528,
            },
        ],
        "CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C": [
            {
                "smiles": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C.Nc1ncnn2c(I)ccc12>Cl[Mg]c1ccccc1.C[Si](C)(C)Cl.CC(C)[Mg]Cl.C1CCOC1.Cl[La](Cl)Cl>CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "reaction_type": "database",
                "confidence_score": 1.0,
                "probability": 1.0,
            },
            {
                "smiles": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C.Nc1ncnn2c(Br)ccc12>C[Si](C)(C)Cl.[Li]CCCC.C1CCOC1>CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "reaction_type": "similarity",
                "confidence_score": 0.6923076808452606,
                "probability": -0.05715880170464516,
            },
            {
                "smiles": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@H]1O[Si](C)(C)C(C)(C)C.Nc1ncnn2c(I)ccc12>>CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "reaction_type": "transformer_network",
                "confidence_score": -0.0757591724395752,
                "probability": -0.05034976080060005,
            },
        ],
        "CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C": [
            {
                "smiles": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C.C[Si](C)(C)C#N.O=C(O)C(F)(F)F>C[Si](C)(C)OS(=O)(=O)C(F)(F)F.CCN(CC)CC.ClCCl.O>CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "reaction_type": "database",
                "confidence_score": 1.0,
                "probability": 1.0,
            },
            {
                "smiles": "CC(C)(C)[Si](C)(C)OC[C@H]1OC(O)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C>C[Si](C)(C)OS(=O)(=O)C(F)(F)F.O=C(O)C(F)(F)F.C[Si](C)(C)C#N.ClCCl>CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "reaction_type": "database",
                "confidence_score": 1.0,
                "probability": 1.0,
            },
            {
                "smiles": "CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO[Si](C)(C)C)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C>>CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "reaction_type": "transformer_network",
                "confidence_score": -0.056912995874881744,
                "probability": -0.08038846403360367,
            },
        ],
        "CCC(CC)COC(=O)[C@H](C)N": [
            {
                "smiles": "CCC(CC)CO.C[C@H](N)C(=O)O>CCCC(C)C.Cc1ccccc1.Cc1ccc(S(=O)(=O)O)cc1>CCC(CC)COC(=O)[C@H](C)N",
                "reaction_type": "database",
                "confidence_score": 1.0,
                "probability": 1.0,
            },
            {
                "smiles": "CCOC(=O)[C@H](C)N.Cl.O=P(Cl)(Cl)Oc1ccccc1>ClCCl>CCC(CC)COC(=O)[C@H](C)N",
                "reaction_type": "database",
                "confidence_score": 1.0,
                "probability": 1.0,
            },
            {
                "smiles": "CCC(CC)CO.C[C@H](NC(=O)OC(C)(C)C)C(=O)O>C[Si](C)(C)Cl>CCC(CC)COC(=O)[C@H](C)N",
                "reaction_type": "database",
                "confidence_score": 1.0,
                "probability": 1.0,
            },
        ],
        "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1": [
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N.O=P(Cl)(Cl)c1ccccc1.Oc1c(F)c(F)c(F)c(F)c1F>>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1",
                "reaction_type": "transformer_network",
                "confidence_score": -0.04458966106176376,
                "probability": -0.09628116339445114,
            }
        ],
        "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1": [
            {
                "smiles": "CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C.CCC(CC)COC(=O)[C@H](C)N[P@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1>>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1",
                "reaction_type": "transformer_network",
                "confidence_score": -0.028011322021484375,
                "probability": -0.056453727185726166,
            },
            {
                "smiles": "CC(C)(C)[Si](C)(C)O[C@@H]1[C@H](O[Si](C)(C)C(C)(C)C)[C@](C#N)(c2ccc3c(N)ncnn23)O[C@@H]1CO.CCC(CC)COC(=O)[C@H](C)N[P@@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1>>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1",
                "reaction_type": "transformer_network",
                "confidence_score": -0.04624204337596893,
                "probability": -0.05625361204147339,
            },
        ],
        "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1": [
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@H]1O[C@H](C)CC(=O)O)c1ccccc1>C1CCOC1.CC(C)(C)[O-].[K+]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H](O[C@H](C)CC(=O)O)[C@H]1O[C@H](C)CC(=O)O)c1ccccc1>C1CCOC1.CC(C)(C)[O-].[K+]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H](O[C@H](C)CC(=O)O)[C@@H]1O)c1ccccc1>C1CCOC1.CC(C)(C)[O-].[K+]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O[Si](c1ccccc1)(c1ccccc1)C(C)(C)C)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](c2ccccc2)(c2ccccc2)C(C)(C)C)[C@@H]1O[Si](c1ccccc1)(c1ccccc1)C(C)(C)C)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](c2ccccc2)(c2ccccc2)C(C)(C)C)[C@@H]1O)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NC(C)=O)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>O.CCO.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N4C(=O)c5ccccc5C4=O)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>NN.O.CCO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NS(=O)(=O)c4ccc(C)cc4)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>[MgH2].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "C=CCOC(=O)Nc1ncnn2c([C@]3(C#N)O[C@H](CO[P@@](=O)(N[C@@H](C)C(=O)OCC(CC)CC)c4ccccc4)[C@@H](O)[C@H]3O)ccc12>C1CCNC1.O.C1COCCO1.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N(C(=O)OC(C)(C)C)C(=O)OC(C)(C)C)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>CCOC(=O)C.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]2OC(C)(C)O[C@H]12)c1ccccc1>O.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NC=O)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>O.Cc1ccccc1.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NCc4ccccc4)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>[H][H].[Pd].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N(Cc4ccccc4)Cc4ccccc4)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>[H][H].[Pd].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "C=CCN(CC=C)c1ncnn2c([C@]3(C#N)O[C@H](CO[P@@](=O)(N[C@@H](C)C(=O)OCC(CC)CC)c4ccccc4)[C@@H](O)[C@H]3O)ccc12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.CN1C(=O)CC(=O)N(C)C1=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NC(=O)OCC[Si](C)(C)C)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC.C1CCOC1>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1OC=O)c1ccccc1>[BH4-].[Na+].C1CCOC1>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC=O)[C@@H]1OC=O)c1ccccc1>[BH4-].[Na+].C1CCOC1>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC=O)[C@@H]1O)c1ccccc1>[BH4-].[Na+].C1CCOC1>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1OC(=O)c1ccc(C)cc1)c1ccccc1>[NH2-].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC(=O)c2ccc(C)cc2)[C@@H]1OC(=O)c1ccc(C)cc1)c1ccccc1>[NH2-].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC(=O)c2ccc(C)cc2)[C@@H]1O)c1ccccc1>[NH2-].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1OC1CCCCO1)c1ccccc1>O.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC2CCCCO2)[C@@H]1OC1CCCCO1)c1ccccc1>O.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC2CCCCO2)[C@@H]1O)c1ccccc1>O.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1OC(=O)c1ccccc1)c1ccccc1>O.C[O-].[Na+].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC(=O)c2ccccc2)[C@@H]1OC(=O)c1ccccc1)c1ccccc1>O.C[O-].[Na+].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC(=O)c2ccccc2)[C@@H]1O)c1ccccc1>O.C[O-].[Na+].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@@H]1C=C[C@](C#N)(c2ccc3c(N)ncnn23)O1)c1ccccc1>N=O.O=[Os](=O)(=O)=O.O.CC(C)=O>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(-n4c(C)ccc4C)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>CCO.Cl.NO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N=C(c4ccccc4)c4ccccc4)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>O.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1OC)c1ccccc1>B(Br)(Br)Br.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC)[C@@H]1OC)c1ccccc1>B(Br)(Br)Br.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC)[C@@H]1O)c1ccccc1>B(Br)(Br)Br.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]2OC(c3ccccc3)O[C@H]12)c1ccccc1>[H][H].[Pd]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NC(=O)OC(C)(C)C)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>CCOC(=O)C.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]2O[Si](C(C)(C)C)(C(C)(C)C)O[C@H]12)c1ccccc1>C1CCOC1>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert_system",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
        ],
    },
}

app.layout = html.Div(
    [
        dash_chemical_flow.ChemicalFlow(
            id="input",
            label="my-label",
            nodes=DRY_RUN_DATA["nodes"],
            edges=DRY_RUN_DATA["edges"],
        ),
        html.Div(id="output"),
    ]
)


@callback(Output("output", "children"), Input("input", "selectionEvent"))
def display_output(value):
    return "You have entered {}".format(value)


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
