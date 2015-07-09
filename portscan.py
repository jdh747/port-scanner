__author__ = 'joshuahayes'

import socket
import datetime

def main():
    # host = socket.gethostbyname(socket.gethostname())         # local host
    host = 'http://scanme.nmap.org/'
    openports = []

    start_time = last_time = current_time = datetime.datetime.now()
    print('\nScanning', host, 'Ports...')
    print('-'*60)

    for port in range(90):                                   # max 16-bit ports
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.connect((host, port))
        except socket.error as error:
            pass
        else:
            openports.append(port)

        current_time = datetime.datetime.now()
        if (current_time - last_time).seconds > 30:
            print('Still Working, Port:', port, 'of 65,535')
            last_time = current_time

        s.close()

    for port in openports:
        print('Port', port, 'Open')

    print('-'*60, '\n', 'Completed In(hh:mm:ss:us): ', current_time-start_time, sep='')

if __name__ == '__main__':
    main()
