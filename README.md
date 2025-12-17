# site-tree-generator

Generate a site tree PDF from an Excel breadcrumb file (LVL0 LVL1 ...).

## Install
```bash
pip install git+https://github.com/arashsayfi/site-tree-generator.git

## Usage
site-tree --input breadcrumbs.xlsx --output site_tree.pdf

## Input format
Excel file with columns like:
LVL 0 | LVL 1 | LVL 2 | LVL 3 | LVL 4 | ...
Each row represents one path in the site tree.
