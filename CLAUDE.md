# nyan

Terminal Nyan Cat animation, ported from Python 2 (taizilongxu/nyancat).

@/home/rg/Agents/AGENTS.md

## Running

```
rs nyan                          # run with auto-selected scheme
python3 nyancat.py --scheme ireland
python3 nyancat.py --random
```

Schemes are defined in `schemes.py`. The scheme auto-selects by date: national flags on their national days, `trans` throughout June, `rainbow` otherwise.

```
rs preview [output.png]          # screenshot every scheme and assemble a preview grid
```
