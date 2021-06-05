# MakotoMiner
CPU miner for MakotoCoin.

# Required libraries
- requests : pip install requests

# How it works
- The MakotoCoin server replies with a 403 Forbidden if the random number is an incorrect guess.
- It returns a 200 OK if a correct guess is made, along with the instructions on obtaining the "coin."
- The code will break if the response contains the substring "200".
- The range has been narrowed down to:
- ```python
- for i in range(0, 10):
-     possible_hashes = f"40{i}00000"
- ```
- The code, with 10 instances running, does 100 H/s.
- It takes a theoretical maximum of 1.1 days to mine one MakotoCoin.
