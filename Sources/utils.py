
import os

# If directony don't exist will create it!
def checkDirectory(directoryPath):
    if not os.path.exists(directoryPath):
        os.makedirs(directoryPath)
