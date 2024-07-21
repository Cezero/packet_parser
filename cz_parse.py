#
# Script for reading network stream from PCAP recording and attempting to parse Everquest AA data
#
import sys
from lib.util import *
from lib.eqreader import *
import xmltodict

EQ64Bit = True
 
def handleEQPacket(opcode, bytes, timeStamp, clientToServer, clientPort):
	if clientToServer is True:
		print(f'opcode: {opcode} From EQ Client -> Server')
	else:
		print(f'opcode: {opcode} From EQ Server -> Client')

  # print 16 bytes per line
	width = 16
	for i in range(0, len(bytes), width):
		b = bytes[i:i+width]
		hex_str = ' '.join(f'{byte:02X}' for byte in b)
		ascii_str = ''
		for byte in b:
			if 32 <= byte < 128:
				ascii_str = ascii_str + chr(byte)
			else:
				ascii_str = ascii_str + '.'
		print(f'{hex_str} {ascii_str}')

def main(args):
  if (len(args) < 1):
    print ('Usage: ' + args[0] + ' <pcap file>')

  print('Reading %s' % args[1])
  readPcap(handleEQPacket, args[1])

main(sys.argv)
