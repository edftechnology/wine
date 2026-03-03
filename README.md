# Como configurar/instalar/configurar o `Wine` no `Linux Ubuntu`

## Resumo

Neste documento estão contidos os principais comandos e configurações para configurar/instalar/configurar o `Wine` no `Linux Ubuntu`.

## _Abstract_

_This document contains the main commands and settings for configuring/installing/use `Wine` on `Linux Ubuntu`._

### Descrição

### `wine`

O `Wine` é uma camada de compatibilidade que permite executar aplicativos do `Windows` em sistemas operacionais baseados em `Unix`, como `Linux` e `macOS`. Ele traduz chamadas de sistema do `Windows` para o ambiente `Unix` correspondente, permitindo que programas desenvolvidos para `Windows` sejam executados sem a necessidade de uma instalação do sistema operacional `Windows`. Essa ferramenta é especialmente útil para usuários que precisam executar aplicativos específicos do `Windows` em plataformas diferentes.


## 1. Configurar/Instalar/Usar o `Wine` no `Linux Ubuntu` [1]

Para instalar o `Wine` no `Linux Ubuntu`, você pode seguir estas etapas:

1. Abrir o `Terminal Emulator`. Você pode fazer isso pressionando:

    ```bash
    Ctrl + Alt + T
    ```


2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
    ```bash
    sudo apt clean
    ```
    
    2.2 Remover pacotes `.deb` antigos ou duplicados do `cache` local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
    ```bash
    sudo apt autoclean
    ```

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
    ```bash
    sudo apt autoremove -y
    ```

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`:
    ```bash
    sudo apt update
    ```

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
    ```bash
    sudo apt --fix-broken install
    ```

    2.6 Limpar o `cache` do gerenciador de pacotes `apt` novamente:
    ```bash
    sudo apt clean
    ```
    
    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:
    ```bash
    sudo apt list --upgradable
    ```

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
    ```bash
    sudo apt full-upgrade -y
    ```
    

3. **Preparação:** Se o seu sistema é 64 bit, habilite a arquitetura 32 (se você não já tiver):

    ```bash
    sudo dpkg --add-architecture i386
    sudo apt update
    ```

4. **Garantir que main + universe estão ativos**:

    ```bash
    sudo add-apt-repository main
    sudo add-apt-repository universe
    sudo add-apt-repository multiverse
    sudo apt update
    ```

5. **Adicionar o(s) repositório(s):** baixar e adicionar a chave do repositório:

    ```bash
    sudo mkdir -pm755 /etc/apt/keyrings
    sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key
    sudo wget -NP /etc/apt/sources.list.d/ \
        https://dl.winehq.org/wine-builds/ubuntu/dists/jammy/winehq-jammy.sources
    sudo apt update
    ```

6. **Instalar o `Wine`**:

    ```bash
    sudo apt install --install-recommends winehq-stable -y
    ```

7. **Criar o prefixo inicial do `Wine`** Na primeira execução, rode:

    ```bash
    winecfg
    ```

    Isso irá:

    - Criar o diretório `~/.wine`

    - Configurar ambiente Windows padrão (geralmente `Windows 10`)

    - Instalar componentes básicos

8. Ao abrir a janela de configuração, está tudo certo, cliclar em `Install`:

    <div align="center">
        <img src="docs/figures/wine_mono_installer.png" alt="Minha Imagem" />
        <p>Fig. 1 Wine Mono Installer.</p>
    </div>        

9. **Verificar instalação**

    ```bash
    wine --version
    ```

    Se aparecer algo como:

    ```bash
    wine-11.x
    ```

    Está instalado corretamente.

10. **Instalar o `winetricks`**:

    ```bash
    sudo apt install winetricks -y
    ```

11. **Verificar versão do `winetricks`**:

    ```bash
    winetricks --version
    ```

    Se aparecer algo como:

    ```bash
    20210206 - sha256sum: xxx
    ```

    Está instalado corretamente.


### 1.2 Código completo para configurar/instalar/usar

Para configurar/instalar/usar o `wine` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abrir o `Terminal Emulator`. Você pode fazer isso pressionando:

    ```bash
    Ctrl + Alt + T
    ```

2. Digite o seguinte comando e pressione `Enter`:

    ```bash
    sudo apt clean
    sudo apt autoclean
    sudo apt autoremove -y
    sudo apt update
    sudo apt --fix-broken install
    sudo apt clean
    sudo apt list --upgradable
    sudo apt full-upgrade -y
    sudo dpkg --add-architecture i386
    sudo apt update
    sudo add-apt-repository main
    sudo add-apt-repository universe
    sudo add-apt-repository multiverse
    sudo apt update
    sudo mkdir -pm755 /etc/apt/keyrings
    sudo wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key
    sudo wget -NP /etc/apt/sources.list.d/ \
        https://dl.winehq.org/wine-builds/ubuntu/dists/jammy/winehq-jammy.sources
    sudo apt update
    sudo apt install --install-recommends winehq-stable -y
    wine --version
    winecfg
    sudo apt install winetricks -y
    winetricks --version
    ```

## 2. Troubleshooting: conflito entre versões `amd66` e `i386`

Se ocorrer erro como:

```bash
libgstreamer1.0-0:i386 : Depends: libdw1:i386
```

Verifique as versões:

```bash
apt policy libelf1 libelf1:i386
```

Se as versões forem diferentes, pode ser necessário alinhar manualmente:

```bash
sudo apt install libelf1=<versao> libelf1:i386=<versao>
```

Substitua `<versao>` pela versão disponível no seu sistema.

## Referências

[1] OPENAI. ***Instalar o `wine` no `linux ubuntu` pelo `terminal emulator`.*** Disponível em: <https://chatgpt.com/g/g-p-6980caf949648191ad6acfcdbe590f9e-instalar/c/69a549e6-0bac-8328-afc9-8d03a4a89441> (texto adaptado). Acessado em: 02/03/2026 00:37.

[2] WINE HQ TEAM. ***Ubuntu winehq repository.*** Disponível em: <https://wiki.winehq.org/Ubuntu> (texto adaptado). Acessado em: 21/10/2023 00:09.

[3] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 09/02/2024 00:37.


