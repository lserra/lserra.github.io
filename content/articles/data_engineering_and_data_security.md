Title: O papel da engenharia de dados na segurança dos dados
Date: 2026-09-23 18:30
Modified: 2026-09-23 18:30
Category: Data Engineering, Data Security
Slug: data-engineering-and-data-security
Summary: Quando uma empresa coleta dados pessoais, ela assume uma responsabilidade. Isso inclui informações óbvias, como nome, CPF, telefone e endereço, mas também dados que podem revelar hábitos, localização, preferências, histórico de compras, comportamento profissional ou condições de saúde.
Tags: security information, data engineering, data security, threat intel, lgpd, data governance
Authors: Laercio Serra
Status: published

# O que realmente está em risco

Quando uma empresa coleta dados pessoais, ela assume uma responsabilidade. Isso inclui informações óbvias, como nome, CPF, telefone e endereço, mas também dados que podem revelar hábitos, localização, preferências, histórico de compras, comportamento profissional ou condições de saúde.

O risco não aparece somente quando um criminoso invade um sistema. Ele também pode surgir durante atividades autorizadas, como:

- Coletar mais informações do que o necessário.
- Compartilhar dados com um fornecedor sem avaliar adequadamente o contrato e os controles existentes.
- Manter registros por tempo indefinido.
- Usar uma informação para uma finalidade diferente daquela informada ao cliente.
- Dar acesso amplo a funcionários que não precisam consultar aqueles dados.
- Colocar informações pessoais em relatórios, planilhas ou registros técnicos sem necessidade.
- Utilizar dados reais em ambientes de teste.

## O papel da engenharia de dados

A engenharia de dados tem participação direta na privacidade. Pipelines, integrações, relatórios e processos de cópia podem reduzir riscos ou ampliá-los.

Algumas práticas importantes são:

- Classificar os dados conforme o impacto que sua exposição causaria.
- Separar informações identificáveis dos dados usados para análise quando possível.
- Substituir dados reais por dados fictícios em testes.
- Aplicar mascaramento ou redução de detalhes nos relatórios.
- Evitar transportar campos que não são utilizados pelo sistema de destino.
- Controlar quem pode consultar dados brutos.
- Monitorar exportações e acessos fora do padrão.
- Definir prazos para retenção em tabelas, arquivos, filas e cópias.
- Documentar a origem, o uso e os responsáveis por cada conjunto de dados.
- Garantir que a exclusão seja refletida também em cópias e sistemas dependentes, quando aplicável.

Um relatório para a área financeira talvez precise mostrar o valor de uma compra, mas não o documento completo do cliente. Um painel de desempenho pode usar uma identificação interna em vez de nome, telefone e endereço. Pequenas reduções de exposição, repetidas em muitos processos, podem diminuir bastante o impacto de um incidente.

## Proteção não significa segurança absoluta

Nenhuma empresa consegue prometer risco zero. Sistemas falham, pessoas erram, fornecedores sofrem ataques e novas formas de abuso aparecem.

Uma abordagem responsável reconhece essa realidade e se prepara para ela.

Isso inclui:

- Identificar os dados mais sensíveis.
- Corrigir as fraquezas mais perigosas primeiro.
- Usar autenticação forte nas contas importantes.
- Limitar acessos e revisar permissões.
- Manter sistemas atualizados.
- Proteger informações durante o armazenamento e a transmissão.
- Criar cópias de segurança e testar a recuperação.
- Registrar eventos relevantes para investigar problemas.
- Preparar um procedimento para responder a incidentes.
- Treinar as pessoas para reconhecer erros e tentativas de fraude.

O objetivo não é comprar todas as ferramentas disponíveis. É reduzir a probabilidade de um problema, limitar seu impacto e aumentar a capacidade de resposta.

Uma pequena empresa pode começar com controles simples e bem executados. Uma lista de sistemas e dados, contas individuais, cópias testadas, atualizações regulares e revisão de acessos já podem produzir resultados concretos.

## O perigo da privacidade de fachada

É possível ter uma política de privacidade bem escrita e continuar tratando os dados de forma inadequada.

Isso acontece quando:

- O texto informa uma coisa, mas o sistema faz outra.
- O cliente não consegue exercer seus direitos de maneira prática.
- A empresa coleta dados “por precaução”.
- Os funcionários compartilham planilhas sem controle.
- O fornecedor recebe mais informações do que precisa.
- Não existe prazo para excluir dados.
- A organização não sabe quais informações possui.
- Os registros de operação guardam dados pessoais desnecessários.
- A segurança é tratada apenas como compra de ferramentas.

Privacidade não deve ser avaliada apenas pela existência de documentos. Ela precisa aparecer no comportamento do sistema e nas decisões diárias da empresa.

## Um caminho prático para começar

Uma organização que queira adotar privacidade como padrão pode seguir uma sequência simples:

1. Liste os sistemas, arquivos e fornecedores que tratam dados pessoais.
2. Identifique quais informações são coletadas e para qual finalidade.
3. Remova campos que não são necessários.
4. Separe dados essenciais de dados usados apenas para análise ou conveniência.
5. Revise acessos, contas compartilhadas e permissões antigas.
6. Defina prazos de retenção para cada tipo de informação.
7. Proteja os dados mais sensíveis e monitore acessos relevantes.
8. Substitua dados reais por dados fictícios em desenvolvimento e testes.
9. Crie um procedimento para responder a incidentes.
10. Revise o processo sempre que um produto, fornecedor ou finalidade mudar.

Esse trabalho não precisa começar com um grande projeto. Pode começar por um processo crítico, como cadastro de clientes, atendimento, faturamento ou recursos humanos.

A prioridade deve ser dada aos dados cuja exposição, alteração ou perda causaria maior prejuízo às pessoas e à empresa.

Privacidade, segurança e engenharia de dados fazem parte do mesmo problema: decidir como reduzir riscos enquanto a empresa usa informações para operar.

Ameaças exploram vulnerabilidades, mas nem todo problema de privacidade começa com um ataque. Muitos surgem de coletas excessivas, acessos mal definidos, cópias esquecidas, relatórios inadequados ou decisões tomadas sem considerar as consequências para as pessoas.

Adotar privacidade como padrão não significa tornar a empresa lenta nem impedir o uso de dados. Significa coletar menos, proteger melhor, explicar com clareza e assumir responsabilidade por todo o caminho percorrido pelas informações.

No fim, a pergunta mais importante não é apenas “como impedir que alguém roube esses dados?”. É também:

> “Por que temos esses dados, quem realmente precisa deles e o que podemos fazer para reduzir o risco antes que algo aconteça?”
