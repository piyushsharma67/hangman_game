const express=require("express");
const app=express();
const bodyParser=require("body-parser");
const mongoose=require("mongoose");
// const teacherRoutes=require('../routes/teacher');
// const studentRoutes=require('../routes/student');
const signUpRoute=require('./routes/sign_up');
const logInRoute=require('./routes/login');
const studentRoute=require('./routes/student');

mongoose.connect('mongodb://localhost:27017',
{
    useNewUrlParser: true,
    useUnifiedTopology: true 
});

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended : true}));

app.use('/sign_up',signUpRoute);
app.use('/login',logInRoute);

module.exports=app;


