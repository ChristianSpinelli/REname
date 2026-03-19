# REname 🚀

**REname** é uma ferramenta desenvolvida para automatizar a **renomeação de arquivos em lote**, inspirada por uma necessidade real de escritório.  

Minha noiva, que é advogada, precisava renomear documentos repetidamente seguindo um padrão específico. Para otimizar essa tarefa, criei esta aplicação em **Python** para **Windows**, tornando o processo rápido e eficiente.

---

## ✨ Funcionalidades

- ✅ Renomeação automática de arquivos em **lote**  
- ✅ Definição de **padrões personalizados** de nomes  
- ✅ Economia de tempo em tarefas repetitivas de escritório  
- ✅ Interface simples e intuitiva (**GUI**)  

---

## 🛠 Pré-requisitos

- Python 3.7 ou superior (para rodar via script `.py`)  
- Biblioteca PyInstaller (apenas se for gerar o executável)  

## Instalação do PyInstaller:

pip install pyinstaller
Como usar
1. Executando o projeto no Python
python main.py
2. Gerando um executável para Windows
pyinstaller --noconsole --onefile main.py

O executável final ficará na pasta dist/ e pode ser usado em qualquer máquina Windows sem precisar do Python instalado.

## Exemplo de uso

Suponha que você tenha uma pasta com arquivos como:

documento1.pdf  
documento2.docx  
documento3.xlsx  

Com REname, você pode renomeá-los rapidamente para um padrão como:

documento1 - NOME CLIENTE.pdf  
documento2 - NOME CLIENTE.docx  
documento3 - NOME CLIENTE.xlsx

Basta colocá-los na mesma pasta, informar para o REname a pasta em que estão os arquivos, informar o texto a ser adicionado no final (opcional), 
adicionar o texto que deseja remover (opcional) e então a aplicação irá renomear todos os arquivos daquela pasta com o padrão informado.  

obs.:
- É obrigatório informar pelo menos um campo de texto, mas caso mande um o outro se torna opcional, permitindo que o usuário possa apenas remover ou 
adicionar texto.
- Caso um texto a ser removido não esteja presente em todos os arquivos da pasta, ele irá remover apenas os que possuem o texto e não irá retornar erro.
- O sistema considera diferenças de maiúsculo ou minúsculo, então caso deseje remover deve ser digitado da mesma forma que está escrito.
- Por padão remove apenas a primeira ocorrência, mas pode marcar um checkbox para remover todas as ocorrências
- Caso remova e insira ao mesmo tempo o texto inserido será na posição do texto que foi removido.  

## Contribuindo

Se quiser melhorar o projeto, adicionar novos recursos ou corrigir bugs, fique à vontade para abrir um pull request ou enviar issues.

## Licença

Este projeto é open-source e pode ser usado livremente.
