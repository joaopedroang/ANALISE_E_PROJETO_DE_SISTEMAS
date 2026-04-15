# Exercício 11 - Sistema de Gestão Unificada
## Cenário
Este projeto apresenta uma solução de modelagem para um sistema de cadastro organizacional. A arquitetura foca na Generalização, onde dados comuns de indivíduos são centralizados em uma superclasse, enquanto comportamentos específicos de Clientes e Funcionários são tratados em subclasses. O sistema também gerencia múltiplas associações para endereços, contatos, cargos e profissões.

## 1. Identificação de Classes, Atributos e Métodos
Superclasse: PESSOA
Atributos: NOME, DTNASC.
Associações: Endereço (1..*), Telefone (1..*).
Subclasse: CLIENTE (Herda de Pessoa)
Atributos: CODIGO, LIMCREDITO.
Associação: Profissão (1).
Subclasse: FUNCIONARIO (Herda de Pessoa)
Atributos: MATRICULA, SALARIO, DTADMI.
Associação: Cargo (1).

## 2. Requisitos Funcionais (RF)
[RF01] Cadastrar dados básicos de pessoas (Nome e Nascimento).
[RF02] Registrar Clientes com códigos únicos e limites de crédito.
[RF03] Registrar Funcionários com matrícula, salário e data de admissão.
[RF04] Vincular múltiplos endereços e telefones a um mesmo indivíduo.
[RF05] Atribuir profissões aos clientes e cargos aos funcionários para fins de classificação.

## 3. Requisitos Não Funcionais (RNF)
[RNF01] Garantir a integridade da herança: dados de pessoa são obrigatórios para qualquer subclasse.
[RNF02] Diferenciar permissões de acesso: apenas administradores podem gerir dados de funcionários.
[RNF03] Suportar a multiplicidade 1..* para contatos e endereços.
[RNF04] Padronização de datas para evitar erros de cálculo de idade ou tempo de serviço.

## 4. Diagramas UML
Diagrama de Classes
[<img width="661" height="468" alt="image" src="https://github.com/user-attachments/assets/307b270f-6203-4e9f-95a8-65a510ed6d5f" />]

Diagrama de Casos de Uso
[<img width="571" height="469" alt="image" src="https://github.com/user-attachments/assets/81c13287-9bc8-4e43-9d12-492f0ae69398" />]
