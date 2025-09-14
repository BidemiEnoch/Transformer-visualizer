const express = require("express");
const axios = require("axios");
const bodyParser = require('body-parser');
const path = require("path");
const util = require("./src/util/util");

app = express();
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, "public"));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));

const PORT = 3000;

const dummy_input = ["<bos>","it", "is", "not", "exagerrated","<eos>"];
const segments = util.getTokenColors(dummy_input);

app.get('/', (req, res) => {
    res.render("home", { segments });
});

app.post('/submit', async (req, res) => {
    const data = req.body;

    res.render("home", { segments });
    try {
        const response = await axios.post(FLASK_SERVER, data);
        console.log(response.data);
        console.log(data);
    }
    catch (err) {
        console.log(err);
    }
});

app.listen(PORT, () => {
    console.log("Listening on port 3000");
});
