import java.util.Scanner;

public class TestaLista {
   public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      ListaDuplamenteEncadeada lista = new ListaDuplamenteEncadeada();

      System.out.print("Quantos números você deseja inserir? ");
      int quantidade = scanner.nextInt();

      for (int i = 0; i < quantidade; i++) {
         System.out.print("Digite o " + (i + 1) + "º número: ");
         int valor = scanner.nextInt();
         lista.inserirOrdenado(valor);
      }

      System.out.println("Lista ordenada: " + lista.toString());
      scanner.close();
   }
}
