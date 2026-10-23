#!/usr/bin/env python3
"""Deterministic falsification checks; supplementary evidence, not theorem proofs."""
from decimal import Decimal, localcontext
from pathlib import Path
import datetime
import json
import math

results = []

def record(name, cases, passed, **details):
    results.append(dict(name=name, cases=cases, status='PASS' if passed else 'FAIL', **details))

with localcontext() as ctx:
    ctx.prec = 70
    masses = ['0.03', '0.1', '1', '3', '100']
    am_values = ['0.00000001', '0.00001', '0.01', '0.2', '0.5', '0.9', '0.99999999']
    momenta = ['0', '0.00000001', '0.01', '0.3', '1', '2', '10', '1000', '1000000']
    count = 0
    max_mass_residual = Decimal(0)
    max_error_ratio = Decimal(0)
    good = True
    for ms in masses:
        m = Decimal(ms)
        for bs in am_values:
            a = Decimal(bs)/m
            mu = 1/a
            kap2 = mu*mu-m*m
            r = kap2/(mu*mu)
            for ws in momenta:
                for qs in momenta:
                    w, q = m*Decimal(ws), m*Decimal(qs)
                    D = m*m+w*w+q*q
                    ca = 1/(D+a*a*w*w*q*q)
                    c0 = 1/D
                    cmu = mu*mu/((mu*mu+w*w)*(mu*mu+q*q))
                    residual = abs((1/cmu-kap2)-(1/ca))/(1/ca)
                    max_mass_residual = max(max_mass_residual, residual)
                    coarse = 1/(m*m*(1+a*a*w*w)*(1+a*a*q*q))
                    difference = a*a*w*w*q*q/(D*(D+a*a*w*w*q*q))
                    error = (c0.sqrt()-ca.sqrt())**2
                    eps = Decimal('1e-52')
                    good &= (ca <= c0*(1+eps) and ca <= coarse*(1+eps))
                    good &= (difference <= min(a*a/4,c0)*(1+eps)+eps*ca)
                    good &= (error <= difference*(1+eps)+eps*ca)
                    good &= (0 <= kap2*cmu <= r*(1+eps))
                    max_error_ratio = max(max_error_ratio, error/(a*a/4))
                    count += 1
    good &= max_mass_residual < Decimal('1e-45')
    record('spectral identities and exact G8 constants, 70-digit decimal',count,good,
           max_relative_mass_shift_residual=str(max_mass_residual),
           largest_observed_squared_error_over_a2_quarter=str(max_error_ratio),
           minimum_am=am_values[0], maximum_am=am_values[-1])

ts = [10.0**(i/100) for i in range(-1200,1201)] + [0.0,1.0]
ratios=[]
for t in ts:
    if t:
        g=t*(math.log1p(4/(t*t))+2)
        ratios.append(g/(math.pi*min(t,1)))
record('literal logarithmic increment majorant',len(ts),min(ratios)>=1,
       minimum_g_over_pi_min=float(min(ratios)), includes_zero_convention=True)

ratios=[]
hs=[0,1e-12,1e-8,1e-4,.01,.1,.3,.6,1]
for a in [1e-5,.1,1,10,100]:
    for alpha in [.01,.1,.3,.5,.9,.99]:
        for x in hs:
            for y in hs:
                h=math.hypot(x,y)
                if not 0<h<=1:
                    continue
                lhs=sum(t*(math.log1p(4*a*a/(t*t))+2) for t in [x,y] if t)
                rhs=2*(2*(2*a)**(1-alpha)/(1-alpha)+2)*h**alpha
                ratios.append(lhs/rhs)
record('literal M_a_alpha small-displacement constant',len(ratios),max(ratios)<=1,
       largest_lhs_over_rhs=max(ratios),includes_axis_displacements=True)

I=[[1.,0.],[0.,1.]]
P=[[1.,0.],[0.,0.]]
Q=[[0.,0.],[0.,1.]]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]
def scale(s,A):
    return [[s*x for x in row] for row in A]
def sub(A,B):
    return add(A,scale(-1,B))
def inv(A):
    det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return [[A[1][1]/det,-A[0][1]/det],[-A[1][0]/det,A[0][0]/det]]
def normmax(A):
    return max(abs(x) for row in A for x in row)
def mineig(A):
    return (A[0][0]+A[1][1]-math.hypot(A[0][0]-A[1][1],A[0][1]+A[1][0]))/2
count=0
maxres=0.
lowesteig=1.
for b in [.03,.13,.24,.3]:
    H=[[.4,b],[b,.25]]
    maxeig=(.65+math.hypot(.15,2*b))/2
    for kap2 in [.1,.7,1.5,1.8]:
        if kap2*maxeig >= .99:
            continue
        Ca=mm(H,inv(sub(I,scale(kap2,H))))
        Cp=mm(H,inv(sub(I,scale(kap2,mm(P,H)))))
        Delta=sub(Ca,Cp)
        one=scale(kap2,mm(mm(Ca,Q),Cp))
        two=scale(kap2,mm(mm(Cp,Q),Ca))
        positive=add(scale(kap2,mm(mm(Cp,Q),Cp)),
                     scale(kap2**2,mm(mm(mm(mm(Cp,Q),Ca),Q),Cp)))
        denom=max(1,normmax(Delta))
        maxres=max(maxres,normmax(sub(Delta,one))/denom,
                   normmax(sub(Delta,two))/denom,normmax(sub(Delta,positive))/denom)
        lowesteig=min(lowesteig,mineig(Delta),mineig(sub(Cp,H)))
        count+=1
record('noncommuting 2-by-2 resolvent identities and both PSD differences',count,
       maxres<1e-12 and lowesteig>-1e-12,
       max_scaled_identity_residual=maxres,lowest_observed_eigenvalue=lowesteig,
       caveat='Finite-dimensional test only; no continuum or kernel-order inference.')

def simpson(fun,lo,hi,n):
    h=(hi-lo)/n
    total=fun(lo)+fun(hi)
    total+=4*sum(fun(lo+i*h) for i in range(1,n,2))
    total+=2*sum(fun(lo+i*h) for i in range(2,n,2))
    return total*h/3

cs=[]
for b in [.02,.1,.3,.7,.99,1.0]:
    ca=simpson(lambda t:1/math.sqrt(math.cos(t)**2+b*b*math.sin(t)**2),0,math.pi/2,16384)/(2*math.pi)
    cs.append(dict(am=b,c_a=ca))
okay=all(x['c_a']>=.25-1e-12 and x['c_a']<=1/(4*x['am']**2)+1e-12 for x in cs)
okay &= all(cs[i]['c_a']>=cs[i+1]['c_a'] for i in range(len(cs)-1))
okay &= abs(cs[-1]['c_a']-.25)<1e-12
record('independent quadrature of diagonal constant and endpoint limit',len(cs),okay,
       values=cs,simpson_subintervals=16384,
       caveat='The am=1 row checks the endpoint limiting expression, not an extra G2 endpoint claim.')

payload=dict(task='GB',status='PASS' if all(r['status']=='PASS' for r in results) else 'FAIL',
             generated_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
             deterministic=True,network_used=False,external_packages_used=False,
             total_cases=sum(r['cases'] for r in results),checks=results,
             limits='Finite checks are supplementary falsification attempts; symbolic proof and review remain necessary.')
Path('check-results.json').write_text(json.JSONEncoder(indent=2).encode(payload)+'\n')
print(json.JSONEncoder(indent=2).encode(payload))
if payload['status']!='PASS':
    raise SystemExit(1)
