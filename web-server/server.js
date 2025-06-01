const express = require("express");
const axios = require("axios");
const bodyParser = require('body-parser');
const path = require("path");

app = express();
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, "src"));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "src")));

const PORT = 3000;
const FLASK_SERVER = "http://127.0.0.1:5000/flask";

app.get('/', (req, res) => {
    res.render("home");
});

app.post('/submit', async (req, res) => {
    const data = req.body;
    res.render("home");
    try{
        const response = await axios.post(FLASK_SERVER, data);
        console.log(response.data);
    }
    catch(err){
        console.log(err);
    }
});

app.listen(PORT, () => {
    console.log("Listening on port 3000");
});
