let transacoes = [];

function adicionarTransacao() {
    const descricao = document.getElementById('descricao').value;
    const valor = parseFloat(document.getElementById('valor').value);
    const tipo = document.getElementById('tipo').value;

    if (!descricao || isNaN(valor)) {
        alert("Por favor, preencha todos os campos.");
        return;
    }

    const transacao = {
        descricao,
        valor,
        tipo,
    };

    transacoes.push(transacao);
    atualizarListaTransacoes();
    atualizarResumo();
    
    document.getElementById('descricao').value = '';
    document.getElementById('valor').value = '';
}

function atualizarListaTransacoes() {
    const listaTransacoes = document.getElementById('lista-transacoes');
    listaTransacoes.innerHTML = '';

    transacoes.forEach((transacao) => {
        const li = document.createElement('li');
        li.textContent = `${transacao.descricao}: R$ ${transacao.valor.toFixed(2)} (${transacao.tipo})`;
        listaTransacoes.appendChild(li);
    });
}

function atualizarResumo() {
    let receitaTotal = 0;
    let despesaTotal = 0;

    transacoes.forEach(transacao => {
        if (transacao.tipo === 'receita') {
            receitaTotal += transacao.valor;
        } else {
            despesaTotal += transacao.valor;
        }
    });

    document.getElementById('receitas').textContent = receitaTotal.toFixed(2);
    document.getElementById('despesas').textContent = despesaTotal.toFixed(2);
    document.getElementById('saldo').textContent = (receitaTotal - despesaTotal).toFixed(2);
}

function toggleMenu() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('active');
}
