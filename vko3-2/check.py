import argparse
parser = argparse.ArgumentParser()
file = open("checkpoint.txt")
parser.add_argument('rivit', type=int, help='rivien maara')
args = parser.parse_args()
lines_to_print = [0, args.rivit-1]

for index, line in enumerate(file):
  if index == args.rivit:
      break
  print(line)