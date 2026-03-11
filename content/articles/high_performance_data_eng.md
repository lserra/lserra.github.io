Title: High Performance Data Engineering
Date: 2026-03-15 00:00
Modified: 2026-03-15 00:00
Category: Data Engineering
Slug: data-eng
Summary: Golang (Go) para Engenharia de Dados de Alto Desempenho
Tags: static, site, pelican, markdown, data engineering, code, go
Authors: Laercio Serra
Status: published

# Whats the idea?

Hoje eu irei falar da linguagem de programação Golang (Go) e como ela pode ser estrategicamente utilizado para construir sistemas de engenharia de dados de 
alto desempenho, especialmente em arquiteturas cloud-native.
Mas **não** é utilizado (ainda), porque o seu ecossitema é pequeno (ainda), se comparado com o ecossistema do Python. 
Porém, isso não significa que não seja possível usar esta linguagem de programação neste universo.
E quando pensamos ou falamos em engenharia de dados de alto desempenho, esta deveria ser a nossa primeira opção. 
Na verdade Go, se apresenta como uma escolha robusta para data pipelines e sistemas modernos devido às suas forças inerentes em **concorrência, eficiência e 
baixo consumo de recursos**. Seus principais achados incluem ganhos significativos de desempenho e a redução de custos operacionais em implantações na nuvem. 
Podemos dizer que Go é idealmente posicionado como um **motor de alta performance** dentro de uma arquitetura de dados poliglota (complementando linguagens como Python 
para tarefas especializadas).
E hoje, esta é a ideia que eu quero apresentar ou passar neste post.

# Quick Overview

Para um melhor entendimento, antes eu vou falar do cenário em evolução da Engenharia de Dados e uma possível ascensão do Golang.
A engenharia de dados é impulsionada pela escalada do volume, velocidade e variedade de dados (Big Data), exigindo processamento em tempo real, escalabilidade e 
eficiência de custos. O Go, é uma linguagem compilada e tipada estaticamente desenvolvida no Google, foi concebida com simplicidade e eficiência, alinhando-se 
perfeitamente com o "imperativo de desempenho" do setor. Um exemplo notável de caso de uso (projeto de cidade inteligente) em que demonstrou uma **redução de 90% na 
latência de processamento e 60% nos custos de infraestrutura de nuvem** após a migração de processos ETL de Python para Go.

# Go Attributes

Podemos destacar alguns atributos da linguagem Go que vão de encontro à Excelência em Engenharia de Dados:

## Desempenho: Compilação, Velocidade e Eficiência

Como uma linguagem compilada, o Go se traduz diretamente em código de máquina, resultando em velocidades de execução superiores para tarefas que exigem muita CPU. 
Sua eficiência se traduz em uma menor pegada de memória e menor uso de CPU, o que impacta diretamente a capacidade de usar instâncias de nuvem menores ou em menor 
número, diminuindo os custos operacionais.

## Concorrência: Goroutines, Channels e Processamento Paralelo

A linguagem Go, também se destaca pelo seu suporte embutido à concorrência através de goroutines (funções leves e concorrentes) e channels (canais tipados para 
comunicação e sincronização). Esse modelo é perfeitamente adequado para tarefas I/O-bound (como leitura de múltiplas fontes de dados) e para a criação de pipelines
distribuídos e robustos, evitando falhas comuns associadas à memória compartilhada.

## Simplicidade e Legibilidade: Impacto no Desenvolvimento e Manutenção

Com uma sintaxe concisa (apenas 25 palavras-chave) e uma biblioteca padrão abrangente, o Golang oferece uma curva de aprendizado relativamente suave. 
Sua simplicidade e código explícito facilitam a leitura e a manutenção de plataformas de dados de grande escala e longa duração, priorizando a produtividade da 
equipe e a consistência do código.

## Tipagem Estática e Tratamento de Erros: Construindo Sistemas de Dados Robustos

O sistema de tipagem estática do Go permite que classes de erros sejam detectadas durante a compilação. Seu mecanismo de tratamento de erros explícito 
(funções retornam um valor de erro que deve ser verificado, ex: if err != nil) força os desenvolvedores a considerar e endereçar conscientemente as falhas, 
aumentando a robustez dos sistemas de dados em produção.

## Pegada de Recurso: Implicações para Custo e Escalabilidade

As aplicações Go têm um consumo modesto de recursos, o que é uma grande vantagem em ambientes de nuvem onde o uso de recursos está ligado ao custo. 
A capacidade de compilar para um único binário estaticamente ligado simplifica drasticamente o processo de implantação, acelera a construção de imagens de 
contêineres (Docker) e facilita a orquestração em plataformas como Kubernetes.

# Golang vs. Python

Como mencionado anteriormente, embora o Python continue a dominar a Engenharia/Ciência de Dados devido ao seu vasto ecossistema, o Golang é a alternativa mais 
convincente quando os requisitos são desempenho bruto e concorrência para a infraestrutura subjacente de dados.

# High Performance Pipelines (ETL/ELT)

As concorrências (data race) do Go são ideais para pipelines ETL/ELT, utilizando goroutines para processamento paralelo e channels para gerenciar o fluxo de 
dados entre estágios (fan-in e fan-out). O gerenciamento cuidadoso de alocação de memória e o uso de canais Go simples (em vez de sistemas complexos de filas) 
podem otimizar o fluxo de dados e a manutenibilidade.

O ecossistema para tarefas de engenharia de dados (serialização de dados, bancos de dados, filas de mensagens) é robusto. 
O Go se integra bem com AWS, GCP e Azure, oferecendo SDKs maduros. Sua força estratégica é construir componentes personalizados e de alto desempenho (como agentes 
de ingestão ou microsserviços de processamento) que aumentam ou se integram com serviços de dados gerenciados da nuvem (ex: S3, BigQuery, Kinesis, Pub/Sub), em vez
de tentar replicar funcionalidades de grandes serviços gerenciados como AWS Glue, GCP Dataflow ou Azure Data Factory.

# The Future (Big Data, AI/ML)

Se você percebe que existe na sua organização, a necessidade de que para obter resultados extraordinários é necessário mudar de paradigma, eu sugiro que a adoção
seja incremental e focada em problemas. Recomendo começar com um gargalo específico, construir Proof-of-Concepts (PoCs) para benchmark. Depois investir 
em treinamento e garantir a integração incremental com sistemas existentes usando interfaces padronizadas (REST APIs, gRPC, filas de mensagens).

Embora não seja, atualmente, a principal linguagem de treinamento de modelos de IA/ML (pois o domínio é do Python), o Go aos poucos está ganhando terreno em:
- **Serviço de Inferência de ML**: sua alta performance e baixa latência o tornam excelente para a implantação de servidores de inferência de modelos em tempo real.
- **Pré-processamento de Dados**: oferece ganhos significativos de velocidade para tarefas intensivas de pré-processamento e engenharia de features para grandes conjuntos de dados.
- **Ferramentas de Infraestrutura**: continua sendo a linguagem dominante em ferramentas de infraestrutura cloud-native (Docker, Kubernetes, Prometheus).

Este é um artigo introdutório, sobre as minhas descobertas desta linguagem, aplicada no campo da Engenharia de Dados. E nos próximos artigos, eu trarei mais detalhes 
sobre o uso prático e os resultados obtidos, com esta linguagem de programação.

Stay safe, stay at home-office!
