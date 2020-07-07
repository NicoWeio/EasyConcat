const util = require('util');
const exec = util.promisify(require('child_process').exec);
const fs = require('fs').promises;
const path = require('path');

const MYDIR = process.argv[2] || '.';
// console.log('Got dir: ' + MYDIR);
// || __dirname

async function getDuration(file) {
  const {
    stdout,
    stderr
  } = await exec(`ffprobe -i "${path.join(MYDIR, file)}" -show_entries format=duration -of compact=p=0:nk=1`);
  return parseFloat(stdout);
}

async function getList() {
  let filePath = path.join(MYDIR, 'list.txt');
  let data = await fs.readFile(filePath, {
    encoding: 'utf-8'
  });
  return data.trim().split('\n').map(l => l.substr('file '.length));
}

function formatTime(totalSeconds) {
  hours = Math.floor(totalSeconds / 3600);
  totalSeconds %= 3600;
  minutes = Math.floor(totalSeconds / 60);
  seconds = Math.floor(totalSeconds % 60);
  return ('0' + hours).slice(-2) + ':' + ('0' + minutes).slice(-2) + ':' + ('0' + seconds).slice(-2);
}

async function main() {
  let list = await getList();
  // console.log(list);
  let data = await Promise.all(list.map(async f => {
    return {
      filename: f,
      duration: await getDuration(f)
    };
  }));
  // console.log(data);
  let totalTime = data.reduce((acc, curr) => {
    console.log(formatTime(acc) + ' ' + curr.filename);
    return acc + curr.duration;
  }, 0);
  console.log(`Gesamtdauer: ${formatTime(totalTime)}`);
}
main();
