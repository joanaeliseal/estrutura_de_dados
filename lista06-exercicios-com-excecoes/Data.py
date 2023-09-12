class Data:
   __validacao = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
   def __init__(self, dia:int, mes:int, ano:int):
       assert ano > 0,'Ano invalido. O ano tem que ser maior do que zero.'
       assert mes >=1 and mes <=12, 'Mes invalido. O mes deve ser um numero entre 1 e 12.'
       assert dia >=1 and dia <= Data.__validacao[mes],f'Dia invalido para o mes {mes}'

       self.__dia = dia
       self.__mes = mes
       self.__ano = ano


   def __str__(self):
       return f'{self.__dia}/{self.__mes}/{self.__ano}'


   def get_dia(self):
       return self.__dia


   def get_mes(self):
       return self.__mes


   def get_ano(self):
       return self.__ano


   def set_dia(self, dia:1):
       assert dia >=1 and dia <= Data.__validacao[self.__mes],f'Dia invalido para o mes {self.__mes}'
       self.__dia = dia


   def set_mes(self, mes):
       assert mes >=1 and mes <=12, 'Mes invalido. O mes deve ser um numero entre 1 e 12.'
       assert self.__dia <= Data.__validacao[mes],f'O dia {self.__dia} embutido na data não é valido par ao mes {mes}'
       self.__mes = mes


   def set_ano(self, ano):
       assert ano > 0,'Ano invalido. O ano tem que ser maior do que zero.'
       self.__ano = ano




