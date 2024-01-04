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
          let oldBase = arr[Math.floor(Math.random() * arr.length)];
          console.log(oldBase);
          let newBase = returnRandBase();
          while (oldBase === newBase) {
            newBase = returnRandBase();
          };
          oldBase = newBase;
          return this.dna;
        }
    }; 
}

//test
//console.log(pAequorFactory(1, mockUpStrand()));
let inst1 = pAequorFactory(1, mockUpStrand());
console.log(inst1.dna);
inst1.mutate();
//console.log(inst1.dna);
//console.log('test');*/