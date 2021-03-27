#Import dos conectores com a página
from browser import document, console
from browser.template import Template

#Função citada no name.html
def incr(event, element):
    console.log(event)  #imprime o console.log do javascript a função event( o que ta acontecendo )
    
    #Vai pegar o elemento com a tag: {myname}
    #document['write'], vai pegar o elemento com id='write', usando '.value' pega o valor do input
    element.data.counter += 1
    pass

# 'name' é o Id de onde está a Div. [nrm] passa a função.  '.render' vai renderizar e iniciar como '' a tag:  {myname}
Template('increment', [incr]).render(counter=0)