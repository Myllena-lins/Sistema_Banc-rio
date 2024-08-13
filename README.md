# Sistema_Bancário
Deafio feito pela plataforma DIO, do Bootcamp de Python. É um sistema bancário simples que permite aos usuários realizar operações básicas de conta bancária, como depósito, saque, consulta de saldo e extrato. O sistema também inclui controle de limites diários de saque e um registro das transações realizadas.

## Funcionalidades
- Depositar: Permite ao usuário realizar depósitos na conta, atualizando o saldo e o extrato.
- Sacar: Permite ao usuário realizar saques, com controle de limite diário e número máximo de saques permitidos por dia.
- Extrato: Exibe um resumo das transações realizadas (depósitos e saques) e o saldo atual da conta.
- Consultar Saldo da Conta: Mostra o saldo atual da conta.
- Sair: Encerra o programa.

## Regras e Limitações
- Limite de Saque Diário: O valor máximo permitido para saque diário é de R$ 500.
- Número Máximo de Saques Diários: O usuário pode realizar no máximo 3 saques por dia.
- Validação de Valores: O sistema garante que apenas valores positivos são aceitos para depósitos e saques.

## Exemplo de Uso
1. Depositar:
   - O usuário seleciona a opção de depósito e informa o valor.
   - O valor é adicionado ao saldo e registrado no extrato.
2. Sacar:
   - O usuário seleciona a opção de saque e informa o valor.
   - O sistema verifica se o valor está disponível e se não ultrapassa o limite diário.
   - O valor é subtraído do saldo e registrado no extrato.
3. Extrato:
   - O usuário solicita o extrato, que mostra todas as movimentações e o saldo atual.
5. Consultar Saldo da Conta:
   - O usuário pode consultar o saldo da conta a qualquer momento.

## Tecnologias Utilizadas
- Python (módulos padrão)

## Observações Finais
A criação desse sistema foi uma solução simples e aplicável em qualquer sistema de gerenciamento de restaurantes. Qualquer sugestão para melhoria do mesmo será bem-vinda!
