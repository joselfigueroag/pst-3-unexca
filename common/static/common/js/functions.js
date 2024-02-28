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