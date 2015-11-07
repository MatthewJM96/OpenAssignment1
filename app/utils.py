# utils.py

# Collection of utility functions.

def readFile(filePath):
  # readFile
  # Reads a file of the given file path.
  # Author: Matthew Marshall
  # Data Created: 23/10/2015
  # Output Data: [ { Name: , Type: , Population: , Latitude: , Longitude: } ]

  # Attempt to open file.
  try:
    file = open(filePath)
  except:
    print("Failed to open file at: " + filePath + "!")
    return 0
  
  # Collect lines in an array.
  try:
    skipLine = 1;
    lines = []
    for line in file:
      if skipLine == 1:
        skipLine = 0
        continue
      lines.append(line.split(","))
  except:
    print("File not in expected format.")
    return 0
    
  # Close file and return lines.
  file.close()
  return lines
  
def writeFile(data, filePath):
  # writeFile
  # Writes to a file of the given file path, entering given data.
  # Author: Matthew Marshall
  # Data Created: 23/10/2015
  # Expected Data: [ { Name: , Type: , Population: , Latitude: , Longitude: } ]
  
  # Attempt to open file.
  try:
    file = open(filePath, "w")
  except:
    print("Failed to open file at: " + filePath + "!")
    return 0
    
  # Loop over data and write to file.
  try:
    for entry in data:
      line = "Name: {:20s}, Location: {:5s}, Population: {:10s}, Latitude: {:10s}, Longitude: {:10s}".format(entry["Name"], entry["Type"], entry["Population"], entry["Latitude"], entry["Longitude"])
      file.write(line)
  except:
    print("Failed to iterate data, data in incorrect form.")
    return 0
  
  # Close file and return.
  file.close()
  return