# Programa para calcular IMC - MASM 2020
import webbrowser

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Apresentação do Programa
print()
print('          CALCULADORA IMC - MASM 2020')
print('   ******************************************')
print('   *                                        *')
print('   *   III   MMM       MMM    CCCCCCCCC     *')
print('   *   III   MMMMMM  MMMMM   CCCCCCCCCCC    *')
print('   *   III   MMM MM MM MMM  CCCC            *')
print('   *   III   MMM  MMM  MMM   CCCC           *')
print('   *   III   MMM       MMM    CCCCCCCCCC    *')
print('   *   III   MMM       MMM     CCCCCCCC     *')
print('   *                                        *')
print('   ******************************************')
print()
print()
print()
print('Seja bem vindo ao programa de Cálculo de IMC')
print()
print('Inserindo dados de identificação, peso e altura você receberá o valor e sua classificação de IMC...')
print()
print('Para mais informações sobre IMC consulte:')
print('https://www.who.int/data/gho/data/themes/theme-details/GHO/body-mass-index-(bmi)')
site = input('Para abrir o site clique na tecla Y. Se não quiser clique em qualquer tecla para continuar:   '
             '')
if (site == 'y'):
    webbrowser.open('https://www.who.int/data/gho/data/themes/theme-details/GHO/body-mass-index-(bmi)')
else:
    print()
input('Clique em qualquer tecla para continuar....')
print()
print()

# Entrada de dados de Identificação
print('Por favor, entre com seus dados abaixo:')
nome = input('Digite seu primeiro nome: ')
sobrenome = input('Digite seu Sobrenome: ')
sexo = input('Digite o seu sexo - masculino (m) ou feminino (f): ')
print()
print()

# Entrada de dados biometricos
txt1 = 'Olá, ' + nome + ' ' + sobrenome + ' muito obrigado pelas informações!'
txt2 = 'Por favor insira os valores de peso (kg) e altura (m) abaixo:'
print(txt1)
print(txt2)
peso = eval(input('Digite o seu peso (kg): '))
altura = eval(input('Digite a sua altura (m): '))
print()

# Cálculo do IMC com arredondamento em 2 casas
imc = round((peso / altura ** 2), 2)

# Definição do Nível baseado no IMC calculado
if (imc < 19):
    status = 'desnutrido'
elif (imc > 19 and imc < 25):
    status = 'normal'
elif (imc > 25 and imc < 30):
    status = 'sobrepeso'
else:
    status = 'obeso'

# Estimativa de redução ou aumento de peso
if (status == 'sobrepeso' or status == 'obeso'):
    pesodif = round(peso - (24.9 * (altura ** 2)), 2)
elif (status == 'desnutrido'):
    pesodif = round((20 * (altura ** 2)) - peso, 2)
else:
    pesodif = 0

# Classificação de redução ou aumento de peso
if (status == 'sobrepeso' or status == 'obeso'):
    tipo = 'perca'
elif (status == 'desnutrido'):
    tipo = 'ganhe'
else:
    tipo = 'perca'

# Peso ideal
if (sexo == 'm'):
    pesoid = round(((72.7 * altura) - 58), 2)
elif (sexo == 'f'):
    pesoid = round(((62.1 * altura) - 44.7), 2)
else:
    print()

# Diferença - Peso ideal
difp = round((peso - pesoid), 2)

# Resultado
input('Clique em qualquer tecla para obter o resultado')
print()
print('*********************************************************************************')
txt6 = 'Muito obrigado por usar a Calculadora de IMC, ' + nome + ' ' + sobrenome + '!'
print()
print(nome + ' o seu IMC é ' + color.RED + str(imc) + color.END + ' e você está classificado como: ' + color.RED + status + color.END)
print('É recomendável que você ' + tipo + ' ' + color.RED + str(pesodif) + color.END + ' kg para chegar ao nível normal do IMC.')
print('Seu peso ideal é ' + color.BLUE + str(pesoid) + color.END + ' kg. Para chegar nele é preciso que você ' + tipo + ' ' + color.RED + str(difp) + color.END + ' kg')
print()
print('*********************************************************************************')
print(txt6)

# Mensagens finais
print(color.GREEN + 'Valores apenas para referência!' + color.END)
print(color.PURPLE + 'Consulte sempre um médico e nutricionista!' + color.END)
print()
print('*********************************************************************************')
print()
print(color.BLUE + 'MASM 2020 - Todos os direitos reservados'+ color.END)
print('marcos.molnar@gmail.com')
