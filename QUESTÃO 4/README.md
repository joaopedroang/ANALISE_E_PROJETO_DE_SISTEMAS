# Exercício 04 - Sistema de Controle de Remédios
## Cenário
Este projeto consiste em uma aplicação de controle pessoal de horários de medicamentos. O sistema permite o cadastro de prescrições médicas, sugere horários automáticos baseados na frequência diária e possui uma funcionalidade inteligente de reorganização de horários caso o usuário (Maurício) atrase uma dose.

## 1. Identificação de Classes, Atributos e Métodos
Classe: Paciente
Atributos: nome.
Métodos: consultarPlanilha().
Classe: Remedio
Atributos: nomeRemedio, dosagem.
Classe: Prescricao
Atributos: dataInicio, duracaoDias, vezesAoDia, horarioInicial, +/dataTermino (Atributo Derivado).
Métodos: sugerirHorarios(), gerarPlanilha().
Classe: PlanilhaHorario
Atributos: dataReferencia, horariosDoDia (list).
Métodos: reorganizarPorAtraso(novoHorario), exibirPlanilha().

## 2. Requisitos Funcionais (RF)
[RF01] Permitir o cadastro do remédio com nome do paciente, data, duração, frequência, dosagem e nome do medicamento.
[RF02] Sugerir todos os horários possíveis para as doses.
[RF03] Permitir que o usuário escolha o melhor horário inicial.
[RF04] Exibir a data de término do tratamento automaticamente.
[RF05] Preparar e exibir a planilha de horários completa.
[RF06] Permitir a seleção da planilha específica do dia atual.
[RF07] Reorganizar automaticamente os horários do dia em caso de atraso notificado.

## 3. Requisitos Não Funcionais (RNF)
[RNF01] Execução em ambiente mobile/smartphone.
[RNF02] Interface intuitiva para controle pessoal de saúde.
[RNF03] Processamento imediato para recálculo de horários (baixa latência).
[RNF04] Organização de código seguindo princípios de POO e Clean Code.

## 4. Diagramas UML
Diagrama de Classes
[<img width="678" height="445" alt="image" src="https://github.com/user-attachments/assets/6cb33579-50c0-4e8d-a21a-3f77263d45ca" />
]
Diagrama de Casos de Uso
[<img width="467" height="524" alt="image" src="https://github.com/user-attachments/assets/36caa7bd-26e0-4400-8cb6-2e1c5f75e4c4" />
]
