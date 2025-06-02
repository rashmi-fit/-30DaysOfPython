with open('myData', 'r' ) as source, open('create_file', 'w') as target:
      for line in source :
            target.write(line)
