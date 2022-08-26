<h1> Automatizar o "Unzipe" dos arquivos baixados. </h1>
<p>Quem nunca perdeu tempo tendo que fazer o processo de "unzipar" uma pasta ao baixar o arquivo? E quando são vários arquivos zipados é pior ainda. Temos que entrar um por um, clicar com o botão direito e procurar a opção de "unzipar" e depois excluir a pasta".zip" original.</p> 
<p>O projeto é um código em Python, desenvolvido no Pycharm para automatizar esse processo chato de "unzipar" os arquivos.</p>

<h2> Bibliotecas Utilizadas </h2>
<p>- Zipfile</p>
<p>- Os</p>
<p>- Time</p>
<p>- Watchdog</p>

<h2> Como funciona? </h2>
<p>Primeiramente usamos a biblioteca Watchdog para monitorar os arquivos de uma determinada pasta, nesse caso é a pasta "Downloads". Onde cada vez que houver uma criação de pasta nela, vamos rodar o código para "unzipar".</p>
<p>Rodamos o código para "unzipar", onde percorremos a pasta "Downloads" com um for, procurando arquivos com extensão ".zip" nele. Ao encontramos utilizamos a biblioteca Zipfile para realizar o "unzipe", depois excluímos o arquivo original ".zip" com a biblioteca OS.</p>
<p>Para tornarmos esse processo contínuo precisamos seguir dois passos:</p>
<p>- Tornar o arquivo executável, com o pystaller --onefile --noconsole, onde não abriremos a tela do programa.</p>
<p>- Criar um atalho do executável e colocarmos ele na pasta "Startup" do Windows.</p>
<p>- Reiniciar o computador para quando iniciar, o programa já começar a rodar no background.</p>

<p>As vezes precisamos dar um F5 para atualizarmos a pasta quando entrar um arquivo ".zip".</p>
