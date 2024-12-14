let sumar = () =>{
    let num1 = parseInt(prompt('numero1: '))
    let num2 = parseInt(prompt('numero2: '))
    let resultado = num1 + num2;
    return resultado;
};

let restar = () => {
    let num1 = parseInt(prompt('numero1: '))
    let num2 = parseInt(prompt('numero2: '))
    let resultado = num1 - num2;
    return resultado;
};

let multiplicar= () => {
    let num1 = parseInt(prompt('numero1: '))
    let num2 = parseInt(prompt('numero2: '))
    let resultado = num1 * num2;
    return resultado;
};

let dividir = () => {
    let num1 = parseInt(prompt('numero1: '))
    let num2 = parseInt(prompt('numero2: '))
    let resultado = num1 - num2;
    return resultado;
};

let potencia= () => {
    let num1 = parseInt(prompt('numero1: '))
    let num2 = parseInt(prompt('numero2: '))
    let resultado = num1 * num2;
    return resultado;
};

let calculadora = () => {
    opcion = parseInt(prompt('Digite la opcion que desea: '));
    if (opcion === 1){
        document.write(sumar())
    }
    else if (opcion === 2){
        document.write(restar())
    }
    else if (opcion === 3){
        document.write(multiplicar())
    }
    else if (opcion === 4){
        document.write(dividir())
    }
    else if (opcion === 5){
        document.write(potencia())
    }
    else{
        alert('opcion no valida')
    }
}

calculadora()
