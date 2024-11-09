window.onload = function() {
    carregarHistorico();
};

function carregarHistorico() {
    let historicoTransacoes = document.getElementById('historico-transacoes');
    
  
    let dados = JSON.parse(localStorage.getItem('dados')) || { transacoes: [] };

    historicoTransacoes.innerHTML = ''; 

    if (dados.transacoes.length === 0) {
        historicoTransacoes.innerHTML = '<li>Não há transações no histórico.</li>';
    } else {
        dados.transacoes.forEach(transacao => {
            let li = document.createElement('li');
            li.innerHTML = `
                <span>${transacao.descricao} - R$ ${transacao.valor.toFixed(2)} (${transacao.tipo})</span>
            `;
            historicoTransacoes.appendChild(li);
        });
    }
}


function limparHistorico() {
    if (confirm('Tem certeza que deseja limpar o histórico?')) {
        localStorage.removeItem('dados');  
        carregarHistorico();               
    }
}


function toggleMenu() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('active');
}

function carregarHistorico() {
    let historicoTransacoes = document.getElementById('historico-transacoes');
    let dados = JSON.parse(localStorage.getItem('dados')) || { transacoes: [] };

    historicoTransacoes.innerHTML = ''; 

    if (dados.transacoes.length === 0) {
        historicoTransacoes.innerHTML = '<li>Não há transações no histórico.</li>';
    } else {
        dados.transacoes.forEach(transacao => {
            let li = document.createElement('li');
            li.innerHTML = `
                <span class="${transacao.tipo === 'despesa' ? 'despesa' : 'receita'}">
                    ${transacao.descricao} - R$ ${transacao.valor.toFixed(2)} (${transacao.tipo})
                </span>
            `;
            historicoTransacoes.appendChild(li);
        });
    }
}
