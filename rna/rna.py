"""
1. Given an RNA sequence, such as ACAGU, we can predict its secondary structure 
   by tagging each nucleotide as (, ., or ). Each matching pair of () must be 
   AU, GC, or GU (or their mirror symmetries: UA, CG, UG). 
   We also assume pairs can _not_ cross each other. 
   The following are valid structures for ACAGU:

   ACAGU
   .....
   ...()
   ..(.)
   .(.).
   (...)
   ((.))    

   We want to find the structure with the maximum number of matching pairs. 
   In the above example, the last structure is optimal (2 pairs). 

   >>> best("ACAGU")
   (2, '((.))')

   [UPDATE] Tie-breaking: arbitrary is fine. Don't worry as long as your structure
   is one of the correct best structures.
UUCAGGA
(3, '(((.)))')
GUUAGAGUCU
(4, '(.()((.)))')
GCACG
(2, '().()')
AUAACCUUAUAGGGCUCUG
(8, '.(((..)()()((()))))')
UUGGACUUGAGAAAAG
(5, '((...((()))...))')
UCAAUGGGUAGUAAAU
(6, '(((.)))((..(.)))')
UUUGGCACUUUCAGA
(6, '(((((.(..))))))')
ACACACCUUGUCCGUGAA
(6, '.((.(..)))(.()(.))')   
GAUGCCGUGUAGUCCAAAGACUUCACCGUUGG
(14, '.()()(()(()())(((.((.)(.))()))))')
CGCGAAUAAAAAGGCACUGUU
(8, '()()((((....(().)))))')
ACGGCCAGUAAAGGUCAUAUACGCGGAAUGACAGGUCUAUCUAC
(19, '.()(((.)(..))(((.()()(())))(((.)((())))))())')
UGGGUGAGUCGCACACUCUGCGUACUCUUUCCGUAAUU
(15, '.((()((((.()).(.)))(()())).((...()))))')
AUACGUCGGGGACAAGAAUUACGG
(8, '.(.(((()((..(..)..))))))')
AGGCAUCAAACCCUGCAUGGGAGCACCGCCACUGGCGAUUUUGGUA
(20, '.(()())...((((()()))((()(.()(((.)))()())))))()')
CGAGGUGGCACUGACCAAACACCACCGAAAC
(9, '.(.((((().)((.)..))).)...()...)')
CGCCGUCCGGGCGCGCCUUUUACGUAGAUUU
(12, '.(..(...((((())))(((.(())))))))')
CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU
(18, '(()())(((((.)))()(((())(.(.().()()))))))')
AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU
(11, '(((.(..(.((.)((...().))()))))))')

2. Total number of all possible structures

   >>> total("ACAGU")
   6

3. k-best structures: output the 1-best, 2nd-best, ... kth-best structures.

   >>> kbest("ACAGU", 3)
   [(2, '((.))'), (1, '(...)'), (1, '.(.).')]
   
   The list must be sorted. 
   [UPDATE] Arbitray tie-breaking is fine.

   In case the input k is bigger than the number of possible structures, output all.

   Sanity check: kbest(s, 1)[0][0] == best(s)[0] for each RNA sequence s.

All three functions should be in one file: rna.py.

See testcases at the end (also in test.txt on canvas).
"""
from collections import defaultdict
import heapq

def pair(a, b):
   if a == 'A' and b == 'U': return True
   if a == 'G' and (b == 'C' or b == 'U'): return True
   if a == 'U' and (b == 'A' or b == 'G'): return True
   if a == 'C' and b == 'G': return True
   return False

def best(rna, opt = defaultdict(int)):
   if rna not in opt:
      if len(rna) == 1: opt[rna] = (0, '.') 
      elif len(rna) == 0: opt[rna] = (0, '')
      else:
         max_numPair = 0
         max_pairSeq = ''
         rnal = len(rna)
         numPair, pairSeq = best(rna[1:])
         max_numPair, max_pairSeq = numPair, '.' + pairSeq
         for k in range(1, rnal):
            if pair(rna[0], rna[k]):
               left_numPair, left_pairSeq = best(rna[1:k])
               right_numPair, right_pairSeq = best(rna[k+1:])
               if max_numPair < left_numPair + right_numPair + 1:
                  max_numPair = left_numPair + right_numPair + 1
                  max_pairSeq = '(' + left_pairSeq + ')' + right_pairSeq
         opt[rna] = (max_numPair, max_pairSeq)
   return opt[rna]

def total(rna, opt = defaultdict(int)):
   if rna not in opt:
      if len(rna) == 1: opt[rna] = 1
      elif len(rna) == 0: opt[rna] = 1
      else:
         total_numPair = 0
         rnal = len(rna)
         total_numPair += total(rna[1:])
         for k in range(1, rnal):
            if pair(rna[0], rna[k]):
               left_numPair = total(rna[1:k])
               right_numPair = total(rna[k+1:])
               total_numPair += (left_numPair * right_numPair)
         opt[rna] = total_numPair
   return opt[rna]

def kbest(rna, k, opt = defaultdict(int)):
   if rna not in opt:
      if len(rna) == 1: opt[rna] = [(0, '.')] 
      elif len(rna) == 0: opt[rna] = [(0, '')]
      else:
         pq = []
         match = []
         seen = set()
         rnal = len(rna)

         unmatch = kbest(rna[1:], k) # if the first element does not match
         match.append((rna[1:])) # if the first element match
         seen.add((rna[1:], 0))
         heapq.heappush(pq, (-unmatch[0][0], '.' + unmatch[0][1], 0, 0))
         lmatch = 1 # length of the match matrix
         for l in range(1, rnal):
            if pair(rna[0], rna[l]):
               left = kbest(rna[1:l], k)
               right = kbest(rna[l+1:], k)
               heapq.heappush(pq, (-1-left[0][0]-right[0][0], '('+left[0][1]+')'+right[0][1], lmatch, 0, 0)) 
               # the maximum number, corresponding rna structure, position of the match blocks, the position in one of the block
               match.append((rna[1:l], rna[l+1:]))
               seen.add((rna[1:l], rna[l+1:], 0, 0))
               lmatch += 1

         res = []
         while (len(res) < k) and len(pq):
            item = heapq.heappop(pq)
            res.append((-item[0], item[1]))
            block_pos = item[2]
            if block_pos == 0: # the unmatched case
               idx = item[3]
               sol = kbest(match[0], k)
               if (idx+1 < len(sol)) and ((match[0], idx+1) not in seen):
                  heapq.heappush(pq, (-sol[idx+1][0], '.'+sol[idx+1][1], 0, idx+1))
                  seen.add((match[0], idx+1))
            else:
               left_idx = item[3]
               right_idx = item[4]
               left_sol = kbest(match[block_pos][0], k)
               right_sol = kbest(match[block_pos][1], k)

               if (left_idx + 1 < len(left_sol)) and (match[block_pos][0], match[block_pos][1], left_idx+1, right_idx) not in seen:
                  heapq.heappush(pq, (-1-left_sol[left_idx+1][0]-right_sol[right_idx][0], '('+left_sol[left_idx+1][1]+')'+right_sol[right_idx][1], block_pos, left_idx+1, right_idx))
                  seen.add((match[block_pos][0], match[block_pos][1], left_idx+1, right_idx))
               if (right_idx + 1 < len(right_sol)) and (match[block_pos][0], match[block_pos][1], left_idx, right_idx+1) not in seen:
                  heapq.heappush(pq, (-1-left_sol[left_idx][0]-right_sol[right_idx+1][0], '('+left_sol[left_idx][1]+')'+right_sol[right_idx+1][1], block_pos, left_idx, right_idx+1))
                  seen.add((match[block_pos][0], match[block_pos][1], left_idx, right_idx+1))
         opt[rna] = res
   return opt[rna]

def main():
   print(best('ACAGU'))# == (3, '(((.)))'))
   print(total('ACAGU'))
   print(kbest('ACAGU', 10))
   print(best('CCCGGG'))# == (4, '(.()((.)))'))
   print(total('CCCGGG'))
   print(kbest('CCCGGG', 10))

if __name__ == '__main__':
   main()










