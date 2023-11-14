import dash_chemical_flow
from dash import Dash, callback, html, Input, Output

app = Dash(__name__)
# workflow = {
#     "nodes": [
#         {
#             "id": "a1",
#             "data": {
#                 "value": "COc1ccc(I)c(C(=O)O)c1",
#                 "label": "COc1ccc(I)c(C(=O)O)c1",
#                 "commercial": True,
#                 "price": "19.89¥/g"
#             },
#             "type": "molecule"
#         },
#         {
#             "id": "a2",
#             "data": {
#                 "value": "c1c[nH]nn1",
#                 "label": "c1c[nH]nn1",
#                 "commercial": True,
#                 "price": "1.494¥/g"
#             },
#             "type": "molecule"
#         },
#         {
#             "id": "a3",
#             "data": {
#                 "value": "+",
#                 "label": "+"
#             },
#             "type": "reaction",
#             "label": "+"
#         },
#         {
#             "id": "a4",
#             "data": {
#                 "value": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
#                 "label": "COc1ccc(-n2nccn2)c(C(=O)O)c1",
#                 "commercial": False
#             },
#             "type": "molecule"
#         },
#         {
#             "id": "a5",
#             "data": {
#                 "value": "C[C@@]1(C(=O)O)CCCN1",
#                 "label": "C[C@@]1(C(=O)O)CCCN1",
#                 "commercial": True,
#                 "price": "99.2¥/g"
#             },
#             "type": "molecule"
#         },
#         {
#             "id": "a6",
#             "data": {
#                 "value": "+",
#                 "label": "+"
#             },
#             "type": "reaction",
#             "label": "+"
#         },
#         {
#             "id": "a7",
#             "data": {
#                 "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
#                 "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
#                 "commercial": False
#             },
#             "type": "molecule"
#         },
#         {
#             "id": "a8",
#             "data": {
#                 "value": "Cc1c(Cl)ccc(N)c1N",
#                 "label": "Cc1c(Cl)ccc(N)c1N",
#                 "commercial": True,
#                 "price": "281.0¥/g"
#             },
#             "type": "molecule"
#         },
#         {
#             "id": "a9",
#             "data": {
#                 "value": "+",
#                 "label": "+"
#             },
#             "type": "reaction",
#             "label": "+"
#         },
#         {
#             "id": "a10",
#             "data": {
#                 "value": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "label": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "commercial": False
#             },
#             "type": "molecule"
#         }
#     ],
#     "edges": [
#         {
#             "id": "1-3",
#             "source": "a1",
#             "target": "a3",
#             "type": "step",
#             "animated": True
#         },
#         {
#             "id": "2-3",
#             "source": "a2",
#             "target": "a3",
#             "type": "step",
#             "animated": True
#         },
#         {
#             "id": "3-4",
#             "source": "a3",
#             "label": "database",
#             "data": {
#                 "catalyst": ""
#             },
#             "target": "a4",
#             "type": "molecule",
#             "animated": True,
#             "markerEnd": {
#                 "type": "arrowclosed",
#                 "color": "#000",
#                 "width": 20,
#                 "height": 20
#             }
#         },
#         {
#             "id": "4-6",
#             "source": "a4",
#             "target": "a6",
#             "type": "step",
#             "animated": True
#         },
#         {
#             "id": "5-6",
#             "source": "a5",
#             "target": "a6",
#             "type": "step",
#             "animated": True
#         },
#         {
#             "id": "6-7",
#             "source": "a6",
#             "label": "similarity",
#             "data": {
#                 "catalyst": ""
#             },
#             "target": "a7",
#             "type": "molecule",
#             "animated": True,
#             "markerEnd": {
#                 "type": "arrowclosed",
#                 "color": "#000",
#                 "width": 20,
#                 "height": 20
#             }
#         },
#         {
#             "id": "7-9",
#             "source": "a7",
#             "target": "a9",
#             "type": "step",
#             "animated": True
#         },
#         {
#             "id": "8-9",
#             "source": "a8",
#             "target": "a9",
#             "type": "step",
#             "animated": True
#         },
#         {
#             "id": "9-10",
#             "source": "a9",
#             "label": "expert",
#             "data": {
#                 "catalyst": ""
#             },
#             "target": "a10",
#             "type": "molecule",
#             "animated": True,
#             "markerEnd": {
#                 "type": "arrowclosed",
#                 "color": "#000",
#                 "width": 20,
#                 "height": 20
#             }
#         }
#     ],
#     "backup_reactions": {
#         "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1": [
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC=C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CC#C[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H][H].[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "CB(O)O.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "CB1OC(C)(C)C(C)(C)O1.COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(Br)c3[nH]2)c1>O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].Cc1ccccc1.CO.[Na+].[Na+].[O-]C([O-])=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(N)c(C)c3[nH]2)c1>CC#N.Cl[Cu]Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2ncc(N)n2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1cc(N)c(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1cc(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c(-n2nccn2)cc1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1N>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3c(N)cc(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3cc(N)c(Cl)c(C)c3[nH]2)c1>O.Cl.N(=O)[O-].[Na+].CCO.O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COS(=O)(=O)OC.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>CC(C)=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.[Cl-].CCN(CCC[NH+](C)C)C#N.CN(C)C=O>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2Cc2ccccc2)c1>[H][H].[Pd].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "C=C(c1cc(OC)ccc1-n1nccn1)N1CCC[C@@]1(C)c1nc2ccc(Cl)c(C)c2[nH]1>[O-][O+]=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(O)ccc3-n3nccn3)[nH]c12>COS(=O)(=O)OC.CN(C)C=O.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(c2ccccc2)(c2ccccc2)c2ccccc2)c1>C1COCCO1.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(Cn2c([C@]3(C)CCCN3C(=O)c3cc(OC)ccc3-n3nccn3)nc3ccc(Cl)c(C)c32)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(Br)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd].C[S](C)=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2c(N)ccc(Cl)c2C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C2CCCCO2)c1>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CO)c3[nH]2)c1>Cl.[H][H].CCO.[Pd]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(=O)OC(C)(C)C)c1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OC(=O)C(F)(F)F>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.OCCN(CCO)CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.Cc1c(Cl)ccc(N)c1N>CN(C)C(=[O+]n1nnc2cccnc12)N(C)C.F[P-](F)(F)(F)(F)F.CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "CCC(C)(C)OC(=O)n1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>[Na+].OC([O-])=O.CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(NN)c(C)c3[nH]2)c1>CC#N.C1(=O)N(C(=O)N(C(=O)N1Cl)Cl)Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)CC[Si](C)(C)C)c1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(C)(=O)=O)c1>[OH-].[Na+].CO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)C(F)(F)F)c1>CO.C(=O)([O-])[O-].[K+].[K+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2S(=O)(=O)c2ccccc2)c1>O.CO.[OH-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(I)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>Cc1ccccc1.C(=O)([O-])[O-].[K+].[K+].[Pd](OC(C)=O)OC(C)=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3n2C(C)(C)C)c1>COO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Cl)c1.Cc1c(Cl)ccc(N)c1N>OCCN(CCO)CCO.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2Br)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(N)=Nc2ccc(Cl)c(C)c2I)c1>CNCCNC.C(=O)([O-])[O-].[K+].[K+].C1COCCO1.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "CO[Na].Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(I)ccc3-n3nccn3)[nH]c12>CN(C)C=O.CO.[Cu]I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COCn1c([C@]2(C)CCCN2C(=O)c2cc(OC)ccc2-n2nccn2)nc2ccc(Cl)c(C)c21>O.Cl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc(N)c1[N+](=O)[O-]>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)[B-](F)(F)F)c1.[K+].Cc1c(Cl)ccc2nc(Cl)[nH]c12>O.[Na+].[Na+].[O-]C([O-])=O.C1COCCO1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCBr)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCI)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(C)(=O)=O)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)c2ccc(C)cc2)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N[C@@](C)(CCCOS(=O)(=O)C(F)(F)F)c2nc3ccc(Cl)c(C)c3[nH]2)c1>[H-].[Na+].C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)Oc2c(Cl)cc(Cl)cc2Cl)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>OCCN(CCO)CCO.C1CCOC1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(N)ccc3-n3nccn3)[nH]c12>Cl.CO.N(=O)[O-].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(B(O)O)c(C)c3[nH]2)c1>[Cl-].[Cu+].CC#N>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)ON2C(=O)CCC2=O)c1.Cc1c(Cl)ccc2nc([C@]3(C)CCCN3)[nH]c12>CN(C)C=O.CCN(C(C)C)C(C)C>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C=O)c1.Cc1c(Cl)ccc([N+](=O)[O-])c1N>CCO.[O-]S(=O)S(=O)[O-].[Na+].[Na+]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(CCl)c3[nH]2)c1>[Zn].CCO>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "expert",
#                 "confidence_score": 0.8,
#                 "probability": 0.8
#             },
#             {
#                 "smiles": "Cc1c(Cl)ccc2nc([C@]3(C)CCCN3C(=O)c3cc(F)ccc3-n3nccn3)[nH]c12>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "similarity",
#                 "confidence_score": 0.42424243688583374,
#                 "probability": -0.12521551549434662
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)Nc2ccc(Cl)c(C)c2N)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "transformer",
#                 "confidence_score": -0.04267781600356102,
#                 "probability": -0.07558560371398926
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.Cc1c(Cl)ccc2nc([C@@]3(C)CCCN3)[nH]c12>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "transformer",
#                 "confidence_score": -0.060306668281555176,
#                 "probability": -0.06755616515874863
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)c2nc3ccc(Cl)c(C)c3n2COCC[Si](C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)c2nc3ccc(Cl)c(C)c3[nH]2)c1",
#                 "reaction_type": "unimol",
#                 "confidence_score": -6.134176731109619,
#                 "probability": -0.12802264094352722
#             }
#         ],
#         "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1": [
#             {
#                 "smiles": "COC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>CO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
#                 "reaction_type": "database",
#                 "confidence_score": 1,
#                 "probability": 1
#             },
#             {
#                 "smiles": "C[C@@]1(C(=O)O)CCCN1C(=O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
#                 "reaction_type": "similarity",
#                 "confidence_score": 0.5800000131130219,
#                 "probability": -0.1068539023399353
#             },
#             {
#                 "smiles": "COc1ccc(I)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1.c1c[nH]nn1>O=C(O)c1cccc(-n2ccc(C(F)(F)F)n2)c1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
#                 "reaction_type": "similarity",
#                 "confidence_score": 0.5800000131130219,
#                 "probability": -0.09788434952497482
#             },
#             {
#                 "smiles": "CCOC(=O)[C@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>O.CCO.O[Na]>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
#                 "reaction_type": "similarity",
#                 "confidence_score": 0.4363636374473572,
#                 "probability": -0.09341540932655334
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@@]1(C(=O)O)CCCN1>Cc1cc(C)nc(N2C[C@@H]3CCNC[C@@H]32)n1.O=C(O)c1ccccc1-c1cccs1>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
#                 "reaction_type": "similarity",
#                 "confidence_score": 0.43421053886413574,
#                 "probability": 0
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)Cl)c1.C[C@@]1(C(=O)O)CCCN1>CCN(CC)CC.ClCCl>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
#                 "reaction_type": "similarity",
#                 "confidence_score": 0.4285714030265808,
#                 "probability": -0.20377855002880096
#             },
#             {
#                 "smiles": "COC(=O)[C@@]1(C)CCCN1C(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
#                 "reaction_type": "transformer",
#                 "confidence_score": -0.07035081088542938,
#                 "probability": -0.09458772093057632
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)[O-])c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
#                 "reaction_type": "transformer",
#                 "confidence_score": -0.1351894736289978,
#                 "probability": -0.11803625524044037
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)O)c1.C[C@]1(C(=O)O)CCCN1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
#                 "reaction_type": "transformer",
#                 "confidence_score": -0.14947395026683807,
#                 "probability": -0.09298502653837204
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)OCc2ccccc2)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
#                 "reaction_type": "transformer",
#                 "confidence_score": -0.15171797573566437,
#                 "probability": -0.08790042251348495
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)N2CCCC2(C)C(=O)OC(C)(C)C)c1>>COc1ccc(-n2nccn2)c(C(=O)N2CCC[C@@]2(C)C(=O)O)c1",
#                 "reaction_type": "unimol",
#                 "confidence_score": -3.8154542446136475,
#                 "probability": -0.16713565587997437
#             }
#         ],
#         "COc1ccc(-n2nccn2)c(C(=O)O)c1": [
#             {
#                 "smiles": "O=C(O)c1cc(F)ccc1-n1nccn1>COc1ccc(I)c(C(=O)O)c1.O=C(O)c1cc(F)ccc1I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
#                 "reaction_type": "database",
#                 "confidence_score": 1,
#                 "probability": 1
#             },
#             {
#                 "smiles": "COc1ccc(I)c(C(=O)O)c1.c1c[nH]nn1>CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
#                 "reaction_type": "database",
#                 "confidence_score": 1,
#                 "probability": 1
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[K])c1>O.COC(C)(C)C>COc1ccc(-n2nccn2)c(C(=O)O)c1",
#                 "reaction_type": "database",
#                 "confidence_score": 1,
#                 "probability": 1
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(I)c1>CC(C)[Mg]Cl>COc1ccc(-n2nccn2)c(C(=O)O)c1",
#                 "reaction_type": "database",
#                 "confidence_score": 1,
#                 "probability": 1
#             },
#             {
#                 "smiles": "COc1ccc(I)c(C(=O)O)c1.c1cn[nH]n1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
#                 "reaction_type": "database",
#                 "confidence_score": 1,
#                 "probability": 1
#             },
#             {
#                 "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1cn[nH]n1>CN[C@@H]1CCCC[C@H]1NC.CCOC(C)=O.O=C(O[Cs])O[Cs].C1COCCO1.O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
#                 "reaction_type": "similarity",
#                 "confidence_score": 0.7777777761220932,
#                 "probability": -0.11192844063043594
#             },
#             {
#                 "smiles": "COc1ccc(Br)c(C(=O)O)c1.c1c[nH]nn1>CO.CN[C@H]1CCCC[C@@H]1NC.CN(C)C=O.O=C(O[Cs])O[Cs].[Cu]I>COc1ccc(-n2nccn2)c(C(=O)O)c1",
#                 "reaction_type": "similarity",
#                 "confidence_score": 0.6486486494541168,
#                 "probability": -0.11164479702711105
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C#N)c1>Cl.O[Na]>COc1ccc(-n2nccn2)c(C(=O)O)c1",
#                 "reaction_type": "similarity",
#                 "confidence_score": 0.6486486494541168,
#                 "probability": -0.11898676306009293
#             },
#             {
#                 "smiles": "COc1ccc(-n2nccn2)c(C(=O)O[Na])c1>O>COc1ccc(-n2nccn2)c(C(=O)O)c1",
#                 "reaction_type": "similarity",
#                 "confidence_score": 0.6486486494541168,
#                 "probability": -0.13990871608257294
#             },
#             {
#                 "smiles": "COC(=O)c1cc(OC)ccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
#                 "reaction_type": "unimol",
#                 "confidence_score": -2.821465015411377,
#                 "probability": -0.12816283106803894
#             },
#             {
#                 "smiles": "COc1ccc(I)c(C(=O)O)c1.O=C(O)c1ccccc1-n1nccn1>>COc1ccc(-n2nccn2)c(C(=O)O)c1",
#                 "reaction_type": "unimol",
#                 "confidence_score": -4.799795627593994,
#                 "probability": -0.11633466929197311
#             }
#         ]
#     }
# }

workflow = {
            "nodes": [
                {
                    "id": "1",
                    "data": {
                        "value": "COc1ccc2ccc(=O)oc2c1CC=C(C)C",
                        "label": "COc1ccc2ccc(=O)oc2c1CC=C(C)C",
                        "commercial": True,
                        "price": "20.72\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "2",
                    "data": {
                        "value": "CC(C)=CCc1c(O)ccc2ccc(=O)oc12",
                        "label": "CC(C)=CCc1c(O)ccc2ccc(=O)oc12",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "3",
                    "data": {
                        "value": "O=C(OO)c1cccc(Cl)c1",
                        "label": "O=C(OO)c1cccc(Cl)c1",
                        "commercial": True,
                        "price": "0.55\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "4",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "5",
                    "data": {
                        "value": "CC1(C)OC1Cc1c(O)ccc2ccc(=O)oc12",
                        "label": "CC1(C)OC1Cc1c(O)ccc2ccc(=O)oc12",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "6",
                    "data": {
                        "value": "COCCl",
                        "label": "COCCl",
                        "commercial": True,
                        "price": "0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "7",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "8",
                    "data": {
                        "value": "COCOc1ccc2ccc(=O)oc2c1CC1OC1(C)C",
                        "label": "COCOc1ccc2ccc(=O)oc2c1CC1OC1(C)C",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "9",
                    "data": {
                        "value": "OCc1ccccc1",
                        "label": "OCc1ccccc1",
                        "commercial": True,
                        "price": "0.49841199999999997\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "10",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "11",
                    "data": {
                        "value": "COCOc1ccc2ccc(=O)oc2c1C[C@@H](O)C(C)(C)OCc1ccccc1",
                        "label": "COCOc1ccc2ccc(=O)oc2c1C[C@@H](O)C(C)(C)OCc1ccccc1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "12",
                    "data": {
                        "value": "CC(C)(OCc1ccccc1)[C@H](O)Cc1c(O)ccc2ccc(=O)oc12",
                        "label": "CC(C)(OCc1ccccc1)[C@H](O)Cc1c(O)ccc2ccc(=O)oc12",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "13",
                    "data": {
                        "value": "CC(C)(OCc1ccccc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "label": "CC(C)(OCc1ccccc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "14",
                    "data": {
                        "value": "CC(C)(O)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "label": "CC(C)(O)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "15",
                    "data": {
                        "value": "COc1ccc(/C=C/C(=O)Cl)cc1",
                        "label": "COc1ccc(/C=C/C(=O)Cl)cc1",
                        "commercial": True,
                        "price": "3916.0\u00a5/g"
                    },
                    "type": "molecule"
                },
                {
                    "id": "16",
                    "data": {
                        "value": "+",
                        "label": "+"
                    },
                    "type": "reaction",
                    "label": "+"
                },
                {
                    "id": "17",
                    "data": {
                        "value": "COc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1",
                        "label": "COc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1",
                        "commercial": False
                    },
                    "type": "molecule"
                },
                {
                    "id": "18",
                    "data": {
                        "value": "CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "label": "CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "commercial": False
                    },
                    "type": "molecule"
                }
            ],
            "edges": [
                {
                    "id": "1-2",
                    "source": "1",
                    "label": "unknown",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "2",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "2-4",
                    "source": "2",
                    "target": "4",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "3-4",
                    "source": "3",
                    "target": "4",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "4-5",
                    "source": "4",
                    "label": "unknown",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "5",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "5-7",
                    "source": "5",
                    "target": "7",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "6-7",
                    "source": "6",
                    "target": "7",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "7-8",
                    "source": "7",
                    "label": "unknown",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "8",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "8-10",
                    "source": "8",
                    "target": "10",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "9-10",
                    "source": "9",
                    "target": "10",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "10-11",
                    "source": "10",
                    "label": "unknown",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "11",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "11-12",
                    "source": "11",
                    "label": "unknown",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "12",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "12-13",
                    "source": "12",
                    "label": "unknown",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "13",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "13-14",
                    "source": "13",
                    "label": "unknown",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "14",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "14-16",
                    "source": "14",
                    "target": "16",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "15-16",
                    "source": "15",
                    "target": "16",
                    "type": "step",
                    "animated": True
                },
                {
                    "id": "16-17",
                    "source": "16",
                    "label": "unknown",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "17",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                },
                {
                    "id": "17-18",
                    "source": "17",
                    "label": "unknown",
                    "data": {
                        "catalyst": ""
                    },
                    "target": "18",
                    "type": "molecule",
                    "animated": True,
                    "markerEnd": {
                        "type": "arrowclosed",
                        "color": "#000",
                        "width": 20,
                        "height": 20
                    }
                }
            ],
            "backup_reactions": {
                "CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1": [
                    {
                        "smiles": "COc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1>B(Br)(Br)Br.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)(C)Oc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.CC#N.OC(=O)C(F)(F)F.C1CCOC1>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)Oc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1>B(Cl)(Cl)Cl.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)(OC(=O)/C=C/c1ccc(O[Si](C)(C)C(C)(C)C)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)(C)C(=O)Oc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1>O.CO.[OH-].[Na+].C1CCOC1>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)(C)OC(=O)Oc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1>OC(=O)C(F)(F)F.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)(OC(=O)/C=C/c1ccc(OC(=O)c2ccccc2)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1>O.[OH-].[Na+].CO>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)(OC(=O)/C=C/c1ccc(B(O)O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1>OO.O>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)(OC(=O)/C=C/c1ccc(O[Si](c2ccccc2)(c2ccccc2)C(C)(C)C)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1>O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC.C1CCOC1>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)(OC(=O)/C=C/c1ccc([O-])c([N+]#N)c1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1>C1CCOC1.[BH4-].[Na+]>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)(OC(=O)/C=C/c1ccc(O[Si](C)(C)C)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1>O.Cl.C1CCOC1>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC[Si](CC)(CC)Oc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1>O.Cl.C1CCOC1>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)[Si](Oc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1)(C(C)C)C(C)C>O.Cl.C1CCOC1>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)[Si](Oc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1)(c1ccccc1)c1ccccc1>O.Cl.C1CCOC1>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)(OC(=O)/C=C/c1ccc(O[Si](C)(c2ccccc2)c2ccccc2)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1>O.Cl.C1CCOC1>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)(OC(=O)C=P(c1ccccc1)(c1ccccc1)c1ccccc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1.O=Cc1ccc(O)cc1>C1CCOC1>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)(OC(=O)/C=C/c1ccc(B2OC(C)(C)C(C)(C)O2)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1>CCO.OO.O.[OH-].[Na+]>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "CC(C)(OC(=O)/C=C/c1ccc(OC2CCCCO2)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1>CO>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "COc1ccc(COc2ccc(/C=C/C(=O)OC(C)(C)[C@@H]3Cc4c(ccc5ccc(=O)oc45)O3)cc2)cc1>OC(=O)C(F)(F)F.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 1.0,
                        "probability": 1.0,
                        "confirmed": True,
                        "reaction_cost": 1.2
                    },
                    {
                        "smiles": "C=CC(=O)OC(C)(C)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1.Oc1ccc(Br)cc1>CC(=O)O[Pd]OC(C)=O.CN1CCCC1=O.O=C(O[K])O[K].ClCCl.O>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 0.45454543828964233,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(=O)Oc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1>Cl.CC(C)=O>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 0.37974685430526733,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(C)(OC(=O)Cc1ccccc1P(c1ccccc1)c1ccccc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1.O=Cc1ccc(O)cc1>O>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 0.375,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "C=CC(=O)OC(C)(C)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1.Oc1ccc(I)cc1>CC(=O)O[Pd]OC(C)=O.CCN(CC)CC.CC#N>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 0.3658536672592163,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(C)(OC(=O)CC(=O)O)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1.O=Cc1ccc(O)cc1>CN(C)c1ccncc1.C1CCNCC1.CN(C)C=O>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 0.3606557250022888,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "COCOc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1>>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": -0.07206928730010986,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(C)(OC(=O)/C=C/c1ccc(OCc2ccccc2)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1>>CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": -0.07227762043476105,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    }
                ],
                "COc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1": [
                    {
                        "smiles": "CC(C)(O)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1.COc1ccc(/C=C/C(=O)Cl)cc1>>COc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1",
                        "reaction_type": "unknown",
                        "confidence_score": -0.04675523564219475,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(C)(O)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1.COc1ccc(/C=C/C(=O)O)cc1>>COc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1",
                        "reaction_type": "unknown",
                        "confidence_score": -0.05064165219664574,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "C=CC(=O)OC(C)(C)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1.COc1ccc(I)cc1>CCCCCCC.CCOC(C)=O>COc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1",
                        "reaction_type": "unknown",
                        "confidence_score": 0.4736841917037964,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(C)(OC(=O)/C=C/c1ccc(O)cc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1.COS(=O)(=O)OC>CC(=O)N(C)C.O=C(O[K])O[K]>COc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1",
                        "reaction_type": "unknown",
                        "confidence_score": 0.4736841917037964,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "C=CC(=O)OC(C)(C)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1.COc1ccc(Br)cc1>O=C(/C=C/c1ccccc1)/C=C/c1ccccc1.O=C(/C=C/c1ccccc1)/C=C/c1ccccc1.Brc1cccc(C2OCCO2)c1.FC(F)(F)c1ccc(Br)cc1.Brc1cccc2ccccc12.COc1ccccc1Br.Cc1ccc(Br)cc1.CCN(CC)CC.Brc1ccccc1.CN(C)C=O.[Li]Cl.[Pd].[Pd]>COc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1",
                        "reaction_type": "unknown",
                        "confidence_score": 0.4035087823867798,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(C)(OC(=O)C=P(c1ccccc1)(c1ccccc1)c1ccccc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1.COc1ccc(C=O)cc1>C1CCOC1>COc1ccc(/C=C/C(=O)OC(C)(C)[C@@H]2Cc3c(ccc4ccc(=O)oc34)O2)cc1",
                        "reaction_type": "unknown",
                        "confidence_score": 0.4035087823867798,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    }
                ],
                "CC(C)(O)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1": [
                    {
                        "smiles": "COC(=O)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1.C[Mg]Br>CCOC(C)=O.C1CCOC1>CC(C)(O)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 0.3617021441459656,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(C)(OCc1ccccc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1>C1COCCO1.CC(=O)O.CC(=O)O.O[Pd]O.Cl>CC(C)(O)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 0.32758623361587524,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(C)(O)[C@H]1Cc2c(ccc3ccc(=O)oc23)O1>>CC(C)(O)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": -0.11902449280023575,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    }
                ],
                "CC(C)(OCc1ccccc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1": [
                    {
                        "smiles": "BrCc1ccccc1.CC(C)(O)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1>CCCC[N+](CCCC)(CCCC)CCCC.C1CCOC1.[I-].[NaH]>CC(C)(OCc1ccccc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": 0.42105263471603394,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(C)(OCc1ccccc1)[C@H](O)Cc1c(O)ccc2ccc(=O)oc12>>CC(C)(OCc1ccccc1)[C@@H]1Cc2c(ccc3ccc(=O)oc23)O1",
                        "reaction_type": "unknown",
                        "confidence_score": -0.10563260316848755,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    }
                ],
                "CC(C)(OCc1ccccc1)[C@H](O)Cc1c(O)ccc2ccc(=O)oc12": [
                    {
                        "smiles": "CC(C)(OCc1ccccc1)[C@H](O)Cc1c(OCc2ccccc2)ccc2ccc(=O)oc12>>CC(C)(OCc1ccccc1)[C@H](O)Cc1c(O)ccc2ccc(=O)oc12",
                        "reaction_type": "unknown",
                        "confidence_score": -0.06149297580122948,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(C)(C)C(=O)Oc1ccc2ccc(=O)oc2c1C[C@@H](O)C(C)(C)OCc1ccccc1>>CC(C)(OCc1ccccc1)[C@H](O)Cc1c(O)ccc2ccc(=O)oc12",
                        "reaction_type": "unknown",
                        "confidence_score": -0.07780490070581436,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(=O)Oc1ccc2ccc(=O)oc2c1C[C@@H](O)C(C)(C)OCc1ccccc1>>CC(C)(OCc1ccccc1)[C@H](O)Cc1c(O)ccc2ccc(=O)oc12",
                        "reaction_type": "unknown",
                        "confidence_score": -0.08968893438577652,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "COCOc1ccc2ccc(=O)oc2c1C[C@@H](O)C(C)(C)OCc1ccccc1>>CC(C)(OCc1ccccc1)[C@H](O)Cc1c(O)ccc2ccc(=O)oc12",
                        "reaction_type": "unknown",
                        "confidence_score": -0.09784355759620667,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(C)(OCc1ccccc1)[C@H](O)Cc1c(OC(=O)c2ccccc2)ccc2ccc(=O)oc12>>CC(C)(OCc1ccccc1)[C@H](O)Cc1c(O)ccc2ccc(=O)oc12",
                        "reaction_type": "unknown",
                        "confidence_score": -0.0999549925327301,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    }
                ],
                "COCOc1ccc2ccc(=O)oc2c1C[C@@H](O)C(C)(C)OCc1ccccc1": [
                    {
                        "smiles": "CC(C)(OCc1ccccc1)[C@H]1CO1.COCOc1ccc2ccc(=O)oc2c1>>COCOc1ccc2ccc(=O)oc2c1C[C@@H](O)C(C)(C)OCc1ccccc1",
                        "reaction_type": "unknown",
                        "confidence_score": -0.06982885301113129,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "COCOc1ccc2ccc(=O)oc2c1C[C@H](O)C(C)(C)OCc1ccccc1>>COCOc1ccc2ccc(=O)oc2c1C[C@@H](O)C(C)(C)OCc1ccccc1",
                        "reaction_type": "unknown",
                        "confidence_score": -0.0988755002617836,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(C)(OCc1ccccc1)[C@@H]1CO1.COCOc1ccc2ccc(=O)oc2c1>>COCOc1ccc2ccc(=O)oc2c1C[C@@H](O)C(C)(C)OCc1ccccc1",
                        "reaction_type": "unknown",
                        "confidence_score": -0.1015579029917717,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(C)(OCc1ccccc1)[C@H](O)Cc1c(O)ccc2ccc(=O)oc12.COCCl>>COCOc1ccc2ccc(=O)oc2c1C[C@@H](O)C(C)(C)OCc1ccccc1",
                        "reaction_type": "unknown",
                        "confidence_score": -0.11078803986310959,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "COCOc1ccc2ccc(=O)oc2c1C[C@H]1OC1(C)C.OCc1ccccc1>>COCOc1ccc2ccc(=O)oc2c1C[C@@H](O)C(C)(C)OCc1ccccc1",
                        "reaction_type": "unknown",
                        "confidence_score": -0.11474432051181793,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "COCOc1ccc2ccc(=O)oc2c1CC1OC1(C)C.OCc1ccccc1>>COCOc1ccc2ccc(=O)oc2c1C[C@@H](O)C(C)(C)OCc1ccccc1",
                        "reaction_type": "unknown",
                        "confidence_score": -3.901345729827881,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    }
                ],
                "COCOc1ccc2ccc(=O)oc2c1CC1OC1(C)C": [
                    {
                        "smiles": "CC1(C)OC1Cc1c(O)ccc2ccc(=O)oc12.COCCl>CCOC(C)=O.CN(C)C=O.O=C(O[K])O[K]>COCOc1ccc2ccc(=O)oc2c1CC1OC1(C)C",
                        "reaction_type": "unknown",
                        "confidence_score": 0.43396228551864624,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "COCOc1ccc2ccc(=O)oc2c1CC=C(C)C.O=C(OO)c1cccc(Cl)c1>ClCCl>COCOc1ccc2ccc(=O)oc2c1CC1OC1(C)C",
                        "reaction_type": "unknown",
                        "confidence_score": 0.3469387888908386,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(=O)OO.COCOc1ccc2ccc(=O)oc2c1CC=C(C)C>>COCOc1ccc2ccc(=O)oc2c1CC1OC1(C)C",
                        "reaction_type": "unknown",
                        "confidence_score": -0.12686873972415924,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "COCOc1ccc2ccc(=O)oc2c1CC=C(C)C.O=S(=O)(OO)O[K]>>COCOc1ccc2ccc(=O)oc2c1CC1OC1(C)C",
                        "reaction_type": "unknown",
                        "confidence_score": -4.634546279907227,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "COCOc1ccc2ccc(=O)oc2c1CC(O)C(C)(C)Br>>COCOc1ccc2ccc(=O)oc2c1CC1OC1(C)C",
                        "reaction_type": "unknown",
                        "confidence_score": -5.321547508239746,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "COCOc1ccc2ccc(=O)oc2c1CC(Br)C(C)(C)O>>COCOc1ccc2ccc(=O)oc2c1CC1OC1(C)C",
                        "reaction_type": "unknown",
                        "confidence_score": -5.55853271484375,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    }
                ],
                "CC1(C)OC1Cc1c(O)ccc2ccc(=O)oc12": [
                    {
                        "smiles": "CC(C)=CCc1c(O)ccc2ccc(=O)oc12.O=C(OO)c1cccc(Cl)c1>ClCCl>CC1(C)OC1Cc1c(O)ccc2ccc(=O)oc12",
                        "reaction_type": "unknown",
                        "confidence_score": 0.39534884691238403,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC1(C)OC1Cc1c(OCc2ccccc2)ccc2ccc(=O)oc12>CO.ClCCl.BrB(Br)Br>CC1(C)OC1Cc1c(O)ccc2ccc(=O)oc12",
                        "reaction_type": "unknown",
                        "confidence_score": 0.37777775526046753,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC1(C)OC1Cc1c(OC(=O)OCc2ccccc2)ccc2ccc(=O)oc12>>CC1(C)OC1Cc1c(O)ccc2ccc(=O)oc12",
                        "reaction_type": "unknown",
                        "confidence_score": -0.14922821521759033,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(=O)OO.CC(C)=CCc1c(O)ccc2ccc(=O)oc12>>CC1(C)OC1Cc1c(O)ccc2ccc(=O)oc12",
                        "reaction_type": "unknown",
                        "confidence_score": -4.665151119232178,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    }
                ],
                "CC(C)=CCc1c(O)ccc2ccc(=O)oc12": [
                    {
                        "smiles": "COCOc1ccc2ccc(=O)oc2c1CC=C(C)C>Cl.CC(=O)O.ClCCl>CC(C)=CCc1c(O)ccc2ccc(=O)oc12",
                        "reaction_type": "unknown",
                        "confidence_score": 0.4259259104728699,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "COc1ccc2ccc(=O)oc2c1CC=C(C)C>c1ccncc1.c1ccncc1.ClCCCl.Cl[Al](Cl)Cl.Cl[Al](Cl)Cl.O>CC(C)=CCc1c(O)ccc2ccc(=O)oc12",
                        "reaction_type": "unknown",
                        "confidence_score": 0.3999999761581421,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(C)=CCc1c(OCc2ccccc2)ccc2ccc(=O)oc12>CO.ClCCl.BrB(Br)Br>CC(C)=CCc1c(O)ccc2ccc(=O)oc12",
                        "reaction_type": "unknown",
                        "confidence_score": 0.39534884691238403,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(C)=CCOc1ccc2ccc(=O)oc2c1>>CC(C)=CCc1c(O)ccc2ccc(=O)oc12",
                        "reaction_type": "unknown",
                        "confidence_score": -0.0829094648361206,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    },
                    {
                        "smiles": "CC(=O)Oc1ccc2ccc(=O)oc2c1CC=C(C)C>>CC(C)=CCc1c(O)ccc2ccc(=O)oc12",
                        "reaction_type": "unknown",
                        "confidence_score": -0.13051128387451172,
                        "probability": 0.0,
                        "confirmed": False,
                        "reaction_cost": 1
                    }
                ]
            }
        }

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
            "label": "transformer",
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
            "label": "transformer",
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
            "label": "transformer",
            "data": {"catalyst": "CCO"},
            "target": "13",
            "type": "molecule",
            "animated": True,
        },
        {
            "id": "13-14",
            "source": "13",
            "label": "expert",
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
                "reaction_type": "transformer",
                "confidence_score": -0.07182464748620987,
                "probability": -0.06447131931781769,
            },
            {
                "smiles": "CC(C)(C)[Si](C)(C)Cl.O=C1O[C@H](CO)[C@@H](O)[C@H]1O>>CC(C)(C)[Si](C)(C)OC[C@H]1OC(=O)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C",
                "reaction_type": "transformer",
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
                "reaction_type": "transformer",
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
                "reaction_type": "transformer",
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
                "reaction_type": "transformer",
                "confidence_score": -0.04458966106176376,
                "probability": -0.09628116339445114,
            }
        ],
        "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1": [
            {
                "smiles": "CC(C)(C)[Si](C)(C)O[C@@H]1[C@@H](CO)O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]1O[Si](C)(C)C(C)(C)C.CCC(CC)COC(=O)[C@H](C)N[P@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1>>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1",
                "reaction_type": "transformer",
                "confidence_score": -0.028011322021484375,
                "probability": -0.056453727185726166,
            },
            {
                "smiles": "CC(C)(C)[Si](C)(C)O[C@@H]1[C@H](O[Si](C)(C)C(C)(C)C)[C@](C#N)(c2ccc3c(N)ncnn23)O[C@@H]1CO.CCC(CC)COC(=O)[C@H](C)N[P@@](=O)(Oc1c(F)c(F)c(F)c(F)c1F)c1ccccc1>>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1",
                "reaction_type": "transformer",
                "confidence_score": -0.04624204337596893,
                "probability": -0.05625361204147339,
            },
        ],
        "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1": [
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@H]1O[C@H](C)CC(=O)O)c1ccccc1>C1CCOC1.CC(C)(C)[O-].[K+]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H](O[C@H](C)CC(=O)O)[C@H]1O[C@H](C)CC(=O)O)c1ccccc1>C1CCOC1.CC(C)(C)[O-].[K+]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H](O[C@H](C)CC(=O)O)[C@@H]1O)c1ccccc1>C1CCOC1.CC(C)(C)[O-].[K+]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O[Si](c1ccccc1)(c1ccccc1)C(C)(C)C)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](c2ccccc2)(c2ccccc2)C(C)(C)C)[C@@H]1O[Si](c1ccccc1)(c1ccccc1)C(C)(C)C)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](c2ccccc2)(c2ccccc2)C(C)(C)C)[C@@H]1O)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NC(C)=O)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>O.CCO.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N4C(=O)c5ccccc5C4=O)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>NN.O.CCO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NS(=O)(=O)c4ccc(C)cc4)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>[MgH2].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "C=CCOC(=O)Nc1ncnn2c([C@]3(C#N)O[C@H](CO[P@@](=O)(N[C@@H](C)C(=O)OCC(CC)CC)c4ccccc4)[C@@H](O)[C@H]3O)ccc12>C1CCNC1.O.C1COCCO1.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N(C(=O)OC(C)(C)C)C(=O)OC(C)(C)C)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>CCOC(=O)C.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]2OC(C)(C)O[C@H]12)c1ccccc1>O.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NC=O)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>O.Cc1ccccc1.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NCc4ccccc4)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>[H][H].[Pd].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N(Cc4ccccc4)Cc4ccccc4)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>[H][H].[Pd].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "C=CCN(CC=C)c1ncnn2c([C@]3(C#N)O[C@H](CO[P@@](=O)(N[C@@H](C)C(=O)OCC(CC)CC)c4ccccc4)[C@@H](O)[C@H]3O)ccc12>NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2.CN1C(=O)CC(=O)N(C)C1=O.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.C1=CC=C(C=C1)P(C2=CC=CC=C2)C3=CC=CC=C3.[Pd]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NC(=O)OCC[Si](C)(C)C)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC.C1CCOC1>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O[Si](C)(C)C(C)(C)C)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O[Si](C)(C)C(C)(C)C)[C@@H]1O)c1ccccc1>C1CCOC1.O.O.O.[F-].CCCC[N+](CCCC)(CCCC)CCCC>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1OC=O)c1ccccc1>[BH4-].[Na+].C1CCOC1>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC=O)[C@@H]1OC=O)c1ccccc1>[BH4-].[Na+].C1CCOC1>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC=O)[C@@H]1O)c1ccccc1>[BH4-].[Na+].C1CCOC1>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1OC(=O)c1ccc(C)cc1)c1ccccc1>[NH2-].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC(=O)c2ccc(C)cc2)[C@@H]1OC(=O)c1ccc(C)cc1)c1ccccc1>[NH2-].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC(=O)c2ccc(C)cc2)[C@@H]1O)c1ccccc1>[NH2-].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1OC1CCCCO1)c1ccccc1>O.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC2CCCCO2)[C@@H]1OC1CCCCO1)c1ccccc1>O.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC2CCCCO2)[C@@H]1O)c1ccccc1>O.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1OC(=O)c1ccccc1)c1ccccc1>O.C[O-].[Na+].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC(=O)c2ccccc2)[C@@H]1OC(=O)c1ccccc1)c1ccccc1>O.C[O-].[Na+].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC(=O)c2ccccc2)[C@@H]1O)c1ccccc1>O.C[O-].[Na+].CO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@@H]1C=C[C@](C#N)(c2ccc3c(N)ncnn23)O1)c1ccccc1>N=O.O=[Os](=O)(=O)=O.O.CC(C)=O>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(-n4c(C)ccc4C)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>CCO.Cl.NO>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N=C(c4ccccc4)c4ccccc4)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>O.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1OC)c1ccccc1>B(Br)(Br)Br.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC)[C@@H]1OC)c1ccccc1>B(Br)(Br)Br.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](OC)[C@@H]1O)c1ccccc1>B(Br)(Br)Br.NC1=NC(=O)N(C=C1)[C@H]2C[C@H](O)[C@@H](CO[P](O)(O)=O)O2>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]2OC(c3ccccc3)O[C@H]12)c1ccccc1>[H][H].[Pd]>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(NC(=O)OC(C)(C)C)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1>CCOC(=O)C.Cl>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
            {
                "smiles": "CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@@H]2O[Si](C(C)(C)C)(C(C)(C)C)O[C@H]12)c1ccccc1>C1CCOC1>CCC(CC)COC(=O)[C@H](C)N[P@](=O)(OC[C@H]1O[C@@](C#N)(c2ccc3c(N)ncnn23)[C@H](O)[C@@H]1O)c1ccccc1",
                "reaction_type": "expert",
                "confidence_score": 0.8,
                "probability": 0.8,
            },
        ],
    },
}

app.layout = html.Div(
    [
        html.Div(
            [
                dash_chemical_flow.ChemicalFlow(
                    id="workflow",
                    label="my-label",
                    # nodes=DRY_RUN_DATA["nodes"],
                    # edges=DRY_RUN_DATA["edges"],
                    nodes=workflow["nodes"],
                    edges=workflow["edges"],
                )
            ],
            id="view"
        ),
        html.Button("change workflow data", id="btn")
    ]
)


@callback(
    [
        Output("view", "children"),
    ],
    Input("btn", "n_clicks"),
    prevent_initial_call=True

)
def rerender_workflow(n_clicks):
    return [
        dash_chemical_flow.ChemicalFlow(
            id="workflow-2",
            label="my-label",
            nodes=DRY_RUN_DATA["nodes"],
            edges=DRY_RUN_DATA["edges"],
            # nodes=workflow["nodes"],
            # edges=workflow["edges"],
        )
    ]


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
