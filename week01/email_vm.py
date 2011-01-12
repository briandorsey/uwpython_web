import smtplib
from pprint import pprint

def send_email(from_addr, to_addrs, subject, message, debug = False):

    template = """From: %s
To: %s
Subject: %s

"""
    headers = template % (from_addr, to_addrs, subject)

    if debug:
        print '#### debugging on'
        print headers + message
        print
        pprint(locals())
        print '#### '
    s = smtplib.SMTP('mail.blueboxgrid.com')
    if debug:
        s.set_debuglevel(1)
    s.ehlo()
    if debug:
        print '#### sendmail()'
    s.sendmail(from_addr, to_addrs, headers + message)
    s.close()

if __name__ == '__main__':
    failed_addrs = send_email( 'Darth Vader <darth@deathstar.com>',
                         'briandorsey@gmail.com',
                         "I'm your father.",
                         'message body',
                         True)
    print failed_addrs

                         

