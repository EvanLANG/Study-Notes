Node.js

Below are some of the popular modules which are used in a Node js application

1.Express framework – Express is a minimal and flexible Node js web application framework that provides a robust set of features for the web and Mobile applications.
2.Socket.io - Socket.IO enables real-time bidirectional event-based communication. This module is good for creation of chatting based applications.
3.Jade - Jade is a high-performance template engine and implemented with JavaScript for node and browsers.
4.MongoDB - The MongoDB Node.js driver is the officially supported node.js driver for MongoDB.
5.Restify - restify is a lightweight framework, similar to express for building REST APIs
6.Bluebird - Bluebird is a fully featured promise library with focus on innovative features and performance



1.To use the express module:
npm install express

use the key word "require" and create an object.

var express=require('express');
var app=express();
app.set('view engine','jade');
app.get('/',function(req,res)
{
});
var server=app.listen(3000,function()
{

2. Create your own module:

Addition.js
var exports=module.exports={};
exports.AddNumber=function(a,b)
{
return a+b;
};

2.1The "exports" keyword is used to ensure that the functionality defined in this file can actually be accessed by other files.
2.2We are then defining a function called 'AddNumber'. This function is defined to take 2 parameters, a and b. The function is added to the module "exports" to make the function as a public function that can be accessed by other application modules.
2.3We are finally making our function return the added value of the parameters.

app.js
var Addition=require('./Addition.js');
console.log(Addition.AddNumber(1,2));

2.4We are using the "require" keyword to include the functionality in the Addition.js file.
3.5Since the functions in the Addition.js file are now accessible, we can now make a call to the AddNumber function. In the function, we are passing 2 numbers as parameters. We are then displaying the value in the console.


HTTP:

var http = require('http')
var server = http.createserver(function(request, response)
{
	reponse.writeHead(200,{'Content-Type':'Text/html'});
	reponse.end('Hello World');
})
server.listen(7000);

GET Requests:

var request = require("request");
	request("http://www.google.com",function(error,response,body)
	{
		console.log(body);
	});




