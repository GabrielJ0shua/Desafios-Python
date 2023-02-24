menu = '''
1 - Depositar
2 - Sacar
3 - Consultar
4 - Sair
'''
c = 0.00
lim = 500.00
saque = 3

while(True):
  print(menu)
  opc = input()

  if(opc == '1'):
    v = float(input('Quanto quer depositar?\n'))

    if(v > 0): c+=v
    
  elif(opc == '2'):
    if(saque == 0 or lim == 0):
      print("Opção indisponivel, limite de saque atingido ou valor retirado.")
    else:
      v = float(input('Quanto quer sacar?\n'))
  
      if(v < c): 
        c-=v
        lim-=v
        saque-=1
      else: print("Valor inválido.")
    
  elif(opc == '3'): 
    print(f"R$ {c}")
  elif(opc == '4'): break
  else: print("Inválido")

print("Fechando aplicação.")