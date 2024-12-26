# pixelize


This package uses [uv](https://docs.astral.sh/uv/getting-started/installation/)
for installing and running with dependencies.


Example usage:

```
#see documentation
uv run pixelize.py --help

#run with default options (4 colors, 16x16 pixels)
uv run pixelize.py /tmp/hooh.jpg

#preview the output
uv run pixelize.py /tmp/hooh.jpg --show

#get a 32x32 pixel version
uv run pixelize.py --bits 32 /tmp/hooh.jpg

#get a 2 color version
uv run pixelize.py --colors 2 /tmp/hooh.jpg
```
