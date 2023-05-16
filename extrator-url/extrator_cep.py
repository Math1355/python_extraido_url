import re # Regular Expression ou RegEx

endereco = "Rua das Flores 72, apartamento 1002, Laranjeira, Rio de Janeiro, Rj, 23440-120"

# 5 digitos + hifen (opcional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) #Match
if busca:
    cep = busca.group()
    print(cep)