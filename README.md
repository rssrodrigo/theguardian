# News The Guardian

![The Guardian](https://media-manager.noticiasaominuto.com/naom_5ae1d9b0e3b1e.jpg?&w=1920)

> Um script modularizado para buscar, através da API do jornal The Guardian, as últimas notícias e exportar para CSV os títulos e links das notícias de algumas categorias:

  - News
  - Sports
  - Arts

### Funções 

```sh
exportar_csv(titulo, link, nome)
buscar_noticias(dados)
buscar_sports(dados)
buscar_news(dados)
buscar_arts(dados)
```

### Execução
```sh
$ git clone https://github.com/rssrodrigo/theguardian.git
$ cd theguardian
$ pip install requests
$ pip install pandas
$ python news.py
```
### Comandos do GIT
```sh
$ git status
$ git add .
$ git commit -m "texto"
$ git pull --rebase origin master
$ git push origin master
```

### Desenvolvedor
> Rodrigo Santana
>>>>>>> Projeto que busca dados de noticias no the guardian
