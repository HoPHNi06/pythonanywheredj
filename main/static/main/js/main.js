//document.getElementById('main-form').addEventListener("submit", checkform);

function checkForm(el) {
	//event.preventDefault();
	//var el = document.getElementById('main-form');
	var a = el.number.value;
	var b = el.number1.value;
	var state = el.state.value;
	var fail = "";
	var ans = "";

	if(a == "" || b == "" || state == "")
		fail = "Заполните все поля!";

	else if(a.length > 100 || b.length > 100)
		fail = "Введите число длина которого не превышает 100 символов!";


	var ans = "";

	if(fail != ""){
		console.log(fail);
		document.getElementById('error').innerHTML = fail;
	}else if(state == "Сложение"){
		a = Number(a);
		b = Number(b);
		ans = a + b;
		console.log(ans);
		document.getElementById('answer').innerHTML = ans;
	}else if(state == "Вычитание"){
		a = Number(a)
		b = Number(b)
		ans = a - b;
		console.log(ans);
		document.getElementById('answer').innerHTML = ans;
	}else if(state == "Умножение"){
		a = Number(a);
		b = Number(b);
		ans = a * b;
		console.log(ans);
		document.getElementById('answer').innerHTML = ans;
	}else if(state == "Деление"){
		a = Number(a);
		b = Number(b);
		ans = a / b;
		console.log(ans);
		document.getElementById('answer').innerHTML = ans;
	}else if(state == "Возведение в степень"){
		a = Number(a);
		b = Number(b);
		ans = a ** b;
		console.log(ans);
		document.getElementById('answer').innerHTML = ans;
	}else if(state == "Остаток при делении"){
		a = Number(a);
		b = Number(b);
		ans = a % b;
		console.log(ans);
		document.getElementById('answer').innerHTML = ans;
	}

	return false
}

var ocb = 0
function OnClickButton(){
	ocb += 1
	console.log("Нажатий: " + ocb)
}
