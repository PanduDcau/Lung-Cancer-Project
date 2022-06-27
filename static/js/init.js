$(document).ready(function(){
    $('select').formSelect();
  });

  $(document).ready(function(){
    $('.collapsible').collapsible();
  });

    let elem = document.querySelector('.collapsible.expandable');
    let instance = M.Collapsible.init(elem, {accordion: false });

    document.addEventListener('DOMContentLoaded', function() {
    let elems = document.querySelectorAll('select');
    let instances = M.FormSelect.init(elems);
  });