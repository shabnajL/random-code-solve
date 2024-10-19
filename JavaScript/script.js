// link: https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures-v8/
// JavaScript Algorithms and Data Structures (Beta)
// Review JavaScript Fundamentals by Building a Gradebook App
// —------------------------------------------------------------------------
// step 1:
// —------------------------------------------------------------------------

function getAverage(scores) {
  var total = 0;
  var leng = scores.length;
  for(var i = 0; i < leng; i++) {
        
        total += scores[i];
        
  }
 
  var length = total/leng;
  return length;
}

console.log(getAverage([92, 88, 12, 77, 57, 100, 67, 38, 97, 89]));
console.log(getAverage([45, 87, 98, 100, 86, 94, 67, 88, 94, 95]));

// —------------------------------------------------------------------------
// step 2:
// —------------------------------------------------------------------------


// —------------------------------------------------------------------------
// step 3:
// —------------------------------------------------------------------------


// —------------------------------------------------------------------------
// step 4:
// —------------------------------------------------------------------------
