// Atajo para acceder a elementos del DOM
const d = document;
const $ = s => d.querySelector(s); // Selecciona el primer elemento que coincida con el selector

// Selecciona el formulario del HTML
const form = $('.form');

// Selecciona el lugar donde se mostrará el resultado
const distance = $('.evaluator');

// Cuando se envíe el formulario...
form.onsubmit = (ev) => {
  ev.preventDefault(); // Detiene el comportamiento normal del formulario (evita recargar la página)
  
  // Toma los valores que se ingresaron en el formulario
  const formData = new FormData(ev.target);
  const vel = formData.get('vel');   // Velocidad ingresada
  const timer = formData.get('tim'); // Tiempo ingresado

  // Calcula la distancia (velocidad * tiempo) y muestra el resultado
  distance.textContent = `Distancia recorrida ${vel * timer}`;
  console.log(vel); // Muestra en consola el valor ingresado de velocidad (opcional)
}
