# MelitaSuite
# Language: Python
# Input: TXT 
# Output: varies
# Tested with: PluMA 1.0, Python 3.6

PluMA plugin to interface to the Melita suite of analysis tools
for degenerate primers (Jaric et al, 2013)

Melita contains eight available pipelines.  The input to this plugin
is a TXT file with the first line containing the name of the Melita
pipeline to run, and the second its input file (if any).

Output will vary depending on the pipeline you are running (some take
an output file, some do not).

Note: The environment variable MELITA_HOME should be set to the location 
of the Melita toolkit, and this same directory should also be in your system
PATH.
