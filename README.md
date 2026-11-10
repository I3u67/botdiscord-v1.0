# botdiscord
Estou aprendendo a desenvolver meu primeiro bot de Discord, usando Python.
main é o arquivo principal, onde tem a estrutura base do BOT, e alguns comandos principais a qual quis destacar.
e a pasta cogs possue subpastas categorizadas com arquivos.py de comandos e eventos que seguem o tema de sua subpasta, achei necessário para organizar o bot e não misturar os comandos, e acumula-los em um só lugar, oque daria numa bagunça.

Usei:
diretorio = "cogs"
for root,dirs,files in os.walk(diretorio):
for file in files:
if file.endswith(".py") and file != "__init__.py":
caminho = os.path.join(root,file).replace("\\","/").replace("/",".")[:-3]
await self.load_extension(caminho)
print(f"cog carregado {caminho}"
                    
Para que eu não precise ficar colocando cada caminho novo toda hora que eu criasse uma pasta ou subpasta nova, então agora com esse looping, o sistema passará a sempre ver todos os diretorios e arquivos do root selecionado a qual chamei de "cogs", que é o nome da pasta. Vi na internet que o comando ficaria mais completo com essa adição de "caminho", a qual entendi que também poderia colocar o replace para evitar problemas na forma de escrita de direcionamento, substituindo-os pelo que o sistema identifica, que é o "."
