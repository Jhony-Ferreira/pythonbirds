class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=32):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_clsse(cls):
        return f'{cls} - olhos: {cls.olhos}'


if __name__ == '__main__':
    jhony = Pessoa(nome='Jhony')
    zegrilo = Pessoa(jhony, nome='zegrilo')
    print(Pessoa.cumprimentar(zegrilo))
    print(id(zegrilo))
    print(zegrilo.cumprimentar())
    print(zegrilo.nome)
    print(zegrilo.idade)
    for filho in zegrilo.filhos:
        print(filho.nome)
    # print(zegrilo.filhos)  imprime o nome da classe seguido do objeto ID e não o atributo filhos dentro do objeto
    zegrilo.sobrenome = 'Ferreira'
    del zegrilo.filhos
    zegrilo.olhos = 1
    del zegrilo.olhos
    print(zegrilo.sobrenome)
    print(zegrilo.__dict__)
    print(jhony.__dict__)
    print(Pessoa.olhos)
    print(jhony.olhos)
    print(zegrilo.olhos)
    print(Pessoa.metodo_estatico(), zegrilo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_clsse(), zegrilo.nome_e_atributos_de_clsse())
