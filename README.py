#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/configurar o `Wine` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/configurar o `Wine` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/use `Wine` on `Linux Ubuntu`._

# ### Descrição
# 
# ### `wine`
# 
# O `Wine` é uma camada de compatibilidade que permite executar aplicativos do `Windows` em sistemas operacionais baseados em `Unix`, como `Linux` e `macOS`. Ele traduz chamadas de sistema do `Windows` para o ambiente `Unix` correspondente, permitindo que programas desenvolvidos para `Windows` sejam executados sem a necessidade de uma instalação do sistema operacional `Windows`. Essa ferramenta é especialmente útil para usuários que precisam executar aplicativos específicos do `Windows` em plataformas diferentes.
# 

# ## 1. Configurar/Instalar/Usar o `Wine` no `Linux Ubuntu` [1]
# 
# Para instalar o `Wine` no `Linux Ubuntu`, você pode seguir estas etapas:
# 
# 1. Abrir o `Terminal Emulator`. Você pode fazer isso pressionando:
# 
#     ```bash
#     Ctrl + Alt + T
#     ```
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
#     ```bash
#     sudo apt clean
#     ```
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do `cache` local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
#     ```bash
#     sudo apt autoclean
#     ```
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
#     ```bash
#     sudo apt autoremove -y
#     ```
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt update
#     ```
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
#     ```bash
#     sudo apt --fix-broken install
#     ```
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt` novamente:
#     ```bash
#     sudo apt clean
#     ```
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt list --upgradable
#     ```
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt full-upgrade -y
#     ```
#     

# 3. **Preparação:** Se o seu sistema é 64 bit, habilite a arquitetura 32 (se você não já tiver):
# 
#     ```bash
#     sudo dpkg --add-architecture i386
#     ```
# 
# 4. **Garantir que main + universe estão ativos**:
# 
#     ```bash
#     sudo add-apt-repository main
#     sudo add-apt-repository universe
#     sudo add-apt-repository multiverse
#     ```
# 
# 5. **Atualizar novamente**:
# 
#     ```bash
#     sudo apt update
#     ```
# 
# 6. **Verificar se `libdw1:i386` existe**:
# 
#     ```bash
#     apt policy libdw1:i386
#     ```
# 
#     Você deve ver algo como:
# 
#     ```bash
#     Candidate: 0.186-1ubuntu0.1
#     ```
# 
#     Se aparecer `none`, ainda há problema no repositório.
# 
# 7. **Vamos alinhar manualmente as bibliotecas base para a mesma versão**: Execute:
# 
#     ```bash
#     sudo apt install libelf1=0.186-1ubuntu0.1 libelf1:i386=0.186-1ubuntu0.1
#     ```
# 
# 8. **Adicionar o repositório:** baixar e adicionar a chave do repositório:
# 
#     ```bash
#     sudo mkdir -pm755 /etc/apt/keyrings
#     sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key
#     ```
# 
# 9. **Primeiro descubra sua versão**:
# 
#     ```bash
#     lsb_release -a
#     ```
# 
# 10. **Adicionar o repositório correto para sua versão do `Linux Ubuntu`**: 
# 
#     ```bash
#     sudo wget -NP /etc/apt/sources.list.d/ https://dl.winehq.org/wine-builds/ubuntu/dists/jammy/winehq-jammy.sources
#     ```
# 
# 11. **Atualizar novamente**:
# 
#     ```bash
#     sudo apt update
#     ```
# 
# 12. **Instalar o `Wine`**: Você pode escolher entre:
# 
#  - **Versão estável (recomendado)**:
# 
#     ```bash
#     sudo apt install wine-stable
#     sudo apt install --install-recommends winehq-stable
#     ```
# 
#     - **Versão staging (mais experimental)**:
# 
#     ```bash
#     sudo apt install wine-stable
#     sudo apt install --install-recommends winehq-staging
#     ```
# 
# 13. **Verificar instalação**
# 
#     ```bash
#     wine --version
#     ```
# 
#     Se aparecer algo como:
# 
#     ```bash
#     wine-9.x
#     ```
# 
#     Está instalado corretamente.
# 
# 14. **Criar o prefixo inicial do `Wine`** Na primeira execução, rode:
# 
#     ```bash
#     winecfg
#     ```
# 
#     Isso irá:
# 
#     - Criar o diretório ~/.wine
# 
#     - Configurar ambiente Windows padrão (geralmente `Windows 10`)
# 
#     - Instalar componentes básicos
# 
#     Se abrir a janela de configuração, está tudo certo.
# 
# 15. Quando a GUI do `Wine` abrir, clicar em `Install`
# 
# 16. **Verificar arquitetura ativa**:
# 
#     ```bash
#     wine --version
#     ```
# 
# 17. **Instalar o `winetricks`**:
# 
#     ```bash
#     sudo apt install winetricks -y
#     ```
# 

# ## 2. Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `wine` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abrir o `Terminal Emulator`. Você pode fazer isso pressionando:
# 
#     ```bash
#     Ctrl + Alt + T
#     ```
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```bash
#     sudo apt clean
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo dpkg --add-architecture i386
#     sudo mkdir -pm755 /etc/apt/keyrings
#     sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key
#     ```

# ## Referências
# 
# [1] OPENAI. ***Instalar o `wine` no `linux ubuntu` pelo `terminal emulator`.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 02/03/2026 00:37.
# 
# [2] WINE HQ TEAM. ***Ubuntu winehq repository.*** Disponível em: <https://wiki.winehq.org/Ubuntu> (texto adaptado). Acessado em: 21/10/2023 00:09.
# 
# [3] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 09/02/2024 00:37.
# 
# 
