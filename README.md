#SiteSweep

Uma ferramenta de segurança para fazer uma varredura simples

##Introdução
O SiteSweep é uma ferramenta que ajuda a identificar vulnerabilidades e diretórios não anexados

`ACHO IMPORTANTE DESTACAR QUE O TUTORIAL DE INSTALAÇÃO E EXECUÇÃO FOI FEITO PARA O SISTEMA OPERACIONAL LINUX`

##Instalação
para instalar o SiteSweep execute os seguintes comandos:

```
pkg install python3 -y

pkg install git -y

git clone https://github.com/admfmind/SiteSweep

cd SiteSweep

pip install -r requirements.txt
```

##Funcionalidades
- Identificar vunerabilidade xss
- Fornecer relatorio sobre as vunerabilidades
- Mapear diretoreos

##Exemplo de uso
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

Esta função recebe o nome do arquivo que sera esta com os nomes do diretorios. ela deve receber esse nome como uma string, caso queira usar os diretórios da ferramenta, utilize como parametros o None
Para usar seu arquivo: geral('exemplo.txt')
Para usar os da ferramenta: geral(None)
"""
site = Scopo('http://exemplo.com/', 'exemplo.com')
site.geral(None)
print(site)

```

##Contribuição
Para contribuir com o SiteSweep envie um `pull request` para o repositorio do git GitHub

##Licença
o SiteSweep é distribuido pela licença CC BY-NC 4.0

