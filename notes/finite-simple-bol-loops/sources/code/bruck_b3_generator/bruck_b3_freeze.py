import runpy,io,contextlib,json,argparse
parser=argparse.ArgumentParser()
parser.add_argument("--output", required=True, help="Generated JSON path outside the checkout")
args=parser.parse_args()
with contextlib.redirect_stdout(io.StringIO()):d=runpy.run_path('bruck_b3_stabilizer.py')
s=d['s'];G=s['G'];gi={g:i for i,g in enumerate(G)};n=30
obj={'Hdelta':[[[(v>>(8*i))&255 for i in range(18)],[(v>>(144+8*d['ki'][g]))&255 for g in d['K']]] for v in d['central_kernel']], 'perms':[[list(g[0]),list(g[1])] for g in G], 'p':gi[s['sh']['p']], 'q':gi[s['sh']['q']], 'mul':[[gi[s['mul'](g,h)] for h in G] for g in G], 'unit':gi[s['unit']], 'diag':s['t']['diag'], 'pol':s['t']['pol'], 'gen':[gi[g] for g in s['gens']], 'alphaV':[[s['alpha'](g,1<<i,0)[0] for i in range(n)] for g in G], 'alphaZ':[[s['alpha'](g,1<<i,0)[1] for i in range(n)] for g in G], 'onZ':[[s['actZ'](1<<i,g) for i in range(8)] for g in G], 'F':[[list(s['F'][g,h]) for h in G] for g in G], 'K':[gi[g] for g in d['K']], 'B':d['basis'], 'ell':d['ell'], 'H':{gi[g]:list(d['Hsec'][g][0]) for g in d['K']}}
open(args.output,'w').write(json.dumps(obj,separators=(',',':')))
print('Wrote frozen explicit structure data')
