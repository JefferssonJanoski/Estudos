import java.util.Scanner;

public class ClassificacaoNota {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite a nota (0 a 100): ");
        int nota = scanner.nextInt();

        if (nota >= 90) {
            System.out.println("Classificação: A");
        } else if (nota >= 80) {
            System.out.println("Classificação: B");
        } else if (nota >= 70) {
            System.out.println("Classificação: C");
        } else if (nota >= 60) {
            System.out.println("Classificação: D");
        } else {
            System.out.println("Classificação: F");
        }
    }
}