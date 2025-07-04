####
# Assuming Raspbian, Ubuntu or Windows
#
# **Prerequisites**
#
# On every node:
# sudo apt-get update; sudo apt-get -y install python-mpi4py
# OR
# uv init.
# uv add mpi4py
# uv run main.py
# On master node
# ssh-keygen -t rsa
#
# For everynode: Replace IP-ADDRESS with IP of each node
# cat ~/.ssh/id_rsa.pub | ssh pi@IP-ADDRESS "cat >> .ssh/authorized_keys"
#
# Create cluster file on master node. One line per cluster.
# 192.168.1.10
# 192.168.1.11
# etc
#
# On each node make sure all other nodes are listed in
# /etc/hosts with their right hostnames, e.g.
# 192.168.1.10   node1
# 192.168.1.11   node2
#
# A copy of the script must be present on each node with the 
# same path and filename
#
# To run it on on cluster
# mpiexec -hostfile ~/clusterfile python ./main.py
###

from mpi4py import MPI
import math
import time
from typing import Optional

def isPrimeTrialDiv(num):
    # Returns True if num is a prime number, otherwise False.
    # Uses the trial division algorithm for testing primality.
    # All numbers less than 2 are not prime.
    if num < 2:
        return False

    # See if num is divisible by any number up to the square root of num:
    i = 2
    lim = int(math.sqrt(num)) + 1
    while i < lim:
        if num % i == 0:
                return False
        i = i + 1

    return True


mylist: Optional[list[list[int]]] = []
numstested = 0
BATCHSZ = 30000
MAXTOTEST = 48 * BATCHSZ
primesfound = 0
primei = 0

comm = MPI.COMM_WORLD
rank = comm.rank
totalnodes = comm.size
if rank == 0:
    print("TOTALCORES=" + str(totalnodes))

while numstested < MAXTOTEST:
    if rank == 0:
        mylist = []
        for i in range(0, totalnodes):
            innerlist = []
            innerlist.append(primei * BATCHSZ)
            innerlist.append(((primei + 1) * BATCHSZ) - 1)
            mylist.append(innerlist)
            primei = primei + 1
    else:
        mylist = None

    me = comm.scatter(mylist, root=0)
    numstested = numstested + (totalnodes * BATCHSZ)
    results = []
    for p in range(me[0], me[1]):
        if isPrimeTrialDiv(p):
            results.append(p)

    gathered = comm.gather(results, root=0)
    if rank == 0 and gathered is not None:
        for inn in gathered:
            primesfound = primesfound + len(inn)
        print("Primes found so far: " + str(primesfound))


def main():
    print("mpicluster!")


if __name__ == "__main__":
   main()
