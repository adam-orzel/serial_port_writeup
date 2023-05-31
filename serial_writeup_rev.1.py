import serial
import time
port_number = input('COM Port:')
baud = input('baud rate(9600, 115200, etc...):')
com_port = 'COM'f'{port_number}'
ser = serial.Serial(com_port , baud, timeout=1, xonxoff=True, rtscts=True, dsrdtr=True)
ser.set_buffer_size(rx_size = 12800, tx_size = 12800)
message = f'Reading off of {ser.name} please wait this may take a moment...'
print(message)

ser.reset_input_buffer()

ser.write(b'\r\n')
ser.write(b'enable\n')
time.sleep(2)
login = b''
login += ser.read_all()
prompt = login.decode('utf-8')
while True:
    if 'Password:' in prompt:
        password = input('Provide enable secret password:')
        ser.write(password.encode('utf-8') + b'\n')
        break
    if 'Switch#' in prompt:
        print('No password required:')
        time.sleep(2)
        break
    else:
        print('failure to login')
        time.sleep(5)
        break

#b indicates bytes, treated as a sequences of bytes instead of a string.
ser.write(b'terminal length 0\n')           
#sets terminal to display without any breaks
ser.write(b'show version\n')
ser.write(b'show run\n')                    
#\n simulates "enter" key and \r returns cursor to the beginning.
time.sleep(1)

output = b''
output += ser.read_all()
output = output.decode('utf-8')             #decode"utf-8" converts unicode string to utf-8 encoding 

print(output)