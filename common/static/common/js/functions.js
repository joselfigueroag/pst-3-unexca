let sidebarOffcanvas = new bootstrap.Offcanvas(document.getElementById('sidebarOffcanvas'))
function openMenu(opc){
  switch (opc){
      case 'open':
          sidebarOffcanvas.show();
      break;
      case 'close':
          sidebarOffcanvas.hide();
      break;
  }
}