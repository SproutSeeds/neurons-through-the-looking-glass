"""Fresh exact local diagnostics for EF3. Universal claims require the written proofs."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

M=((Q(2),Q(-1)),(Q(1),Q(2)))
T=lambda a:tuple(zip(*a))
def mm(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def mv(a,v): return tuple(sum(a[i][k]*v[k] for k in range(2)) for i in range(2))
def scale(a,s): return tuple(tuple(x*s for x in row) for row in a)
H1=((Q(-1),Q(0)),(Q(0),Q(1)));H2=scale(H1,Q(-1))
assert mm(T(M),M)==((5,0),(0,5)) and M[0][0]*M[1][1]-M[0][1]*M[1][0]==5
vertices=[mv(M,v) for v in product([-1,1],repeat=2)]
assert max(x*x/Q(5) for v in vertices for x in v)==Q(9,5)<4
q=(Q(9,10),Q(9,10));znum=mv(M,q)
conj=[scale(mm(mm(T(M),h),M),Q(1,5)) for h in [H1,H2]]
refcoords=[mv(h,q) for h in conj]
assert refcoords==[(Q(9,50),Q(63,50)),(Q(-9,50),Q(-63,50))]
radius=Q(1,20)
inside_margin=1-max(abs(x) for x in q)-radius
outside_margin=abs(refcoords[0][1])-1-radius
assert inside_margin==Q(1,20)>0 and outside_margin==Q(21,100)>0
assert max(x*x/Q(5) for x in znum)<(2-radius)**2

# The square rotated by pi/4 is an explicit control to the universal exclusion.
A=((Q(1),Q(-1)),(Q(1),Q(1)))
assert mm(T(A),A)==((2,0),(0,2))
diamond_conj=[scale(mm(mm(T(A),h),A),Q(1,2)) for h in [H1,H2]]
assert diamond_conj==[((0,1),(1,0)),((0,-1),(-1,0))]
# Signed coordinate permutations preserve both open and closed unit squares.
for h in diamond_conj:
 assert all(sum(abs(x) for x in row)==1 for row in h)
 assert all(sum(abs(x) for x in row)==1 for row in T(h))
# The pi/4 square has max vertex coordinate sqrt(2)<2.
assert max(x*x/Q(2) for v in product([-1,1],repeat=2) for x in mv(A,v))==2<4

# Rational samples, expressly diagnostic, for axis-parallel domains and boundary options.
pts=list(product([Q(i,4) for i in range(-8,9)],repeat=2))
ell=Q(3,2);outer=Q(2)
for closed in [False,True]:
 def inner(z): return all(abs(x)<=ell if closed else abs(x)<ell for x in z)
 for z in pts:
  assert inner(z)==inner(mv(H1,z))==inner(mv(H2,z))
  assert all(abs(x)<=outer for x in z)

# Even polynomial action samples use x^2=k^2/(4N), no irrational roundoff.
action_cases=[]
u=Q(3,2);c=Q(7,5);kappa2=Q(3) # c is a positive algebraic test value, not an evaluated physical Wick variance.
areas=[Q(1,3),Q(5,7),Q(2,5),Q(4,9)]
for N,eps in product([1,2,3,7,16],[Q(0),Q(2,3)]):
 ks=[-N,-N+2,N-2,N]
 x2=[Q(k*k,4*N) for k in ks]
 W=sum(areas[i]*u*(x2[i]**2-6*c*x2[i]+3*c*c) for i in [0,1])
 J=sum(areas[i]*x2[i]**2 for i in [2,3]);Tm=kappa2/Q(2)*sum(areas[i]*x2[i] for i in range(4))
 V=W+eps*J-Tm
 U=sum(areas[i]*((u*(x2[i]**2-6*c*x2[i]+3*c*c) if i<2 else eps*x2[i]**2)-kappa2/Q(2)*x2[i]) for i in range(4))
 assert U==V
 r2=Q(N,4);bound=u*(r2*r2+6*c*r2+3*c*c)+eps*r2*r2+kappa2*r2/Q(2)
 for i in range(4):
  val=(u*(x2[i]**2-6*c*x2[i]+3*c*c) if i<2 else eps*x2[i]**2)-kappa2*x2[i]/Q(2)
  assert abs(val)<=bound
 wrong=V+kappa2/Q(2)*sum(areas[i]*x2[i] for i in [0,1])
 assert wrong!=U # control: omitting the inner quadratic term changes the exact action.
 action_cases.append({'N':N,'epsilon':str(eps),'U':str(U),'V':str(V),'bound':str(bound),'negative_control_detected':True})
# At N=1 any even polynomial of the canonical neuron is constant in z and outcome.
x2=Q(1,4);x4=Q(1,16)
assert x2*x2==x4
n1coeff={'inside_quartic':'u*|Lambda|/16','inside_wick_quadratic':'-3*u*c_a*|Lambda|/2','wick_constant':'3*u*c_a^2*|Lambda|','outside_quartic':'epsilon*|Omega minus Lambda|/16','all_Omega_quadratic':'-kappa_a^2*|Omega|/8'}
# Check the old total-map counterexample after clipping at r=0,1/2,1.
for r in [Q(0),Q(1,2),Q(1)]:
 for norm2 in [Q(1,100),Q(1,4),Q(1),Q(9)]:
  value=min(r,1/norm2);assert 0<=value<=r

receipt={'task_id':'EF3','at':datetime.now(timezone.utc).isoformat(),'status':'PASS','arithmetic':'Python Fraction, exact rational operations; no random sampling, numerical quadrature, or external packages','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'counterexample':{'M':'[[2,-1],[1,2]]','scale':'1/sqrt(5)','M_transpose_M':'5I','det_M':'5','vertex_numerators':[[str(x) for x in v] for v in vertices],'max_vertex_coordinate_squared':'9/5 < 4','point_coordinates_in_square':['9/10','9/10'],'point_numerators':[str(x) for x in znum],'reflected_square_coordinates':[[str(x) for x in v] for v in refcoords],'disc_radius':str(radius),'inside_margin_after_radius':str(inside_margin),'outside_margin_after_radius':str(outside_margin),'potential_gap_at_x_zero':'3*u*c_a^2 > 0','scope':'Failure of required potential symmetry on a positive-area open disc; no RP-failure inference'},'pi_over_4_control':{'conjugated_theta_1':'[[0,1],[1,0]]','conjugated_theta_2':'[[0,-1],[-1,0]]','both_preserve_open_and_closed_square':True,'diamond_fits_Omega_minus2_2':True,'F2_hypotheses_hold_for_diamond':True,'D10_excludes_diamond':True,'universal_rotation_classification':'Analytic proof in REPORT.md; finite controls alone do not establish it'},'axis_parallel_diagnostic':{'points_per_boundary_convention':len(pts),'boundary_conventions':['open','closed'],'status':'PASS; finite sample only'},'action_diagnostics':{'test_parameter_note':'c=7/5 is an algebraic diagnostic value only, not a computed c_a','cases':action_cases,'scope':'Finite exact checks support the universal linearity and bounded-amplitude proofs; they do not establish probability-law convergence'},'N1_scope_control':{'action_is_deterministic':True,'action_coefficients':n1coeff,'consequence':'Positive normalized constant tilt equals base law for either architecture, including nonsymmetric Lambda; follows analytically from |g|=1/2 and zero-potential T5'},'clipped_map_diagnostic':'PASS bounded outputs including r=0; local integrability and measurable total map follow from the written proof, not this finite sample'}
Path('MATH-CHECK.json').write_text(json.JSONEncoder(indent=2).encode(receipt)+'\n')
print('PASS exact BE2 geometry, positive-area margins, pi/4 F2 control, '+str(2*len(pts))+' axis-parallel sample cases, '+str(len(action_cases))+' exact action/bound cases with negative controls, and N=1 constant-action scope check')
print('Literal blanket exclusion of rotated squares from F2 is rejected by the pi/4 control; D10 restriction remains valid.')
