
Text-to-Speech Converter

Uma aplicação gráfica simples desenvolvida em Python que converte texto em áudio. Utilize a biblioteca gTTS (Google Text-to-Speech) para gerar arquivos de áudio em diferentes idiomas e sotaques de forma rápida e prática.


Funcionalidades

Conversão de texto para áudio em formato .mp3.

Suporte a diferentes idiomas (Português, Inglês, Espanhol, Francês, Alemão).

Seleção de sotaques para personalização da voz.

Reprodução imediata do áudio gerado.

Interface gráfica amigável desenvolvida com Tkinter.

Botão para resetar configurações e limpar o campo de texto.


Pré-requisitos

Antes de executar o projeto, certifique-se de ter:

Python 3.x instalado em sua máquina.

As seguintes bibliotecas Python instaladas:

pip install gtts playsound


Como usar

1. Clone o repositório:

git clone https://github.com/seuusuario/text-to-speech-converter.git


2. Navegue até o diretório do projeto:

cd text-to-speech-converter


3. Execute o script principal:

python app.py


4. Insira o texto no campo da interface, selecione o idioma e o sotaque desejado, e clique no botão "Iniciar" para gerar e ouvir o áudio.


Tecnologias utilizadas

Python: Linguagem de programação principal.

gTTS (Google Text-to-Speech): Biblioteca para geração de fala a partir de texto.

playsound: Para reproduzir o áudio gerado.

Tkinter: Interface gráfica.



Estrutura do Projeto

app.py: Código principal da aplicação.

output.mp3: Arquivo de áudio gerado automaticamente.



Melhorias Futuras

Ajustes de velocidade e tom da fala.

Suporte para upload de arquivos de texto.

Opção para salvar os arquivos em diretórios personalizados.

Inclusão de vozes mais realistas ou personalizadas.



Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

