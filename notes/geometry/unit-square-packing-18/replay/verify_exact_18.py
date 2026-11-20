"""One-command replay of the complete arbitrary-rotation s(18) theorem."""
from pathlib import Path
from fractions import Fraction
import argparse,os,subprocess,sys,time
if __name__=='__main__':
 if sys.flags.optimize:raise RuntimeError('assertions required')
 ap=argparse.ArgumentParser();ap.add_argument('--workers',type=int,default=4);w=ap.parse_args().workers;assert 1<=w<=16
 os.chdir(Path(__file__).resolve().parent)
 # Side comparison over Q without a floating square root.
 U=Fraction(4822876,10**6);assert 2*U-7>0 and (2*U-7)**2>7
 phases=[('six_tilt18.py',),('verify_six_endpoint_classes.py',),('verify_full_endpoint_mask.py',),('verify_second_endpoint_mask.py',),('verify_fork_mask.py',),*(('verify_residual_masks.py',str(i))for i in (92,82,115))]
 t=time.monotonic()
 for cmd in phases:
  args=[sys.executable,'-S',*cmd]+([] if cmd==phases[0]else['--workers',str(w)])
  print('Running',*cmd,flush=True);subprocess.run(args,check=True)
 print('PASS s(18)=(7+sqrt(7))/2: exact construction + all 187 physical mask classes; 428 lower-bound terminals.',round(time.monotonic()-t,3))
