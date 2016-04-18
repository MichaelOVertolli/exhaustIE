from itertools import chain, combinations
from sympy.logic.boolalg import And, Or, Not
from sympy.abc import A, B, C


def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def exhIEL(phi, alt):
    temp = set([_ for _ in alt])
    if phi.args == ():
        # make phi the set if there are no other disjuncts
        fphi = set([phi])
    else:
        fphi = set(phi.args)
    #  print 'h', h
    mc = dict()
    # build maximal (ALT, phi)-compatible
    for p in fphi:
        mc[p] = temp - set([p])
    # intersect maximal (ALT, phi)-compatible
    ie = list(reduce(set.intersection, mc.values()))
    # the rest are random details handling edge cases for the final output.
    if len(ie) == 0:
        ie = reduce(Or, fphi)
    else:
        ie = reduce(And, [Not(_) for _ in ie])
        if len(fphi) > 1:
            fphi = reduce(Or, fphi)
        else:
            fphi = list(fphi)[0]
        ie = And(fphi, ie)
    return ie

C1 = [A, B, And(A, B)]
C2 = [A, B]
C3 = [A, B, C]
CIE = [exhIEL(A, [A, B]), exhIEL(B, [A, B])]
P = Or(A, B)
