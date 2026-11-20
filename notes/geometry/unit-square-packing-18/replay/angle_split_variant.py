"""Standalone addendum to split_variant: split the actual index of a closed angular cover, no chart matching."""
from split_variant import extend
from pathlib import Path
def extend_angle(source,target):
 extend(source,target);s=Path(target).read_text()
 a='HP h=t==0?';b='''if(t==4||t==5){if(v<=0||v>=B)throw runtime_error("angle cut");for(int k=0;k<B;k++)if((t==4&&k>=v)||(t==5&&k<v))C[k][j].clear();continue;}
 HP h=t==0?'''
 assert s.count(a)==1 and s.count('t<0||t>3')==1
 Path(target).write_text(s.replace(a,b).replace('t<0||t>3','t<0||t>5'))
