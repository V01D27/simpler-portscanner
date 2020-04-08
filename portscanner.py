import socket
#
def istoffen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(1)
      print("port", ran,"Offen")
   except:
      print("port", ran,"Zu")
#ip und port von User
ip = input("Ip: ")

#für die for schleife
von = (int(input("Von: ")))
bis = (int(input("Bis: ")))
bis = ((bis) + 1)
#for schleife
for ran in range((von), (bis)):
    # print(port)
    istoffen(ip, ran)