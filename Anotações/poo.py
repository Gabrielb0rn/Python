pessoas = []

class Pessoa:
  def __init__(self, nome: str, idade: int, altura: float):
    self.nome = nome
    self.idade = idade
    self.altura = altura

  def dizer_ola(self):
    print(f'Olá, meu nome é {self.nome}. Tenho {self.idade} '
          f'anos e minha altura é {self.altura}m.')

  def cozinhar(self, receita: str):
    print(f'Estou cozinhando um(a): {receita}')

  def andar(self, distancia: float):
    print(f'Saí para andar. Volto quando completar {distancia} metros')


novaPessoa = Pessoa(nome='Oberti', idade=28, altura=1.75)

novaPessoa.dizer_ola()
novaPessoa.cozinhar('rabada')
novaPessoa.andar(10.5)

# dados = str(f'Nome: {novaPessoa.nome}\nIdade: {novaPessoa.idade}\nAltura: {novaPessoa.altura}')
# print(dados)