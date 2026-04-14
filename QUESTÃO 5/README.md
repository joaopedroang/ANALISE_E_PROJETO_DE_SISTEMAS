# Exercício 05 - Sistema de Gastos Diários (Vera)
## Cenário
O projeto simula a automação de uma planilha de gastos pessoais. O sistema permite que a usuária (Vera) registre despesas cotidianas categorizadas por tipo e forma de pagamento. Ao final do período, o software processa esses dados para gerar relatórios agrupados, permitindo uma visão clara de onde o dinheiro foi aplicado e qual método de pagamento foi mais utilizado.

## 1. Identificação de Classes, Atributos e Métodos
Classe: Gasto
Atributos: tipoGasto, data, valor, formaPagamento.
Classe: ControleFinanceiro
Atributos: +/listaGastos (Relacionamento), +/totalMensal (Atributo Derivado).
Métodos: adicionarGasto(), gerarRelatorioMensal(), agruparPorTipo().

## 2. Requisitos Funcionais (RF)
[RF01] O sistema deve permitir o cadastro de gastos com tipo, data, valor e forma de pagamento.
[RF02] O sistema deve oferecer categorias pré-definidas (Remédio, Roupa, Refeição, etc).
[RF03] O sistema deve suportar múltiplas formas de pagamento (Dinheiro, Cartões, Tickets).
[RF04] O sistema deve calcular o valor total gasto em um mês específico.
[RF05] O sistema deve agrupar e exibir o total de gastos por tipo de categoria.
[RF06] O sistema deve detalhar o quanto foi gasto em cada forma de pagamento dentro dos agrupamentos.

## 3. Requisitos Não Funcionais (RNF)
[RNF01] O sistema deve apresentar os dados em formato de tabela, assemelhando-se a uma planilha Excel.
[RNF02] Os cálculos financeiros devem manter precisão de duas casas decimais.
[RNF03] A interface deve ser responsiva e permitir filtragem rápida por mês.
[RNF04] O código deve seguir os princípios de separação de responsabilidades (POO).

## 4. Diagramas UML
Diagrama de Classes [![Diagrama de classes](https://github.com/user-attachments/assets/740c0cb1-1cd2-4db0-834f-7849f7144d5f)
]

Diagrama de Casos de Uso [![UseCaseDiagram1](https://github.com/user-attachments/assets/2eb8152b-8f33-4dc4-8ae5-4541b1e07880)
]
