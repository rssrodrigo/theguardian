import requests
import json
import pandas as pd
import decimal


def exportar_csv(cat, tit, lin, hor, nome):
        df = pd.DataFrame({'Categoria': cat, 'Título': tit, 'Link': lin, 'Hora': hor})
        df.to_csv("%s.csv" % nome, index=False, sep=";", encoding='utf-8-sig')
        print("")
        print("Arquivo *.csv exportado com sucesso, para a pasta do projeto!")   
        print("")


def buscar_tudo(dados):
        categoria = []
        hora = []
        titulo = []
        link = []

        for posicao in dados['response']['results']:
            print("Categoria:", posicao['pillarName'])
            print("Hora:", posicao['webPublicationDate'])
            print("Título:", posicao['webTitle'])
            print("Link: ", posicao['webUrl'])
            print("---------------------")

            categoria.append(posicao['pillarName'])
            hora.append(posicao['webPublicationDate'])
            titulo.append(posicao['webTitle'])
            link.append(posicao['webUrl'])
        exportar_csv(categoria, titulo, link, hora,"Tudo")    


def buscar_opinion(dados):
        categoria = []     
        hora = []
        titulo = []
        link = []

        for posicao in dados['response']['results']:
            if posicao['pillarName'] == 'Opinion':
                categoria.append(posicao['pillarName'])
                hora.append(posicao['webPublicationDate'])
                titulo.append(posicao['webTitle'])
                link.append(posicao['webUrl'])
        if len(titulo) == 0:
            print("Não há posts sobre Opiniões neste momento. Tente mais tarde, por favor!")
        else:
            exportar_csv(categoria, titulo, link, hora,"Opinião")


def buscar_sport(dados):
        categoria = []
        hora = []
        titulo = []
        link = []

        for posicao in dados['response']['results']:
            if posicao['pillarName'] == 'Sport':
                categoria.append(posicao['pillarName'])
                hora.append(posicao['webPublicationDate'])
                titulo.append(posicao['webTitle'])
                link.append(posicao['webUrl'])
        if len(titulo) == 0:
            print("Não há posts sobre Esportes neste momento. Tente mais tarde, por favor!")
        else:   
            exportar_csv(categoria, titulo, link, hora,"Esportes")    


def buscar_news(dados):
        categoria = []
        hora = []
        titulo = []
        link = []

        for posicao in dados['response']['results']:
            if posicao['pillarName'] == 'News':
                categoria.append(posicao['pillarName'])
                hora.append(posicao['webPublicationDate'])
                titulo.append(posicao['webTitle'])
                link.append(posicao['webUrl'])
        if len(titulo) == 0:
            print("Não há posts sobre News neste momento. Tente mais tarde, por favor!")
        else:
            exportar_csv(categoria, titulo, link, hora,"Notícias")


def buscar_arts(dados):
        categoria = []
        hora = []
        titulo = []
        link = []

        for posicao in dados['response']['results']:
            if posicao['pillarName'] == 'Arts':
                categoria.append(posicao['pillarName'])
                hora.append(posicao['webPublicationDate'])
                titulo.append(posicao['webTitle'])
                link.append(posicao['webUrl'])
        if len(titulo) == 0:
            print("Não há posts sobre Artes neste momento. Tente mais tarde, por favor!")
        else:
            exportar_csv(categoria, titulo, link, hora,"Artes")



def main():
    # THE GUARDIAN
    # Objetivo: criação um programa que consume a API do jornal The Guardian, mostrando o título e o link das notícas do dia: https://open-plataform.theguardian.com/ tomando cuidado para o email de informação da API não ir para a caixa de spam

    print("")
    print("")
    print("### THE GUARDIAN ###")
    print("")

    url = "https://content.guardianapis.com/search?api-key=4c7a42c5-c217-4ab1-854f-efc9697324f2"

    response = requests.get(url)

    if response.status_code == 200:
        
        print("Acessando base de dados do The Guardian...")
        print("")
        print("NOTÍCIAS RECENTES:")
        print("")
        print("---------------------")  

        dados = response.json()
        buscar_tudo(dados)
        buscar_opinion(dados)
        buscar_sport(dados)
        buscar_news(dados)
        buscar_arts(dados) 
        
    else:
        print("Não foi possível acessar a base de dados do The Guardian!")

if _name_ == "_main_":
    main()

print("Fim!")