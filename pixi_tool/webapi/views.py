from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from paramiko import SSHClient, AutoAddPolicy

class LinuxCommandView(APIView):
    def post(self, request, format = None):
        # Extract data from request
        server_address = request.data.get('server_address')
        username = request.data.get('username')
        password = request.data.get('password')
        command = request.data.get('command')

        if not all([server_address, username, password, command]):
            return Response({'error': 'Missing required parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Connect to the Linux server
            ssh = SSHClient()
            ssh.set_missing_host_key_policy(AutoAddPolicy())
            ssh.connect(server_address, username=username, password=password)

            # Execute the command
            stdin, stdout, stderr = ssh.exec_command(command)

            # Read the output
            output = stdout.read().decode('utf-8')

            # Close the SSH connection
            ssh.close()

            return Response({'output': output})

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
