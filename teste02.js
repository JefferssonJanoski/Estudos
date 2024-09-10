function pertenceFibonacci(num) {
        // Início da sequência de Fibonacci
        let a = 0, b = 1;
        
        // Se o número for 0 ou 1, ele já pertence à sequência
        if (num === 0 || num === 1) {
            return true;
        }
        
        // Calcular a sequência até encontrar um número maior ou igual ao informado
        while (b <= num) {
            if (b === num) {
                return true;
            }
            [a, b] = [b, a + b]; // Atualiza os valores de a e b
        }
        
        return false;
        }

        // Entrada do usuário
        let numero = parseInt(prompt("Informe um número:"));

        // Verificação se o número pertence à sequência de Fibonacci
        if (pertenceFibonacci(numero)) {
            console.log(`O número ${numero} pertence à sequência de Fibonacci.`);
        } else {
            console.log(`O número ${numero} não pertence à sequência de Fibonacci.`);
        }