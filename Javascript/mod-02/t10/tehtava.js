
'use strict';
const candidates_amount = +prompt("Give the amount of participants:")
let candidates = []

for (let i = 0; i < candidates_amount; i++) {
    candidates.push({name: prompt(`Name for candidate ${i+1}:`), votes: 0});    
}




const voters_amount = +prompt("Give the amount of voters:")
let candidates_string = ""

let vote
for (let i = 0; i < voters_amount; i++) {
    candidates_string = `VOTER NUMBER:  [ ${i+1} ]\n\nCANDIDATES:`
    for (let j = 0; j < candidates.length; j++) {
        candidates_string += `\n[ ${j+1} ] - ${candidates[j].name}`
    }
    candidates_string += "\n\nENTER THE NUMBER OF CANDIDATE TO VOTE:"
    vote = +prompt(candidates_string)
    if (0 < vote < candidates.length){
        candidates[vote-1].votes +=1
    }

}




candidates.sort(function(a, b){return b.votes - a.votes});

console.log(`The winner is ${candidates[0].name} with ${candidates[0].votes} votes.\nresults:`)

for (let i = 0; i < candidates.length; i++) {
    console.log(`${candidates[i].name}: ${candidates[i].votes} votes`)
}
