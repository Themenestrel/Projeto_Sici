function inputTipo(tipo) {
	let input = document.getElementById('busca');
	input.removeAttribute('hidden');
	if (tipo == 'cd_ua') {
		input.setAttribute('type', "number");
		input.setAttribute('placeholder', "Digite o Código da Unidade");
	} else {
		input.setAttribute('type', "text");
		if (tipo == 'nome') {
			input.setAttribute('placeholder', "Digite o Nome da Unidade");
		} else {
			input.setAttribute('placeholder', "Digite o Nome do Gestor");
		}
	}
}
