# Read numbers from a file and handle errors gracefully

with open('readfile','r') as file:
      for line in file:
            number = line.strip()
            try:
                  number = int(number)
                  print(f'Number: {number}')
            except ValueError as e:
                  print(f'Error converting "{number}" to an integer: {e}')
            except Exception as e:
                  print(f'An unexpected error occurred: {e}')
            finally:
                  print(f'Finished processing line: {line.strip()}')    
