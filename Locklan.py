
from rivescript import RiveScript


rs = RiveScript(utf8=True)
rs.load_directory("./eg/brain")
rs.sort_replies()

print """Hello I'm Locklan, I can assist you with passwords
------------------------------------------------------------------------------

"""

while True:
    msg = raw_input("You> ")
    if msg == '/quit':
        quit()
    reply = rs.reply("localuser", msg)
    print "Locklan>", reply


 