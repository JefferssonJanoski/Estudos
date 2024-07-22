package discentes;
import discentes.Aluno;
import discentes.AlunoSuperior;

public class Principal {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		AlunoSuperior aluno = new AlunoSuperior();
		
		aluno.nome = "Jeffersson";
		aluno.teste = 9;
		aluno.prova = 10;
		
		System.out.println(aluno.nome + "\n" + aluno.getMedia());
	}

}
