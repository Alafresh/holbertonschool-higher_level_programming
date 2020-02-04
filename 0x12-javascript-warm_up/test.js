#!/usr/bin/node
const command = process.argv;
const noNumber = parseInt(command[2]);

if (isNaN(noNumber)){ 
    console.log('Not number');
}
else{
    console.log(noNumber);
}
