from Data import Data

while(True):
    try:
        dia = int(input('Dia: '))
        mes = int(input('Mês: '))
        ano = int(input('Ano '))

        # teste = [ 1,2,3]
        # print(teste[10])
        x = 10/0
        

        data1 = Data(dia, mes, ano)
    except ValueError:
        print('Erro na digitação do dia, mes ou ano')
        continue
    except AssertionError as ae:
        print(ae)
        continue
    except Exception as e:
        print('O sistema esta instavel. Nossos desenvolvedores vao corrigir em pouco tempo')
        print(e.__class__.__name__)
        exit()

    break



try:
    print('Testando getters and setters')
    data1.get_dia()
    dia = int(input('Dia:'))
    data1.set_dia(dia)
    data1.get_mes()
    mes = int(input('Mes:'))
    data1.set_mes(mes)
    data1.get_ano()
    ano = int(input('Ano:'))
    data1.set_ano(ano)
except AssertionError as ae:
    print(ae)


print('Impressão da data: ', data1)