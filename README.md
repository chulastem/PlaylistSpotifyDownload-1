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


<<<<<<< HEAD
=======
Siga estas etapas para configurar o ambiente e executar o projeto:

1. Faça o download do código-fonte do projeto e salve-o em um diretório de sua escolha.

2. Abra o prompt de comando e navegue até o diretório onde você salvou o código-fonte do projeto.

3. Crie um ambiente virtual (opcional): Embora não seja obrigatório, é recomendável criar um ambiente virtual para isolar as dependências do projeto. Execute o seguinte comando para criar um ambiente virtual chamado "env":

   ```bash
   python -m venv env
   ```

4. Ative o ambiente virtual (opcional): Se você optou por criar um ambiente virtual, ative-o executando o seguinte comando:

   - No Windows:

     ```bash
     .\env\Scripts\activate
     ```

5. Instale as dependências: Use o gerenciador de pacotes `pip` para instalar as dependências necessárias. Execute o seguinte comando para instalar as dependências:

   ```bash
   pip install spotipy youtube-search moviepy pytube
   ```

6. Configure as credenciais do Spotify: Antes de executar o projeto, você precisa configurar as credenciais do cliente do Spotify. Acesse o [Dashboard de Desenvolvedor do Spotify](https://developer.spotify.com/dashboard/) e faça login ou crie uma conta. Crie um novo aplicativo e obtenha o ID do cliente e o segredo do cliente. Substitua as variáveis `client_id` e `client_secret` no código-fonte pelo seu ID de cliente e segredo de cliente, respectivamente.

7. Configure o link da playlist do Spotify: No código-fonte, substitua o valor da variável `playlist_url` pelo link da playlist do Spotify que você deseja baixar.

8. Execute o projeto: Após concluir as etapas acima, você está pronto para executar o projeto. Use o seguinte comando para iniciar a execução:

   ```bash
   python seu_arquivo.py
   ```

   Certifique-se de substituir `seu_arquivo.py` pelo nome do arquivo que contém o código-fonte do projeto.

9. Selecione o diretório de download: Quando o projeto for iniciado, uma janela de diálogo será exibida para selecionar o diretório onde as músicas serão baixadas. Navegue até o diretório desejado e clique em "OK".

10. Aguarde o processo de download: O projeto começará a pesquisar os links do YouTube para cada faixa da playlist do Spotify e baixará as músicas correspondentes no diretório selecionado. Aguarde até que todas as músicas sejam baixadas.

11. Verifique as músicas baixadas: Após o término do processo de download, verifique o diretório selecionado para encontrar as músicas baixadas. As músicas serão nomeadas no formato `<nome_da_faixa>.mp3`.

>>>>>>> 9646c085feb1c35aa3c4f6deebdb84b581a4bf88
