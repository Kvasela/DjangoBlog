(function(){
  /*Search form into main menu*/
  function search_form(e) {
    // Send on enter to validate
    if (event.keyCode == 13) {
      validate_submit_search_form(e);
    }
  }

  function validate_submit_search_form(e) {
    // Validate search form
    var search_field = document.getElementById('search-field');
    search_field.value = search_field.value.trim();
    if (search_field.value.length > 0) {
      document.forms['search-form'].submit();
    }
    return false;
  }

  function activate_search_form(e) {
    // Switch search form visible or invisible
    var search_form = document.getElementById('search-form');
    if( search_form.className === 'active'){
      var search_field = document.getElementById('search-field');
      if (validate_submit_search_form(e)) {
        search_form.className = '';
      }
    }
    else{
      search_form.className = 'active';
      document.getElementById('search-field').focus();
    }
  }

  function search_field_focus_out(e) {
    // Hide search form in main menu if focus isn't on search field
    setTimeout(function () {
      document.getElementById('search-form').className = '';
    }, 196);
  }

  /*Main menu for screen that is less 768px*/
  function active_navbar_toggle(e) {
    // Show or hide main menu on toggle button
    var menu = document.getElementById('masthead_menu');
    if(menu.className === 'nav-menu') {
      menu.className = 'nav-menu active';
    } else {
      menu.className = 'nav-menu';
    }
  }

  document.getElementById('open-search-btn').addEventListener('click', activate_search_form);
  document.getElementById('search-field').addEventListener('focusout', search_field_focus_out);
  document.getElementById('navbar_toggle').addEventListener('click' , active_navbar_toggle);

  /*Activate highlight.pack.js*/
  hljs.initHighlightingOnLoad();
})();