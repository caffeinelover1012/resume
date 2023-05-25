const express = require('express');
const multer = require('multer');
const cors = require('cors');
const fs = require('fs');
const pdfParse = require('pdf-parse');

const upload = multer({ dest: 'uploads/' });

const app = express();

// Enable CORS
app.use(cors());

app.post('/upload', upload.single('file'), (req, res) => {
    let dataBuffer = fs.readFileSync(req.file.path);
    
    pdfParse(dataBuffer).then(function(data) {
        res.send(data.text);
    });
});

app.listen(3000, () => console.log('Server started on port 3000'));
