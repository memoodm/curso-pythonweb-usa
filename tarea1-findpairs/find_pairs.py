import sys, getopt

def find_pairs(numbers,target):
    pairs = []
    memory = set()
    for n in numbers:
        complement = target - n
        if complement in memory:
            pairs.append([n,complement])
        memory.add(n)
    return pairs

if __name__ == "__main__":
   numbers = [int(x) for x in sys.argv[1].split(",")]  # int
   target = int( sys.argv[2] )# list[int]
   print(f"Pairs: { find_pairs(numbers,target) }")