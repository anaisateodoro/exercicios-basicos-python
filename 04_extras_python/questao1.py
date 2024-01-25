"""1)Faça um programa, com uma função que necessite de três argumentos, 
e que forneça a soma desses três argumentos."""

print('\nTotal de Episódios Assistidos - Séries de TV\n')

def soma_episodios(stranger_things, vincenzo , the_good_fight ):
    total_episodios = stranger_things + vincenzo  + the_good_fight 
    print(f'\nParabéns! Você assistiu até o momento {total_episodios} episódios.')

stranger_things = int(input('\nDigite a quantidade de episódios que você assistiu na série Stranger Things: '))
vincenzo  = int(input('\nDigite a quantidade de episódios que você assistiu a série Vincenzo: '))
the_good_fight  = int(input('\nDigite a quantidade de episódios que você assistiu na série The Good Fight: '))

soma_episodios(stranger_things, vincenzo , the_good_fight )


