#!/usr/bin/env python3
"""Clean-room exact-operation fixtures matching STPGC Algorithms 1--3.

The implementation uses closed-neighborhood node dominance and open-edge
neighborhood dominance as specified in the pinned source, avoiding the DBLP/GNN
benchmark path.  It reports clique-complex Betti_0/Betti_1 for tiny fixtures.
"""
import argparse, csv, hashlib, json, platform, sys, time
from collections import defaultdict
from pathlib import Path


def graph(edges):
    a=defaultdict(set)
    for x,y in edges:
        a[x].add(y); a[y].add(x)
    return {str(k): sorted(v) for k,v in sorted(a.items())}
def adj(g): return {int(k):set(v) for k,v in g.items()}
def edgeset(a): return {tuple(sorted((u,v))) for u in a for v in a[u] if u<v}
def closed(a,u): return a[u]|{u}
def comps(a):
    seen=set(); c=0
    for u in a:
        if u not in seen:
            c+=1; stack=[u]; seen.add(u)
            while stack:
                x=stack.pop()
                for y in a[x]:
                    if y not in seen: seen.add(y);stack.append(y)
    return c
def triangles(a):
    return sum(1 for u in a for v in a[u] if u<v for w in a[u]&a[v] if v<w)
def betti(a):
    # For these fixtures (at most one filled triangle), clique-complex beta1.
    return {'beta0':comps(a),'beta1':len(edgeset(a))-len(a)+comps(a)-triangles(a)}
def remove_node(a,u):
    a={x:set(ns) for x,ns in a.items() if x!=u}
    for ns in a.values(): ns.discard(u)
    return a
def remove_edge(a,x,y):
    a={u:set(ns) for u,ns in a.items()};a[x].discard(y);a[y].discard(x);return a
def add_edge(a,x,y):
    a={u:set(ns) for u,ns in a.items()};a[x].add(y);a[y].add(x);return a

def strong_step(a,u,v):
    assert v in a[u] and closed(a,u)<=closed(a,v)
    return remove_node(a,u)
def edge_dominator(a,x,y):
    common=(a[x]&a[y])-{x,y}
    for v in common:
        if common <= closed(a,v): return v
    return None
def edge_step(a,x,y):
    v=edge_dominator(a,x,y); assert v is not None
    return remove_edge(a,x,y),v
def coning_step(a,u,v):
    # Algorithm 3: insert missing (v,w) only if each is an edge-collapse edge.
    inserted=[]
    for w in sorted(a[u]-{v}):
        if w not in a[v]:
            assert edge_dominator(add_edge(a,v,w),v,w) is not None
            a=add_edge(a,v,w);inserted.append((v,w))
    assert closed(a,u)<=closed(a,v)
    return remove_node(a,u),inserted

def run():
    rows=[]
    # GStrongCollapse: pendant node 0 dominated by its neighbor 1.
    a=adj(graph([(0,1),(1,2),(1,3),(2,3)])); b0=betti(a); after=strong_step(a,0,1)
    rows.append(('GStrongCollapse','pendant_into_dominator',b0,betti(after),{'removed_node':0,'dominator':1}))
    # GEdgeCollapse: each triangle edge has singleton open neighborhood witness.
    a=adj(graph([(0,1),(1,2),(0,2)])); b0=betti(a); after,w=edge_step(a,0,1)
    rows.append(('GEdgeCollapse','triangle_edge',b0,betti(after),{'removed_edge':[0,1],'edge_dominator':w}))
    # NeighborhoodConing: path 1--0--2 lacks strong/edge move; insert dominated
    # edge 1--2 (witness 0), then remove 0 dominated by 1.
    a=adj(graph([(0,1),(0,2)])); b0=betti(a); after,ins=coning_step(a,0,1)
    rows.append(('NeighborhoodConing','two_star_coning',b0,betti(after),{'removed_node':0,'dominator':1,'inserted_edges':[list(x) for x in ins]}))
    # destructive negative control: arbitrary non-dominance node removal changes beta0.
    a=adj(graph([(0,1),(1,2)])); before=betti(a); bad=remove_node(a,1); bad_after=betti(bad)
    control={'operation':'destructive_non_dominance_removal','before':before,'after':bad_after,
             'expected_failure':before!=bad_after}
    assert all(r[2]==r[3] for r in rows) and control['expected_failure']
    return rows,control

def main():
    p=argparse.ArgumentParser();p.add_argument('--out',required=True);args=p.parse_args(); out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    rows,control=run(); record={'method':'clean-room source-faithful discrete Algorithm 1/2/3 fixtures','source_upstream_commit':'9f73ec9500b084e27be7a37f5007de5abe60d2c3','rows':[], 'negative_control':control,'python':sys.version,'platform':platform.platform(),'seed':'deterministic'}
    with (out/'results.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['operation','fixture','beta0_before','beta1_before','beta0_after','beta1_after','detail']);w.writeheader()
        for op,fix,bef,aft,detail in rows:
            d={'operation':op,'fixture':fix,'beta0_before':bef['beta0'],'beta1_before':bef['beta1'],'beta0_after':aft['beta0'],'beta1_after':aft['beta1'],'detail':json.dumps(detail,sort_keys=True)};w.writerow(d);record['rows'].append(d)
    (out/'result.json').write_text(json.dumps(record,indent=2)+'\n')
    (out/'run.log').write_text('command: '+ ' '.join(sys.argv)+'\nall three source-faithful discrete fixtures preserve reported clique-complex Betti numbers; destructive control changes beta0.\n')
    manifest=[]
    for name in ['results.csv','result.json','run.log']:
        manifest.append(f"{hashlib.sha256((out/name).read_bytes()).hexdigest()}  {name}")
    (out/'SHA256SUMS').write_text('\n'.join(manifest)+'\n')
if __name__=='__main__': main()
