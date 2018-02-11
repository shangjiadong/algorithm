"""
3. Number of bit strings of length n that has

   1) no two consecutive 0s.
   2) two consecutive 0s.
   
   >>> num_no(3)
   5
   >>> num_yes(3)
   3

   [HINT] There are three 3-bit 0/1-strings that have two consecutive 0s.
            001  100  000
          The other five 3-bit 0/1-strings have no two consecutive 0s:
       010  011  101  110  111

   Feel free to choose any implementation style.

   Filename: bitstrings.py

"""
def num_no(n):
    no = {1: 2, 2: 3}
    if n in no:
        return no[n]
    else:
        no[n] = num_no(n-1) + num_no(n-2)
        return no[n]

def num_yes(n):
    yes = {1: 0, 2: 1, 3: 3}
    if n in yes:
        return yes[n]
    else:
        yes[n] = 2**(n-2) + num_yes(n-2) + num_yes(n-1)
        return yes[n]

def main():
   print(num_yes(10))
   print(num_no(10))

if __name__ == '__main__':
   main()