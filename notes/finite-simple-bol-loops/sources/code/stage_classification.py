#!/usr/bin/env python3
"""Stage the published exact programs in their original repository-relative layout.

Usage: python stage_classification.py /absolute/path/to/new-workspace
The destination must not exist. No programs or network operations are executed.
"""
from pathlib import Path
import hashlib
import json
import shutil
import sys


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    dest = Path(sys.argv[1]).resolve()
    dest.mkdir(parents=True, exist_ok=False)
    root = Path(__file__).resolve().parents[2]
    manifest = json.loads((root / 'classification-source-map.json').read_text())
    count = 0
    for entry in manifest['files']:
        source_path = entry['source_path']
        if '/code/' not in source_path:
            continue
        public = root / entry['public_path']
        data = public.read_bytes()
        expected = entry['public_sha256']
        if hashlib.sha256(data).hexdigest() != expected:
            raise SystemExit(f'Hash mismatch: {public}')
        target = dest / source_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        count += 1
    print(f'Staged {count} files in {dest}')
    print(f'cd {dest}')
    print('Run the desired source command from sources/code/README.md.')
    print('This stages programs only, not the math-wip repository-wide integrity suite.')


if __name__ == '__main__':
    main()
