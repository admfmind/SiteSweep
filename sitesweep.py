import socket
from time import sleep
from os import system
import requests
from bs4 import BeautifulSoup as BS

def clear():
    try: system('clear')
    except: pass

def titulo():
    clear()
    print('''
SITE
SWEEP


 .oooooo..o ooooo ooooooooooooo oooooooooooo
d8P'    `Y8 `888' 8'   888   `8 `888'     `8
Y88bo.       888       888       888
 `"Y8888o.   888       888       888oooo8
     `"Y88b  888       888       888    "
oo     .d8P  888       888       888       o
8""88888P'  o888o     o888o     o888ooooood8

 .oooooo..o oooooo   oooooo     oooo oooooooooooo oooooooooooo ooooooooo.
d8P'    `Y8  `888.    `888.     .8'  `888'     `8 `888'     `8 `888   `Y88.
Y88bo.        `888.   .8888.   .8'    888          888          888   .d88'
 `"Y8888o.     `888  .8'`888. .8'     888oooo8     888oooo8     888ooo88P'
     `"Y88b     `888.8'  `888.8'      888    "     888    "     888
oo     .d8P      `888'    `888'       888       o  888       o  888
8""88888P'        `8'      `8'       o888ooooood8 o888ooooood8 o888o


''')

def cor(opcao):
    if opcao == 1:
        return '\033[31m' # vernelho
    elif opcao == 2:
        return '\033[32m' # verde
    elif opcao == 3:
        return '\033[33m' # amarelo
    else:
        return '\033[m'

def carregar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def salvar_arquivo(nome_arquivo, novo_dado):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(novo_dado)
    print(f'\n[+] arquivo {nome_arquivo} salvo')

class Scopo:
    def __init__(self, url, host):
        # configuração de requisição
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Cache-Control': 'max-age=6000'
        }
        # dados armazenados
        self.url = url.strip()
        self.requisicao = requests.get(url, headers=self.headers, allow_redirects=False)
        # obter servidor
        try:
            self.servidor = self.requisicao.headers.get('Server')
            if self.servidor == None:
                self.servidor = ''
        except:
            self.servidor = ''
        # obter IP
        try:
            if socket.gethostbyname(host) == '0.0.0.0':
                self.ip = ''
            else:
                self.ip = socket.gethostbyname(host)
        except:
            self.ip = ''
        self.links = []
        self.diretorios_aparentes = []
        self.diretorios_ocultos = []
        # vunerabilidade
        self.injecao_js = []

    def __str__(self):
        titulo()

        links = ''
        for link in self.links:
            links += f'\n    {link}'

        diretorios = ''
        for diretorio in self.diretorios_aparentes:
            diretorios += f'\n    {self.url}{diretorio}'

        diretorios_bruto = ''
        for diretorio in self.diretorios_ocultos:
            diretorios_bruto += f'\n    {cor(3)}[{diretorio:^15}] {cor(1)}{self.url}{diretorio}{cor(2)}'

        xss = ''
        for injecao in self.injecao_js:
            injecao = injecao.replace('\n', '\n    ')
            xss += f'\n\n    {cor(3)}{injecao}{cor(1)}'

        return f'''{cor(1)}
URL_____________________________________| \n    {cor(3)}{self.url}{cor(1)}

SERVIDOR________________________________| \n    {cor(3)}{self.servidor}{cor(1)}

IP______________________________________| \n    {cor(3)}{self.ip}{cor(1)}

LINKS DO HTML___________________________| {cor(3)}{links}{cor(1)}

DIRETORIOS______________________________| {cor(3)}{diretorios}{cor(1)}

DIRETORIOS ENCONTRADOS COM FORÇA BRUTA__| {cor(3)}{diretorios_bruto}{cor(1)}

INJEÇÃO DE JAVA SCRIPT__________________| {cor(3)}{xss}
{cor(0)}'''

    def buscar_servidor(self):
        headers = self.requisicao.headers
        try:
            self.servidor = headers['Server']
        except KeyError:
            pass

    def buscar_diretorios(self):
        html = self.requisicao.text
        sopa_html = BS(self.requisicao.content, 'html.parser')
        tags_a = sopa_html.find_all("a", href=True)
        tags_href = [href.get("href") for href in tags_a]
        for tag_href in tags_href:
            if 'http' in tag_href or 'www.' in tag_href:
                self.links.append(tag_href)
            else:
                self.diretorios_aparentes.append(tag_href)

    def forca_diretorio(self, nome_arquivo):
        if nome_arquivo == None:
            diretorios = ["admin","admins","sobre","conta","api","aplicativo","ativos","blog","cache","cgi","cgibin","contato","conteudo","css","db","depuracao","docs","download","editor","erro","erros","faq","arquivo","arquivos","forum","ftp","galeria","ajuda","imagem","imagens","img","incluir","inclusoes","indice","informacoes","instalar","js","basedeconhecimento","idioma","idiomas","biblioteca","licenca","log","logs","login","logout","senhaperdida","email","manutencao","midia","membro","membros","mensagem","mensagens","misc","movel","modulo","modulos","minhaconta","mysql","noticias","boletim","novotopico","notificacao","notificacoes","antigo","online","pedido","pedidos","pagina","paginas","senha","pagamento","php","figura","figuras","plugin","plugins","enquete","portal","post","posts","perfil","projeto","projetos","publico","registrar","registro","about","account","app","assets","contact","content","debug","faq","file","files","forum","gallery","help","image","images","include","includes","index","info","install","knowledgebase","language","languages","lib","library","license","maintenance","media","member","members","message","messages","mobile","mod","module","modules","myaccount","news","newsletter","newtopic","notification","notifications","old","order","orders","page","pages","password","payment","pic","pics","poll","portal","profile","project","projects","public","register","registration","release","releases","reply","report","reports","reset","resource","resources","restore","rss","sale","search","secure","security","send","server","service","services","session","sessions","setting","settings","setup","shop","sidebar","site","sitemap","sites","smtp","sql","src","ssl","static","stats","status","store","style","styles","stylesheet","stylesheets","subscribe","support","system","tablet","tag","tags","task","tasks","template","templates","test","testing","text","theme","themes","thread","threads","ticket","tickets","tmp","todo","tool","toolbar","tools","topic","topics","tracker","tracking","traffic","transfer","translate","troubleshoot","tutorial","twitter","type","types","uninstall","unsubscribe","update","updates","upload","uploads","url","user","username","users","utility","var","vendor","version","video","videos","view","views","vote","votes","wall","web","website","widget","widgets","wiki","windows","wireless","word","wordpress","work","works","workflow","workflows","workspace","workspaces","write","writer","writers","www","xml","xsl","xslt","yaml","year","years","zip"]
        else:
            diretorios = []
            with open(nome_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    diretorios.append(linha.strip())

        keep_alive = True
        sessao = requests.Session()
        sessao.keep_alive = True
        posicao = 0
        for diretorio in diretorios:
            posicao += 1
            resposta = requests.get(f'{self.url}{diretorio}', headers=self.headers, allow_redirects=False)
            print(f'[ {posicao:^5} ]',diretorio)
            if resposta.status_code > 199 and resposta.status_code < 300:
                if diretorio in self.diretorios_ocultos or diretorio in self.diretorios_aparentes:
                    pass
                else:
                    self.diretorios_ocultos.append(diretorio)
            elif resposta.status_code > 299 and resposta.status_code < 400:
                if diretorio in self.diretorios_ocultos or diretorio in self.diretorios_aparentes:
                    pass
                else:
                    self.diretorios_ocultos.append(f'{diretorio} | redirecionado')
            else: pass
            sleep(1)
        sessao.close()

    def buscar_xss(self):
        site = BS(self.requisicao.content, 'html.parser')

        registro_forms = site.find_all('form')
        registro_forms = [registro_form.get('action') for registro_form in registro_forms]

        registro_inputs = site.find_all('input')
        registro_inputs = [registro_input.get('name') for registro_input in registro_inputs]

        script = "<script>document.write('0129834765')</script>"

        for form in registro_forms:
            for input in registro_inputs:
                dados = {
                    input: script
                }

                if form != None:
                    resposta_site = requests.post(f'{self.url}{form}', data=dados, headers=self.headers)
                else:
                    resposta_site = requests.post(self.url, data=dados, headers=self.headers)

                if script in str(resposta_site.text):
                    self.injecao_js.append(f'form(action): {form}\ninput(name): {input}')

    def geral(self, site, nome_arquivo):
        site.buscar_xss()
        site.buscar_diretorios()
        site.forca_diretorio(nome_arquivo)

    def gerar_relatorio(self, opcao):
        if opcao == 'txt':
            registro_link = ''
            for link in self.links:
                registro_link += f'{link}\n'
            if registro_link != '':
                salvar_arquivo('SWEEP-links.txt', registro_link)

            registro_diretorios = ''
            for diretorio in self.diretorios_aparentes:
                registro_diretorios += f'{self.url}{diretorio}\n'
            if registro_diretorios != '':
                salvar_arquivo('SWEEP-diretorios-aparentes.txt', registro_diretorios)

            registro_diretorios = ''
            for diretorio in self.diretorios_ocultos:
                registro_diretorios += f'{self.url}{diretorio}\n'
            if registro_diretorios != '':
                salvar_arquivo('SWEEP-diretorios-forcado.txt', registro_diretorios)

            registro_js = ''
            for xss in self.injecao_js:
                registro_js += f'{xss}\n'
            if registro_js != '':
                salvar_arquivo('SWEEP-injecao-xss.txt', registro_js)

        elif opcao == 'json':
            dados = {
                "url": self.url,
                "servidor": self.servidor,
                "links": self.links,
                "diretorios_forcados": self.diretorios_ocultos,
                "diretorios_padina": self.diretorios_aparentes,
                "injecao_js": self.injecao_js
            }
            salvar_arquivo('SWEEP-dados.json', str(dados).replace("'", '"'))

        else:
            print('\nmetodo de salvar arquivo não existe')


