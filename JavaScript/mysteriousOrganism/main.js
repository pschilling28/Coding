// Returns a random DNA base
const returnRandBase = () => {
    const dnaBases = ['A', 'T', 'C', 'G']
    return dnaBases[Math.floor(Math.random() * 4)] 
  }
  
  // Returns a random single strand of DNA containing 15 bases
  const mockUpStrand = () => {
    const newStrand = []
    for (let i = 0; i < 15; i++) {
      newStrand.push(returnRandBase())
    }
    return newStrand
  }

const pAequorFactory = (num, arr) => {
    return {
        specimenNum: num,
        dna: arr,
        mutate() {
          let oldBaseIndex = Math.floor(Math.random() * arr.length);
          let oldBase = arr[oldBaseIndex];
          let newBase = returnRandBase();
          while (oldBase === newBase) {
            console.log(newBase);
            newBase = returnRandBase();
          };
          arr[oldBaseIndex] = newBase;
          return this.dna;
        },
        compareDNA(pAequor) {
          let sameCount = 0;
          for(let i = 0; i < this.dna.length; i++) {
            if (this.dna[i] === pAequor.dna[i]) {
              sameCount++;
            }
          }
          let percentInCommon = ((sameCount/this.dna.length)* 100).toFixed(2);
          console.log(`Specimen #${this.specimenNum} and specimen #${pAequor.specimenNum} have ${percentInCommon}% DNA in common.`);
        },
        willLikelySurvive() {
          let CGCount = 0;
          for(let i = 0; i < this.dna.length; i++) {
            if (this.dna[i] === 'C'|| this.dna[i] === 'G') {
              CGCount++;
            }
          }
          if(CGCount/this.dna.length >= 0.6) {
            return true;
          } else {
            return false;
          };
        }
    }; 
}

const buildSurvivalArray = num => {
  let survivalArray = [];
  let i = 1;
  while (survivalArray.length < num) {
    let strand = pAequorFactory(i, mockUpStrand());
    if (strand.willLikelySurvive() === true) {
      survivalArray.push(strand);
    }
    i++;
    console.log(i);
    console.log(survivalArray.length);
  }
  return survivalArray;
}


//testScript
//let testStrand1 = pAequorFactory(1, mockUpStrand());
//console.log(testStrand1.dna);
//let testStrand2 = pAequorFactory(2, mockUpStrand());
//console.log(testStrand2.dna);
//console.log(testStrand1.willLikelySurvive());
console.log(buildSurvivalArray(30));
