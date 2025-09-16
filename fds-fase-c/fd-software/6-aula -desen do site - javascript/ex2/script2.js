const campo1 = document.querySelector("#campo1");
const campo2 = document.querySelector("#campo2");
const seletor= document.querySelector("#operacao");
const botao = document.querySelector("#igual");
let resposta = document.querySelector("#resposta");

botao.addEventListener("click", calcular);


function calcular() {
    // value resgata o valor que foi preenchido no campo.
    //parseInt Transforma "text" em numeros inteiro, para a soma.
            const valor1 = parseInt(campo1.value);
            const valor2 = parseInt(campo2.value);
    //resgata a operação.(para verificar tipo de String"soma ou multiplicação, para fazer o calculo certo.)
            const operacao = seletor.value;
    
            //'===' para que possa fazer a comparação, tipo de calculo.
            if (operacao === "somar")
            //innerHTML vai trocar os valores pela resposta do calculo.
                resposta.innerHTML = valor1 + valor2;
    
            if (operacao === "subtrair")
                resposta.innerHTML = valor1 - valor2;
    
            if (operacao === "multiplicar")
                resposta.innerHTML = valor1 * valor2;
    
            if (operacao === "dividir")
                resposta.innerHTML = valor1 / valor2;
    
    }
    