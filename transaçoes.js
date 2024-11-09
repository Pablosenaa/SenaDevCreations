// Tenta carregar os dados do Local Storage
let dados = JSON.parse(localStorage.getItem('dados')) || { transacoes: [], receitaTotal: 0, despesaTotal: 0 };

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

    dados.transacoes.push(transacao);

    if (tipo === 'receita') {
        dados.receitaTotal += valor;
    } else {
        dados.despesaTotal += valor;
    }

    atualizarListaTransacoes();
    atualizarResumo();
    salvarDados();

    document.getElementById('descricao').value = '';
    document.getElementById('valor').value = '';
}

function atualizarListaTransacoes() {
    const listaTransacoes = document.getElementById('lista-transacoes');
    listaTransacoes.innerHTML = '';

    dados.transacoes.forEach((transacao) => {
        const li = document.createElement('li');
        li.textContent = `${transacao.descricao}: R$ ${transacao.valor.toFixed(2)} (${transacao.tipo})`;
        listaTransacoes.appendChild(li);
    });
}

function atualizarResumo() {
    document.getElementById('receitas').textContent = dados.receitaTotal.toFixed(2);
    document.getElementById('despesas').textContent = dados.despesaTotal.toFixed(2);
    document.getElementById('saldo').textContent = (dados.receitaTotal - dados.despesaTotal).toFixed(2);

    atualizarCores(); 
}

function salvarDados() {
    localStorage.setItem('dados', JSON.stringify(dados));
}

function toggleMenu() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('active');
}

document.addEventListener('DOMContentLoaded', () => {
    atualizarListaTransacoes();
    atualizarResumo();
});


function atualizarCores() {
    const receitas = parseFloat(document.getElementById("receitas").textContent);
    const despesas = parseFloat(document.getElementById("despesas").textContent);
    const saldo = parseFloat(document.getElementById("saldo").textContent);

    // Receitas
    document.getElementById("receitas").style.color = receitas > 0 ? "green" : "red";

    // Despesas
    document.getElementById("despesas").style.color = despesas > 0 ? "red" : "green";

    // Saldo
    document.getElementById("saldo").style.color = saldo >= 0 ? "green" : "red";  
}

// Função para apagar todo o histórico de transações
function apagarHistorico() {
    if (confirm("Tem certeza que deseja apagar todo o histórico de transações?")) {
        dados = { transacoes: [], receitaTotal: 0, despesaTotal: 0 }; // Reseta os dados
        salvarDados(); // Salva os dados resetados no Local Storage
        atualizarListaTransacoes(); // Atualiza a lista de transações
        atualizarResumo(); // Atualiza o resumo
    }
}

// Chamadas iniciais
atualizarCores();
