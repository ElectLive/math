"""Nearest-rack verification with first-exit convex subtraction; no state-file trust."""
import sys,json
from pathlib import Path
import verify_rack_angle as verify
from verify_nearest_lower import certified_init,extend
from edgeclip import transform
def optimized(source,tar):
 extend(source,tar);p=Path(tar);p.write_text(transform(p.read_text()))
if __name__=='__main__':
 if sys.flags.optimize:raise RuntimeError('assertions required')
 if len(sys.argv)!=4:raise ValueError('rack.json owner_count cases.json')
 verify.build_rack=certified_init;verify.extend=optimized
 verify.verify(json.loads(Path(sys.argv[1]).read_text()),int(sys.argv[2]),sys.argv[3])
