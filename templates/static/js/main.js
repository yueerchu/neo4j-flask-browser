  function submit(){
    cypher = document.getElementById('cypher');
    // alert(JSON.stringify(JSON.parse(cypher.value)))
    alert(cypher.value)

    $.ajax({
    	method : 'POST',
    	url : '/cypher',
    	data : cypher.value,
    	contentType: 'text/plain'
    }).success(function(data){
    	// alert(JSON.stringify(data));
    	$('#response').text(JSON.stringify(data, null, '\t'));
    })
  }