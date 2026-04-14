# Exercício 06 - Sistema de Comanda Eletrônica

## Cenário
O sistema foi desenvolvido para automatizar o controle de consumo na padaria Doce Sabor. O fluxo consiste no registro de produtos e quantidades em uma comanda numerada por parte do atendente e a posterior leitura e fechamento dessa comanda pelo caixa, que calcula o valor total com base nos preços unitários.

## 1. Identificação de Classes, Atributos e Métodos

Classe: Produto
Atributos: codigo, nome, valorUnitario.
Método: obterPreco().
Classe: ItemComanda
Atributos: quantidade, +/subtotal (derivado), produto (relação).
Método: calcularSubtotal().
Classe: Comanda
Atributos: numero, itens (lista), +/total (derivado).
Métodos: adicionarItem(), calcularTotal(), fecharComanda().
Classe: Caixa
Atributos: operador.
Métodos: lerComanda(), calcularTotal(), finalizarCompra().

## 2. Requisitos Funcionais (RF)
[RF01] O sistema deve permitir criar uma comanda eletrônica com número único.
[RF02] O sistema deve permitir registrar produtos consumidos na comanda.
[RF03] O sistema deve permitir informar a quantidade de cada produto.
[RF04] O sistema deve associar produtos cadastrados à comanda.
[RF05] O sistema deve permitir consultar os itens registrados na comanda.
[RF06] O sistema deve calcular automaticamente o subtotal de cada item (quantidade × valor unitário).
[RF07] O sistema deve calcular o valor total da comanda com base nos itens registrados.
[RF08] O sistema deve permitir que o caixa leia a comanda no momento do pagamento.
[RF09] O sistema deve permitir finalizar a comanda, impedindo novos lançamentos.
[RF10] O sistema deve exibir o valor total da compra ao cliente.

## 3. Requisitos Não Funcionais (RNF)
[RNF01] O sistema deve calcular o valor total da comanda em tempo inferior a 2 segundos.
[RNF02] O sistema deve possuir interface simples e de fácil uso para os atendentes e caixas.
[RNF03] O sistema deve garantir que os valores calculados sejam precisos e consistentes.
[RNF04] O sistema deve estar disponível durante todo o horário de funcionamento da padaria.
[RNF05] O sistema deve impedir alterações em comandas já finalizadas.
[RNF06] O sistema deve garantir que não existam comandas duplicadas (número único).
[RNF07] O sistema deve ser estruturado de forma que permita fácil manutenção e atualização.
[RNF08] O sistema deve suportar múltiplas comandas sendo utilizadas simultaneamente.

## 4. Diagramas UML
Diagrama de Classes
[![Diagrama de classes](https://github.com/user-attachments/assets/a74aa9b2-f72d-4ff8-a035-94cc4da0c574)
]

Diagrama de Casos de Uso
[![UseCaseDiagram1](https://github.com/user-attachments/assets/e6bf5c77-f2f1-4a06-8b5d-b5aa03eeba60)
]
