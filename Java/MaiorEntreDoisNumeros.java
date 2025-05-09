import java.util.Scanner;

public class MaiorEntreDoisNumeros {
    public static void main(Strings[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o primeiro numero: ");
        int n1 = scanner.nextInt();

        System.out.print("Digite o segundo numero: ");
        int n2 = scanner.nextInt();

        if (n1 > n2){
            System.out.print("Dos numeros digitados, o maior é: "+ n1);
        } else {
            System.out.print("Dos numeros digitados, o maior é: "+ n2);
        }
    }
}