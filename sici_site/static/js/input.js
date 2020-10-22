function inputTipo(tipo) {
	let input = document.getElementById('busca');
	switch (tipo) {
		case 'cd_ua':
			input.setAttribute('type', "number");
			input.setAttribute('placeholder', "Digite o Código da Unidade");
			break;
		case 'nome':
			input.setAttribute('type', "text");
			input.setAttribute('placeholder', "Digite o Nome da Unidade");
			break;

		case 'gestor':
			input.setAttribute('type', "text");
			input.setAttribute('placeholder', "Digite o Nome do Gestor");
			break;
	}
}