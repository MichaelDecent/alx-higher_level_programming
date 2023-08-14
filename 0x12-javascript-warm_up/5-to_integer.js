#!/usr/bin/node
const argv1 = process.argv[2];
if (Number(argv1) && argv1) { console.log('My number: ' + Number(argv1)); } else { console.log('Not a number'); }
