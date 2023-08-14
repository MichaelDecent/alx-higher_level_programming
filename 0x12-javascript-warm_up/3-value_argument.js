#!/usr/bin/node

if (process.argv.length > 1) {
  for (let i = 2; process.argv[i]; i++) { console.log(process.argv[i]); }
} else { console.log('No argument'); }
