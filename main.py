velocidade_carro = int(input("Digite a velocida do carro:"))
velocidade_via = int(input("Digite a velocida do via:"))
velocidade_entrada = ((velocidade_carro-velocidade_via)/velocidade_via)*100
if velocidade_entrada <= 10:
    print(f" {velocidade_entrada}% ultrapassado então {velocidade_carro}km entra na velocidade aceita na via")
    exit()

pontos_entrada = int(input("Digite a quantidade de pontos existente na carteira:"))

# graus de entradas e saidsa
velocidade_referencia = {'medio':[10,25,40],'grave':[30,50,70],'gravissimo':[60,80,100]}
pontos_referencia = {'pequeno':[5,8],'medio':[5,9,11],'alto':[11,12]}
#
pertinencia_velocidade = {'medio':0,'grave':0,'gravissimo':0}
pertinencia_pontos = {'pequeno':0,'medio':0,'alto':0}
fuzificacao = {'pequeno':[],'medio':[], 'alto':[]}


def pertinencias_velocidade():
    #medio
    if  velocidade_referencia['medio'][0] < velocidade_entrada > velocidade_referencia['medio'][2]:
        resultado = 0
    if velocidade_referencia[0] < velocidade_entrada <= velocidade_referencia['medio'][1]:
        resultado = ((velocidade_entrada-velocidade_referencia['medio'][0])/(velocidade_referencia['medio'][1]-velocidade_referencia['medio'][0]))
    if velocidade_referencia[1] < velocidade_entrada <= velocidade_referencia['medio'][2]:
        resultado = ((velocidade_referencia['medio'][2]-velocidade_entrada)/(velocidade_referencia['medio'][2]-velocidade_referencia['medio'][1]))
    pertinencia_velocidade['medio'].append(resultado)
    #grave
    if  velocidade_referencia['grave'][0] < velocidade_entrada > velocidade_referencia['grave'][2]:
        resultado = 0
    if velocidade_referencia[0] < velocidade_entrada <= velocidade_referencia['grave'][1]:
        resultado = ((velocidade_entrada-velocidade_referencia['grave'][0])/(velocidade_referencia['grave'][1]-velocidade_referencia['grave'][0]))
    if velocidade_referencia[1] < velocidade_entrada <= velocidade_referencia['grave'][2]:
        resultado = ((velocidade_referencia['grave'][2]-velocidade_entrada)/(velocidade_referencia['grave'][2]-velocidade_referencia['grave'][1]))
    pertinencia_velocidade['grave'].append(resultado)
    #gravissimo
    if  velocidade_referencia['gravissimo'][0] < velocidade_entrada > velocidade_referencia['gravissimo'][2]:
        resultado = 0
    if velocidade_referencia[0] < velocidade_entrada <= velocidade_referencia['gravissimo'][1]:
        resultado = ((velocidade_entrada-velocidade_referencia['gravissimo'][0])/(velocidade_referencia['gravissimo'][1]-velocidade_referencia['gravissimo'][0]))
    if velocidade_referencia[1] < velocidade_entrada <= velocidade_referencia['gravissimo'][2]:
        resultado = ((velocidade_referencia['gravissimo'][2]-velocidade_entrada)/(velocidade_referencia['gravissimo'][2]-velocidade_referencia['gravissimo'][1]))
    pertinencia_velocidade['gravissimo'].append(resultado)



def pertinencias_pontos():
    #pequeno
    if pontos_entrada <= pontos_referencia['pequeno'][0]:
        resultado = 1
    if pontos_referencia['pequeno'][0] < pontos_entrada < ((pontos_referencia['pequeno'][0]+pontos_referencia['pequeno'][1])/2):
        resultado = 1 - 2((pontos_entrada - pontos_referencia['pequeno'][0])/(pontos_referencia['pequeno'][1]-pontos_referencia['pequeno'][0]))**2
    if ((pontos_referencia['pequeno'][0]+pontos_referencia['pequeno'][1])/2)  <= pontos_entrada < pontos_referencia['pequeno'][1]:
        resultado = 2((pontos_referencia['pequeno'][1]-pontos_entrada)/(pontos_referencia['pequeno'][1]-pontos_referencia['pequeno'][0]))**2
    if pontos_entrada >= pontos_referencia['pequeno'][1]:
        resultado = 0
    
    pertinencia_pontos['pequeno'].append(resultado)
    #medio
    if  velocidade_referencia['medio'][0] < velocidade_entrada > velocidade_referencia['medio'][2]:
        resultado = 0
    if velocidade_referencia[0] < velocidade_entrada <= velocidade_referencia['medio'][1]:
        resultado = ((velocidade_entrada-velocidade_referencia['medio'][0])/(velocidade_referencia['medio'][1]-velocidade_referencia['medio'][0]))
    if velocidade_referencia[1] < velocidade_entrada <= velocidade_referencia['medio'][2]:
        resultado = ((velocidade_referencia['medio'][2]-velocidade_entrada)/(velocidade_referencia['medio'][2]-velocidade_referencia['medio'][1]))
    pertinencia_pontos['medio'].append(resultado)
   
    #alto 
    if pontos_entrada <= pontos_referencia['pequeno'][0]:
        resultado = 0
    if pontos_referencia['pequeno'][0] < pontos_entrada <= ((pontos_referencia['pequeno'][0]+pontos_referencia['pequeno'][1])/2):
        resultado = 2((pontos_entrada - pontos_referencia['pequeno'][0])/(pontos_referencia['pequeno'][1]-pontos_referencia['pequeno'][0]))**2
    if ((pontos_referencia['pequeno'][0]+pontos_referencia['pequeno'][1])/2)  <= pontos_entrada < pontos_referencia['pequeno'][1]:
        resultado = 1- 2((pontos_referencia['pequeno'][1]-pontos_entrada)/(pontos_referencia['pequeno'][1]-pontos_referencia['pequeno'][0]))**2
    if pontos_entrada >= pontos_referencia['pequeno'][1]:
        resultado = 0
    pertinencia_pontos['alto'].append(resultado)

## regras de fuzzy
def regrasfuzzy():
    if pertinencia_velocidade['medio'][0] > 0 and pertinencia_pontos['pequno'][0]:
        if pertinencias_pontos['medio'][0] > pertinencias_pontos['pequeno'][0]:
            

## inferencia
## desfuzificação