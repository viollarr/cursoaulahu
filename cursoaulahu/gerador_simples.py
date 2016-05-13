def f():
    print('Iniciando')
    yield 1
    print('No meio da função')
    yield 2
    print('Finalizando')


gerador = f()
print(gerador)
print(next(gerador))
print(next(gerador))
print(next(gerador))
