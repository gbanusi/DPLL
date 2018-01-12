from Algorithm.DPLLAlg import DPLL, DPLLSatisfiableCNF, DPLLSatisfiableCLA

__author__ = 'gbbanusic'



print str(DPLLSatisfiableCLA
          ("q1, q2, q3 <- r1, r2, r3; r2 <- q1, q2, r3, r2; q1 <- r1")) + "\n"

#print str(DPLLSatisfiableCNF("(-a || -b || c || d) && (c || d || -b) && (-c || -d || -f || d) && "
#               "(-d || c || -f) && (c) && (-c || -d || -e || b) && (-c || d || d || e)") )