import sys
import telepot
from telepot.loop import MessageLoop

"""
usage: $ python eyeinthesky.py <token>
"""

try:
   token = sys.argv[1]
except:
   print "Error in token initialization"
   sys.exit(0)


bot = telepot.bot(token)
MessageLoop(bot, handle).run_as_thread()
