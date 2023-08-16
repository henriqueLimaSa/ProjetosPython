Enviando meus projetos para o github

1º click botão direito e selecione "(Open Git Bash here)"

2º no comando promont digite "(git init)" para iniciar o repositório

3º digite "(git status)" para visualizar todos os arquivos que estão dentro da pasta selecionada

4º digite o comando "(git add".nome do arquivo")" para enviar o arquivo que deseja 

5º para adicionar todos os arquivos que estão na sua pasta, basta usar o comando "(git add .)"

6º Para realizar os envios dos arquivos através do promot é necessário enviar o comando
	"(git config --global user.email "escreva teu email")"
	"(git config --global user.name " escreva seu nome")"

7º Para enviar uma atualização de um codigo utilize o comando
	"(git commit -m "adicione o comentário que deseja")"

8º para enviar seus codigos para o github através do repositório criado na conta basta digitar
	passo1	"(git remote add origin "adicionar o link http da sua pagina no git")"
	passo2	"(git push --set-upstream origin master)" realize a confirmação na janela que abrirá
			visualize seu codigo na pagina master


Após a validação para adicionar um novo arquivo é nescessário

git init 
git add. or git add nome-do-arquivo
git commit -m "Descrição do que foi alterado"
git log 
q <-- para sair do log 
git push
