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
  })()