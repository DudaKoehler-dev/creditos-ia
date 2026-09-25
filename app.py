from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/',  methods=['GET','POST'])
def pagina_inicial():

    percentual = None
    projecao = None
    percentual_proj = None
    
    if request.method == 'POST':
             
         percentual = request.args.get('percentual')
         projecao = request.args.get('projecao')
         percentual_proj = request.args.get('percentual_proj')
        
         limite = int(request.form['limite'])
         credito = int(request.form['credito'])
         dia = int(request.form['dia'])


         percentual = credito / limite * 100
         projecao = credito * 30 / dia
         percentual_proj = projecao / limite * 100

  

                #REDIRECIONANDO PARA OUTRA ROTA
                #URL_FOR CHAMA OUTRA ROTA
    return render_template('index.html', percentual=percentual,
        projecao=projecao,
        percentual_proj=percentual_proj)



# fica no fim

# Bloco de execução: só roda quando o arquivo é executado diretamente
if __name__ == '__main__':
    # debug=True ativa o recarregamento automático ao salvar o arquivo
    # NUNCA use debug=True em produção (servidor público)
    app.run(debug=True)