


#*******************************************************************************************************************     App Rest  - Formula de processamento "POST"
from flask_restful import Resource
from flask_restful import reqparse  # Recebe o Json para modificações no sistema
from flask import request, send_file


# Rest sobre hoteis, onde vai pesquisar
class ReqNameArq(Resource):
    # Argumentos Usados no POST e PUT.
    ##Configura o requisitos de ids para construir os processos
    argumentos = reqparse.RequestParser()  # Instancia o Request Parse
    # Adiconar os argumentos que você quer que mude, assim evita de mudar algo que não faz parte do sistema
    """
    argumentos.add_argument('nome', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    """
    argumentos.add_argument('pesquisa', type=str, required=True,
                            help="O campo 'pesquisa' deve ser preenchido.")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.

    """
    argumentos.add_argument('endereco-rua', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    argumentos.add_argument('endereco-numeroresidencia', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    argumentos.add_argument('endereco-bairro', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    argumentos.add_argument('endereco-cep', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    argumentos.add_argument('endereco-caixapostal', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    argumentos.add_argument('uf', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    argumentos.add_argument('cidade', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    """


    
    # Post é de fotografia, arrumar para inserir as requisições do Ibama
    def get(self):
        try:
            # Criar um construtor
            Itens = ReqNameArq.argumentos.parse_args()  # Recebe os atributos
            
            import Busca as Bu
            Pesq = str( 'pesquisa'['pesquisa'] )
            
            FullFiles = Bu.BuscaArq().Pequisar(Pesquisa=Pesq, OnlyName=True)
            
            
            return FullFiles



        except Exception as err:
            print("Error acontecido na Pesquisa-Name")
            print(err)
            return ("Error, {}".format(err)), 404








# Rest sobre hoteis, onde vai pesquisar
class ReqFileArq(Resource):
    # Argumentos Usados no POST e PUT.
    ##Configura o requisitos de ids para construir os processos
    argumentos = reqparse.RequestParser()  # Instancia o Request Parse
    # Adiconar os argumentos que você quer que mude, assim evita de mudar algo que não faz parte do sistema
    """
    argumentos.add_argument('nome', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    """
    argumentos.add_argument('arquivos', type=str, required=True,
                            help="O campo 'pesquisa' deve ser preenchido.")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.

    """
    argumentos.add_argument('endereco-rua', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    argumentos.add_argument('endereco-numeroresidencia', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    argumentos.add_argument('endereco-bairro', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    argumentos.add_argument('endereco-cep', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    argumentos.add_argument('endereco-caixapostal', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    argumentos.add_argument('uf', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    argumentos.add_argument('cidade', type=str, required=True,
                            help="The field 'nome' cannot be left blank")  # Coloca o nome exato do argumento que quer aceitar. Required=True o json não pode faltar na requisição do json. Help, mensagem de error caso falte um argumento.
    """


    
    # Post é de fotografia, arrumar para inserir as requisições do Ibama
    def get(self):
        try:
            # Criar um construtor
            Itens = ReqFileArq.argumentos.parse_args()  # Recebe os atributos
            
            import Busca as Bu
            Pesq = str( 'arquivos'['arquivos'] )
            
            FullFiles = Bu.BuscaArq().Pequisar(Pesquisa=Pesq, OnlyArq=True)
            
            ### Criar Motor para Salvar o Arquivo...  // Baixar Somente um arquivo
            ArqBaixar = ""
            for uniq in FullFiles:
                if (Pesq in uniq):
                    ArqBaixar = uniq
            
            ### Criar Motor para Salvar o Arquivo...  // Baixar Somente um arquivo
            
            
            #return FullFiles
            #return send_file(   Cnd[0], attachment_filename=(Cnd[1]), as_attachment=True   )    #Baixar arquivo, usa ultimo parametro(attachment)



        except Exception as err:
            print("Error acontecido na Pesquisa-Name")
            print(err)
            return ("Error, {}".format(err)), 404







#-------------------------------------------------  RestAPI


from flask import Flask
from flask_restful import Api



app = Flask(__name__)
api = Api(app)



#Formula para Executar Algo antes do Unicio
@app.before_first_request
def cria_banco():       #Cria o banco na raiz deste arquivo python
    # Abrir a Classe aqui Inicial
    try:
        files = glob('*.pdf')
        for atuFile in files:
            os.remove(atuFile)
        files = glob('*.png')
        for atuFile in files:
            os.remove(atuFile)
    except Exception:
        pass




#Recurso
@app.route('/', methods=['GET'])
def index():
    return '<h1>CND RF CPF!</h1>'





#Usar para Consultar Nome dos arquivos -- [ok]
api.add_resource(ReqNameArq, '/pesquisa/<str>', methods=['GET'])

#Usar para Consultar os arquivos
api.add_resource(ReqFileArq, '/arquivos', methods=['GET'])




#Inicia a Aplicação
#Ini = CndCpf()  # Abre a e do Requerimento
app.run(debug=True, host='0.0.0.0', port=5000)

#Encerra os processamentos quando terminar ou acontecer error

