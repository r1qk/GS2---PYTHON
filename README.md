# GS2 - Pensamento computacional e automação com Python
## Integrantes
Nome: Pedro Mitsuo Risardi Nisiaymamoto RM: 561710 <br>
Nome: Riquelme Santos da Mata RM: 565053 <br>
Nome: Rodrigo Kenshin Viana Matayoshi RM: 564026 <br>

### Descrição do projeto
O projeto é uma simulação de uma empresa fictícia chamada "Readict". Essa empresa é responsável por recomendar profissões para o futuro 
com base nas melhores aptidões relatadas pelos usuários. O código foi desenvolvido em Python, e está disponível nesse reposistório para 
testes.

### Divisão do projeto
O sistema foi dividido em quatro arquivos: 
* **main.py:** Arquivo principal do projeto, responsável por executar o programa, integrar todos os outros módulos e apresentar a interface
  ao usuário, funcionando como o front-end da aplicação. Todos os outros arquivos são importados para o arquivo main.

* **back.py:** Atua como o backend, criando e gerenciando o arquivo JSON onde as leads são armazenadas, além de realizar toda a lógica de
  salvamento dos dados.

* **model.py:** Contém o modelo que define a estrutura de uma lead.

* **recommendation.py:** Reúne todas as recomendações de profissões utilizadas pelo sistema.

### Como funciona?

O projeto possui um menu interativo no arquivo main.py que permite o usuário escolher uma entre três opcções: 
* **[1] Cadastrar perfil:** O usuário irá digitar seu nome e uma nota para cada aptidão pré-programada, sendo elas: Lógica, Adaptabilidade, Criatividade e Colaboração. As maiores duas notas
  serão utilizadas para fazer uma recomendação de profissão. Todas as combinações estão registradas no arquivo recommendation.py

* **[2] Exibir cadastros:** Aqui o sistema irá mostrar todos os cadastros registrados em uma lead que serão exibidas, por ordem de cadastro, número de cadastro, nome do cliente e a profissão
  sugerida.

* **[3] Sair:** Quando a opção 3 é escolhida, o sistema se encerra e chega ao fim.

O back.py possui a classe **LeadRepository**, aqui é onde o arquivo JSON é criado e usado para armazenar cada um dos registros dos clientes. Vale mencionar que foram utilizadas as bibliotecas 
pathlib e json para criar ou percorrer por um repositório e criar ou ler um arquivo JSON.
O model.py tem a estrutura das leads utilizadas no arquivo JSON, especificando quais informações cada lead deve ter antes de ser registrada no JSON. 
O recomendation.py possui todas as recomendações que podem ser sugeridas, com base nas principais notas que o usuário digitar. 

## Instruções de funcionamento
Primeiramente, é necessário baixar este código para colocá-lo em prática em alguma IDE. Foi utilizado VSCODE, entretanto Pycharm também funcionará normalmente. <br>
Quando rodar o código, irá aparecer um menu de escolha para o usuário.

```
=== READICT - SISTEMA DE RECOMENDAÇÃO DE PROFISSÕES ===
A partir de sua nota para certas aptidões, recomendamos uma profissão!
[1] Cadastrar perfil
[2] Exibir cadastros
[3] Sair
```
Caso o usuário digite 1, ele irá prencher com seu nome e as notas que ele mesmo decidir atribuir. Foi utilizado um sistema restrito em que apenas números são aceitos, tanto inteiros quanto decimais. <br>
```
Digite o número da ação desejada: 1
Digite seu nome: Milo  
Digite uma nota para lógica: 9
Digite uma nota para adaptabilidade: 8
Digite uma nota para criativdade: 7
Digite uma nota para colaboração: 10
Profissão recomendada: Analista de Negócios ou Scrum Master técnico
Perfil cadastrado e profissão sugerida!
```
Caso o usuário digite 2, todos os registros serão exibidos.
```
Digite o número da ação desejada: 2
## | Nome                 | Profissão sugerida  
00 | Aguiar               | Designer de inovação ou Consultor de Transformação Digital
01 | Milo                 | Analista de Negócios ou Scrum Master técnico
```
Caso o usuário digite 3, o programa se encerra. 
```
Digite o número da ação desejada: 3
Saindo... Até mais!
```
### Link do vídeo do sistema funcionando

[https://www.youtube.com/watch?v=bEblULb9vJk](https://www.youtube.com/watch?v=bEblULb9vJk)





  
