#!/usr/bin/env python


def cb((response, cb_arg, error)):
    typ, data = response
    print 'Message %s\n%s\n' % (cb_arg, data[0][1])

import getpass, imaplib2, sys
email = raw_input('What is your full Gmail address? ')
M = imaplib2.IMAP4_SSL('imap.gmail.com', 993)
try:
    M.LOGIN(email, getpass.getpass())
except:
    print "Login error..."
    M.LOGOUT()
    sys.exit(1)

M.SELECT(readonly=True)
#typ, data = M.SEARCH(None, 'ALL')
#for num in data[0].split():
#    print num, "->", type, data
#    M.FETCH(num, '(RFC822)', callback=cb, cb_arg=num)

print "Waiting for new messages..."
M.IDLE(timeout=600)
print "Something happened!"
type, data = M.recent()
for num in data[0].split():
    print num
    M.FETCH(num, '(RFC822)', callback=cb, cb_arg=num)


M.LOGOUT()
