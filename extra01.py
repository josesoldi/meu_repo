class Pessoa:
  def __init__(self):
    self.comendo = False 
    self.falando = False
  
  def interromper_fala(self):
    self.falando = False
    print ('A pessoa parou de falar')

  def interromper_comer(self):
    self.comendo = False
    print ('A pessoa parou de comer')

  def comer(self):
    if self.falando:
      print('Erro: a pessoa não pode comer enquanto fala')
    else:
      self.comendo = True
      print('A pessoa está comendo')

  def falar(self, assunto):
    if self.comendo:
      print('Erro: a pessoa não pode falar enquanto come')
    else:
      self.falando = True
      print(f"A pessoa está falando sobre: {assunto}")
