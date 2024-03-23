const express = require('express')
const app = express()
const port = 5000
const cors = require('cors')
const multer = require('multer')
const { spawn } = require('child_process');
const path = require('path');

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'images/')
  },
  filename: (req, file, cb) => {
    cb(null, 'input.jpg')
  },
})

const upload = multer({ storage: storage })

app.use(cors())
app.use('/images', express.static('images'))

app.post('/image', upload.single('file'), async (req, res) => {
  const inputPath = path.join(__dirname, '..', 'images', 'input.jpg');
  const outputDir = path.join(__dirname, '..', 'images', 'output');
  const progPath = path.join(__dirname, 'operations', 'test.py');


    const pythonProcess = spawn('python3', [progPath, inputPath, outputDir]);
    
    await new Promise((resolve, reject) => {
      pythonProcess.on('close', (code) => {
        if (code === 0) {
          resolve();
        } else {
          reject(`Python script exited with code ${code}`);
        }
      });
    });

  res.json({})
})

app.listen(port, () => {
  console.log(`listening at http://localhost:${port}`)
})
