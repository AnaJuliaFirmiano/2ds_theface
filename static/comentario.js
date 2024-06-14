//function comentario
function publicarComentario() {
    var comentario = document.getElementById("input-comentario").value;
    document.getElementById("input-comentario").value = "";

    var novoComentario = document.createElement("div");
    novoComentario.classList.add("comentario-item");

    var textoComentario = document.createElement("p");
    textoComentario.textContent = comentario;

    var botaoExcluir = document.createElement("button");
    botaoExcluir.textContent = "Excluir";
    botaoExcluir.addEventListener("click", function() {
        novoComentario.remove();
    });

    novoComentario.appendChild(textoComentario);
    novoComentario.appendChild(botaoExcluir);

    var comentariosAnteriores = document.getElementById("comentarios-anteriores");
    comentariosAnteriores.appendChild(novoComentario);

    mostrarMensagem("Comentário publicado");
}

function mostrarMensagem(mensagem) {
    var mensagemElemento = document.getElementById("mensagem-texto");
    mensagemElemento.textContent = mensagem;
    var mensagemDiv = document.getElementById("mensagem-publicacao");
    mensagemDiv.classList.remove("mensagem-hidden");
}

function fecharMensagem() {
    var mensagemDiv = document.getElementById("mensagem-publicacao");
    mensagemDiv.classList.add("mensagem-hidden");
}