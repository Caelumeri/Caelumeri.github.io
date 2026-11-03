#!/usr/bin/env python3
"""生成首屏分子结构 SVG 片段（主题色以 CSS 变量输出）。

用法：
    python tools/make_structure.py > structure.svg
然后把输出粘进 index.html 中 <g class="mol-structure"> 内。

依赖：rdkit（pip install rdkit）。结构来自 PubChem CID 441071（strychnine），
分子式 C21H22N2O2，与手绘无关；改 SMILES 即可换分子。
"""

import re
import sys

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Draw import rdMolDraw2D

SMILES = "C1CN2CC3=CCO[C@H]4CC(=O)N5[C@H]6[C@H]4[C@H]3C[C@H]2[C@@]61C7=CC=CC=C75"

W, H = 460, 450
BOND = 2.4
FONT_MIN, FONT_MAX = 13, 17
PALETTE = {6: (0.19, 0.35, 0.33), 7: (0.71, 0.37, 0.26), 8: (0.25, 0.42, 0.38)}
SWAP = {"#305954": "--mol-c", "#B55E42": "--mol-n", "#3F6B60": "--mol-o"}


def main() -> int:
    mol = Chem.MolFromSmiles(SMILES)
    if mol is None:
        print("bad SMILES", file=sys.stderr)
        return 1
    AllChem.Compute2DCoords(mol)

    drawer = rdMolDraw2D.MolDraw2DSVG(W, H)
    opts = drawer.drawOptions()
    opts.bondLineWidth = BOND
    opts.minFontSize, opts.maxFontSize = FONT_MIN, FONT_MAX
    opts.clearBackground = False
    opts.addStereoAnnotation = False
    opts.padding = 0.06
    opts.setAtomPalette(PALETTE)
    drawer.DrawMolecule(mol)
    drawer.FinishDrawing()

    svg = drawer.GetDrawingText()
    inner = re.search(r"<svg[^>]*>(.*)</svg>", svg, re.S).group(1)
    inner = inner.replace("<!-- END OF HEADER -->", "").strip()

    def atom_cb(match: re.Match) -> str:
        idx, rest = match.group(1), match.group(2)
        hexv = match.group(3).upper()
        var = SWAP.get(hexv, "--mol-c")
        return f"<path class='atom-{idx}'{rest} style='fill:var({var})'/>"

    inner = re.sub(
        r"<path class='atom-(\d+)'( d='[^']*')\s*fill='(#[0-9A-Fa-f]{6})'\s*/>",
        atom_cb,
        inner,
    )
    for hexv, var in SWAP.items():
        inner = inner.replace(f"stroke:{hexv};", f"stroke:var({var});")
        inner = inner.replace(f"fill:{hexv};", f"fill:var({var});")
    inner = inner.replace("stroke:#000000;", "stroke:var(--mol-c);")
    inner = inner.replace("fill:#000000;", "fill:var(--mol-c);")
    inner = inner.replace("fill='#000000'", "style='fill:var(--mol-c)'")

    sys.stdout.write(inner + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())