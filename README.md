# SiteSweep

Uma ferramenta de segurança para fazer uma varredura simples.

## Introdução
O SiteSweep é uma ferramenta que ajuda a identificar vulnerabilidades e diretórios não anexados.

`ACHO IMPORTANTE DESTACAR QUE O TUTORIAL DE INSTALAÇÃO FOI FEITO PARA O SISTEMA OPERACIONAL LINUX`

## Instalação
para instalar o SiteSweep execute os seguintes comandos:

```
pkg install python3 -y

pkg install git -y

git clone https://github.com/admfmind/SiteSweep

cd SiteSweep

pip install -r requirements.txt
```

## Funcionalidades
- Identificar vunerabilidade xss
- Fornecer relatorio sobre as vunerabilidades
- Mapear diretoreos

## Exemplo de uso
```py
from sitesweep import Scopo

"""
o cabeçalho da requisicao dessa ferramenta foi alterado.
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3
Cache-Control: max-age=6000
"""

# BUSCAR XSS
site = Scopo('http://exemplo.com/', 'exemplo.com')
site.buscar_xss()
print(site)

# BISCAR LINKS E DIRETÓRIOS NO HTML
site = Scopo('http://exemplo.com/', 'exemplo.com')
site.buscar_diretorios()
print(site)

# FORÇAR DIRETORIOS
"""
Você pode utilizar os 340 diretórios pré-definidos ou
utilizar seu arquivo de preferencia.
Ao chamar a função forcar_dirrtorio()

Para usar os diretorios da ferramenta chame a função desse modo: forcar_dirrtorio(None)
Para usar seis dirrtorios colowuebo nome do arquivo na função: forcar_diretorio('exemplo.txt')
"""
site = Scopo('http://exemplo.com/', 'exemplo.com')
site.forcar_diretorio(None)
print(site)

# GERAR RELATÓRIO

# em .txt
site.gerar_relatorio('txt')
# em .json
site.gerar_relatorio('json')

# FAZER VERIFICAÇÃO COMPLETA
"""
Esta função utiliza todas as outras de uma vez.

1° parâmetro: objeto Scopo
2° parâmetro desta função: recebe o nome do arquivo com os nomes dos diretorios. ele deve receber esse nome como uma string, caso queira usar os diretórios da ferramenta, utilize como parametros o None
Para usar seu arquivo: geral('exemplo.txt')
Para usar os da ferramenta: geral(None)
"""
site = Scopo('http://exemplo.com/', 'exemplo.com')
site.geral(None)
print(site)

```

## Como funciona
`Busca de diretorios no html:` É filtrado por meio da biblioteca __bs4__ todo o conteudo da tag __href__ de todo o html. Alem de diretórios, também é possível achar links, por isso ao utilizar essa função ele registra esses links nos dados.

`Forçar diretios:` Apos a requisição utilizando o diretorio (http://exemplo.com/diretorio), é analizado o codigo da resposta, se o código for entre 200 e 299, sera retornado como um diretório veridico(que existe) no site, mas caso seja entre 300 e 399 ira retornar como diretório redirecionado(diretorio não existe). Outros tipos de código de resposta não são registrados.

`Verificação da existência de XSS:` É feito uma análise no código html. Se existe um formulário(form), sera salvo todos os conteúdos das tag's __action__ deles e depois o conteudo das entradas de dados(input) da tag __name__, apos isso ser afeita requisições utilizando as tag's action como diretório e sera enviado via post para o input um código js, se o código js tiver presente no html da resposta da requisição, sera salvo como vulnerabilidade encontrada.

## Contribuição
Para contribuir com o SiteSweep envie um `pull request` para o repositorio do git GitHub.

## Licença
o SiteSweep é distribuido pela licença CC BY-NC 4.0.

