import keyring as kr
import keyring.util.platform_;
import os

#VERIFICA SENHA E GRUPO ESPECIFICO
cred = kr.get_credential("servico","svc_telecom")
  
print(cred) 
  
print("Username : ",cred.username)
print("Password : ",cred.password)

senha = cred.password

print(senha)

#VERIFICA TODAS AS SENHAS NO LOCAL ARMAZENADO
#print(keyring.util.platform_.data_root())
#os.system('cat /home/backup/.local/share/python_keyring/keyring_pass.cfg')