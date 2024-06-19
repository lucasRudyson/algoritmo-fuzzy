


#variaveis de entrada
referencias_velocidade = {'medio':[10,25,40],'grave':[30,50,70],'gravissimo':[60,80,100]}

referencias_pontos= {'pequeno':[5,8],'medio':[5,8,12],'grande':[11,12]}
saida_pontos = {'pequeno':[0,7,15],'medio':[15,20,25],'grande':[25,30,40]}

#resultado da inferencia e agregação
inferencia = {'pequeno':[],'medio':[],'grande':[]}
agregar = {'pequeno':[],'medio':[],'grande':[]}




#graus de pertinencia
fuzificar_velocidade= {'medio':-1,'grave':-1,'gravissimo':-1}
fuzificar_ponto= {'pequeno':-1,'medio':-1,'grande':-1}

pertinencia_velocidade = {'medio':[],'grave':[],'gravissimo':[]}
pertinencia_pontos = {'pequeno':[],'medio':[],'grande':[]}


# saida = {'pequeno':,'medio','grave','gravissimo'}
velocidade_carro = int(input("Digite a velocidade do carro:"))
velocidade_via = int(input("velocidade da via:"))
n_pontos= int(input("quantidade de pontos da carteira:"))
velocidade_pocentagem = ((velocidade_carro - velocidade_via)/velocidade_via) * 100
if velocidade_pocentagem <= 0:
     print('não ultrapassou a velocidade')
     exit()
print(f"\nVelocidade ultrapassada:{velocidade_pocentagem}\n")


# inferência na entrada médio
if velocidade_pocentagem <= referencias_velocidade['medio'][0] or velocidade_pocentagem >= referencias_velocidade['medio'][2]:
    fuzificar_velocidade['medio'] = 0

elif referencias_velocidade['medio'][0] < velocidade_pocentagem <= referencias_velocidade['medio'][1]:
        resultado = (velocidade_pocentagem-referencias_velocidade['medio'][0])/ (referencias_velocidade['medio'][1]-referencias_velocidade['medio'][0])
        fuzificar_velocidade['medio']=  resultado

elif referencias_velocidade['medio'][1] < velocidade_pocentagem < referencias_velocidade['medio'][2]:
        resultado = (referencias_velocidade['medio'][2]-velocidade_pocentagem)/ (referencias_velocidade['medio'][2]-referencias_velocidade['medio'][1])
        fuzificar_velocidade['medio']= resultado

#inferencia na entrada grave

if velocidade_pocentagem <= referencias_velocidade['grave'][0] or velocidade_pocentagem >= referencias_velocidade['grave'][2]:
    fuzificar_velocidade['grave']= 0
elif referencias_velocidade['grave'][0] < velocidade_pocentagem <= referencias_velocidade['grave'][1]:
        resultado = (velocidade_pocentagem-referencias_velocidade['grave'][0])/ (referencias_velocidade['grave'][1]-referencias_velocidade['grave'][0])
        fuzificar_velocidade['grave']=  resultado
elif referencias_velocidade['grave'][1] < velocidade_pocentagem < referencias_velocidade['grave'][2]:
        resultado = (referencias_velocidade['grave'][2]-velocidade_pocentagem)/ (referencias_velocidade['grave'][2]-referencias_velocidade['grave'][1])
        fuzificar_velocidade['grave']= resultado
#inferência na  entrada gravissimo


if velocidade_pocentagem <= referencias_velocidade['gravissimo'][0] or velocidade_pocentagem >= referencias_velocidade['gravissimo'][2]:
    fuzificar_velocidade['gravissimo']= 0
elif referencias_velocidade['gravissimo'][0] < velocidade_pocentagem <= referencias_velocidade['gravissimo'][1]:
        resultado = (velocidade_pocentagem-referencias_velocidade['gravissimo'][0])/ (referencias_velocidade['gravissimo'][1]-referencias_velocidade['gravissimo'][0])
        fuzificar_velocidade['gravissimo']=  resultado
elif referencias_velocidade['gravissimo'][1] < velocidade_pocentagem < referencias_velocidade['gravissimo'][2]:
        resultado = (referencias_velocidade['gravissimo'][2]-velocidade_pocentagem)/ (referencias_velocidade['gravissimo'][2]-referencias_velocidade['gravissimo'][1])
        pertinencia_velocidade['gravissimo']= resultado




#pontos pequenos função z
if n_pontos <= referencias_pontos['pequeno'][0]:
    resultado = 1
    fuzificar_ponto['pequeno'] = resultado
elif referencias_pontos['pequeno'][0] < n_pontos < ((referencias_pontos['pequeno'][0]+referencias_pontos['pequeno'][1])/2):
    resultado = (1-(2*(((n_pontos - referencias_pontos['pequeno'][0])/(referencias_pontos['pequeno'][1]-referencias_pontos['pequeno'][0]))**2)))
    fuzificar_ponto['pequeno'] = resultado
elif ((referencias_pontos['pequeno'][0]+referencias_pontos['pequeno'][1])/2) <= n_pontos < referencias_pontos['pequeno'][1]:
    resultado =(2*(((n_pontos - referencias_pontos['pequeno'][0])/(referencias_pontos['pequeno'][1]-referencias_pontos['pequeno'][0]))**2))
    fuzificar_ponto['pequeno'] = resultado
elif n_pontos >= referencias_pontos['pequeno'][1]:
    resultado = 0
    fuzificar_ponto['pequeno'] = resultado

#pontos medios função triangular
if referencias_pontos['medio'][0] >= n_pontos <=referencias_pontos['medio'][1]:
    resultado = 0
    fuzificar_ponto['medio'] = resultado
elif referencias_pontos['medio'][0] < n_pontos <= referencias_pontos['medio'][1]:
    resultado = ((n_pontos-referencias_pontos['medio'][0])/(referencias_pontos['medio'][1]-referencias_pontos['medio'][0]))
    fuzificar_ponto['medio'] = resultado
elif referencias_pontos['medio'][1] < n_pontos < referencias_pontos['medio'][2]:
    resultado = ((referencias_pontos['medio'][2]-n_pontos)/(referencias_pontos['medio'][2]-referencias_pontos['medio'][1]))
    
    fuzificar_ponto['medio'] = resultado

#pontos grandes função -z
if n_pontos <= referencias_pontos['grande'][0]:
    resultado = 0
    fuzificar_ponto['grande'] = resultado
elif referencias_pontos['grande'][0] < n_pontos < ((referencias_pontos['grande'][0]+referencias_pontos['grande'][1])/2):
    resultado = (2*(((n_pontos - referencias_pontos['grande'][0])/(referencias_pontos['grande'][1]-referencias_pontos['grande'][0]))**2))
        
    fuzificar_ponto['grande'] = resultado
elif ((referencias_pontos['grande'][0]+referencias_pontos['grande'][1])/2) <= n_pontos < referencias_pontos['grande'][1]:
    resultado = (1-(2*(((n_pontos - referencias_pontos['grande'][0])/(referencias_pontos['grande'][1]-referencias_pontos['grande'][0]))**2)))
    fuzificar_ponto['grande'] = resultado
elif n_pontos >= referencias_pontos['grande'][1]:
    resultado = 1
    fuzificar_ponto['grande'] = resultado
######################################################## Inferencia #####################################################################################

#regra de inferência
if fuzificar_velocidade["medio"] > 0 and fuzificar_ponto["pequeno"]> 0:
    if fuzificar_velocidade["medio"] >= fuzificar_ponto["pequeno"]:
        inferencia['pequeno'].append(fuzificar_ponto['pequeno'])
    else:
        inferencia['pequeno'].append(fuzificar_velocidade['medio'])
         


if fuzificar_velocidade["grave"] > 0 and fuzificar_ponto["pequeno"]> 0:
    if fuzificar_velocidade["grave"] >= fuzificar_ponto["pequeno"]:
        inferencia['pequeno'].append(fuzificar_ponto['pequeno'])
    else:
        inferencia['pequeno'].append(fuzificar_velocidade['grave'])
         

if fuzificar_velocidade["gravissimo"] > 0 and fuzificar_ponto["pequeno"]> 0:
    if fuzificar_velocidade["gravissimo"] >= fuzificar_ponto["pequeno"]:
        inferencia['medio'].append(fuzificar_ponto['pequeno'])
    else:
        inferencia['medio'].append(fuzificar_velocidade['gravissimo'])
         





if fuzificar_velocidade["medio"] > 0 and fuzificar_ponto["medio"]> 0:
    if fuzificar_velocidade["medio"] >= fuzificar_ponto["medio"]:
        inferencia['pequeno'].append(fuzificar_ponto['medio'])
    else:
         inferencia['pequeno'].append(fuzificar_velocidade['medio'])



if fuzificar_velocidade["grave"] > 0 and fuzificar_ponto["medio"]> 0:
    if fuzificar_velocidade["grave"] >= fuzificar_ponto["medio"]:
        inferencia['medio'].append(fuzificar_ponto['medio'])
    else:
        inferencia['medio'].append(fuzificar_velocidade['grave'])
    

if fuzificar_velocidade["gravissimo"] > 0 and fuzificar_ponto["medio"]> 0:
    if fuzificar_velocidade["gravissimo"] >= fuzificar_ponto["medio"]:
        inferencia['grande'].append(fuzificar_ponto['medio'])
    else:
        inferencia['grande'].append(fuzificar_velocidade['gravissimo'])






if fuzificar_velocidade["medio"] > 0 and fuzificar_ponto["grande"]> 0:
    if fuzificar_velocidade["medio"] >= fuzificar_ponto["grande"]:
        inferencia['medio'].append(fuzificar_ponto['grande'])
    else:
        inferencia['medio'].append(fuzificar_velocidade['medio'])
    




if fuzificar_velocidade["grave"] > 0 and fuzificar_ponto["grande"]> 0:
    if fuzificar_velocidade["grave"] >= fuzificar_ponto["grande"]:
        inferencia['grande'].append(fuzificar_ponto['grave'])
    else:
        inferencia['grande'].append(fuzificar_velocidade['grave'])




if fuzificar_velocidade["gravissimo"] > 0 and fuzificar_ponto["grande"]> 0:
    if fuzificar_velocidade["gravissimo"] >= fuzificar_ponto["grande"]:
         inferencia['grande'].append(fuzificar_ponto['grande'])

    else:
        inferencia['grande'].append(fuzificar_velocidade['gravissimo'])
   
#####################################agregar##########################################
if len(inferencia['pequeno']) > 0:
    agregar['pequeno'] = max(inferencia['pequeno'])
else:
     agregar['pequeno'] = 0
if len(inferencia['medio']) > 0:
    agregar['medio'] = max(inferencia['medio'])
else:
    agregar['medio'] = 0
if len(inferencia['grande']) > 0: 
    agregar['grande'] = max(inferencia['grande'])
else:
    agregar['grande'] = 0

print("\nresultado da fuzificação velocidade",fuzificar_velocidade)
print("\nresultado da fuzificação ponto",fuzificar_ponto)
print("\ninferencia",inferencia)
print("\nagregrar",agregar)
######################################desfuzificar####################################
referencia_saida = [7,20,30]

somatorio = (agregar['pequeno']*referencia_saida[0])+(agregar['medio']*referencia_saida[1])+(agregar['grande']*referencia_saida[2])
somatorio = somatorio/(agregar['pequeno']+agregar['medio']+agregar['grande'])
print('=-'*50)
if somatorio <= 15:
     print(f'o resultado foi uma multa pequena e os pontos perdidos foram: {round(somatorio)}')
elif somatorio < 25:
     print(f'o resultado foi uma multa media e os pontos perdidos foram: {round(somatorio)}')
else:
     print(f'o resultado foi uma multa  e os pontos perdidos foram: {round(somatorio)}')
