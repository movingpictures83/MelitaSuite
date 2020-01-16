import sys
import numpy
import os


class MelitaSuitePlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      self.command = "runMelita.sh "
      filestuff = open(self.myfile, 'r')
      lines = []
      for line in filestuff:
         self.command += line.strip() + " "

   def output(self, filename):
      if (filename != "none"):
         self.command += filename
      os.system(self.command)

