/*let sidebarOffcanvas = new bootstrap.Offcanvas(document.getElementById('sidebarOffcanvas'))
function openMenu(opc){
  switch (opc){
      case 'open':
          sidebarOffcanvas.show();
      break;
      case 'close':
          sidebarOffcanvas.hide();
      break;
  }
}*/

(function () {
    console.log('needs-validation')
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
  
          form.classList.add('was-validated')
        }, false)
      })
  })();

  (function busqueda(){
    console.log('active search')
    const info = document.getElementById('info')
    document.addEventListener('keyup', found =>{
        if (found.target.matches('#search')){
            document.querySelectorAll(".find").forEach(item =>{
                if (item.textContent.toLowerCase().includes(found.target.value.toLowerCase())){
                    document.getElementById("table_"+item.id).classList.remove('visually-hidden');
                    item.classList.add('visible');
                }else{
                    document.getElementById("table_"+item.id).classList.add('visually-hidden');
                    document.getElementById("table_"+item.id).classList.remove('fila');
                    item.classList.remove('visible');
                }
             
            })
            document.querySelectorAll('.visible').forEach(fila =>{
                document.getElementById("table_"+fila.id).classList.remove('visually-hidden')
                document.getElementById("table_"+fila.id).classList.add('fila')
            })
            const coincidencias = document.querySelectorAll('.visible')
            if (coincidencias.length == 0){
                info.classList.remove('visually-hidden');
            }else{
                info.classList.add('visually-hidden')
            }
          
        }
    })
})();


document.add
let selectedTuition = "";
let selectedSubject = "";
let selectedMoment = "";

function handleChangeSelectTuition(event) {
  selectedTuition = event.target.value;
  console.log("tuition", selectedTuition)
}

function handleChangeSelectSubject(event) {
  selectedSubject = event.target.value;
  console.log("subject", selectedSubject)
}

function handleChangeSelectMoment(event) {
  selectedMoment = event.target.value;
  console.log("moment", selectedMoment)
}

function getData(event) {
  event.preventDefault();
  if (selectedTuition && selectedSubject && selectedMoment){
    let endpoint = `/academic-data/api/tuition_detail_api/${selectedTuition}/${selectedSubject}/${selectedMoment}`
      fetch(endpoint)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la solicitud: ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            // Manejar los datos recibidos
            generateData(data)
            console.log(data)
        })
        .catch(error => {
            // Manejar errores
            console.error(error);
        });
  } else {
    console.log("Faltan los parametros de consulta")
  } 
}

function generateData(data) {
  let body_table = document.getElementById("body_table");

  body_table.innerHTML = "";

  if (data.students) {
    for (let student of data.students){
      let row = body_table.insertRow()
      let cellName = row.insertCell(0)
      cellName.textContent = student.full_name
      let cellNote = row.insertCell(1)
      let inputNote = document.createElement("input");
      inputNote.type = "number"
      inputNote.name = `note_${student.id}`;
      inputNote.value = student.qualifications[0] ? student.qualifications[0].note : 0.0; 
      inputNote.classList.add("form-control");
      cellNote.appendChild(inputNote);
    }
  } else {
    let row = body_table.insertRow();
    let cell = row.insertCell();
    cell.colSpan = 2; // Para que ocupe ambas columnas
    cell.textContent = "No hay estudiantes registrados en la matricula";
  }

}

function block_unblock(obj){
    let save = document.getElementById('save')
    let state = {} 
    document.querySelectorAll('.carga').forEach((item,index) => {
        state[index] = item.value;
    })
    switch (obj.id){
        case 'selectTuition':
            save.disabled = true
        break;
        case 'selectSubject':
            save.disabled = true
        break;
        case 'selectMoment':
            save.disabled = true
        break;
        case 'consulta':
            if (state[0] == 0 || state[1] == 0 || state[2] == 0){
                save.disabled = true
            }else{
                save.disabled = false
            }
            
        break;
    }
}