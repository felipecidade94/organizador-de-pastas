public class ListaDuplamenteEncadeada {

    private class No {
        int valor;
        No anterior;
        No proximo;

        No(int valor) {
            this.valor = valor;
        }
    }

    private No inicio;
    private No ultimo;

    public void inserirOrdenado(int valor) {
        No novo = new No(valor);

        if (inicio == null) {
            inicio = ultimo = novo;
            return;
        }

        No atual = inicio;
        while (atual != null && valor > atual.valor) {
            atual = atual.proximo;
        }

        if (atual == inicio) {
            novo.proximo = inicio;
            inicio.anterior = novo;
            inicio = novo;
        } else if (atual == null) {
            // Inserir no final
            ultimo.proximo = novo;
            novo.anterior = ultimo;
            ultimo = novo;
        } else {
            No anterior = atual.anterior;
            anterior.proximo = novo;
            novo.anterior = anterior;
            novo.proximo = atual;
            atual.anterior = novo;
        }
    }

    @Override
    public String toString() {
        String resultado = "";
        No atual = inicio;
        while (atual != null) {
            resultado += atual.valor + (atual.proximo != null ? " " : "");
            atual = atual.proximo;
        }

        return resultado;
    }
}

