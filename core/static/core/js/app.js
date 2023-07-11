
var emailLog = document.getElementById('emaillog');
var passwordLog = document.getElementById('passwordlog');
var checkoutLog = document.getElementById('checklog');

var emailReg = document.getElementById('emailreg');
var passwordReg = document.getElementById('passwordreg');
var cpassword = document.getElementById('cpassword');
var checkoutReg = document.getElementById('checkreg');
var address = document.getElementById('address');
var lastname = document.getElementById('lastname');
var nombre = document.getElementById('nombre');
var city = document.getElementById('city');
var selectRegion = document.getElementById('selectRegion');

var msj = document.getElementById('error');

var options = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Accept-Version': 'application/vnd.shipit.v2'
  }
};

fetch('https://api.shipit.cl/v/regions', options)
  .then(response => response.json())
  .then(data => {
    var regions = Object.values(data);
    console.log(data)
    regions.forEach(region => {
      var option = document.createElement('option');
      option.value = region.id;
      option.textContent = region.name;
      selectRegion.appendChild(option);
    });
  })
  .catch(error => {
    console.error('Error al obtener las regiones:', error);
    var option = document.createElement('option');
    option.value = '';
    option.textContent = 'Error al obtener las regiones';
    selectRegion.appendChild(option);
  });







function sendLogin() {
  var mensaje = [];
  if (emailLog.value === null || emailLog.value === '') {
    mensaje.push('No ingresó correo electronico y contraseña');
  }
  if (passwordLog.value === null || passwordLog.value === '') {
    mensaje.push('Intentelo nuevamente');
  }
  msj.innerHTML = mensaje.join(', ');

  return false;
}

function sendRegister() {
  var mensaje = [];
  if (nombre.value === null || nombre.value === '') {
    mensaje.push('Falto ingresar tu nombre');
  }
  if (lastname.value === null || lastname.value === '') {
    mensaje.push('Falto ingresar tu apellido ');
  }
  if (passwordReg.value === null || passwordReg.value === '') {
    mensaje.push('No ingresaste tu contraseña');
  }
  if (cpassword.value === null || cpassword.value === '') {
    mensaje.push('No ingresaste la confirmacion de contraseña');
  }
  if (emailReg.value === null || emailReg.value === '') {
    mensaje.push('No ingresaste tu correo');
  }
  if (address.value === null || address.value === '') {
    mensaje.push('Falto ingresar tu direccion ');
  }
  if (city.value === null || city.value === '') {
    mensaje.push('Falto ingresar tu ciudad');
  }
  if (selectRegion.value === null || selectRegion.value === '') { // Modificado aquí
    mensaje.push('Falto seleccionar tu region');
  }
  msj.innerHTML = mensaje.join(' , ');

  return false;
}
