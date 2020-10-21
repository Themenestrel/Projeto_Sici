function inputTipo(tipo) {
	var input = document.getElementById('busca');
	switch (tipo) {
		case 'cod_ua':
		    console.log('cod_ua')
			if (input.type == "number") {
				return
			} else {
				input.setAttribute('type', "number");
				input.setAttribute('placeholder', "Digite o Código da Unidade");
			}
			break;
		case 'nome':
		    console.log('nome')
			input.setAttribute('type', "text");
			input.setAttribute('placeholder', "Digite o Nome da Unidade");

			break;

		case 'gestor':
		    console.log('gestor')
			input.setAttribute('type', "text");
			input.setAttribute('placeholder', "Digite o Nome do Gestor");
			break;
	}
}