
import os
import re

# If directony don't exist will create it!
def checkDirectory(directoryPath):
    if not os.path.exists(directoryPath):
        os.makedirs(directoryPath)


def extractResult(outputDirectory, fileName, regexPattern):

    file = open("{}/{}".format(outputDirectory, fileName))
    text = file.read()

    matchObjList = re.findall(regexPattern, text, re.M|re.I)

    return matchObjList