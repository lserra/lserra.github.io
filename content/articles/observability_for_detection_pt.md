Title: Observabilidade de Dados (Insider Threat)
Date: 2026-09-24 18:30
Modified: 2026-09-24 18:30
Category: Data Engineering, Data Security
Slug: observability-for-detection-pt
Summary: Nem todo incidente de segurança começa com um ataque externo, um vírus ou uma senha roubada. Em muitos casos, o problema surge quando uma pessoa que já possui acesso legítimo usa esse acesso de forma indevida. Por isso, registros de acesso, números de uso e o caminho percorrido por cada solicitação devem ser tratados como ativos de segurança. Quando analisados em conjunto, eles ajudam a identificar comportamentos fora do padrão sem transformar qualquer atividade normal em um alerta. A proposta não é vigiar pessoas de forma indiscriminada. O objetivo é proteger dados sensíveis, entender o contexto de cada acesso e agir antes que uma extração indevida cause prejuízos.
Tags: cybersecurity, data engineering, data security, insider threat, data observability
Authors: Laercio Serra
Status: published

# O que deve ser observado

Uma boa análise começa pela coleta de três tipos de informação:

| Informação | O que mostra | Exemplo |
|---|---|---|
| Registros | Quem fez algo, quando e onde | Usuário consultou dados de clientes às 23h |
| Números de uso | Quanto foi acessado ou transferido | 20 GB exportados em uma hora |
| Caminho da operação | Como a ação aconteceu | Painel de BI, API, banco de dados e arquivo exportado |

Os registros ajudam a responder perguntas básicas:

- Qual usuário realizou a consulta?
- Qual aplicação foi usada?
- Quais tabelas ou arquivos foram acessados?
- O acesso ocorreu a partir de qual dispositivo ou endereço de rede?
- Houve download, exportação ou cópia?
- O usuário tinha uma tarefa que justificasse aquela ação?

Os números de uso mostram mudanças que podem passar despercebidas em uma análise manual:

- Aumento repentino no número de consultas.
- Acesso a uma quantidade incomum de clientes ou documentos.
- Exportação de arquivos muito maiores que o normal.
- Transferência de dados para um destino nunca utilizado.
- Repetição de consultas semelhantes em curto período.

Já o caminho da operação mostra a sequência completa. Por exemplo: um usuário acessa um painel, o painel consulta o banco, uma API prepara os dados e, em seguida, um arquivo é gerado para download. Essa visão é mais útil do que analisar cada evento separadamente.

## Como identificar desvios

O primeiro passo é conhecer o comportamento normal de cada função. Um analista financeiro, por exemplo, pode consultar dados de vendas durante o horário comercial e exportar pequenos relatórios. Um administrador de banco pode acessar muitas tabelas, mas normalmente trabalha com ferramentas e horários conhecidos.

O comportamento esperado deve ser definido por função, aplicação e tipo de dado. Comparar todos os usuários com a mesma regra costuma gerar muitos alertas sem importância.

Uma forma simples de análise é combinar sinais:

| Sinal observado | Exemplo | Importância |
|---|---|---|
| Consulta fora do padrão | Acesso a uma tabela nunca usada pelo usuário | Média |
| Horário incomum | Acesso durante a madrugada | Baixa ou média |
| Grande quantidade de dados | Exportação de milhões de registros | Alta |
| Novo dispositivo | Acesso por equipamento não registrado | Média |
| Acesso a dado sensível | Consulta a salário, saúde ou dados bancários | Alta |
| Mudança de permissão | Usuário recebeu acesso pouco antes da consulta | Alta |

Nenhum desses sinais, sozinho, prova que existe abuso. Um acesso fora do horário pode ocorrer por causa de uma emergência. Uma grande exportação pode fazer parte de uma tarefa autorizada. O risco aumenta quando vários sinais aparecem juntos.

Por exemplo, uma consulta fora do horário pode receber baixa prioridade. Porém, se o mesmo usuário também acessar dados sensíveis, usar um dispositivo desconhecido e exportar grande volume de informações, o caso merece investigação.

Essa combinação reduz o excesso de alertas e direciona a equipe para situações que realmente precisam de atenção.

## Um caso prático

Um exemplo que ocorreu recentemente. Um funcionário acessou, sem justificativa profissional, informações de milhares de clientes durante um período prolongado. Foi identificado, que foram realizadas mais de 6.600 consultas envolvendo cerca de 3.573 clientes entre 2022 e 2024. Após auditoria interna, descobriu-se que o funcionário estava exfiltrando estas informações.

Esse caso mostra que o abuso interno nem sempre aparece como uma grande cópia de dados em poucos minutos. Ele também pode ocorrer por meio de muitas consultas menores, repetidas ao longo do tempo.

Se a organização observasse apenas o volume diário de dados, talvez cada consulta parecesse normal. Uma análise mais completa poderia considerar:

- A quantidade de clientes consultados.
- A relação entre esses clientes e a função do funcionário.
- A repetição de consultas fora da necessidade de trabalho.
- O acesso a pessoas ligadas ao funcionário.
- A frequência e a duração do comportamento.
- A existência ou não de uma tarefa registrada para justificar os acessos.

Outro caso, também recente, envolveu um funcionário de uma empresa de tecnologia que tinha acesso administrativo aos ambientes da AWS e do GitHub. Este mesmo colaborador baixou gigabytes de arquivos confidenciais e alterou configurações relacionadas à retenção dos registros para esconder sua atividade.

Esses dois episódios reforçam bem a importância de proteger os próprios registros. Se uma pessoa com acesso administrativo puder apagar ou alterar os registros, a organização perde uma das principais fontes de evidência.

Por isso, os registros devem ser enviados para um local separado, com acesso limitado e retenção protegida contra alterações. O responsável pelo ambiente não deve ser capaz de apagar sozinho os sinais da própria atividade.

## Como aplicar na prática

Uma implantação eficiente pode ser feita em etapas.

### 1. Escolha os dados mais importantes

Comece por informações que causariam maior prejuízo se fossem expostas:

- Dados pessoais de clientes.
- Informações financeiras.
- Segredos comerciais.
- Código-fonte.
- Credenciais e chaves de acesso.
- Dados de funcionários.
- Relatórios estratégicos.

Não é necessário monitorar tudo com o mesmo nível de detalhe desde o início.

### 2. Registre as ações principais

Para cada acesso importante, registre:

- Usuário ou conta utilizada.
- Data e horário.
- Sistema de origem.
- Aplicação usada.
- Tipo de dado acessado.
- Quantidade de registros consultados.
- Tamanho do arquivo exportado.
- Destino do download.
- Resultado da operação.

O registro deve evitar guardar o conteúdo completo dos dados. Na maioria dos casos, basta registrar o tipo de informação, a quantidade e o identificador da operação. Isso reduz riscos adicionais e facilita o respeito às regras internas de privacidade.

### 3. Crie uma referência de comportamento normal

Observe o ambiente por algumas semanas e estabeleça uma referência para cada grupo de usuários. Essa referência pode considerar:

- Horário habitual de trabalho.
- Sistemas normalmente utilizados.
- Volume médio de consultas.
- Tabelas e arquivos acessados com frequência.
- Local ou dispositivo normalmente utilizado.
- Quantidade usual de exportações.

A referência precisa ser atualizada. Mudanças de projeto, plantões e períodos de fechamento financeiro podem alterar o comportamento normal.

### 4. Combine os sinais

Em vez de criar um alerta para cada evento, atribua maior prioridade quando vários sinais ocorrerem próximos no tempo.

Um exemplo:

- Consulta a dados sensíveis: 3 pontos.
- Volume muito acima da média: 3 pontos.
- Dispositivo desconhecido: 2 pontos.
- Exportação para destino novo: 2 pontos.
- Horário incomum: 1 ponto.
- Mudança recente de permissão: 3 pontos.

Uma ocorrência com poucos pontos pode apenas ser registrada. Uma ocorrência com pontuação elevada pode gerar uma investigação. Esses valores são apenas um exemplo e devem ser ajustados ao perfil da organização.

O horário fora do expediente não deve ser usado como prova isolada. Pesquisas do MITRE recomendam cautela com esse tipo de indicador, pois trabalhar fora do horário normal pode ser comum em determinadas funções.

### 5. Valide antes de tomar uma medida

O sistema deve indicar que existe um comportamento incomum, mas a decisão final deve considerar o contexto.

Antes de bloquear uma conta ou acusar um funcionário, a equipe deve verificar:

- Existe uma solicitação de trabalho relacionada?
- O acesso foi autorizado pelo gestor?
- O usuário estava em plantão?
- O sistema executou uma tarefa automática?
- O arquivo exportado contém realmente dados sensíveis?
- Houve transferência para fora da empresa?
- O mesmo comportamento ocorre com outras pessoas da mesma função?

Em situações de baixo risco, pode ser suficiente solicitar uma justificativa ou acompanhar a atividade. Em casos mais graves, a organização pode limitar temporariamente o acesso, preservar os registros e iniciar o processo interno de resposta.

A CISA organiza a gestão de risco interno em quatro etapas: definir o risco, detectar e identificar sinais, avaliar o caso e administrar a resposta. Essa abordagem ajuda a evitar decisões precipitadas baseadas em um único evento.

## Como reduzir o excesso de alertas

O excesso de alertas é um dos maiores problemas em qualquer equipe de segurança. Quando tudo parece urgente, os casos importantes podem ser ignorados.

Algumas práticas ajudam a manter o controle:

- Criar regras diferentes para cada função.
- Priorizar dados sensíveis e ações de exportação.
- Usar períodos de comparação, em vez de limites fixos.
- Agrupar eventos do mesmo usuário em uma única ocorrência.
- Ignorar tarefas automáticas já conhecidas.
- Permitir que equipes registrem mudanças planejadas.
- Revisar as regras após cada investigação.
- Separar alerta informativo de alerta que exige ação imediata.

Também é importante evitar uma abordagem baseada em desconfiança. O objetivo não deve ser criar um histórico detalhado da vida profissional de cada pessoa, mas detectar ações que possam colocar dados e sistemas em risco.

Uma regra simples pode ser:

> Quanto mais sensível for o dado e mais distante for a ação do comportamento esperado, maior deve ser a prioridade da análise.

## Conclusão

A observabilidade pode cumprir uma função muito maior do que medir desempenho. Quando registros, números de uso e caminhos das operações são analisados em conjunto, eles se tornam uma camada importante de proteção contra abuso interno.

O principal aprendizado dos casos reais é que o risco pode aparecer de formas diferentes: consultas pequenas repetidas ao longo de meses, uma exportação extensa em poucos minutos ou a tentativa de apagar os próprios registros.

A melhor estratégia é combinar contexto, proteção dos registros e análise gradual. Dessa forma, a organização consegue encontrar sinais relevantes sem interromper o trabalho normal nem transformar cada comportamento diferente em uma acusação.

Para empresas que trabalham com grandes volumes de dados, essa integração entre engenharia de dados e segurança representa uma oportunidade prática: os mesmos dados usados para melhorar sistemas também podem ajudar a proteger clientes, funcionários e o próprio negócio.
