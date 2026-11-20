"""Replay exact nearest-rack proofs. Reuse complete cover/verifier; only add native filters."""
import sys,json,tempfile,subprocess
from pathlib import Path
from nearest_rack import emit
from nearest_init import source
from short_facets import transform
from angle_split_variant import extend_angle
from rack_lattice_input import build_rack
import verify_rack_angle as verify
def certified_init(o,B,p):
 with tempfile.TemporaryDirectory() as td:
  d=Path(td);init=d/'input';fac=d/'facets';cc=d/'filter.cpp';exe=d/'filter'
  build_rack(o,B,init)
  with fac.open('w') as f:emit(o,B,f)
  source('lattice_kernel.cpp',cc);subprocess.run(['g++','-std=c++17','-O3',cc,'-o',exe],check=True)
  with Path(p).open('w') as f:subprocess.run([exe,init,fac],stdout=f,check=True)
def extend(source,target):
 extend_angle(source,target);p=Path(target);p.write_text(transform(p.read_text()))
if __name__=='__main__':
 if sys.flags.optimize:raise RuntimeError('assertions required')
 if len(sys.argv)!=4:raise ValueError('rack.json owner_count cases.json')
 verify.build_rack=certified_init;verify.extend=extend
 verify.verify(json.loads(Path(sys.argv[1]).read_text()),int(sys.argv[2]),sys.argv[3])
