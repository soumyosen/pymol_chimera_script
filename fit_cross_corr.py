import os
from chimera import runCommand as rc # use 'rc' as shorthand for runCommand
from chimera import replyobj # for emitting status messages
from chimera.tkgui import saveReplyLog

file_names = [fn for fn in os.listdir(".") if fn.endswith(".pdb")]
#f = open('corr_file.dat', 'w')

for fn in file_names:
    replyobj.status("Processing " + fn) # show what file we're working on
    rc("open " + fn)
    rc("mmaker #1 #2")
    rc("fitmap #2 #0 resolution 4 metric correlation")
    rc("measure correlation #2.1 #0")
    #f.write('%s %s\n' %(fn, corr))
    #print(rc("measure correlation #2.1 #0"))
    saveReplyLog("%s.log" % fn)
    rc("close #2")

#f.close()

