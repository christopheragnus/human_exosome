import src.fetch_data as fetch_data 
import src.parse_data as parse_data
import argparse

def main():

  parser = argparse.ArgumentParser()
  parser.add_argument('-f', '--file', type=str, help='Input file')

  args = parser.parse_args()
  arg_file = args.file

  print(f"Reading file: {arg_file}")
  with open(arg_file, "r") as file:
          contents = file.read()

          items = contents.split(',')

          for item in items:
            item = item.strip()
            fetch_data.fetch_data(item)

  parse_data.main()

if __name__ == "__main__":
    main()