programa {

 inclua biblioteca Matematica --> mat


  funcao inicio() {
    //1 Passo - declarar as variaveis
    real peso
    real altura
    real imc

    //2 Passo - Entrada 
    escreva("Digite seu Peso: ")
    leia(peso)

    escreva("Digite sua altura: ")
    leia(altura)

    //3 - Passo - Pracessamento
    imc = peso / (altura * altura)

    //4 Passo - Saida
    escreva("Seu IMC é: ", mat.arredondar(imc,2))




 }
 
}
