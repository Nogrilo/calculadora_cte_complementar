Olá, irei apresentar o projeto simples que fiz para me ajudar no trabalho.

Na Transgires umas das minhas funções é emitir Conhecimento de Transporte Eletrônico (CTe) Complementar de Reembolso de Descarga.

Para exemplificar, vou utilizar um exemplo prática:
- Carregamos na Pepsico de Cabreúva para Campo Grande, e no ato da descarga precisamos pagar R$ 950 para descarregar a mercadoria da carreta.
- Com isso, eu emito um CTe Complementar de Reembolso de Descarga, para o cliente nos devolver esse dinheiro, mas tem um porém. Precisamos adicionar impostos
no valor total.

Então, pegando esse exemplo vou somar 950 + 7% ICMS (por ser campo grande é 0,93).
Com isso, irei emitir um CTe Complementar no valor de R$ 1.021,51 .

Mas esse é só um exemplo, e foi muito comum de eu errar essa conta simples na calculadora. Por isso, desenvolvi esse software simples para me ajudar
a fazer o documento com o valor cheio.

Na prática, ele apenas vai pegar os inputs do usuário, e aplicar na formúla que é:
valor_com_imposto = valor_descarga / valor_icms / pis (caso possua PIS)

E irá copiar o valor calculado para o CTRL+C , assim me ajudando a não cometer erros bobos na emissão.

Uso diariamente esse programa, pois me ajuda a realizar a conta de uma forma estremamente rápida, e sem erros.
