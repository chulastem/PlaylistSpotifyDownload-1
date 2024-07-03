# Spotify Downloader

Spotify Downloader é uma aplicação Python que permite aos usuários baixar faixas, álbuns e playlists do Spotify. Ele utiliza a API Web do Spotify para buscar informações das músicas e usa `ytmdl` para realizar o download das músicas.

## Funcionalidades

- Baixe faixas individuais, álbuns ou playlists inteiras do Spotify.
- Busque e exiba capas de álbuns durante o processo de download.
- Pause e retome downloads.
- Cancele downloads.
- Gere um relatório de todas as faixas baixadas.

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados no seu sistema:

1. Python 3.7+
2. `ytmdl` - uma ferramenta para baixar músicas do YouTube:
    ```bash
    pip install ytmdl
    ```
3. Outras bibliotecas Python necessárias:
    ```bash
    pip install spotipy ttkbootstrap requests pillow
    ```

## Instalação

1. Clone este repositório para sua máquina local:
    ```bash
    git clone https://github.com/seuusuario/spotify-downloader.git
    cd spotify-downloader
    ```

2. Instale as bibliotecas Python necessárias:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure suas credenciais da API do Spotify:
    - Crie uma conta de desenvolvedor Spotify e crie uma aplicação no [Painel de Desenvolvedor Spotify](https://developer.spotify.com/dashboard/applications).
    - Anote seu `Client ID` e `Client Secret`.

4. Atualize as variáveis `client_id` e `client_secret` no código com suas credenciais da API do Spotify:
    ```python
    client_id = 'seu_client_id'
    client_secret = 'seu_client_secret'
    ```

## Uso

1. Execute a aplicação:
    ```bash
    python spotify_downloader.py
    ```

2. Insira a URL do Spotify da faixa, álbum ou playlist que você deseja baixar no campo "Spotify URL".

3. Opcionalmente, adicione um sufixo que será anexado aos nomes dos arquivos baixados.

4. Clique no botão "Download" e selecione um diretório para salvar os arquivos baixados.

5. A aplicação exibirá o progresso do download e mensagens de log na interface gráfica.

6. Use os botões "Pause Download" e "Cancel Download" para controlar o processo de download.

## Visão Geral da Interface

- **Spotify URL**: Insira a URL da faixa, álbum ou playlist do Spotify que você deseja baixar.
- **Optional Suffix**: Insira um sufixo que será anexado aos nomes dos arquivos baixados (ex: " - Ao Vivo", " - Acústico").
- **Download**: Inicia o processo de download.
- **Progress Bar**: Mostra o progresso geral do download.
- **Progress Log**: Exibe mensagens de log e atualizações durante o processo de download.
- **Cancel Download**: Cancela o download em andamento.
- **Pause Download**: Pausa o download em andamento. Este botão alterna entre "Pause Download" e "Resume Download".
- **Album Cover**: Exibe a capa do álbum da faixa que está sendo baixada no momento.

## Detalhes do Funcionamento do Código


