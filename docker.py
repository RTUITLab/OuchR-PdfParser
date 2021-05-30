import os
import subprocess

# def runCont(image):
#
#     t = ""
#     with open('docker-compose.yml', 'r',  encoding='utf-') as dock:
#         t = dock.read().replace("shureck/userback", image)
#     with open('docker-compose.yml', 'w', encoding='cp1251') as token:
#         token.write(t)
#
#     process = subprocess.Popen(['docker-compose', 'up', '--build'],
#                                stdout=subprocess.PIPE,
#                                universal_newlines=True)
#     output = ""
#     while True:
#         output += process.stdout.readline()
#         print(output.strip())
#         # Do something else
#         if "Test request" in output and "Test secret" in output:
#             stream = os.popen(chr(3))
#             output = ""
#             output += stream.readline()
#             print(output)
#
#             t = ""
#             with open('docker-compose.yml', 'r') as dock:
#                 t = dock.read().replace(image, "shureck/userback")
#             with open('docker-compose.yml', 'w') as token:
#                 token.write(t)
#             return True
#
#         if "pdfapi_localback_1 exited with code 0" in output:
#             stream = os.popen(chr(3))
#             output = ""
#             output += stream.readline()
#             print(output)
#
#             t = ""
#             with open('docker-compose.yml', 'r') as dock:
#                 t = dock.read().replace(image, "shureck/userback")
#             with open('docker-compose.yml', 'w') as token:
#                 token.write(t)
#             return False

# runCont("shureck/userback")