const produtos = [
    { nome: "Sérum Cotton", src: "/static/img/prod_azul.png", cor: "azul" },
    { nome: "Sérum Lavanda", src: "/static/img/prod_laranja.png", cor: "laranja" },
    { nome: "Sérum Maçã-verde", src: "/static/img/prod_roxo.png", cor: "roxo" },
    { nome: "Sérum Bergamota", src: "/static/img/prod_verde.png", cor: "verde" }
];

// 
function sortearProduto() {
    return Math.floor(Math.random() * produtos.length);
}

function atualizarInterface(indiceProduto) {
    const produtoSorteado = produtos[indiceProduto];
    const containerProduto = document.getElementById('produtoSorteado');
    containerProduto.style.backgroundImage = `url(${produtoSorteado.src})`;
}

document.addEventListener("DOMContentLoaded", function() {
    const botaoSortear = document.getElementById('botaoSortear');
    botaoSortear.addEventListener("click", () => {
        const indiceAleatorio = sortearProduto();
        atualizarInterface(indiceAleatorio);
        botaoSortear.style.display = "none";
    });
});




document.addEventListener('DOMContentLoaded', function() {
    const itens = document.querySelectorAll('.itens');
    let currentIndex = 0;
  
    function showItem(index) {
      itens.forEach(item => {
        item.style.transform = `translateX(-${index * 100}%)`;
      });
    }
  
    function nextItem() {
      if (currentIndex < itens.length - 1) {
        currentIndex++;
      } else {
        currentIndex = 0;
      }
      showItem(currentIndex);
    }
  
    function prevItem() {
      if (currentIndex > 0) {
        currentIndex--;
      } else {
        currentIndex = itens.length - 1;
      }
      showItem(currentIndex);
    }
  
    document.querySelector('.anterior').addEventListener('click', prevItem);
    document.querySelector('.próximo').addEventListener('click', nextItem);
  });


function removerAcentos(texto) {
    return texto.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

function pesquisar() {
    var input, filtro, carrossel, itens, nomeProduto;
    input = document.getElementById('pesquisa');
    filtro = removerAcentos(input.value.toUpperCase()); // Normalizar e converter para maiúsculas
    carrossel = document.querySelector(".interior-carrossel");
    itens = carrossel.querySelectorAll('.itens');

    itens.forEach(item => {
        nomeProduto = removerAcentos(item.querySelector('h4').textContent.toUpperCase()); // Normalizar e converter para maiúsculas
        if (nomeProduto.indexOf(filtro) > -1) {
            item.style.display = ""; // Mostrar item se corresponder ao filtro
        } else {
            item.style.display = "none"; // Ocultar item se não corresponder ao filtro
        }
    });
}
