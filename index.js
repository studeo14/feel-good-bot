var express = require('express');
var app = express();
var bp = require('body-parser');
var request = require('request');

app.set('port', (process.env.PORT || 5000));

var jsonParser = bp.json();

var groupId = '29852246';
var appId = 'b8dca444de029ccb0262f74496';

function like_msg(id){
	var fd = {
		"bot_id": appId,
		"text": text
	};
	request.post({url:"https://api.groupme.com/v3/messages",form:fd});
}

app.post('/', jsonParser, function(request, response) {
    //parse
    var id = request.body.id;
    response.end();
});

app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
});


