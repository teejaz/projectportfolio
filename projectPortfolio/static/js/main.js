function getData() {
  $.ajax({
    url: '/project/ProjectModel/',
    type: 'GET',
    dataType: 'json',
    success: function(data) {
      console.log(data);
    },
    error: function(xhr, status, error) {
      console.log(error);
    }
  });
}